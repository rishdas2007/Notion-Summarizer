from notion_client import Client
from config import NOTION_TOKEN, DATABASE_ID, get_week_date_range
import logging

class NotionClient:
    def __init__(self):
        self.client = Client(auth=NOTION_TOKEN)
        self.database_id = DATABASE_ID
        
    def get_weekly_episodes(self):
        """Fetch episodes from the past Monday-Friday based on when they were listened to (Last snip date)"""
        monday, friday = get_week_date_range()

        try:
            response = self.client.databases.query(
                database_id=self.database_id,
                filter={
                    "and": [
                        {
                            "property": "Last snip date",
                            "date": {
                                "on_or_after": monday.isoformat()
                            }
                        },
                        {
                            "property": "Last snip date",
                            "date": {
                                "on_or_before": friday.isoformat()
                            }
                        }
                    ]
                },
                sorts=[
                    {
                        "property": "Last snip date",
                        "direction": "ascending"
                    }
                ]
            )
            return response["results"]
        except Exception as e:
            logging.error(f"Error fetching episodes: {e}")
            return []
    
    def get_page_content(self, page_id):
        """Fetch full content of a Notion page including all nested blocks"""
        try:
            # Get page properties
            page = self.client.pages.retrieve(page_id)
            
            # Get ALL page blocks (with pagination and nesting)
            blocks = self.get_all_blocks_with_pagination(page_id)
            
            return page, blocks
        except Exception as e:
            logging.error(f"Error fetching page content for {page_id}: {e}")
            return None, []
    
    def get_all_blocks_with_pagination(self, block_id):
        """Fetch all blocks with pagination and recursive nesting"""
        all_blocks = []
        start_cursor = None
        
        while True:
            try:
                # Get blocks with pagination
                kwargs = {"block_id": block_id, "page_size": 100}
                if start_cursor:
                    kwargs["start_cursor"] = start_cursor
                    
                response = self.client.blocks.children.list(**kwargs)
                blocks = response["results"]
                
                # Process each block and get nested content
                for block in blocks:
                    all_blocks.append(block)
                    
                    # If block has children, fetch them recursively
                    if block.get("has_children", False):
                        nested_blocks = self.get_all_blocks_with_pagination(block["id"])
                        # Add indentation info to nested blocks for proper markdown conversion
                        for nested_block in nested_blocks:
                            nested_block["_parent_id"] = block["id"]
                            nested_block["_is_nested"] = True
                        all_blocks.extend(nested_blocks)
                
                # Check if there are more pages
                if not response.get("has_more", False):
                    break
                    
                start_cursor = response.get("next_cursor")
                
            except Exception as e:
                logging.error(f"Error fetching blocks for {block_id}: {e}")
                break
        
        return all_blocks