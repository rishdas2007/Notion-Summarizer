# Is the DeFi Mullet Strategy the Best Way to Bring Finance Onchain?

**Citation:** "Is the DeFi Mullet Strategy the Best Way to Bring Finance Onchain?." *Unchained*, 13 Mar. 2026,


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Maple Finance's Hybrid Institutional Model](#maple-finances-hybrid-institutional-model)
   - [Morpho's Infrastructure-First Approach](#morphos-infrastructure-first-approach)
   - [The DeFi Mullet Strategy](#the-defi-mullet-strategy)
   - [Morpho V2: Market-Driven Rates and Fixed Terms](#morpho-v2-market-driven-rates-and-fixed-terms)
   - [Governance and Organizational Structure](#governance-and-organizational-structure)
   - [Multi-Chain Strategy and Future Outlook](#multi-chain-strategy-and-future-outlook)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [References and Citations](#references-and-citations)

## Executive Summary

This episode of Unchained explores how institutional finance is quietly integrating with decentralized finance (DeFi) protocols through what has been termed the "DeFi mullet" strategy—centralized, user-friendly front-ends powered by on-chain infrastructure. The conversation features Sid Powell, CEO of Maple Finance, and Paul Frambot, co-founder of Morpho, two protocols at the center of this transformation.

**Main Arguments:**

1. **Institutional adoption is accelerating**: Major traditional finance players including Cantor Fitzgerald, Apollo Global Management, and Coinbase are building financial products on DeFi rails, signaling a fundamental shift in how institutional lending operates.

2. **The DeFi mullet model works when specific conditions are met**: Success requires account abstraction, protocol immutability (control without trust assumptions), and access to global liquidity networks. The model allows distributors to own infrastructure end-to-end while maintaining user experience parity with traditional products.

3. **Different protocols serve different niches**: Maple operates as a hybrid between CeFi and DeFi, focusing on institutional borrowers with off-chain legal agreements and on-chain capital sourcing. Morpho provides infrastructure for others to build non-custodial lending products, positioning itself as rails rather than a product.

4. **Fixed-rate, fixed-term lending is the missing piece**: Current DeFi lending relies on algorithmic variable rates, but institutional and retail users need predictability. Morpho's V2 introduces market-driven pricing and term structures, bringing DeFi closer to traditional finance practices.

5. **Governance structures matter**: Traditional DAO governance proves too slow for competitive markets. Morpho's approach minimizes governance to treasury and fee decisions, with an immutable protocol and externalized risk management, while avoiding a separate labs entity.

**Key Objectives:**

- Demonstrate how institutional capital is flowing into on-chain lending
- Explain the technical and strategic requirements for successful DeFi integration with traditional finance
- Contrast different approaches to on-chain lending (Maple's hybrid model vs. Morpho's infrastructure model)
- Identify limitations of current DeFi lending and how next-generation protocols address them

## Detailed Analysis

### Maple Finance's Hybrid Institutional Model

Maple Finance occupies a unique position in the DeFi lending landscape by operating as a hybrid between centralized finance (CeFi) and decentralized finance (DeFi). As Sid Powell explains, "we source capital on chain. We have Syrup USDC, Syrup USDT, which folks can deposit to through smart contracts. However, when we do loans with our institutional borrowers, we sign off-chain legal agreements with them. And then we can also accept collateral into qualified custodians."

**Target Market and Operations:**

Maple does not serve retail users. Instead, its clients include:
- Asset managers running yield or liquid token strategies
- Trading firms and exchanges
- Prime brokers providing margin and settlement services
- Family offices with significant crypto holdings

Loan sizes range from $10 million minimum to a maximum of $500 million (executed just before Christmas, according to Powell). Borrowers post collateral in major cryptocurrencies including Bitcoin, ETH, Solana, or XRP, providing protection against credit losses.

**Business Model:**

The hybrid approach allows Maple to combine the capital efficiency of on-chain sourcing with the legal certainty and institutional comfort of off-chain agreements. This structure addresses a key friction point: institutional borrowers often require traditional legal frameworks while lenders seek the transparency and efficiency of blockchain-based systems.

**Growth Trajectory and AI Integration:**

Powell outlines a three-stage vision for scaling operations through AI:

- **Stage 1 (Current)**: AI assists with data extraction from documents and basic analysis
- **Stage 2**: AI handles initial loan structuring and term sheet generation
- **Stage 3**: Senior underwriters manage AI agents that handle negotiation, settlement, servicing, and collections

This automation strategy aims to enable Maple to manage multiples of current volume ($4 billion AUM as of the interview) without proportional headcount increases, improving unit economics.

**Revenue Goals:**

Maple targets $100 million in annual recurring revenue (ARR) for 2026, up from approximately $30 million at the time of recording. This requires:
- Scaling AUM from $4 billion to $15-20 billion
- Increasing utilization rates through expanded borrower relationships
- Entering new markets like on-chain private credit

Powell notes that Maple rose from fourth to second-ranked institutional lender (behind Tether) in Q4, suggesting market share gains are achievable.

### Morpho's Infrastructure-First Approach

Paul Frambot positions Morpho fundamentally differently from traditional DeFi lending protocols. "Morpho is an infrastructure for people to build their own on-chain lending and borrowing use cases. We don't manage like assets or issue loans ourselves as a DAO or as an entity. Instead, we provide people with a stack that they configure the way they want."

**The Coinbase Integration:**

The Morpho-Coinbase partnership exemplifies the DeFi mullet strategy. Coinbase previously offered centralized lending with limited liquidity and rates constrained by its balance sheet. By integrating Morpho's infrastructure:

- Coinbase users can borrow against Bitcoin to purchase houses or spend via Coinbase card
- Behind the scenes, wallets are created for users (abstracted away from the UX)
- Liquidity comes from global sources including other exchanges (BitPanda, Binance, OKEx)
- Users experience "complete feature parity with your traditional product, except that this time it's super powered by Web3 infrastructure"

The integration has generated over $2 billion in total loans since launching approximately one year prior to the interview. Frambot notes this met expectations, though he characterizes the ambitions as "bigger."

Critically, Coinbase also launched the lending side, creating an internal flywheel: "the more lenders they get on one end, the better the product is going to be for the borrower, right? And vice versa, like the more borrowers come in, the more interest are paid to the lenders."

**Vault Architecture and Curators:**

Morpho's technical architecture centers on "vaults"—non-custodial savings products managed by curators. Frambot explains: "If you think of the stablecoin as the checking account, the Morpho vault is the savings account."

Key participants:
- **Distributors** (e.g., Coinbase): Provide user interface and customer relationships
- **Curators** (e.g., Steakhouse Financial for Coinbase, Bitwise for their own vault): Manage asset allocation, underwriting decisions, and risk parameters
- **Morpho Protocol**: Provides immutable infrastructure connecting all parties

This differs fundamentally from Compound or Aave, where "it's more of a DAO that is operating like the risk parameters. Here it's the free market. Anyone can come in, create their own vault, you know, and if you have risk management capabilities, you can basically discover who is eligible to basically receive funding from you."

**Traditional Finance Integration:**

The Apollo Global Management deal represents a significant milestone. Apollo committed to acquiring up to 90 million Morpho tokens (approximately 9% of supply) over 48 months, and Apollo Crypto uses Morpho in its MEVUSD product. While Frambot could not disclose specifics, he frames this as part of a broader trend: "now fintechs that have not much to do with crypto are going to come on chain to power their financial services."

The evolution Frambot describes: "The V2 of the DeFi mullet is basically going to be fintechs that are running on-chain products that can be run by TradFi, traditional finance with the traditional finance trust and expertise."

### The DeFi Mullet Strategy

The term "DeFi mullet" describes products with centralized, user-friendly front-ends ("business in the front") and decentralized, on-chain infrastructure ("party in the back"). Frambot identifies three essential requirements for this model to succeed:

**1. Account Abstraction:**

"You need the core piece of infrastructure that the distributor needs is account abstraction, you know, so having your own wallet that has capabilities that you can spin off for every single one of your users." 

Distributors managing user funds should create self-custody wallets for each user, hidden from the user experience. Services like Privy from Stripe or Fireblocks provide this capability, enabling access to on-chain infrastructure without exposing users to blockchain complexity.

**2. Control and Immutability:**

"Distributors want infrastructure that they can own and that they can control. They want to control the code, they want to control the compliance, they want to control the risk, the fees, everything."

This translates to specific technical requirements:
- **Immutable code**: "Having your code being immutable, not relying on someone that can upgrade it and change the parameters of it, where you have billions of dollars of your own users, is very, very important for them."
- **No external governance dependencies**: Distributors cannot rely on DAO votes or external parties to manage risk parameters when they have fiduciary responsibility to users
- **End-to-end ownership**: After a decade of owning distribution but not infrastructure (relying on TradFi), distributors view DeFi as an opportunity to control the full stack

Frambot emphasizes: "You want a DeFi infrastructure, not a DeFi product."

**3. Openness and Global Networks:**

"Why moving on-chain in the first place? Well, you need the financial product to be better. And how do you have the financial product that is better? By aggregating intents from all over the world."

The value proposition: "The reason we have every single exchange like, you know, plugged into Morpho, whether that is like crypto.com, Gemini, Coinbase, Kraken, OKEx, Binance, everybody is moving there is because we connect everybody."

This creates a network effect where "you move from a world where everybody has their own backend with their own exchange that is segregated with segregated liquidity to a world where everything is globalized. And as a result, you get much better financial products because it's more efficient, get better prices, again, deeper liquidity, etc."

**When the Model Works:**

The DeFi mullet strategy makes strategic sense when:
- Users need familiar UX but benefit from on-chain efficiency
- Distributors want infrastructure ownership without building from scratch
- Global liquidity aggregation provides meaningful competitive advantage
- Regulatory clarity allows on-chain operations with proper compliance layers

### Morpho V2: Market-Driven Rates and Fixed Terms

Morpho's upcoming V2 represents a fundamental evolution in DeFi lending design. Frambot identifies the core limitation of current systems: "We externalize the risk management, we don't externalize the rate management."

**The Problem with Algorithmic Rates:**

Since Compound's innovation years ago, DeFi lending has relied on formulaic interest rates based on pool utilization. Frambot acknowledges this was "a beautiful innovation" given constraints of early DeFi (no sophisticated market participants, low liquidity, high gas costs).

However: "Talking to a lot of TradFi players, like frankly, this is what I've been doing for the last year and a half, is absolutely not the way things are done in TradFi. And there's, you know, 30 years of innovation behind them. There's a reason they do the way they do things. They want expressivity and control on the price for the risk."

The fundamental issue: "If you are underwriting people, and it seems obvious when you say this, but you need to basically set the price yourself."

**V2 Innovations:**

1. **Market-Driven Pricing**: Asset managers (curators) can set their own rates rather than relying on algorithmic formulas, allowing them to price risk based on their underwriting expertise.

2. **Fixed-Rate, Fixed-Term Lending**: "The key missing piece in lending today was a term structure where you can have fixed rate, fixed term lending and borrowing."

This addresses both infrastructure and product needs:
- **Infrastructure perspective**: Enables sophisticated lending strategies matching TradFi practices
- **Product perspective**: "When we get integrated into those large distribution platforms, the number one feedback that we get is the rate is variable. Like, you know, I'm buying a house right now. Like, I can't have a variable rate to buy a house, right?"

3. **Liquidity Profiles**: Users can choose between liquidity and yield. Frambot notes that current DeFi operates under the assumption that "this is only up technology unless you get hacked in case you go to zero. And DeFi protocols can never lose money and you can always exit."

But "that's not the reality of financing. In finance, the reality is that sometimes people don't repay and sometimes there is bad debt. Or sometimes people need money to borrow for more than one block. And they effectively need to borrow for 20 years for long-term financing."

**User Experience Changes:**

For lenders: "As a user, you could still be able to earn yield on your stablecoin, right? And you'll still have a vault that provides you a very liquid experience."

For borrowers: "Borrowers can borrow fixed rate, right? And so you can lock in a specific term and a specific fixed rate."

For asset managers: "They have now more levers to pull to be able to provide better interest rate, better liquidity. And this is basically issuing those fixed-term, fixed-rate loans."

The architecture maintains liquid savings products for end users while enabling sophisticated term lending underneath, managed by professional curators.

### Governance and Organizational Structure

The conversation addresses a critical challenge facing DeFi protocols: governance structures that enable both speed and trust. Frambot explicitly rejects the traditional DAO model for Morpho's core protocol.

**Why Morpho Avoided Traditional DAO Governance:**

"In the case of Morpho, the protocol in itself, the product in itself, has no use of governance or token. We're just a piece of code, right? We're just an immutable piece of code like Uniswap."

The reasoning: "The protocol is the most decentralized you could think of. Like, I can't even change the protocol. No one can. Like there's no, you know, oracle that I need to change or update. Those are like the asset, you know, the asset curators that are choosing those risk parameters. I don't update the risk parameters, right?"

This contrasts sharply with protocols like Aave, which face challenges with DAO governance speed. Frambot notes that Stani Kulechov of Aave Labs has written about how temperature checks and voting periods prevent nimble responses.

**The Token Model:**

"Really what the Morpho token was about is owning a share of the network value of the protocol."

Frambot explains the value creation: "Morpho aggregates a bunch of lenders with a bunch of partners, right? Forms the state of the smart contract. So it's a piece of code that has a specific state, right? And this is an act of value creation. You bring together two sides of the market that were not knowledgeable of each other."

The protocol can charge fees for this value creation, and "the owner of that fee, the owner of the treasury, is a set of token holders that have programmatic control over this value."

**Foundation vs. Labs Entity:**

Morpho operates only through a foundation, without a separate labs entity. Frambot frames this as alignment: "We believe in tokens, generally, more than we do in equity. We believe this is the best way to own a share of a decentralized network."

The advantages:
- **Programmable ownership**: "You're able to distribute ownership in that network in such a way that you can incentivize growth of that network, whether that is through incentives to distributors, to lenders, to borrowers, etc."
- **Minimal structure**: "We're just like a French foundation that is researching about what should be the next version of the protocol and publishing this code on chain and giving ownership to token owners."

**Competitive Positioning:**

Frambot explicitly rejects the framing of Aave as a competitor: "I don't think Aave as a competitor to Morpho. I know a lot of people like to compare the two because there is a word lending somewhere. But I think of Aave aspiring to become like the JP Morgan of the world, whereas Morpho aspires to become infrastructure for JP Morgan."

He notes that Compound, formerly an Aave competitor, now builds on Morpho with its own vaults. "Aave could build on Morpho as well, leveraging like Morpho's technology and everything to manage their assets through their DAO."

This infrastructure positioning allows Morpho to serve multiple asset managers simultaneously, including potential competitors to each other, all using the same underlying rails.

### Multi-Chain Strategy and Future Outlook

**Current Deployment:**

Morpho V1 operates on almost 40 chains, many of them Ethereum L2s. V2 will launch on multiple chains as well. Frambot explains the ease of deployment: "For us, deploying on a chain is easy, right? We are just an immutable piece of software that anyone can come in and deploy permissionlessly to operate."

**Chain Landscape Evolution:**

Frambot describes the industry's progression through several phases:

1. **Ethereum only**: Single-chain dominance
2. **Multi-chain emergence**: Ethereum, OP Mainnet, Arbitrum, Solana—"five, six players"
3. **Proliferation**: "We're going to have a myriad of chains, and we started deploying a bunch of chains everywhere"
4. **Consolidation (current view)**: "You're probably going to have five, six dominant chains for quite a while. And then you're going to have a bunch of very small chains for dedicated enterprises."

Expected dominant chains include Tempo, Base, Ethereum mainnet, Robinhood chain, "and a few others."

**Long-Term Convergence:**

"I think over time we're going to go through cycles of bundling, and unbundling, and bundling, and unbundling until maybe one day we have one single atomic world computer that scales to infinite throughput."

Frambot observes that all major chains are converging on similar architectures: "When you look at Solana's roadmap, Ethereum's roadmap, Arbitrum, Optimism, they all converge to the same idea of having some form of sharded computer, whether you call this a multi-core, a super chain, shards, it's basically the same thing, right?"

**Path Dependency and Moats:**

However, consolidation will take time due to distributor lock-in: "There is so much path dependency with distributors. Some distributors are married to some chains, you know, Robinhood was Robinhood chain, Coinbase was Base, Stripe was Tempo. And so this is going to create such a moat that's going to take, you know, ages, like 10 years to re-aggregate."

**Ethereum Foundation Shift:**

When asked about the Ethereum Foundation's shift away from an L2-centric roadmap toward scaling L1, Frambot's multi-chain agnosticism provides flexibility: "We're much more agnostic of where we deploy, as long as you're EVM compatible and your chain has the most recent version of the EVM and practical constraints like this."

This infrastructure positioning allows Morpho to adapt to whatever chain landscape emerges without betting on specific winners.

## Key Insights and Implications

### 1. Infrastructure vs. Product Positioning Creates Different Competitive Dynamics

Morpho's explicit positioning as infrastructure rather than a lending product fundamentally changes its competitive landscape. By enabling others (including potential competitors like Compound) to build on its rails, Morpho can capture value from the entire ecosystem rather than competing for market share in specific lending markets. This mirrors successful infrastructure plays in traditional tech (AWS, Stripe) where the platform provider benefits from ecosystem growth regardless of which specific applications succeed.

### 2. The DeFi Mullet Requires Specific Technical Prerequisites

The success of centralized-front-end, decentralized-backend products depends on three non-negotiable requirements: account abstraction, protocol immutability (control without trust), and global liquidity networks. This framework provides a clear test for whether a given DeFi protocol can successfully integrate with traditional distributors. Protocols lacking any of these three elements will struggle to attract institutional partners regardless of other features.

### 3. Fixed-Rate Lending Is Not Optional for Mass Adoption

The consistent feedback from distributors that variable rates are unsuitable for real-world use cases (home purchases, business planning) reveals a fundamental product-market fit gap in current DeFi. Morpho V2's introduction of fixed-rate, fixed-term lending addresses this, but the broader implication is that DeFi protocols optimized for crypto-native users may require substantial redesign to serve mainstream financial needs.

### 4. Governance Minimization May Be More Sustainable Than DAO Optimization

Rather than attempting to make DAO governance faster or more efficient, Morpho's approach eliminates governance from protocol operations entirely, restricting it to treasury and fee decisions. This suggests that the industry's focus on improving DAO governance may be solving the wrong problem—the real solution may be designing protocols that don't require ongoing governance for core operations.

### 5. Traditional Finance Expertise Will Operate On-Chain Infrastructure

Frambot's vision of "TradFi operators running on-chain services" represents a significant shift from DeFi's crypto-native origins. The Apollo deal and similar partnerships suggest that on-chain infrastructure will increasingly be operated by traditional financial institutions bringing decades of risk management expertise, while crypto protocols provide the rails. This division of labor may prove more sustainable than expecting crypto-native teams to develop institutional-grade risk management capabilities.

### 6. AI Integration Will Determine Institutional Lending Scale

Maple's three-stage AI roadmap reveals that human underwriting capacity is a binding constraint on institutional lending growth. The ability to automate underwriting, servicing, and collections through AI agents will determine which protocols can scale to manage tens of billions in AUM without proportional cost increases. This suggests that AI capabilities may become a key competitive differentiator in institutional DeFi.

### 7. Multi-Chain Fragmentation Will Persist Due to Distributor Lock-In

Despite technical convergence toward similar architectures, Frambot's observation about distributor path dependency suggests that chain fragmentation will persist longer than technical considerations alone would predict. Protocols must maintain multi-chain strategies not because of technical necessity but because major distributors (Coinbase/Base, Robinhood/Robinhood chain, Stripe/Tempo) have committed to specific chains for strategic reasons.

### 8. The Hybrid Model Addresses Institutional Comfort Without Sacrificing Efficiency

Maple's combination of on-chain capital sourcing with off-chain legal agreements and qualified custodians demonstrates that full decentralization may not be necessary or desirable for institutional adoption. The hybrid approach provides the legal certainty institutions require while capturing the capital efficiency benefits of on-chain operations, suggesting that pragmatic combinations of CeFi and DeFi elements may outperform purist approaches.

## Data and Figures

### Maple Finance Metrics

- **Current AUM**: Approximately $4 billion
- **Loan size range**: $10 million (minimum) to $500 million (maximum, executed before Christmas)
- **Current ARR**: Just over $30 million
- **Target ARR for 2026**: $100 million (requiring 3-4x growth)
- **Required AUM for target**: $15-20 billion
- **Market position**: Rose from 4th to 2nd ranked institutional lender in Q4 (behind Tether)
- **Collateral types**: Bitcoin, ETH, Solana, XRP, and other large-cap cryptocurrencies

### Morpho Metrics

- **Coinbase integration total loans**: Over $2 billion (approximately one year after launch)
- **Apollo token commitment**: Up to 90 million Morpho tokens (approximately 9% of total supply) over 48 months
- **Deployment scale**: V1 on almost 40 chains, primarily Ethereum L2s
- **Integration partners**: Coinbase, Bitwise, Steakhouse Financial, crypto.com, Gemini, Kraken, OKEx, Binance, and others

### Growth Calculations

For Maple to achieve $100 million ARR from current $30 million:

$$\text{Required Growth Factor} = \frac{100}{30} \approx 3.33\text{x}$$

For AUM scaling:

$$\text{Target AUM} = \text{Current AUM} \times \text{Growth Factor} = 4\text{B} \times 3.33 \approx 13.3\text{B to }20\text{B}$$

The range accounts for varying utilization rates and expansion into new markets like private credit.

## Definitions and Terminology

**DeFi Mullet**: A product design pattern featuring centralized, user-friendly front-ends ("business in the front") with decentralized, on-chain infrastructure ("party in the back"). Users experience traditional fintech UX while transactions execute on blockchain rails.

**Account Abstraction**: Technology enabling the creation of smart contract wallets with programmable features, hidden from end users. Allows distributors to provide self-custody solutions without exposing users to blockchain complexity (private keys, gas fees, etc.).

**Vault (Morpho context)**: A non-custodial savings product that aggregates capital from lenders and allocates it across multiple lending markets. Managed by a curator who makes underwriting and allocation decisions.

**Curator**: An entity or individual responsible for managing a Morpho vault, including decisions about which borrowers to underwrite, acceptable collateral types, interest rates, and risk parameters. Examples include Steakhouse Financial and Bitwise.

**Immutable Protocol**: Smart contract code that cannot be upgraded or modified after deployment. Provides certainty to users and integrators that protocol behavior will not change, eliminating governance risk for core functionality.

**Utilization Rate**: The percentage of available capital that is actively deployed in loans. Higher utilization generates more interest income but reduces liquidity for lenders to withdraw.

**AUM (Assets Under Management)**: Total value of capital managed by a protocol or platform, regardless of whether it is currently deployed in loans.

**ARR (Annual Recurring Revenue)**: Annualized revenue from ongoing operations, typically calculated by multiplying current monthly or quarterly revenue by 12 or 4 respectively.

**Fixed-Rate, Fixed-Term Lending**: Loans with predetermined interest rates and maturity dates, as opposed to variable-rate perpetual loans common in current DeFi. Provides predictability for borrowers and enables traditional financial planning.

**Term Structure**: The relationship between interest rates and loan maturities across different time periods (e.g., 1-month, 3-month, 1-year, 5-year rates). Essential for sophisticated financial markets.

**Qualified Custodian**: A regulated entity authorized to hold client assets, providing institutional-grade security and legal protections. Used by Maple for collateral storage.

**Prime Broker**: A financial institution providing bundled services to institutional clients, including margin lending, securities lending, and trade settlement.

## References and Citations

### Direct Quotations

**On Maple's Hybrid Model:**
> "We source capital on chain. We have Syrup USDC, Syrup USDT, which folks can deposit to through smart contracts. However, when we do loans with our institutional borrowers, we sign off-chain legal agreements with them. And then we can also accept collateral into qualified custodians." — Sid Powell

**On Morpho's Infrastructure Positioning:**
> "Morpho is an infrastructure for people to build their own on-chain lending and borrowing use cases. We don't manage like assets or issue loans ourselves as a DAO or as an entity. Instead, we provide people with a stack that they configure the way they want." — Paul Frambot

**On the DeFi Mullet Value Proposition:**
> "Complete feature parity with your traditional product, except that this time it's super powered by Web3 infrastructure, which allows you for, you know, again, deeper liquidity, better pricing is mostly what it brings you." — Paul Frambot

**On Control Requirements:**
> "Distributors want infrastructure that they can own and that they can control. They want to control the code, they want to control the compliance, they want to control the risk, the fees, everything." — Paul Frambot

**On Traditional Finance Integration:**
> "The V2 of the DeFi mullet is basically going to be fintechs that are running on-chain products that can be run by TradFi, traditional finance with the traditional finance trust and expertise." — Paul Frambot

**On Fixed-Rate Necessity:**
> "When we get integrated into those large distribution platforms, the number one feedback that we get is the rate is variable. Like, you know, I'm buying a house right now. Like, I can't have a variable rate to buy a house, right?" — Paul Frambot

**On Governance Philosophy:**
> "The protocol is the most decentralized you could think of. Like, I can't even change the protocol. No one can. Like there's no, you know, oracle that I need to change or update. Those are like the asset, you know, the asset curators that are choosing those risk parameters. I don't update the risk parameters, right?" — Paul Frambot

**On Competitive Positioning:**
> "I don't think Aave as a competitor to Morpho. I know a lot of people like to compare the two because there is a word lending somewhere. But I think of Aave aspiring to become like the JP Morgan of the world, whereas Morpho aspires to become infrastructure for JP Morgan." — Paul Frambot

### Episode Information

- **Show**: Unchained
- **Host**: Laura Shin
- **Published**: 2026-03-13T21:12:00.000+00:00
- **Guests**: 
  - Sid Powell, CEO & Co-Founder of Maple Finance
  - Paul Frambot, Co-Founder & CEO at Morpho Labs

### Sponsor

- Nexo (premier digital wealth platform)

### Disclaimer

As stated in the episode: "Nothing you hear on Unchained is investment advice. This show is for informational and entertainment purposes only, and my guest tonight may hold assets discussed in the show."