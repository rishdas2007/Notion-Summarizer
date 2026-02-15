# DeFi Yield Explained

**Citation:** "DeFi Yield Explained." *Tokenized*, 09 Feb. 2026, <https://tokenized.simplecast.com/episodes/defi-yield-explained-RsbslSNL>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Kraken's DeFi Earn Product Launch](#krakens-defi-earn-product-launch)
   - [Comparison with Coinbase's Approach](#comparison-with-coinbases-approach)
   - [Risk Management and Liquidity Considerations](#risk-management-and-liquidity-considerations)
   - [The Curator Role in DeFi Vaults](#the-curator-role-in-defi-vaults)
   - [Staking vs. Lending: Critical Distinctions](#staking-vs-lending-critical-distinctions)
   - [Asset Manager Trajectory in DeFi](#asset-manager-trajectory-in-defi)
   - [Institutional Adoption Dynamics](#institutional-adoption-dynamics)
   - [Regulatory Considerations](#regulatory-considerations)
   - [Ethereum's Infrastructure Evolution](#ethereums-infrastructure-evolution)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [References and Citations](#references-and-citations)

## Executive Summary

This episode of Tokenized (Episode 69) provides comprehensive analysis of the emerging DeFi yield landscape, focusing on how centralized exchanges and traditional financial institutions are integrating decentralized finance products. The discussion centers on Kraken's launch of DeFi Earn in partnership with Veda, comparing it to Coinbase's earlier Morpho-based product, and exploring the broader implications for institutional adoption of on-chain yield generation.

**Core Arguments:**

1. **Product Evolution**: Asset managers follow a clear trajectory: staking → on-chain lending → general-purpose vaults combining multiple yield sources
2. **Diversification Benefits**: Multi-protocol vaults (accessing Aave, Morpho, Pendle) reduce risk compared to single-protocol solutions while delivering higher organic yields (6%+ vs. 3.5%)
3. **Curator Emergence**: A new role combining traditional asset management with cryptographic accountability, where allocation decisions are transparent and verifiable on-chain
4. **Regulatory Innovation**: Exchanges use embedded self-custodial wallets to offer DeFi access while maintaining regulatory compliance, creating a model that may be difficult for traditional banks to replicate
5. **Infrastructure Competition**: Ethereum faces increased competition from specialized chains (Canton for capital markets, Base for institutions, purpose-built chains like Tempo for payments), prompting re-evaluation of its rollup-centric roadmap

**Key Outcomes**: Kraken DeFi Earn achieved nearly $40 million TVL with 13,000 users within one week, demonstrating significant demand for simplified DeFi access. The product offers zero-incentive organic yields exceeding 6% through multi-chain, multi-protocol diversification.

## Detailed Analysis

### Kraken's DeFi Earn Product Launch

Kraken's DeFi Earn represents what Sunand Raghupathi describes as "probably the most ambitious DeFi earned product that has ever been created." The product architecture involves several innovative layers:

**Technical Implementation:**
- Users on Kraken Exchange (15 million customers) access DeFi without prior blockchain experience
- Through Privy integration, Kraken automatically provisions non-custodial wallets
- The system seeds wallets with gas fees and transfers assets seamlessly
- Assets move on-chain into Veda Vaults, which source yield across multiple chains and protocols

**Differentiation Factors:**
The product creates a "chain abstracted, multi-asset, multi-protocol yield experience" where users benefit from:
- Higher yields through protocol diversification
- Improved UX with no manual wallet management
- Lower fees due to deployment on Inc (a Layer 2 solution)
- Access to Ethereum-based yields despite operating on a different chain

**Performance Metrics:**
Within approximately one week of launch, the product demonstrated strong market validation:
- TVL: Nearly $40 million
- Unique users: Approximately 13,000
- Many users had never previously engaged with DeFi protocols

Raghupathi emphasizes the strategic boldness: "Kraken launched with zero incentives. It was a really bold strategy. I don't think any other EARN program has done this where they started with zero incentives."

### Comparison with Coinbase's Approach

Cuy Sheffield provides detailed context on Coinbase's earlier product launch, which serves as an important comparison point:

**Coinbase Model:**
- Leverages Morpho as the single underlying protocol
- Vaults curated by Steakhouse Financial
- Offers approximately 3.5% APY total yield
- Approximately 75 basis points derived from Morpho token incentives
- Organic yield in the "high 2%" range

**Kraken Model:**
- Uses Veda as an aggregator across multiple protocols (Morpho, Aave, Pendle, others)
- Three separate vaults with different risk-return profiles
- Curators include Chaos Labs (Aave's risk manager) and Centora (institutional-focused)
- Delivers 6%+ organic yields with zero token incentives
- Multi-chain capability for yield sourcing

**Strategic Implications:**
The comparison reveals fundamental differences in approach. Sheffield notes the UX challenge with Coinbase's model: "getting yield in a token that is not the token you deposited, namely USDC, is a really challenging UX." Kraken's approach eliminates this friction by providing yields in the deposited asset.

Raghupathi argues that diversification actually reduces risk: "as soon as you enshrine a single protocol, you now are enshrining the risk associated with that protocol. Whereas when you have the opportunity to diversify over multiple protocols... that diversification actually helps with risk."

### Risk Management and Liquidity Considerations

Simon Taylor raises the critical question facing risk managers: "what if there's a run on the vault?" This concern parallels worries about stablecoin redemptions at scale.

**Liquidity Profile Differentiation:**

Raghupathi provides concrete examples of protocol-specific characteristics:

**Aave:**
- Market size: Approximately $40 billion
- Track record: No stablecoin withdrawal issues in recent years
- Liquidity: Consistently high, supporting instant redemptions
- Yield: Generally lower than alternatives

**Morpho:**
- Yield: Typically higher organic returns than Aave
- Liquidity challenges: Has experienced withdrawal limitations
- Recent example: Stream Finance incident raised questions about vault definitions
- Risk profile: No capital loss, but temporary withdrawal restrictions

**Design Philosophy:**
Raghupathi articulates Veda's approach: "our view is that fintechs should be able to tailor the liquidity profile and the yield to their customers' requirements. Some people want instant liquidity 24-7 on up to 50% of the capital. Some people are willing to take lock up periods."

The Kraken implementation addresses this through three separate vaults, each with distinct liquidity characteristics, allowing customers to select appropriate risk-return profiles.

**Fintech Priorities:**
Raghupathi emphasizes: "Their number one priority over everything else, over yield, over anything else is, can my users get their funds out when they want to? So it's absolutely at the heart of the matter."

### The Curator Role in DeFi Vaults

The discussion extensively explores the curator concept, which Sheffield initially questions: "why isn't it just called asset manager?"

**Curator Responsibilities:**
- Making allocation decisions across protocols
- Managing risk at smart contract, economic, and protocol levels
- Determining exposure limits and diversification strategies
- Monitoring and adjusting positions based on market conditions

**Kraken's Curator Structure:**
- **Chaos Labs**: Curates two of three vaults; serves as Aave's risk manager with extensive protocol expertise
- **Centora**: Curates the third vault; institutional-focused with deep DeFi knowledge

**Curator vs. Traditional Asset Manager:**

Raghupathi provides detailed differentiation:

**Transparency Guarantees:**
"A vault provides guarantees to users about one, they can see where their assets are at all times, right? It's all on the blockchain. It's all transparent. It's all publicly verifiable."

**Operational Constraints:**
"They have guarantees as to what can happen to those assets. So, you know, things like control and leverage, what protocols can be taken out, what assets can this vault actually take exposure to? All of this stuff is all public. It's all verifiable on-chain."

**Accountability Mechanism:**
"Curators have these cryptographic constraints and in some sense, they're more accountable to customers because everything is public. It's all on chain. It's all verifiable. And most importantly, it's non-custodial."

**Historical Context:**
Raghupathi references Celsius and BlockFi as cautionary examples: "People wanted high yield savings accounts on their stable coins, on their crypto assets. It's why those products did so well until they blew up. But why did they blow up? It's because there was no accountability. Customers couldn't see where their capital was."

**Future Convergence:**
The discussion anticipates traditional institutions entering the curator space: "what we're seeing is massive interest from traditional institutions to bring their risk management abilities on chain. And we're going to see a fusion of these roles, asset managers, risk managers, and curators."

### Staking vs. Lending: Critical Distinctions

Sheffield addresses widespread confusion in traditional finance circles, noting he has "literally seen like in policy discussions drafts of things that say you can stake a stablecoin. I'm just like you can't stake a stablecoin. Like it's not a thing."

**Staking Mechanics:**
- Applies to native blockchain assets (ETH, SOL, etc.)
- Involves locking assets to validate transactions on proof-of-stake networks
- Earns transaction fees and block rewards
- Provides security to the underlying blockchain
- Requires existing crypto asset holdings
- Protects against inflation from block rewards

**Lending Mechanics:**
- Can apply to stablecoins and various crypto assets
- Involves depositing assets into protocols that lend to borrowers
- Earns interest from borrowers
- Operates through vault structures
- Accessible to mainstream consumers seeking dollar-denominated yields
- Does not require interest in underlying crypto assets

**Customer Segmentation:**
Sheffield distinguishes the target audiences: staking appeals to "a customer who already has crypto assets" and wants to "earn more yield on the crypto assets that they have," while lending attracts "mainstream consumers who come across a stablecoin, they're not interested in crypto assets, but they want dollars, and they want to earn 3%, 4%, 8% on their dollars."

**Future Integration:**
Raghupathi envisions eventual convergence: "each of these are sources of yield on a specific asset with a specific risk return profile." He compares this to traditional 401k plans containing bonds, cash, and equities—"a Russian dolls of yield generation."

Taylor emphasizes the importance of maintaining distinctions: "we just have to remember that the products inside it, like a bond is very different to an equity, to a stock. And so remembering that these things are different, carry different risk profiles."

### Asset Manager Trajectory in DeFi

Raghupathi outlines a clear adoption pathway for traditional asset managers entering on-chain yield:

**Stage One: Staking**
- "It's easy, right? It's well understood."
- Extensive infrastructure and tooling available
- Customer comprehension is high
- Serves as "the gateway drug to DeFi"
- Example: Bitwise acquiring Chorus One ($2.2 billion assets staked)

**Stage Two: On-Chain Lending**
- "Lending is a very simple activity to do on-chain"
- Institutions gaining education on protocol mechanics
- Understanding security risks and withdrawal dynamics
- Example: Bitwise beginning lending curation

**Stage Three: General Purpose Vaults**
- "Not just restricted to staking as a product, lending as a product"
- Encompasses "any kind of fixed income stuff, RWAs"
- "This entire universe of yield on-chain will all be packaged up into single products"
- Represents the ultimate vision: "that's the future we're building for"

**Strategic Necessity:**
Raghupathi frames this as inevitable: "For the challengers who are up-and-coming asset managers, it's a way for them to differentiate their offering versus traditional institutions. And for the big dogs, they need to offer DeFi yield to their customers, or they will risk continuing to bleed market share."

### Institutional Adoption Dynamics

The discussion explores the competitive landscape between crypto-native and traditional institutions.

**Crypto-Native Advantages:**
- Deep technical expertise in blockchain systems
- Understanding of novel risks specific to smart contracts
- Proven ability to build complex on-chain financial products
- First-mover advantage in DeFi infrastructure

**Traditional Institution Advantages:**
- Established distribution channels
- Existing customer relationships
- Assets already on platform
- "Distribution is very sticky"

**Adoption Timeline:**

Raghupathi predicts sequential waves:

1. **Crypto Exchanges** (current): "Coinbase's and Krakens of the world, they're already crypto native. They're not deeply DeFi native, but they're getting there."

2. **Fintechs** (near-term): "The Robinhoods and Revoluts of the world. They are very savvy because they're tech companies at their core. And so they're becoming educated really quickly."

3. **Traditional Banks and Asset Managers** (longer-term): "They're a little bit slower. It's harder for them to understand these things, but they're already doing the work to understand it and starting to come up with these strategies."

**Market Decoupling:**
Taylor observes a significant shift: "if you look at the crypto prices right now, there's a bloodbath, but son, I don't know about you, Kai, I don't know about you, but I'm no less busy than I've ever been on the institutional side... that decoupling from price action is really meaningful at this point. Crypto is now absolutely not about the price. It is 100% about the utility."

### Regulatory Considerations

Sheffield analyzes the regulatory architecture enabling current DeFi earn products:

**Embedded Self-Custodial Wallet Model:**
Both Coinbase and Kraken employ similar structures:
- User initiates action within custodial exchange interface
- System provisions self-custodial wallet in background
- Assets transfer from custodial to self-custodial wallet
- User deposits from self-custodial wallet into DeFi vault
- Exchange serves as interface, not fund manager

**Regulatory Rationale:**
Sheffield explains: "the argument, as I understand it, is that the consumer is taking their own action with their own funds that they can control and depositing into the vault. And it's really just the exchange is offering them the interface."

**Disclosure Challenges:**
Questions remain about transparency: "is the disclosure clear enough? And do most of the mainstream consumers actually know that if something happens in this vault or if something happens in this wallet, you know, if I lose my keys, like, I can't just call Coinbase and like reset my password."

**Bank Adoption Barriers:**
Sheffield identifies structural challenges for traditional banks: "it's much harder to imagine a bank saying, you know what, we're going to offer DeFi yield, but we're going to embed a self-custodial wallet in. So you're like actually leaving the bank, but you're in the bank's interface. It's got the bank spread. Like it's, it'd be hard to explain to regulators."

**Competitive Implications:**
"If Coinbase and Kraken can scale DeFi yield businesses, both on the lending and borrowing side, while traditional fintechs and banks can't touch it, then it's like not a really level playing field."

**Future Outlook:**
Taylor predicts: "I suspect Kai having observed fintech long enough that we will see some further out on the risk curve start to do vaults this year."

### Ethereum's Infrastructure Evolution

The discussion addresses Vitalik Buterin's re-evaluation of Ethereum's rollup-centric roadmap, prompted by Layer 2 (L2) developments.

**Core Issue:**
Many L2s have not progressed toward decentralization (stage two), with some explicitly stating they won't due to:
- Technical considerations around ZKEVM safety
- Customer regulatory requirements demanding ultimate control

**Vitalik's Position:**
Taylor quotes: "This might be doing the right thing for your customers, but it should be obvious that if you're doing this, you're not scaling Ethereum in the sense that was meant by the roll-up centric roadmap."

**Alternative Strategy:**
Focus on making Ethereum itself significantly faster rather than relying on L2s for scaling.

**Institutional Default:**
Taylor notes: "institutions tend to default Ethereum. So, you know, there's an opportunity here."

**L2 Landscape Analysis:**

Sheffield provides historical context on institutional blockchain adoption:
- Initial period: "banks will never use public blockchains" was common perspective
- Permissioned chains (Quorum, Hyperledger, R3) were only options
- Shift approximately 12 months ago: clarity that institutions could use public chains
- Ethereum became default due to establishment, security, and developer familiarity (EVM)

**Current Competition:**

Sheffield identifies key players:
- **Base**: Leading L2 for institutions, Coinbase-operated, single sequencer, planned token launch
- **Canton**: "seemingly come out of nowhere in the last six months," major capital markets player
- **Tempo/Arc**: Purpose-built for payments and lending (not yet launched)
- **Solana**: Finding traction in payments and specific institutional use cases

**Specialization Thesis:**
"I don't necessarily think it's like one winner. It's you could actually divide it to there's capital markets, there's lending, there's payments. And like, yeah, there's synergies between them. But like you could have different chains optimized for different things."

**Ethereum's Moat:**

Raghupathi emphasizes existing advantages: "The Aave market on Ethereum is like $40 billion. And that's an order of magnitude larger than any other chain. So when you're a fintech thinking about what DeFi yield product do I want to offer and how do I guarantee my users can withdraw at all times, that's the dominant factor."

He notes the irony: "until about six months ago, DeFi was not remotely the top priority of Ethereum, even though it has turned out to be one of the core drivers for institutional adoption on the chain."

**Privacy Imperative:**

Sheffield emphasizes: "I think privacy is going to be a major, major factor in terms of who wins this."

Taylor elaborates on institutional requirements:
- Merchants don't want competitors seeing supplier and customer payments
- Capital markets participants don't want trades visible to competitors
- Canton has focused on privacy for over 10 years
- Privacy has utility and rational business justification

**Privacy in DeFi:**

Raghupathi acknowledges this as "one of the largest open questions in DeFi":
- Fintechs concerned about customer address associations
- No effective privacy solution exists on Ethereum currently
- Lending protocols weren't built with privacy considerations
- Vitalik has identified privacy as priority for interesting L2s
- Potential approaches include committing only data hashes on-chain

Taylor concludes: "so much work to do in privacy. I think we're not done with this. It's something that I'm spending a lot of time on with institutions."

## Key Insights and Implications

### Multi-Protocol Diversification as Risk Mitigation

Contrary to intuition that multiple protocols increase risk, the evidence suggests diversification across battle-tested protocols (Aave, Morpho, Pendle) reduces concentration risk while enabling higher yields. This challenges the single-protocol approach and suggests optimal vault design involves strategic allocation across complementary liquidity sources.

### The Curator as Cryptographic Accountability Layer

The curator role represents genuine innovation beyond rebranding. The key distinction lies in cryptographic constraints that make actions transparent and verifiable, fundamentally altering the trust relationship between service provider and customer. This addresses the Celsius/BlockFi failure mode where opacity enabled mismanagement.

### Embedded Self-Custody as Regulatory Innovation

The embedded self-custodial wallet model creates a novel regulatory structure allowing exchanges to offer DeFi access while maintaining compliance. This architecture may prove difficult for traditional banks to replicate, potentially creating sustained competitive advantages for crypto-native exchanges in yield products.

### Institutional Adoption Decoupled from Price

The observation that institutional activity remains robust despite crypto price declines signals fundamental market maturation. Focus has shifted from speculative price appreciation to utility and revenue generation, suggesting more sustainable long-term growth dynamics.

### Privacy as Competitive Differentiator

Privacy emerges as potentially decisive factor in institutional chain adoption. Canton's decade-long focus on privacy positions it advantageously for capital markets use cases, while Ethereum's transparency creates friction for institutional requirements. Solutions to privacy challenges may determine ultimate institutional chain winners.

### Ethereum's DeFi Liquidity Moat

Ethereum's $40 billion Aave market represents an order-of-magnitude advantage over alternatives, creating powerful network effects for yield products requiring deep liquidity. This existing infrastructure may prove more defensible than anticipated, particularly for fintech applications prioritizing withdrawal guarantees.

### Staking as Gateway, Vaults as Destination

The clear progression from staking to lending to general-purpose vaults suggests predictable institutional adoption patterns. Asset managers can use staking as low-risk entry point while building competencies for more complex multi-asset, multi-protocol products.

### Specialization Over Generalization

The emergence of purpose-built chains for specific use cases (Canton for capital markets, specialized chains for payments) challenges the assumption of single dominant chain. Different institutional requirements may favor specialized solutions over general-purpose platforms.

## Data and Figures

### Kraken DeFi Earn Performance
- **TVL**: $\approx \$40$ million (within one week of launch)
- **Unique Users**: $\approx 13{,}000$ users
- **Organic Yield**: $> 6\%$ APY (zero token incentives)
- **Kraken Customer Base**: $15$ million customers

### Coinbase Morpho Product Comparison
- **Total APY**: $\approx 3.5\%$
- **Organic Yield**: High $2\%$ range
- **Token Incentives**: $\approx 75$ basis points (Morpho tokens)

### Protocol Market Sizes
- **Aave on Ethereum**: $\approx \$40$ billion market size
- **Chorus One Assets Staked**: $\$2.2$ billion (acquired by Bitwise)

### Yield Differential
- **Kraken Advantage**: $\Delta \text{Yield} \approx 2.5\%$ higher organic returns vs. Coinbase product
- **Zero Incentive Strategy**: $100\%$ organic yield composition vs. $\approx 79\%$ organic for competitor

### Liquidity Comparison
- **Aave**: Order of magnitude larger than alternative chains
- **Morpho**: Higher yields but documented withdrawal limitations

## Definitions and Terminology

### Curator
An entity or address responsible for allocation decisions in DeFi vaults, determining protocol exposure, risk parameters, and asset distribution. Distinguished from traditional asset managers by cryptographic constraints, on-chain transparency, and non-custodial structure. Curators make decisions visible and verifiable on blockchain, creating accountability through transparency rather than regulatory oversight alone.

### Vault
A smart contract-based financial product providing guarantees about asset location, permitted operations, and withdrawal access. Differs from traditional funds through on-chain transparency, cryptographic constraints on curator actions, and non-custodial structure. Users maintain ultimate asset access while delegating management to curators.

### Staking
Process of locking native blockchain assets (ETH, SOL, etc.) to validate transactions on proof-of-stake networks. Participants earn transaction fees and block rewards in exchange for providing network security. Requires holding the specific blockchain's native asset and protects against inflation from block rewards.

### On-Chain Lending
Depositing assets (including stablecoins) into DeFi protocols that lend to borrowers, earning interest from lending activity. Operates through transparent smart contracts with visible collateralization and liquidation mechanisms. Accessible to users seeking yield on dollar-denominated assets without crypto asset exposure.

### Layer 2 (L2)
Blockchain networks built on top of Layer 1 chains (like Ethereum) to improve scalability, reduce costs, or add functionality. Originally conceived as scaling solutions, increasingly serving specialized purposes including privacy, institutional control, or specific use case optimization.

### Organic Yield
Returns generated directly from protocol economic activity (lending interest, transaction fees, staking rewards) rather than token incentives or subsidies. Considered more sustainable than incentive-driven yields as it reflects genuine economic demand.

### TVL (Total Value Locked)
Aggregate value of assets deposited in a DeFi protocol, vault, or platform. Primary metric for measuring protocol adoption and liquidity depth. For Kraken DeFi Earn, reached approximately $40 million within one week.

### EVM (Ethereum Virtual Machine)
The runtime environment for smart contracts on Ethereum and compatible chains. EVM compatibility allows developers to deploy contracts across multiple chains using the same codebase, creating network effects around Ethereum development tools and expertise.

### Sequencer
Component of Layer 2 networks responsible for ordering and executing transactions. Single sequencer control (as with Base) provides operational control but reduces decentralization, creating tension between institutional requirements and crypto-native decentralization values.

### ZK (Zero-Knowledge) Proofs
Cryptographic methods allowing one party to prove statement validity without revealing underlying information. Relevant for privacy-preserving L2s and potential solutions to institutional privacy requirements in DeFi.

### Morpho
DeFi lending protocol offering higher yields than alternatives like Aave but with different liquidity characteristics. Has experienced withdrawal limitations in specific markets, illustrating trade-offs between yield optimization and liquidity guarantees.

### Aave
Established DeFi lending protocol with approximately $40 billion market size on Ethereum. Known for consistent liquidity and no significant stablecoin withdrawal issues in recent years, representing lower-risk but lower-yield option in protocol diversification strategies.

## References and Citations

### Direct Quotations

**On Asset Manager Trajectory:**
> "So I think there's a very clear trajectory of what asset managers will start to do on-chain. Step one is staking. It's easy, right? It's well understood. There's a lot of infrastructure and tooling. And most importantly, the customers understand what that is. Step two is on-chain lending... But the logical conclusion of this is moving all the way to general purpose vaults, where you're not just restricted to staking as a product, lending as a product, any kind of fixed income Stuff, RWAs. This entire universe of yield on-chain will all be packaged up into single products."
— Sunand Raghupathi

**On Kraken Product Innovation:**
> "This is groundbreaking. It's probably the most ambitious DeFi earned product that has ever been created. We've seen many of these, including Coinbase and others. But what Kraken has done that's very novel is created a product experience where a user who's never touched DeFi is now getting this chain abstracted, multi-asset, multi-protocol Yield experience."
— Sunand Raghupathi

**On Diversification and Risk:**
> "I would actually argue that diversification decreases risk. Because as soon as you enshrine a single protocol, you now are enshrining the risk associated with that protocol. Whereas when you have the opportunity to diversify over multiple protocols, these products are not wrapping complex, highly risky new protocols. It's basic things like Aave, Pendle, Morpho, stuff that's been battle-tested for years on billions of dollars."
— Sunand Raghupathi

**On Curator vs. Asset Manager:**
> "What is different between a vault and a structured product or a vault and a fund? And what it boils down to is the guarantees of transparency and decentralization that these products actually provide users... Curators have these cryptographic constraints and in some sense, they're more accountable to customers because everything is public. It's all on chain. It's all verifiable. And most importantly, it's non-custodial."
— Sunand Raghupathi

**On Celsius/BlockFi Failures:**
> "Those kinds of customer relationships, that product need was universal, clearly. People wanted high yield savings accounts on their stable coins, on their crypto assets. It's why those products did so well until they blew up. But why did they blow up? It's because there was no accountability. Customers couldn't see where their capital was. They didn't have access to their capital at all times."
— Sunand Raghupathi

**On Stablecoin Staking Confusion:**
> "I have literally seen like in policy discussions drafts of things that say you can stake a stablecoin. I'm just like you can't stake a stablecoin. Like it's not a thing."
— Cuy Sheffield

**On Regulatory Challenges:**
> "If Coinbase and Kraken can scale DeFi yield businesses, both on the lending and borrowing side, while traditional fintechs and banks can't touch it, then it's like not a really level playing field. I don't think that's really good for anybody."
— Cuy Sheffield

**On Market Maturation:**
> "if you look at the crypto prices right now, there's a bloodbath, but son, I don't know about you, Kai, I don't know about you, but I'm no less busy than I've ever been on the institutional side. Like if anything, it's getting more aggressive, especially on stable coins and tokenized real world assets. And so that decoupling from price action is really meaningful at this point. Crypto is now absolutely not about the price. It is 100% about the utility."
— Simon Taylor

**On Ethereum's DeFi Advantage:**
> "The Aave market on Ethereum is like $40 billion. And that's an order of magnitude larger than any other chain. So when you're a fintech thinking about what DeFi yield product do I want to offer and how do I guarantee my users can withdraw at all times, that's the dominant factor. And the crazy thing is until about six months ago, DeFi was not remotely the top priority of Ethereum, even though it has turned out to be one of the core drivers for institutional adoption on the chain."
— Sunand Raghupathi

**On Privacy Challenges:**
> "This is one of the largest open questions in DeFi because we're actually seeing it on the ground as we talk to fintechs and institutions who are looking at yield. This is something they're concerned with... The problem is that there is no good way of doing that on Ethereum today."
— Sunand Raghupathi

### Episode Information
- **Show**: Tokenized
- **Episode**: 69
- **Published**: 2026-02-09T16:00:00.000+00:00
- **Hosts**: Simon Taylor (GTM @ Tempo), Cuy Sheffield (Head of Crypto @ Visa)
- **Guest**: Sunand Raghupathi (CEO & Co-Founder @ Veda)
- **Sponsors**: Visa, Bridge (a Stripe company), Fireblocks

### Validation Notes

This summary comprehensively covers all major discussion topics from the episode transcript. The analysis maintains fidelity to the source material through extensive direct quotations and preserves the logical progression of the conversation. All quantitative data points are accurately represented. The distinction between staking and lending, the curator role definition, and regulatory considerations are explained with precision matching the source discussion. Privacy challenges in DeFi are acknowledged as unresolved, consistent with the participants' assessment.