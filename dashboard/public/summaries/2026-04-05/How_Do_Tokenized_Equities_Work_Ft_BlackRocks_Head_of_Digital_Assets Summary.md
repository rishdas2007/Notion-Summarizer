# How Do Tokenized Equities Work? Ft. BlackRock's Head of Digital Assets

**Citation:** "How Do Tokenized Equities Work? Ft. BlackRock’s Head of Digital Assets." *Tokenized*, 30 Mar. 2026, <https://tokenized.simplecast.com/episodes/how-do-tokenized-equities-work-ft-blackrocks-head-of-digital-assets-PFS1lT0d>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Tokenization as Financial Access Infrastructure](#tokenization-as-financial-access-infrastructure)
   - [Three Structural Models for Tokenized Equities](#three-structural-models-for-tokenized-equities)
   - [Transferability Constraints and Regulatory Compliance](#transferability-constraints-and-regulatory-compliance)
   - [24/7 Trading and Market Structure Evolution](#247-trading-and-market-structure-evolution)
   - [Stablecoins vs. Tokenized Deposits: Distinct Products](#stablecoins-vs-tokenized-deposits-distinct-products)
   - [Bank Consortiums and Infrastructure Development](#bank-consortiums-and-infrastructure-development)
   - [Privacy Requirements in Capital Markets](#privacy-requirements-in-capital-markets)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Definitions and Terminology](#definitions-and-terminology)
5. [References and Citations](#references-and-citations)

## Executive Summary

This episode of Tokenized features a panel discussion with Robert Mitchnick (Head of Digital Assets at BlackRock), Rob Hadick (GP at Dragonfly), and Noah Levine (Partner at Andreessen Horowitz) examining the practical implementation of tokenized equities and digital assets. The conversation centers on three primary themes:

**Core Argument**: Tokenization represents an access story rather than merely an efficiency improvement, enabling crypto-native investors to access traditional financial instruments while maintaining their preferred digital infrastructure.

**Key Points**:
- Three distinct models for tokenized equities exist: SPV structures, tokenized entitlements, and fully on-chain native issuance, each with different tradeoffs regarding ownership, transferability, and composability
- Whitelisting requirements for AML compliance remain a significant friction point preventing full liquidity and DeFi integration
- Stablecoins and tokenized deposits serve fundamentally different user bases and use cases, with stablecoins focused on crypto capital markets and international dollar access, while tokenized deposits target wholesale banking efficiency
- 24/7 trading infrastructure requires tokenized assets to enable proper hedging and collateral management outside traditional market hours
- Privacy solutions are becoming critical for institutional capital markets activity on-chain, though demand has been limited to date

The discussion reveals an industry in transition, with major financial institutions and exchanges actively developing tokenized securities platforms while navigating regulatory uncertainty and technical implementation challenges.

## Detailed Analysis

### Tokenization as Financial Access Infrastructure

BlackRock CEO Larry Fink's 2026 annual letter positioned tokenization as enabling investment access comparable to payment simplicity. Robert Mitchnick elaborated that this represents a shift from viewing tokenization primarily as an efficiency story to recognizing its potential as an **access story**. 

Mitchnick explained: "The idea is that tokenization, which we so often talked about as this efficiency story, is actually, in many respects, potentially even bigger as an access story, where you have this universe of investors who are crypto native, or they're more predisposed towards digital wallets and interacting in the digital assets and DeFi ecosystem. And today they're under allocated, maybe 0% allocated to traditional investments."

The scale of this opportunity is significant: approximately $3 trillion exists in crypto assets compared to $400-500 trillion in total global assets. Tokenization could enable crypto-native investors to build "complete diversified whole portfolios" beyond their current crypto-only allocations.

Rob Hadick provided a complementary perspective focused on **form factor standardization**. He noted that stablecoins have achieved global adoption as "digital oil for a movement of money across different tokenized assets." When assets share the same form factor as stablecoins, swapping between them becomes substantially easier. This contrasts with current cross-border equity access, which requires extensive regulatory licensing and infrastructure that can be "quite costly" for emerging market participants.

Hadick distinguished between current stopgap solutions and true tokenization: "We've seen a lot of people get around this by, you know, if you look at the way like Robinhood is doing some of their, quote unquote, tokenized equity exposure. These are basically derivatives on some sort of US broker dealer that is buying an equity during normal market hours." These derivatives cannot be minted or redeemed during certain periods, meaning they lack the true form factor equivalence that native tokenization would provide.

### Three Structural Models for Tokenized Equities

Noah Levine provided a systematic categorization of tokenized equity structures currently in market:

**1. SPV (Special Purpose Vehicle) Structures**

New SPVs are established to acquire equity, then tokenize the SPV itself and distribute tokens to investors. The primary value proposition is directional exposure to the underlying stock. However, significant challenges exist:

- **Pricing mismatch risk**: When SPV tokens trade 24/7 but underlying markets operate only during specific hours, pricing discrepancies can emerge
- **Ownership risk**: Investors own the SPV rather than the underlying asset directly, creating additional counterparty and structural risks
- **Hedging limitations**: Market makers face difficulty hedging exposure during periods when underlying markets are closed

**2. Tokenized Entitlements**

This model, exemplified by DTCC initiatives and the NYSE-Securitize partnership, involves assets originated off-chain that are subsequently tokenized. Investors with wallets can hold and trade these tokenized entitlements.

Benefits include:
- 24/7 trading capability
- Some degree of composability with DeFi protocols
- Improved efficiency for asset movement

Levine noted "there's still room for improvement" in this category, suggesting it represents an intermediate step rather than the final form.

**3. Fully On-Chain Native Issuance**

Companies like SuperState and Figure are issuing new securities (Q-SIPs) directly on-chain. This represents the most complete form of tokenization, where "by owning this asset, you actually own the underlying stock."

Advantages include:
- Cross-collateralization capabilities
- Direct governance and voting rights
- Full composability with on-chain financial infrastructure
- No dependency on off-chain reconciliation

This model represents "real on-chain origination" rather than merely tokenizing existing assets.

### Transferability Constraints and Regulatory Compliance

Robert Mitchnick clarified an important technical distinction regarding BlackRock's BUIDL fund: "To be clear, what we did with Biddle was not a SPV, was not a feeder fund. That was natively a de novo fund, and the shares are issued directly as tokens."

However, he identified **whitelisting as a critical limitation**: "The transferability, though, is still subject to private fund rules as well as the AML obligations that come with them as an issuer. So tokens are freely transferable between whitelisted parties, right? And that obviously remains a big sticking point and a challenge in terms of truly unlocking the utility in this space."

The friction created by whitelisting requirements:
- Undermines liquidity by requiring pre-approval for transfers
- Limits usability in DeFi protocols that assume permissionless composability
- Creates operational overhead for compliance processes

Mitchnick emphasized the industry is "working through how to solve that in a way that isn't just pure regulatory arbitrage and hope that you can beg forgiveness later kind of strategy."

Noah Levine outlined a two-part path forward:

1. **Regulatory clarity**: Recent SEC guidance represents progress, but comprehensive frameworks remain incomplete. Questions around compliance procedures and anti-money laundering implementation require further specification.

2. **Liquidity infrastructure scaling**: Current solutions like SuperState and Figure require external Alternative Trading Systems (ATS) to provide liquidity. While functional temporarily, these systems "will ultimately need to scale in order to be used in a more institutional context."

### 24/7 Trading and Market Structure Evolution

The NYSE-Securitize partnership announcement revealed plans for a 24/7 tokenized securities platform, with Securitize designated as the first digital transfer agent eligible to mint blockchain-native securities for corporate or ETF issuers.

Rob Hadick explained the fundamental driver: "Everyone believes in the tokenization. And I think there's a reason for that, which is kind of a fewfold. But one of the reasons on the equity side is that we do want to enable trading that is, over the weekend, we want to enable trading that's overnight."

Current market makers employ "dirty hedging" strategies—moving with global market hours to find approximate exposure hedges. However, Hadick noted: "It's really hard to hedge exposure well enough over a weekend. And so if you're going to do it, if you're going to manage collateral, if you're going to be able to do any sort of leverage over that period of time, you're going to have to be able to do it on chain rails over the weekend."

Different exchanges are pursuing distinct architectural approaches:

- **NYSE approach**: A segregated order book operating as a separate exchange with a specific transfer agent dedicated to tokenized assets
- **NASDAQ approach**: A consolidated model where tokenized and non-tokenized assets can trade against each other and are "functionally equivalent"
- **Alternative venues**: Some platforms are exploring tokenized asset trading within dark pools

Hadick characterized this diversity as beneficial: "This is all good for all of us in the whole industry because there's going to be more innovation around this. And eventually we're going to have, in my mind, all assets be tokenized."

### Stablecoins vs. Tokenized Deposits: Distinct Products

The CARI Network announcement—a tokenized deposit network built by US regional banks (Huntington, First Horizon, M&T Bank, KeyCorp, and Old National Bancorp) on ZK Sync's Providium blockchain—prompted discussion about the relationship between stablecoins and tokenized deposits.

Rob Hadick argued the debate "misses the point," suggesting these represent different instruments serving different purposes:

- **Payment stablecoins**: Money movement instruments
- **Tokenized deposits**: Different instrument type enabling fractional banking
- **Tokenized money market funds**: Yet another distinct instrument

He emphasized: "We have them more digitally native, we have them more easily swappable with each other, it's more liquid, we don't have the same kind of plethora of problems from a back office perspective in terms of reconciling these things."

Recent regulatory developments support this differentiation. US regulators now allow stablecoins to be treated as cash equivalents for capital control purposes, which "helps a lot from the capital control perspective."

Noah Levine reinforced the distinction based on **user segmentation**: "The primary user of a tokenized deposit is completely different than who the primary user of a stablecoin is going to be."

Stablecoin product-market fit has emerged in:
- Crypto capital markets (moving value between exchanges)
- DeFi engagement
- Dollar store of value outside the United States

For US regional banks in the CARI Network, the value proposition differs fundamentally: "M&T Bank isn't looking at serving customers in Argentina. Like it's just not their primary customer base. And so I think for them, it's, you know, wholesale, it's more money movement, it's more back-end, back-office stuff."

Levine concluded: "I think for that specific use case, this could be successful. But I don't think it's the type of thing that you necessarily see on headlines because it's much less of a retail thing and more so an efficiency standpoint."

### Bank Consortiums and Infrastructure Development

The consortium model for blockchain infrastructure generated debate among panelists.

Rob Hadick defended the consortium approach, citing historical precedents:
- Visa and MasterCard
- Early Warning (which produced Zelle)
- Synchrony (originally within Goldman Sachs)

His rationale: "It's hard to get a net new startup to go and fund and then kind of sell to all of these different counterparties... it's really hard to build all of the things with venture capital and with being self-funded and to serve the different needs of a bunch of these different counterparties."

He concluded: "It's very clear to me that bank consortiums should play a role or asset management consortiums should play a role in a lot of the innovation that's going to happen on the capital market side. And you almost have to have that."

Robert Mitchnick offered a more skeptical assessment: "I think you're being charitable by zooming out in terms of the broader history of cases where a consortium has been successful because in this space, I think we would probably agree, it's been a pretty tough track record and that's putting it lightly for consortiums."

While not dismissing the model entirely, Mitchnick emphasized: "We need to kind of go in recognizing how hard it has been to produce things of meaningful economic value through a consortium structure thus far in the blockchain and digital asset space."

Noah Levine provided context on bank motivations: "I think there's a common misconception that banks are just sleep at the wheel and don't care and don't want to do something. I think they recognize that there's a massive opportunity to leverage this infrastructure to create competitive products and continue to innovate."

The primary constraint remains **regulatory uncertainty**: "The biggest challenge with banks in general has just been lack of regulatory clarity... things like how does compliance work? How does ML work? Like, it's still very unclear."

Despite challenges, several major banks have pursued tokenization initiatives:
- JPMorgan: JPM Coin evolving to JPMD (issued on public blockchain)
- Citi: Citi Token Services
- Various regional bank consortiums

Levine assessed: "The probability of any individual project or consortium succeeding is low because it's hard. But that being said, you know, I think that for a lot of these banks, like they want to participate. They just, looking for the right opportunity and it's how much risk are they willing to take to get involved."

A tension emerged regarding competitive dynamics. Mitchnick questioned: "There needs to be a really clear definition of why a tokenized deposit solves something or offers something different than stable coins already do. And I don't think that's been made particularly clear anywhere yet."

Hadick responded: "Each individual bank would tell you it just allows them to be in their own deposit base and allow them to continue to do some sort of fractional banking and a tokenized deposit. That's good for them... But on the other side, it's good for you to continue to manage the money market funds, right? And so I think that would be the push pull of what's happening there between the different stakeholders."

### Privacy Requirements in Capital Markets

The CARI Network's use of ZK Sync's Providium blockchain raised questions about privacy infrastructure for tokenized assets.

Rob Hadick challenged the premise that crypto builders have been slow to recognize institutional privacy needs: "I don't think it's taken that long to realize people have been building around the topic for a long time. I think the part of the problem has been that there has actually been no demand for privacy, really. Or the only demand for privacy to date has been for nefarious reasons."

He explained how existing solutions have addressed privacy concerns without dedicated privacy technology: "If you're going to do all of your payments on chain, then you want to do payroll, you want to do payouts. You need to have some sort of privacy because you don't want to know exactly how much each individual person is getting paid. Well, how did we solve that problem? We just did netting, right?"

The example: Payment processors like BVNK aggregate transactions throughout the day and settle with a single on-chain transaction to Ethereum, effectively providing privacy through aggregation since "nobody could actually solve those problems, right? Or could figure out who was, who was getting what."

However, **capital markets present different requirements**: "If you're going to do weekend capital markets, and you're going to do things like collateral mobility and management on chain, that becomes a much different conversation because there is nothing, you can't necessarily do netting in that case when you need to do a capital call when something's moving against you."

Privacy becomes critical when:
- Managing collateral in real-time
- Responding to margin calls
- Operating on chains with limited participant sets where transaction patterns become identifiable

Zero-knowledge proofs offer partial solutions: "ZK proofs go a long way in certain types of transactions to allow you to have some sort of privacy. But ZK proofs are not made for all types of transactions."

Hadick acknowledged competing approaches, referencing Canton's alternative privacy model, and expressed his belief: "I am a strong believer that more and more of this will happen on public permissionless chains and not on a lot of these like private permissioned chains that people are trying to do today. But it is continuing to be a very tough to solve technological problem if you're going to do it on a public chain."

## Key Insights and Implications

### Strategic Insights

1. **Access Trumps Efficiency**: The most significant insight from BlackRock's perspective is reframing tokenization from an operational efficiency story to a financial inclusion narrative. With crypto-native investors representing a substantial demographic with near-zero allocation to traditional assets, tokenization creates a bridge to the remaining $497 trillion in global assets beyond crypto's $3 trillion.

2. **Form Factor Standardization as Infrastructure**: The standardization of assets into token form factors compatible with stablecoins creates network effects similar to internet protocols. This standardization reduces friction more effectively than incremental improvements to legacy infrastructure.

3. **Regulatory Arbitrage vs. Sustainable Models**: The tension between rapid market development through regulatory arbitrage (e.g., derivative-based "tokenized" equities) and building sustainable, compliant infrastructure represents a fundamental strategic choice. BlackRock's emphasis on avoiding "beg forgiveness later" strategies signals institutional preference for regulatory clarity over speed.

4. **Weekend Trading as Killer Use Case**: The inability to properly hedge positions during market closures represents a concrete, quantifiable problem that tokenization solves. This practical driver may prove more compelling than abstract efficiency gains.

5. **User Segmentation Determines Product Success**: The clear differentiation between stablecoin users (crypto capital markets, international dollar access) and tokenized deposit users (wholesale banking, back-office efficiency) suggests that attempting to build universal solutions may be less effective than purpose-built products for specific segments.

### Market Structure Implications

1. **Multiple Equilibria Possible**: The divergent approaches by NYSE (segregated order book), NASDAQ (consolidated model), and alternative venues suggest the market structure for tokenized securities remains unsettled. This experimentation phase will likely produce winners and losers based on liquidity aggregation and user experience.

2. **Consortium Paradox**: While historical precedents (Visa, MasterCard, Zelle) demonstrate consortium success in payments infrastructure, blockchain-specific consortiums have struggled. This suggests either: (a) blockchain infrastructure requires different organizational models, or (b) successful consortiums require longer time horizons than current market expectations allow.

3. **Privacy as Competitive Differentiator**: As capital markets activity moves on-chain, privacy infrastructure may become a key competitive differentiator. However, the lack of current demand (outside nefarious use cases) suggests this remains a forward-looking requirement rather than immediate market need.

### Regulatory and Compliance Implications

1. **Whitelisting as Fundamental Constraint**: The AML-driven requirement for whitelisting creates an inherent tension with blockchain's permissionless composability. Until this is resolved through either regulatory evolution or technical innovation (e.g., privacy-preserving compliance), tokenized securities will remain partially siloed from broader DeFi ecosystems.

2. **Regulatory Clarity as Gating Factor**: Bank hesitation stems primarily from regulatory uncertainty rather than technological limitations or lack of interest. The recent progress on stablecoin regulation (Genius Act) provides a template, but comprehensive frameworks for tokenized securities remain incomplete.

3. **Capital Treatment Parity**: The regulatory decision to treat stablecoins as cash equivalents for capital control purposes represents a significant milestone, potentially accelerating institutional adoption by removing balance sheet penalties.

### Technical Architecture Implications

1. **Public vs. Private Chain Tension**: The debate between public permissionless chains and private permissioned chains reflects different prioritization of transparency, composability, and privacy. Hadick's prediction that "more and more of this will happen on public permissionless chains" suggests eventual convergence, but the path remains uncertain.

2. **Transfer Agent Evolution**: The designation of Securitize as a digital transfer agent represents institutional recognition that blockchain-native securities require new intermediary roles. This suggests evolution rather than elimination of financial infrastructure.

3. **Composability Limitations**: Current tokenized securities' limited composability with DeFi protocols due to whitelisting requirements means the full potential of programmable finance remains unrealized. This represents both a constraint and an opportunity for future development.

## Definitions and Terminology

**Tokenization**: The process of representing ownership rights to assets as digital tokens on a blockchain, enabling programmable transfer and settlement.

**SPV (Special Purpose Vehicle)**: A legal entity created for a specific, limited purpose—in this context, to hold traditional assets and issue tokenized representations of ownership in the vehicle itself rather than direct ownership of underlying assets.

**Whitelisting**: A compliance mechanism requiring pre-approval of addresses or entities authorized to hold or transfer specific tokens, typically implemented to satisfy AML (Anti-Money Laundering) and KYC (Know Your Customer) requirements.

**Form Factor**: The technical and structural characteristics of an asset representation. Assets sharing the same form factor (e.g., all being ERC-20 tokens) can interact seamlessly, while different form factors require conversion or bridging.

**Tokenized Entitlements**: A model where existing off-chain assets are represented on-chain through tokens that convey rights to the underlying asset without the asset itself being natively digital.

**Q-SIP (Qualified Special Investment Product)**: A regulatory classification for certain investment products that can be issued on-chain with direct ownership rights.

**ATS (Alternative Trading System)**: A non-exchange trading venue that matches buyers and sellers of securities, operating under different regulatory requirements than traditional exchanges.

**Dirty Hedging**: An informal term for approximate hedging strategies that use correlated but not identical instruments or markets to offset risk when direct hedging is unavailable (e.g., using Asian market hours to hedge US equity exposure overnight).

**Netting**: The practice of aggregating multiple transactions and settling only the net difference, reducing the number of individual settlements required and providing privacy through aggregation.

**ZK Proofs (Zero-Knowledge Proofs)**: Cryptographic methods allowing one party to prove to another that a statement is true without revealing any information beyond the validity of the statement itself, enabling privacy-preserving verification.

**DeFi (Decentralized Finance)**: Financial applications built on blockchain infrastructure that operate without traditional intermediaries, typically emphasizing composability and permissionless access.

**Composability**: The ability of different protocols, applications, or assets to interact and combine functionality without requiring custom integration for each pairing, often described as "money legos."

**Consortium**: A collaborative organizational structure where multiple independent entities jointly develop and govern shared infrastructure or standards.

**Stablecoin**: A cryptocurrency designed to maintain a stable value relative to a reference asset (typically the US dollar) through various mechanisms including fiat backing, algorithmic controls, or collateralization.

**Tokenized Deposit**: A blockchain representation of a traditional bank deposit, maintaining the deposit relationship with the issuing bank while enabling digital transfer and programmability.

## References and Citations

### Direct Quotations

**Larry Fink (BlackRock CEO), 2026 Annual Letter**:
> "Half the world's population carries a digital wallet on their phone. Imagine if that same digital wallet could also let you invest in a broad mix of companies for the long term, as easily as sending a payment. Tokenization could help accelerate that future by updating the plumbing of the financial system, making investments easier to issue, easier to trade, and easier to access."

**Robert Mitchnick on Access vs. Efficiency**:
> "The idea is that tokenization, which we so often talked about as this efficiency story, is actually, in many respects, potentially even bigger as an access story, where you have this universe of investors who are crypto native, or they're more predisposed towards digital wallets and interacting in the digital assets and DeFi ecosystem."

**Robert Mitchnick on Whitelisting Constraints**:
> "Tokens are freely transferable between whitelisted parties, right? And that obviously remains a big sticking point and a challenge in terms of truly unlocking the utility in this space. Whenever you have to go through whitelisting, you add a significant point of friction that undermines liquidity, undermines usability and DeFi and all those challenges."

**Robert Mitchnick on Consortium Track Record**:
> "In this space, I think we would probably agree, it's been a pretty tough track record and that's putting it lightly for consortiums, which isn't to say that some construct in that area can't work, but I think we need to kind of go in recognizing how hard it has been to produce things of meaningful economic value through a consortium structure thus far in the blockchain and digital asset space."

**Rob Hadick on Privacy Demand**:
> "I don't think it's taken that long to realize people have been building around the topic for a long time. I think the part of the problem has been that there has actually been no demand for privacy, really. Or the only demand for privacy to date has been for nefarious reasons."

**Noah Levine on Product Differentiation**:
> "I think another point with stablecoins and tokenized deposits is that they're fundamentally different products. Like I think we as an industry try and put things together, but at the end of the day, like the primary user of a tokenized deposit is completely different than who the primary user of a stablecoin is going to be."

### Key Announcements Referenced

- **NYSE-Securitize Partnership**: Wall Street Journal exclusive reporting on 24/7 tokenized securities platform development
- **CARI Network**: US regional banks (Huntington, First Horizon, M&T Bank, KeyCorp, Old National Bancorp) tokenized deposit network on ZK Sync's Providium blockchain, targeting 2026 rollout
- **BlackRock BUIDL Fund**: First tokenized money market fund, issued as native on-chain shares (not SPV structure)

### Regulatory Context

- **Genius Act**: Recent US legislation providing framework for stablecoin regulation and OCC rulemaking
- **SEC Guidance**: Recent (within month prior to recording) guidance on digital assets
- **Basel Capital Controls**: Ongoing revision of capital treatment for digital assets
- **Stablecoin Capital Treatment**: US regulatory decision allowing stablecoins to be treated as cash equivalents for capital control purposes

### Companies and Platforms Mentioned

- **Issuers/Platforms**: BlackRock, SuperState, Figure, Securitize, DTCC
- **Exchanges**: NYSE, NASDAQ
- **Banks**: JPMorgan (JPM Coin, JPMD), Citi (Citi Token Services), Huntington, First Horizon, M&T Bank, KeyCorp, Old National Bancorp
- **Infrastructure**: ZK Sync (Providium blockchain), Canton
- **Payment Processors**: BVNK, Robinhood
- **Historical Consortiums**: Visa, MasterCard, Early Warning (Zelle), Synchrony

### Episode Metadata

- **Show**: Tokenized, Episode 76
- **Published**: March 30, 2026
- **Location**: Live recording in New York City during Digital Asset Summit
- **Host**: Pet Berisha (Co-Creator, Tokenized)
- **Guests**: Robert Mitchnick (Head of Digital Assets, BlackRock), Rob Hadick (GP, Dragonfly), Noah Levine (Partner, Andreessen Horowitz)
- **Sponsors**: Visa, Bridge (Stripe company), M0