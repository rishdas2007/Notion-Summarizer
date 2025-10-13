# Banks Do DeFi Now Ft. Nassim Eddequiouaq

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Visa Direct Stablecoin Integration](#visa-direct-stablecoin-integration)
   - [Stripe Open Issuance Platform](#stripe-open-issuance-platform)
   - [Business Rationale for Proprietary Stablecoins](#business-rationale-for-proprietary-stablecoins)
   - [Stablecoin Market Structure Evolution](#stablecoin-market-structure-evolution)
   - [Interoperability Challenges](#interoperability-challenges)
   - [Smart Contract Customization](#smart-contract-customization)
   - [Stablecoins as Business Platforms](#stablecoins-as-business-platforms)
   - [Self-Custodial Wallets and Branded Stablecoins](#self-custodial-wallets-and-branded-stablecoins)
   - [Brex Corporate Card Stablecoin Integration](#brex-corporate-card-stablecoin-integration)
   - [Corporate Treasury Applications](#corporate-treasury-applications)
   - [SG Forge DeFi Deployment](#sg-forge-defi-deployment)
   - [DeFi Evolution into On-Chain Credit](#defi-evolution-into-on-chain-credit)
   - [Banking Business Models](#banking-business-models)
   - [SWIFT Blockchain Modernization](#swift-blockchain-modernization)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Definitions and Terminology](#definitions-and-terminology)
5. [References and Citations](#references-and-citations)

## Executive Summary

This episode of the Tokenized podcast examines the accelerating convergence of traditional finance and decentralized finance (DeFi) through stablecoin adoption. The discussion, featuring Simon Taylor (Tempo), Cuy Sheffield (Visa), and Nassim Eddequiouaq (Bastion), covers five major developments:

**Primary Developments:**

1. **Visa Direct** is integrating stablecoins as a funding mechanism for cross-border payments, enabling 24/7 settlement versus traditional banking hour restrictions
2. **Stripe's Open Issuance** platform democratizes stablecoin creation, allowing businesses to launch branded stablecoins with minimal technical overhead
3. **Brex** became the first global corporate card to accept stablecoin payments for balance settlement
4. **SG Forge** (Société Générale's crypto subsidiary) deployed euro and dollar stablecoins on DeFi protocols Uniswap and Morpho
5. **SWIFT** announced blockchain-based infrastructure modernization with 30 global banks

**Central Thesis:** The stablecoin market is transitioning from a handful of dominant issuers to a proliferated ecosystem where businesses across sectors issue proprietary stablecoins to capture economics, enhance control, and accelerate product development. This shift is enabled by white-label infrastructure providers and driven by demand for yield capture, operational flexibility, and integrated security features.

**Key Arguments:**
- Proprietary stablecoins enable businesses to control economics (reserve yields, mint/burn fees) and customize functionality (fraud reversal, transaction controls)
- Interoperability remains the critical challenge as stablecoin proliferation accelerates
- DeFi protocols are evolving into shared infrastructure for on-chain credit that traditional financial institutions are beginning to adopt
- Speed of iteration enabled by stablecoin standardization represents a fundamental competitive advantage

## Detailed Analysis

### Visa Direct Stablecoin Integration

**Context and Announcement:**
Visa announced at Sibos that Visa Direct, its global money movement platform reaching 11 billion endpoints (cards, accounts, wallets), will integrate stablecoins as a funding mechanism. This represents a significant infrastructure upgrade for cross-border payment settlement.

**Technical Implementation:**
The integration addresses a fundamental constraint in traditional cross-border payments: banking hour restrictions. In the existing fiat-to-fiat model, if a remittance company needs to fund a payout in Mexico but operates from the US, they must predict weekend volume when funding on Friday. Stablecoins enable continuous funding capability.

**Value Proposition:**
Sheffield explained: "When we saw stablecoins emerge, we saw them as just this better settlement layer and funding mechanism where if you could let a client be able to fund Visa Direct seven days a week, 24-7, that is a much more flexible solution without having to predict and plan ahead."

The model operates as: Client sends stablecoins → Visa converts → Local fiat payout globally. This maintains the existing Visa Direct infrastructure while adding a more efficient funding layer.

**Strategic Significance:**
This positions Visa as infrastructure for stablecoin off-ramping, addressing a persistent pain point in the crypto ecosystem. The announcement indicates partnerships are in development but not yet publicly disclosed.

### Stripe Open Issuance Platform

**Product Overview:**
Stripe launched Open Issuance, a platform enabling businesses to launch and manage stablecoins "with just a few lines of code." The company is also applying for a federal banking charter to comply with anticipated US stablecoin regulations.

**Core Features:**
- Issuance on any blockchain network
- Customizable smart contracts
- Reserve management handled by Stripe
- Control over mint and burn fees
- Built-in interoperability between Open Issuance stablecoins

**Launch Partners:**
The platform launched with significant distribution partners:
- **Phantom** (25 million users): Launching "Cash" stablecoin
- **Hyperliquid**: Native stablecoin USDH for the DeFi platform
- **MetaMask**: Leveraging M0 protocol backend
- **Dakota**: Stablecoin-native corporate spend management

**Market Positioning:**
Patrick Collison emphasized the goal of making stablecoins "mainstream" through accessibility. The interoperability feature is particularly notable—stablecoins issued through Open Issuance can natively interact because they share the same underlying issuer and reserves.

### Business Rationale for Proprietary Stablecoins

**Economic Control:**
Eddequiouaq articulated the fundamental value proposition: "You can only go so far by partnering with an existing issuer. You have limitations in terms of the economics that you get on the reserves. You have limitations on the economics that you get out of the redemption fees."

**Three Primary Drivers:**

1. **Reserve Economics:** Capturing yield on reserves rather than ceding it to third-party issuers
2. **Fee Control:** Setting mint/burn fees aligned with business model rather than accepting issuer-imposed fees
3. **Functional Customization:** Integrating fraud detection and transaction reversal capabilities

**Concrete Example:**
Eddequiouaq provided a case study: "We're currently working with one of the largest companies in the world to issue their stablecoin and the mere fact that they have their own stablecoin allows them because they have all the fraud management and detection on the web2 side to be able to undo transactions and revert transactions in a way that is fully integrated into their own security system."

This represents a significant departure from the immutability typically associated with blockchain transactions, demonstrating how proprietary issuance enables application-specific functionality.

**Limitations of Partnership Models:**
Working with established issuers like Circle or Tether provides immediate liquidity and acceptance but constrains:
- Economic upside from reserve management
- Ability to customize smart contract functionality
- Integration with proprietary security and compliance systems
- Marketing and brand control

### Stablecoin Market Structure Evolution

**Historical Context:**
The market historically featured a small number of dominant stablecoins (USDT, USDC, BUSD) with high barriers to entry. PayPal's PYUSD launch via Paxos white-label was considered a major event, indicating the perceived complexity and risk.

**Current Trajectory:**
Sheffield observed: "The general direction of travel is lowering the barrier to entry to creating white label stablecoin products with a number of different providers specializing in different areas."

**Two Stablecoin Architectures:**

1. **Full-Stack Stablecoins:**
   - Proprietary reserves
   - Direct banking relationships
   - Independent compliance infrastructure
   - Complete operational control
   - Requires building distribution and liquidity from scratch

2. **Wrapped Stablecoins:**
   - Built on existing stablecoin infrastructure (e.g., M0 protocol)
   - Leverage existing liquidity pools
   - Faster time-to-market
   - Reduced operational complexity
   - Limited economic capture

**Provider Specialization:**
Different infrastructure providers are targeting distinct market segments:
- **Bridge/Stripe:** Crypto-native companies (MetaMask, Phantom)
- **Bastion:** Enterprises and financial institutions
- **Paxos:** Established brands seeking white-label solutions

Eddequiouaq noted: "Small to medium-sized businesses will tend to focus on the wrapped stablecoin model... larger companies want way more control and way more risk management."

### Interoperability Challenges

**The Fragmentation Problem:**
Sheffield identified the critical challenge: "How do you enable interoperability between Bastion stablecoins and Stripe stablecoins and Paxos stablecoins? What does it look like cross-provider instead of just within provider? That's where we're still super, super early."

**Within-Provider Solutions:**
Stripe's Open Issuance offers native interoperability between stablecoins issued on its platform because they share underlying reserves and issuer infrastructure. This creates a closed ecosystem advantage.

**Cross-Provider Complexity:**
Each new stablecoin and blockchain network creates integration overhead. Taylor noted the operational burden: "Every time a new network or coin pops up it's another thing you have to think about integrating."

**Existing Infrastructure:**
While automated market makers (AMMs), exchanges, and bridging solutions exist, they add friction and cost. The discussion suggested that solutions like Tempo's AMMs could address liquidity fragmentation, though this remains an evolving challenge.

**Network Effects Dynamics:**
The tension between proprietary control and network effects creates strategic complexity. Companies must balance:
- Economic benefits of proprietary issuance
- Liquidity advantages of established stablecoins
- Distribution reach of their platform
- Technical integration costs

### Smart Contract Customization

**Freeze and Seize Mechanisms:**
Sheffield explained that major stablecoins include smart contract functionality allowing issuers to freeze assets and reissue them. However, this capability has been narrowly applied: "Historically, we've seen the smart contract functionality really used only in compliance scenarios, where it's a suspicious address, or it's a subpoena from law enforcement."

**Expanded Use Cases:**
Proprietary issuance enables broader application of smart contract controls:
- **Customer Service:** Recovering funds sent to wrong addresses
- **Fraud Prevention:** Reversing transactions post-hack detection
- **Access Control:** Allow-listing specific customer segments
- **Integration:** Connecting blockchain-level controls with Web2 security systems

**Risk Trade-offs:**
Sheffield noted the inherent tension: "The more complex smart contracts, the more risk, the more attack surface." Customization increases functionality but expands potential vulnerabilities.

**Regulatory Implications:**
The GENIUS Act (stablecoin legislation) was designed assuming a market structure of "a handful of large stablecoins that are relatively static." The proliferation of customized white-label stablecoins under diverse smart contract architectures creates regulatory complexity that rulemaking must address.

**Merchant and Loyalty Applications:**
While merchant adoption remains limited, Sheffield's loyalty background suggests potential for customized stablecoins in closed-loop reward systems, though this remains largely theoretical.

### Stablecoins as Business Platforms

**Platform Economics:**
Eddequiouaq articulated a fundamental shift: "Stablecoins are platforms. A lot of companies are moving away from building on top of APIs and SDKs and starting to build on top of stablecoins instead."

**Extensibility Advantages:**
Building on stablecoins rather than traditional APIs enables:
- Direct economic participation in transaction flow
- Partnership models where partners build on the stablecoin infrastructure
- Reduced integration complexity for new products
- Composability with DeFi protocols

**Example - Phantom's Strategy:**
With 25 million users, Phantom's stablecoin issuance enables expansion into:
- Value storage with yield
- Payment functionality
- Asset holdings (stocks, crypto)
- Quasi-banking services

Taylor observed: "Phantom itself is now doing a lot of different things that look a lot like a neobank, but with 25 million users."

**Prediction:**
Eddequiouaq forecasted: "Chains are going to be issuing, protocols are going to be issuing, wallets are going to be issuing, and we're going to be seeing interesting dynamics of who builds on top of which stablecoin."

### Self-Custodial Wallets and Branded Stablecoins

**Structural Difference from Neobanks:**
Sheffield distinguished between custodial and self-custodial approaches: "The principle of a self-custodial wallet, you can't necessarily default and force someone into using a specific product."

**Two Models:**

1. **Custodial Neobanks:**
   - Auto-convert fiat to proprietary stablecoin on backend
   - Users have no choice in stablecoin selection
   - Full control over economic flow
   - Example: Future stablecoin-native neobanks

2. **Self-Custodial Wallets:**
   - Users maintain control over asset selection
   - Cannot force conversion from USDC to branded stablecoin
   - Must convince users through product features and incentives
   - Examples: MetaMask, Phantom

**Conversion Challenge:**
Sheffield posed the critical question: "How successful can these self-custodial wallets be in converting what likely is billions of dollars of existing stablecoins that are sitting on those wallets today over to the self-custodial wallet branded stablecoin?"

**Distribution Leverage:**
Both MetaMask and Phantom possess significant distribution advantages:
- Large existing user bases
- Control over interface and user experience
- Ability to promote proprietary products
- Financial product integration capabilities

**Strategic Approaches:**
- **MetaMask:** Using M0 protocol for wrapped stablecoin model
- **Phantom:** Full-stack approach with Cash stablecoin

Success depends on converting distribution into economic capture while maintaining user choice principles.

### Brex Corporate Card Stablecoin Integration

**Product Announcement:**
Brex launched stablecoin payment functionality, becoming "the first global corporate card to enable paying your balance with stablecoins." The integration also allows customers to accept and receive stablecoin payments with instant settlement.

**Use Case Focus:**
Unlike Ramp's stablecoin-linked card for market expansion, Brex targets existing customers with stablecoin treasury needs. Taylor noted: "Ramp's proposition was about expanding the markets they could operate in, whereas Brex is about serving the customers they have today that want to move in stablecoins."

**Value Proposition:**
The product addresses specific pain points:
- **Credit Line Payment:** Businesses with stablecoin treasuries can instantly pay corporate card balances
- **Cross-Subsidiary Settlement:** Global companies can move funds between entities without fiat banking delays
- **Instant Settlement:** Eliminates traditional payment processing timelines

**Target Customer Profile:**
Sheffield identified the core segment: "Brex mentioned in the announcement that today they serve a number of crypto companies... crypto companies are using stablecoins as kind of a core part of their corporate treasury."

**Crypto Companies as Attractive Clients:**
The regulatory environment shift has made crypto businesses viable banking customers:
- Rapid growth and fundraising activity
- Significant revenue generation
- Stablecoin-native operations
- Previously underserved by traditional banks

Eddequiouaq added: "The average purchase amount is typically higher whenever it's done in stablecoins."

**Pragmatic Approach:**
Eddequiouaq characterized the strategy: "A much more pragmatic approach in the sense of making it easier for businesses to add stablecoins in a way that builds value tomorrow... without having to change the way you operate your company."

### Corporate Treasury Applications

**Adoption Drivers:**
Taylor identified technology companies as early adopters: "Many at-scale technology companies, they are the early adopters of corporate treasury that's stablecoin native."

**Treasury Use Cases:**
1. **Inter-Entity Settlement:** Moving funds between subsidiaries across jurisdictions
2. **Credit Line Management:** Paying corporate obligations from stablecoin holdings
3. **Yield Optimization:** Earning returns on idle treasury balances
4. **Payment Flexibility:** 24/7 settlement capability

**Growth Trajectory:**
The discussion referenced BVNK's milestone: four years old with annual processed volume exceeding $20 billion, having doubled from $10 billion earlier in the year. Taylor emphasized: "That growth rate is actually accelerating."

**Competitive Dynamics:**
Eddequiouaq warned: "A lot of the companies that are unable to accept stablecoin payments from their clients are going to be left behind."

**Future Direction:**
Eddequiouaq predicted: "The next frontier is going to be stablecoin-linked corporate cards, especially tied to proprietary stablecoins that these companies are going to be issuing over time."

**Institutional Adoption:**
Sheffield noted the shift: "Crypto companies from the perspective of a B2B neobank, where a few years ago, it might have been more challenging to be able to onboard and serve crypto businesses. Now, when you have a regulatory environment that's pretty clear, you could serve businesses that are in the crypto ecosystem."

### SG Forge DeFi Deployment

**Announcement Details:**
Société Générale's crypto subsidiary SG Forge deployed euro (EURCV) and dollar (USDCV) stablecoins on Uniswap and Morpho. Morpho users can now lend these stablecoins and borrow against them.

**Morpho Context:**
Morpho is an on-chain lending protocol that recently surpassed $1 billion in Bitcoin-backed loans. It's embedded in major platforms:
- **Coinbase:** Offering up to 10.6% yield on USDC and Bitcoin-backed loans
- **Crypto.com:** Similar lending product integration

**Historical Precedent:**
Sheffield noted: "Credit to Société Générale, they had done some things with Maker several years ago, like they have been on the forefront of the space for some time."

**Significance:**
Taylor called it "a watershed moment" for a traditional financial institution to directly participate in DeFi protocols, even through a subsidiary structure.

### DeFi Evolution into On-Chain Credit

**Conceptual Reframing:**
Sheffield proposed viewing DeFi through a new lens: "I'm increasingly going down this rabbit hole of how DeFi is really evolving into what I like to think about as on-chain credit and on-chain finance. It's not even just about it being decentralized."

**Morpho as Infrastructure:**
Sheffield explained Morpho's architecture: "It's this protocol that connects lenders and borrowers. But Morpho itself is not a lender. They're just a protocol, and they're now being embedded inside many different applications."

**Shared Infrastructure Model:**
The protocol enables rapid product launches: "If any application could easily launch lending products on top of some shared infrastructure, that becomes very interesting."

**Competitive Composability:**
Sheffield highlighted a remarkable dynamic: "You might actually have a crypto.com customer depositing a stablecoin to earn yield that ends up funding the loan of a Coinbase customer that's borrowing against their Bitcoin. And these are competitors."

This is enabled by "neutral infrastructure" that creates liquidity efficiency impossible in traditional siloed systems.

**Traditional Finance Implications:**
Sheffield predicted: "This is going to be one of the biggest stories of 2026. We're going to see more traditional financial institutions, not just looking at stablecoins for payments, but looking at stablecoins for on-chain credit."

**Efficiency Advantages:**
The value proposition versus legacy systems: "These could be some of the most powerful use cases that are 10x better than existing solutions of managing loan books with spreadsheets and old legacy infrastructure."

**Lending-Payments Integration:**
Sheffield noted the interdependence: "It's really hard to separate lending and payments. If you have significant changes in how lending works, once you receive a stablecoin, you've got to be able to spend it."

### Banking Business Models

**Coinbase as Leading Indicator:**
Taylor offered a predictive framework: "If you want to see what most banks are going to be doing in five years' time, look at what Coinbase is doing today."

**Crypto as Default Bank Feature:**
Buy-sell-hold crypto functionality has become standard across major banks including BBVA, Santander, and PNC Bank, representing a complete reversal from five years prior.

**Stablecoin Business Case Challenge:**
Taylor identified a critical insight: "Most banks don't get a positive business case out of stablecoins necessarily. It's not, I must rush to adopt this unless maybe I could remake correspondent banking, but that's going to be difficult and take time."

**Lending as Entry Point:**
The more compelling opportunity: "Here's this giant lending opportunity that's incredibly efficient."

**Bank Structural Advantages:**
Taylor explained banks' unique position: "Banks are essentially highly levered lenders. For every dollar in deposits they take in, they can lend up to $10. This gives them a unique advantage in lending because they're very good levered risk managers."

**DeFi Liquidity Needs:**
The complementary fit: "What does DeFi really benefit from? It benefits from liquidity." Banks can provide capital scale that DeFi protocols need while accessing efficient distribution.

**Dual Pathways:**
Banks can participate through:
1. **Direct Lending:** Deploying balance sheet into DeFi protocols
2. **Deposit Collection:** Issuing stablecoins backed by bank deposits (SG Forge model)

**Speed of Iteration:**
Eddequiouaq emphasized the transformative aspect: "The speed of iteration is really, in my opinion, the big part of the story. A bank like SG should not be able, even like a sub arm that is smaller, faster, more lean, typically does not move as fast as what we're seeing them do."

**Open Source Dynamics:**
Eddequiouaq referenced a principle (attributed to Naval): "The beauty about open source software is that you only need to solve every single problem once." Once Coinbase implements a solution, others can rapidly follow.

**Stablecoin Journey Framework:**
Eddequiouaq outlined the value chain: "Issue, hold, use. You have the ability to capture the economics on the stablecoin by being the issuer. You have the send, hold, receive piece, which is the core payment part. And then the actual usability with spending, cards, lending, borrowing, trading, and settlement features for various financial instruments."

**Means to an End:**
Eddequiouaq clarified: "At the end of the day, those stablecoins are a means to an end. You want to enable access to some type of service, some type of product."

### SWIFT Blockchain Modernization

**Announcement:**
SWIFT announced a blockchain-based infrastructure overhaul in collaboration with 30 global banks, representing a significant modernization initiative for the $5 trillion daily payment network.

**Eddequiouaq's Perspective:**
"I just want to make sure that we have integrations for each one of those large banking institutions that will enable the same format of money and make it interoperable with the ones that everyone is building currently in the stablecoin space or even the tokenized deposit space."

**Network Effects Potential:**
Standardization across major banks could create powerful interoperability: "That actually allows network effects that are extremely powerful for money movements globally."

**Crypto Community Skepticism:**
Eddequiouaq acknowledged likely criticism: "The crypto crowd is going to be thinking decentralization, decentralization. I feel like having optimization of money movements is an excellent thing."

**Knowledge Gap:**
Sheffield noted: "Most people in the crypto ecosystem don't even know what Swift does. Swift sometimes is seen as this enemy, and they're like, oh, we're going to beat Swift. And you're like, do you know what Swift does?"

**Messaging Layer Role:**
Sheffield emphasized SWIFT's actual function as a messaging standard rather than a payment system itself, making their blockchain initiative logical for modernization.

**Implementation Questions:**
Sheffield identified critical unknowns:
- Partnership with ConsenSys and potential use of Linea L2
- Whether this constitutes a SWIFT-specific L2 with SWIFT as sequencer
- Permissioned versus permissionless architecture
- Bank node operation
- Layer 1 settlement mechanisms

**Optimistic Case:**
Taylor proposed the highest-value scenario: "Something that allows you to turn an ISO message and very quickly have a standard way of turning that into some sort of tokenized deposit and/or be interoperable with the universe of stablecoins."

**SWIFT's Unique Advantage:**
Taylor highlighted an underappreciated capability: "SWIFT's superpower is they enable the top 30 banks to lend to very small banks around the world and fund their cross-border settlement."

**Credit Facilitation:**
The correspondent banking system reduces pre-funding costs for smaller banks through credit lines from larger institutions. Taylor suggested: "That's something that potentially we should think about rebuilding in stablecoins."

**Emerging Solutions:**
Eddequiouaq referenced companies like Centrifuge: "Pulling funds out of Centrifuge and then doing the risk management and credit risk distribution to various banks in emerging markets to help them with their liquidity locally."

**Scale Opportunity:**
Taylor concluded: "Imagine how efficient that would be at SWIFT scale. And imagine how much more capital could be deployed by the large financial institutions into long tail exotic markets that they otherwise would have not made economically viable."

## Key Insights and Implications

### Structural Market Transformation

1. **From Oligopoly to Proliferation:** The stablecoin market is transitioning from a handful of dominant issuers to a proliferated ecosystem where vertical-specific and brand-specific stablecoins become standard. This mirrors the evolution from mainframe computing to distributed systems.

2. **Economics Drive Adoption:** The primary driver is not technological superiority but economic capture. Businesses issuing proprietary stablecoins can capture reserve yields (currently 4-5% on US Treasuries) and control fee structures, creating compelling unit economics.

3. **Speed as Competitive Advantage:** Stablecoin standardization enables product iteration velocity impossible with traditional financial APIs. The PayPal-Venmo integration taking a decade versus Stripe enabling stablecoin issuance in days illustrates this differential.

### Interoperability as Critical Bottleneck

4. **The Fragmentation Paradox:** While proliferation creates innovation, it simultaneously creates fragmentation that undermines network effects. The industry lacks mature cross-provider interoperability solutions, creating opportunity for infrastructure providers.

5. **Within-Provider Moats:** Stripe's approach of enabling interoperability only between Open Issuance stablecoins creates a closed ecosystem advantage, potentially leading to competing stablecoin networks rather than a unified ecosystem.

### Regulatory Arbitrage and Evolution

6. **Genius Act Timing:** The stablecoin legislation passed assuming a static market structure, but implementation is occurring during explosive proliferation of white-label models with diverse smart contract architectures. Rulemaking will need to address this complexity.

7. **Yield Distribution Debate:** The ability to share reserve yields with users remains contentious, with financial institutions viewing it differently than innovators. This mirrors the Durbin Amendment dynamics that enabled the fintech boom.

### Banking Sector Implications

8. **Lending Before Payments:** Banks are more likely to adopt stablecoins for lending than payments because the business case is clearer. DeFi protocols provide efficient distribution to stablecoin-native consumers while banks provide capital scale.

9. **Leverage Advantage:** Banks' ability to lend $10 for every $1 in deposits creates unique advantages in DeFi lending markets that non-bank participants cannot replicate, suggesting banks will ultimately dominate on-chain credit.

10. **Deposit Collection Innovation:** Issuing stablecoins backed by bank deposits (SG Forge model) represents a novel deposit collection mechanism, potentially more efficient than traditional branch networks or digital marketing.

### Self-Custodial Wallet Challenge

11. **Distribution Without Control:** Self-custodial wallets (MetaMask, Phantom) face a unique challenge: they have distribution but cannot force users into proprietary stablecoins. Success requires converting billions in existing stablecoin holdings through superior product features.

### Corporate Treasury Adoption

12. **Crypto Companies as Beachhead:** Crypto-native companies using stablecoins in corporate treasury represent the beachhead market for B2B financial services. Their growth and profitability make them attractive customers previously underserved.

13. **Instant Settlement Value:** The ability to instantly settle corporate card balances or move funds between subsidiaries provides immediate ROI, making adoption pragmatic rather than speculative.

### DeFi Maturation

14. **Shared Infrastructure Emergence:** DeFi is evolving from isolated protocols to shared infrastructure that competitors use simultaneously (Coinbase and Crypto.com both using Morpho). This represents genuine composability rather than theoretical possibility.

15. **Neutral Infrastructure Value:** Only truly neutral infrastructure enables competitors to share liquidity pools, creating market efficiency impossible in traditional finance where each institution maintains separate systems.

### SWIFT Modernization Significance

16. **Credit Facilitation Underappreciated:** SWIFT's role in enabling large banks to provide credit lines to small banks for correspondent banking is underappreciated. Replicating this in stablecoins could unlock capital deployment to exotic corridors.

17. **Standardization Opportunity:** If SWIFT successfully creates interoperability between traditional banking and stablecoin/tokenized deposit ecosystems, it could accelerate institutional adoption more than any other single initiative.

### Market Perception Divergence

18. **Two Universes:** A significant perception gap exists between those viewing crypto as entirely fraudulent and those recognizing publicly-traded companies (Circle, Coinbase) with substantial stablecoin treasuries as legitimate businesses. This gap is narrowing but remains substantial.

19. **Growth Rate Acceleration:** Companies like BVNK reaching $20 billion annual run rate in four years, with accelerating growth, demonstrates real economic activity beyond speculation.

### Future Predictions

20. **2026 as Inflection Year:** Sheffield's prediction that traditional financial institutions adopting on-chain credit will be "one of the biggest stories of 2026" suggests the timeline for mainstream institutional DeFi adoption is 12-18 months, not 5-10 years.

## Definitions and Terminology

**Stablecoin:** A cryptocurrency designed to maintain a stable value relative to a reference asset, typically the US dollar, through various mechanisms including fiat reserves, algorithmic controls, or collateralization.

**DeFi (Decentralized Finance):** Financial services built on blockchain networks using smart contracts, operating without traditional intermediaries like banks or brokerages.

**White-Label Stablecoin:** A stablecoin issued under one brand but utilizing another company's infrastructure for reserves, compliance, and operational management.

**Full-Stack Stablecoin:** A stablecoin where the issuer controls all components including reserves, banking relationships, compliance infrastructure, and smart contracts.

**Wrapped Stablecoin:** A stablecoin built on top of existing stablecoin infrastructure, leveraging the underlying asset's liquidity while adding a branded layer.

**Mint and Burn Fees:** Charges applied when creating new stablecoin tokens (minting) or redeeming them for fiat currency (burning). Originally designed to prevent spam but can become significant revenue sources.

**Smart Contract:** Self-executing code deployed on a blockchain that automatically enforces agreement terms without intermediaries.

**Freeze and Seize Mechanism:** Smart contract functionality allowing stablecoin issuers to freeze assets (prevent transfers) or seize and reissue them, typically used for compliance or security purposes.

**Morpho:** An on-chain lending protocol that connects lenders and borrowers without itself acting as a lender, functioning as neutral infrastructure embedded in multiple applications.

**Composability:** The ability for different blockchain protocols and applications to interact and build upon each other, creating "Lego-like" combinations of functionality.

**Visa Direct:** Visa's global money movement platform enabling financial institutions and remittance companies to push funds to approximately 11 billion endpoints including cards, accounts, and wallets.

**Correspondent Banking:** A system where large banks provide services (including credit lines) to smaller banks to facilitate international transactions and cross-border payments.

**Nostro Account:** An account a bank holds in a foreign currency at another bank, used to facilitate foreign exchange and international transactions. Maintaining these accounts requires capital that earns minimal returns.

**SWIFT (Society for Worldwide Interbank Financial Telecommunication):** A messaging network used by banks and financial institutions to securely transmit information and instructions for financial transactions, processing approximately $5 trillion daily.

**ISO 20022:** An international standard for electronic data interchange between financial institutions, defining message formats for payments and other financial transactions.

**Tokenized Deposit:** A blockchain-based representation of a bank deposit, maintaining the deposit's regulatory status while enabling blockchain-based transfer and programmability.

**Layer 2 (L2):** A secondary blockchain network built on top of a primary blockchain (Layer 1) to improve scalability and reduce transaction costs while inheriting security from the base layer.

**Sequencer:** In Layer 2 blockchain networks, the entity responsible for ordering and batching transactions before submitting them to the Layer 1 blockchain.

**AMM (Automated Market Maker):** A decentralized exchange protocol that uses mathematical formulas to price assets and provide liquidity, eliminating the need for traditional order books.

**Private Credit:** Debt financing provided by non-bank lenders to companies, typically involving direct loans rather than publicly traded bonds.

**GENIUS Act:** US legislation establishing a regulatory framework for stablecoins, including reserve requirements, issuer qualifications, and operational standards.

**Durbin Amendment:** A provision of the Dodd-Frank Act capping debit card interchange fees for banks with over $10 billion in assets, creating an arbitrage opportunity that enabled fintech growth through partnerships with smaller banks.

**Corporate Treasury:** The department within a company responsible for managing cash, investments, and financial risk, including decisions about where to hold and invest company funds.

**On-Chain Credit:** Lending and borrowing activities conducted through blockchain-based protocols using smart contracts, as opposed to traditional off-chain credit systems.

**Liquidity Pool:** A collection of funds locked in a smart contract used to facilitate trading, lending, or other financial activities in DeFi protocols.

**Self-Custodial Wallet:** A cryptocurrency wallet where users control their private keys and therefore have complete control over their assets, as opposed to custodial wallets where a third party holds the keys.

**Custodial Wallet:** A cryptocurrency wallet where a third party (exchange, service provider) controls the private keys and holds assets on behalf of users.

## References and Citations

### Direct Quotations

**On Visa Direct Integration:**
> "When we saw stablecoins emerge, we saw them as just this better settlement layer and funding mechanism where if you could let a client be able to fund Visa Direct seven days a week, 24-7, that is a much more flexible solution without having to predict and plan ahead." — Cuy Sheffield

**On Proprietary Stablecoin Economics:**
> "You can only go so far by partnering with an existing issuer. You have limitations in terms of the economics that you get on the reserves. You have limitations on the economics that you get out of the redemption fees." — Nassim Eddequiouaq

**On Fraud Prevention Capabilities:**
> "We're currently working with one of the largest companies in the world to issue their stablecoin and the mere fact that they have their own stablecoin allows them because they have all the fraud management and detection on the web2 side to be able to undo transactions and revert transactions in a way that is fully integrated into their own security system." — Nassim Eddequiouaq

**On Interoperability Challenges:**
> "How do you enable interoperability between Bastion stablecoins and Stripe stablecoins and Paxos stablecoins? What does it look like cross-provider instead of just within provider? That's where we're still super, super early." — Cuy Sheffield

**On Stablecoins as Platforms:**
> "Stablecoins are platforms. A lot of companies are moving away from building on top of APIs and SDKs and starting to build on top of stablecoins instead." — Nassim Eddequiouaq

**On Self-Custodial Wallet Challenges:**
> "The principle of a self-custodial wallet, you can't necessarily default and force someone into using a specific product." — Cuy Sheffield

**On DeFi Evolution:**
> "I'm increasingly going down this rabbit hole of how DeFi is really evolving into what I like to think about as on-chain credit and on-chain finance. It's not even just about it being decentralized." — Cuy Sheffield

**On Competitive Composability:**
> "You might actually have a crypto.com customer depositing a stablecoin to earn yield that ends up funding the loan of a Coinbase customer that's borrowing against their Bitcoin. And these are competitors." — Cuy Sheffield

**On Banking Business Case:**
> "Most banks don't get a positive business case out of stablecoins necessarily. It's not, I must rush to adopt this unless maybe I could remake correspondent banking, but that's going to be difficult and take time." — Simon Taylor

**On Bank Structural Advantages:**
> "Banks are essentially highly levered lenders. For every dollar in deposits they take in, they can lend up to $10. This gives them a unique advantage in lending because they're very good levered risk managers." — Simon Taylor

**On Speed of Iteration:**
> "The speed of iteration is really, in my opinion, the big part of the story. A bank like SG should not be able, even like a sub arm that is smaller, faster, more lean, typically does not move as fast as what we're seeing them do." — Nassim Eddequiouaq

**On Open Source Dynamics:**
> "The beauty about open source software is that you only need to solve every single problem once." — Nassim Eddequiouaq (attributed to Naval)

**On SWIFT Modernization:**
> "Most people in the crypto ecosystem don't even know what Swift does. Swift sometimes is seen as this enemy, and they're like, oh, we're going to beat Swift. And you're like, do you know what Swift does?" — Cuy Sheffield

**On Predictive Framework:**
> "If you want to see what most banks are going to be doing in five years' time, look at what Coinbase is doing today." — Simon Taylor

### Key Data Points

- **Visa Direct Reach:** 11 billion endpoints (cards, accounts, wallets)
- **Phantom User Base:** 25 million users
- **Morpho Bitcoin Loans:** Exceeded $1 billion
- **Morpho USDC Yield:** Up to 10.6% offered through Coinbase
- **BVNK Annual Volume:** $20 billion run rate (doubled from $10 billion earlier in 2025)
- **SWIFT Daily Volume:** $5 trillion
- **BlackRock Bitcoin ETF Revenue:** $260 million annually
- **Fireblocks Monthly Stablecoin Volume:** Over $100 billion
- **Bank Lending Leverage:** Approximately 10:1 (can lend $10 for every $1 in deposits)

### Episode Information

**Show:** Tokenized  
**Episode:** 51  
**Published:** October 6, 2025  
**Hosts:** Simon Taylor (GTM @ Tempo), Cuy Sheffield (Head of Crypto @ Visa)  
**Guest:** Nassim Eddequiouaq (CEO @ Bastion)  

**Sponsors:** Visa, Bridge (a Stripe company), Fireblocks

### Companies and Entities Referenced

**Financial Institutions:** Visa, Stripe, Société Générale (SG Forge), JPMorgan, Citibank, BBVA, Santander, PNC Bank, Bank of America, SWIFT

**Stablecoin Issuers:** Circle (USDC), Tether (USDT), Paxos, PayPal (PYUSD), Bastion

**Crypto Companies:** Coinbase, Crypto.com, MetaMask, Phantom, Hyperliquid, Bridge, Fireblocks

**DeFi Protocols:** Morpho, Uniswap, Maker, M0, Centrifuge

**Fintech Companies:** Brex, Ramp, Meow, Dakota, BVNK, Tempo

**Infrastructure:** ConsenSys, Linea (L2)

**Investment Firms:** BlackRock, Apollo, Blackstone, KKR

### Validation Notes

This summary comprehensively covers all major discussion topics from the episode transcript. The document structure follows the chronological flow of the conversation while organizing content thematically for clarity. All direct quotations are accurately transcribed from the source material. Data points are presented as stated by participants, though some figures (particularly future dates and projections) should be noted as forward-looking statements subject to change. The episode date appears to contain an error (published as 2025-10-06 but discussed as current events), suggesting either a transcription error or the document represents planned future content.
