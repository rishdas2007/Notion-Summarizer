# Everyone Needs a Stablecoin Acquisition Strategy Ft. Dan Mottice, Itai Turbahn, Matt Marcus & Michael Shaulov

**Citation:** "Everyone Needs a Stablecoin Acquisition Strategy Ft. Dan Mottice, Itai Turbahn, Matt Marcus & Michael Shaulov." *Tokenized*, 03 Nov. 2025, <https://tokenized.simplecast.com/episodes/everyone-needs-a-stablecoin-acquisition-strategy-ft-dan-mottice-itai-turbahn-matt-marcus-PVr6t4_H>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Modern Treasury's Acquisition of Beam](#modern-treasurys-acquisition-of-beam)
   - [Stablecoin Implementation Challenges and Solutions](#stablecoin-implementation-challenges-and-solutions)
   - [Convergence of Fintech and Crypto Rails](#convergence-of-fintech-and-crypto-rails)
   - [Stablecoin-Backed Accounts and Ledgering Infrastructure](#stablecoin-backed-accounts-and-ledgering-infrastructure)
   - [Mastercard's Potential Acquisition of ZeroHash](#mastercards-potential-acquisition-of-zerohash)
   - [Stablecoin Volume Decoupling from Crypto Price Action](#stablecoin-volume-decoupling-from-crypto-price-action)
   - [IBM's Partnership with DFNS](#ibms-partnership-with-dfns)
   - [Fireblocks' Acquisition of Dynamic](#fireblocks-acquisition-of-dynamic)
   - [Market Adoption Patterns and Future Outlook](#market-adoption-patterns-and-future-outlook)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Definitions and Terminology](#definitions-and-terminology)
5. [References and Citations](#references-and-citations)

## Executive Summary

This episode of the Tokenized podcast, published November 3, 2025, examines two major acquisitions in the stablecoin infrastructure space and their implications for the convergence of traditional fintech and crypto payment rails. The discussion centers on Modern Treasury's $40 million acquisition of Beam and Fireblocks' acquisition of Dynamic, both representing strategic moves to build comprehensive stablecoin payment infrastructure.

**Main Arguments:**

1. **Infrastructure Consolidation**: Major fintech and crypto infrastructure companies are acquiring specialized stablecoin capabilities to offer unified payment platforms that seamlessly integrate fiat and stablecoin rails.

2. **Market Maturation**: Stablecoin adoption is decoupling from cryptocurrency speculation, with volume growth driven by utility-focused use cases in remittances, payroll, and cross-border payments rather than trading activity.

3. **Interoperability Imperative**: The future of payments requires platforms that can orchestrate between traditional payment rails (ACH, RTP, FedNow) and stablecoin networks without requiring end-users to understand the underlying complexity.

4. **Enterprise Adoption Wave**: Traditional financial institutions, payment networks (Mastercard, Visa), and Web2 platforms are actively pursuing stablecoin strategies to address gaps in global payment coverage and reduce costs.

**Key Participants:**
- **Dan Mottice** (CEO & Co-Founder, Beam): Focused on instant on/off-ramp orchestration
- **Matt Marcus** (CEO & Co-Founder, Modern Treasury): Payment infrastructure and ledgering systems
- **Itai Turbahn** (Co-founder & CEO, Dynamic): Embedded wallet infrastructure
- **Michael Shaulov** (Co-Founder & CEO, Fireblocks): Digital asset custody and infrastructure
- **Simon Taylor** (GTM, Tempo): Host and moderator

## Detailed Analysis

### Modern Treasury's Acquisition of Beam

Modern Treasury, a San Francisco-based payments infrastructure company that has enabled customers to move hundreds of billions of dollars, acquired Beam for a reported $40 million. This acquisition represents a strategic move to integrate stablecoin capabilities into Modern Treasury's existing fiat payment infrastructure.

**Modern Treasury's Core Business:**
Modern Treasury provides APIs that enable fintechs, marketplaces, and businesses to connect to the financial system. Their customer base includes companies like Procore (embedded payments), Built Rewards (rent payments), and Navon (T&E reimbursements). The company has established expertise in traditional payment rails including ACH, real-time payments (RTP), and FedNow.

**Beam's Specialized Capabilities:**
Beam focused on what Dan Mottice describes as "the orchestration layer" for instant on/off-ramps between stablecoins and instant payment rails. Specifically, Beam enabled:
- Instant conversion between stablecoins and fiat via Visa Direct
- Integration with RTP (Real-Time Payments)
- FedNow connectivity
- Work with customers like Sling Money for off-ramp flows

**Strategic Rationale:**
Matt Marcus articulated the acquisition logic: "We see a tremendous opportunity to provide modern infrastructure that works across fiat and stablecoins. And really, stablecoins is a way to improve on the legacy financial system, but it also needs to be interoperable with it."

The acquisition addresses several market needs:
1. Difficulty for fintechs in establishing banking partnerships due to changing regulatory landscape
2. Need for seamless orchestration between stablecoin and fiat flows
3. Demand for cross-border payment solutions that work like foreign exchange operations
4. Requirement for robust ledgering infrastructure to prevent issues like those seen in the Synapse collapse

### Stablecoin Implementation Challenges and Solutions

Dan Mottice provided insight into the technical and operational challenges of building stablecoin infrastructure, noting "there have been many" pitfalls. The discussion highlighted several critical implementation considerations:

**Scalability Requirements:**
The infrastructure must be "hyper-scalable, hyper-performing, and can really process the hundreds of billions of dollars that we believe that this technology is capable of." This represents a significant engineering challenge beyond simple proof-of-concept implementations.

**Simplification Imperative:**
Mottice emphasized that while other platforms have made it "very easy to get into and out of stable coins," the Beam/Modern Treasury combination aims to make systems "even simpler and made even easier for people to really take advantage of the tech."

**Integration Complexity:**
The technical challenge involves coordinating multiple components:
- Blockchain transaction monitoring and confirmation
- Fiat rail connectivity (ACH, RTP, FedNow, Visa Direct)
- Liquidity management across different currencies and networks
- Compliance and KYC/AML requirements
- Real-time settlement reconciliation

### Convergence of Fintech and Crypto Rails

A central theme throughout the discussion was the inevitable convergence of traditional fintech infrastructure and crypto payment rails into a unified financial system.

**Itai Turbahn's Perspective:**
"Fintech rails and crypto rails are pretty much like the same rails, right? They need to be intertwined. And over time, they're going to be more and more intertwined, right? The movement in and out of stablecoins needs to be accelerated. It shouldn't be a separate topic, right? Today, we talk about it as on-ramps and off-ramps. But in the future, it's just a thing that your fintech infrastructure provider should provide to you."

**Vision for the Future:**
Turbahn articulated a future state where "we don't have anything like crypto conferences or crypto podcasts, but they're just fintech podcasts, right? And fintech conferences, right? And that also implies that there are no crypto fintech companies. They're just fintech companies that might be crypto first."

This represents a fundamental shift from viewing stablecoins as a separate technology category to treating them as simply another payment rail that infrastructure providers should support natively.

**Abstraction of Complexity:**
The goal is to reach a state where developers and businesses don't need to understand the underlying mechanics: "The fact that I have to tell someone, hey, you get an embedded wallet and they get some dynamic, but now let me tell you about on-ramps and off-ramps is a very weird conversation. And I would rather just say, no, it just kind of works."

### Stablecoin-Backed Accounts and Ledgering Infrastructure

Modern Treasury introduced the concept of "stablecoin-backed accounts" as an alternative to traditional For Benefit Of (FBO) accounts that fintechs typically use to hold customer funds.

**Product Offering:**
Matt Marcus explained: "That was the first foray we had into stablecoins was looking at stablecoin backed accounts, somewhat like an FBO account that a lot of these fintechs get. So a way to hold customer funds through a different vehicle."

**Key Benefits:**
1. **Accelerated Innovation**: Provides a medium for fintechs to hold customer funds when traditional banking partnerships are difficult to establish
2. **Maintained Interoperability**: Still allows interaction with fiat rails and traditional banking system
3. **Orchestration Capabilities**: Enables seamless movement between stablecoin and fiat, similar to foreign exchange operations

**Critical Importance of Ledgering:**
Marcus emphasized that robust ledgering infrastructure is essential: "One of the things that the stablecoin backed accounts need is a strong ledger under the hood. And there's been no lack of news about bad ledgering over the last few years."

This reference to the Synapse collapse, where customers were locked out of accounts and some lost life savings due to alleged ledgering issues, underscores the critical nature of this infrastructure component.

**Modern Treasury's Ledger Product:**
The company built "the first Ledger's database product on the market" and works with "a lot of the leading crypto exchanges, stablecoin issuers" providing ledgering capabilities. Marcus noted: "We see what it looks like before they use ledgers. And people aren't ledgering in a lot of cases."

The platform "thinks about ledgering as a first class concern at scale, provides visibility to the fintechs" - treating it as fundamental infrastructure rather than an afterthought.

### Mastercard's Potential Acquisition of ZeroHash

Fortune reported that Mastercard is in talks to acquire ZeroHash for approximately $1.5-2 billion, representing a significant strategic move by a major payment network into stablecoin infrastructure.

**ZeroHash's Role:**
Itai Turbahn described ZeroHash's function: "Really, what ZeroHash does is moves money from fiat to stablecoins and from stablecoins to fiat. It does it at global scale and it does it in a compliant and very powerful way."

**Regulatory Infrastructure:**
ZeroHash has built extensive licensing:
- Money Transmitter Licenses (MTL) across multiple jurisdictions
- New York licenses (notably difficult to obtain)
- Global licensing coverage
- Significant presence in Latin America

**Strategic Value:**
The platform "takes a challenge that is, again, should be behind the scenes and moves it to be behind the scenes, right? And moves it from something that is front and center to just saying, you need a digital dollar? Give me a dollar. I'll give you a digital dollar."

**Mastercard's Motivation:**
Turbahn analyzed: "If you're a MasterCard, in my opinion, you're looking at, again, I am a giant financial corporation. I'm in the business of money movement and global network of money movement, and this is going to be a material part of it."

**Competitive Context:**
The discussion noted that Mastercard was also reportedly interested in BVNK, and that Visa had shown 4x quarter-over-quarter growth in stablecoin-linked card volumes. This suggests intense competition among payment networks to establish stablecoin capabilities.

**Historical Pattern:**
Dan Mottice observed: "Historically, MasterCard has been the first mover from a card network perspective as it relates to alternative ways of moving money. The Vocalink acquisition happened well before I think Visa entered alternative ways of moving money."

Mastercard's acquisition of Vocalink, which operates the UK's Faster Payments instant payment network, established a precedent for the company moving into alternative payment infrastructure.

### Stablecoin Volume Decoupling from Crypto Price Action

A critical market development discussed was the decoupling of stablecoin transaction volume from cryptocurrency price speculation, as documented in Andreessen Horowitz's 2025 crypto report.

**Significance of Decoupling:**
Itai Turbahn expressed strong optimism: "I'm actually extremely bullish on this, right? Like historically, we've talked about crypto as a financial asset. And now we've shifted the conversation to crypto at a technology rail."

**Shift in Use Cases:**
The conversation has moved from speculation to utility: "With things like L1s, like Tempo, etc., it's moving towards being essentially a very complementary, global-first, super-fast, super-cheap set of financial rails that you can leverage. That is a far more interesting conversation to me than price of Ethereum going up, going down."

**Money 2020 Conversations:**
Turbahn reported that at the recent Money 2020 conference, discussions centered on practical applications: "Can we pay, can we remit money faster to the other side of the world? Can we pay vendors? Can we run a global first neobank?"

**Customer Demand Signal:**
Matt Marcus provided ground-level validation: "We see our customers who are fintechs moving money in the US, like escrow businesses, for example, coming to us every day asking about stablecoins. So it's very real. It's not tied to the asset prices. People are interested in the technology, what it means for their business."

**Market Implications:**
Simon Taylor noted the growth trajectory: "I saw in the Visa results that they mentioned, their stablecoin linked card volumes were up 4x, quarter of a quarter. Now, if that continues for a few more quarters, it goes from being like two bips of their overall 2024 volumes to four, eight, 12, you know, it very quickly becomes meaningful amount of their overall volume."

This exponential growth pattern, if sustained, would rapidly transform stablecoins from a negligible to a material portion of major payment networks' transaction volumes.

### IBM's Partnership with DFNS

IBM announced a partnership with DFNS to create "Digital Asset Haven," a platform for managing crypto asset lifecycle within IBM Z series mainframes.

**Technical Scope:**
The platform is designed to:
- Manage custody, transactions, and settlement inside IBM mainframes
- Support up to 40 public and private blockchains
- Provide programmable multi-party approvals
- Integrate KYC, identity, AML, and yield generation services

**Market Context:**
Simon Taylor noted the significance: "Most financial institutions around the world, 70% of the world's money moves on some kind of IBM mainframe."

**Itai Turbahn's Analysis:**
As a former IBM Research employee, Turbahn provided insider perspective: "My outside-in looking perspective, they probably have identified a lot of customers that are coming their way and saying, look, I also want to now move stablecoins."

**Strategic Interpretation:**
Turbahn characterized this as a market test rather than a full product launch: "I read this much more in the lens of a giant corporation putting something out there at the first test to gauge market interest versus kind of an all-in IBM's now a stablecoin company."

**Success Metrics:**
"If in a couple months and years we see follow-up announcements from IBM as to more and more integrations into their system, I think that would be success. I'd count that as kind of the opening bell for IBM, not the full product."

### Fireblocks' Acquisition of Dynamic

Fireblocks acquired Dynamic to complete what Michael Shaulov described as "the complete stack for on-chain finance from custody to consumer."

**Dynamic's Core Offering:**
Itai Turbahn explained: "Dynamic is a wallet infrastructure company for developers. So if you're building your next remittance app or global neobank or payroll app, and you want embedded wallets, non-custodial embedded wallets in your app in order to store money for your end users... we give you the infrastructure to do that."

**Time-to-Market Value:**
"As a developer, within 10 minutes, you can spin up non-custodial embedded wallets for your users within your own UI, own interface."

Customers include Kraken, Stripe, and ZeroHash.

**Fireblocks' Existing Capabilities:**
Michael Shaulov outlined Fireblocks' seven-year history powering:
- Crypto-native companies
- Major fintechs (Revolut, NuBank)
- Market makers (Wintermute, Falcon X, Cumberland)
- Banks
- Remittance companies

**Strategic Rationale:**
Shaulov explained the market demand: "What we're seeing now more and more people coming is that they really want to provide their users something that is a much more DeFi on-chain experience, whether it's using non-custodial wallets or custodial doesn't really matter, but they really want this to be an on-chain wallet or an on-chain account."

**Complete Stack Vision:**
"From our standpoint, now we basically have the full stack to enable him to do anything from treasury, their backend wallets, their custody, and also then to essentially propagate all this functionality to their end users in a very, very simplified offering that from product and business standpoint gives them the fastest time to market."

**Product Roadmap:**
Turbahn outlined the abstraction strategy: "The goal is that any Web2 developer, any developer that is building, again, their next remittance app or payroll app or anything of that sort, can they do it within five minutes without knowing anything about crypto?"

The objective is to eliminate the need for developers to understand concepts like gas payments or on-ramps: "We have lost the plot if we start talking to folks about gas payments or on-ramps or anything of that sort, right?"

### Market Adoption Patterns and Future Outlook

**Current Adoption Wave:**
Michael Shaulov identified the fastest-growing segment: "It's basically all the international money movers, you know, companies like Ria and MoneyGram and all those guys, right? That's actually coming in as we speak."

**Web2 Platform Interest:**
"A lot of the conversations that we're having right now that started to pick up post-Genius Act, and especially I think after people came back from their summer vacation and actually had a bit of thinking about what they can do here, are the big platforms, the big tech platforms that the situation they have is that they have a very global contributors base, right, that they need to pay money to."

**Geographic Payment Gaps:**
Shaulov highlighted the limitations of existing solutions: "You want to push money to people in the United States or you want to push money to people in Europe solve problems more or less you want to push money to people in Indonesia and Philippines and in Africa or in Latin Americans and countries it's far from being solved and you would get like different SLAs and different cost structures."

This "variable user experience or variable SLA is part of the reasons why it's pushing them to look into stable coins as a first order solution."

**Two-Order Value Proposition:**
1. **First Order**: Access to markets and corridors not well-served by traditional rails
2. **Second Order**: Programmability and automation capabilities once infrastructure is in place

**Global Settlement Network Vision:**
Dan Mottice articulated the long-term vision: "Nobody's really bridged together all of the above. And in addition, reached into Asia and really assembled this kind of seamless mesh settlement network that we've all been talking about for a long while with stable coins, but haven't yet built."

**On-Chain FX Future:**
"As a derivative of that, right, on-chain FX will become a thing once that technology and those capabilities are built. And this kind of future state that we all talk about where a large majority of global commerce exists on-chain will actually come to fruition."

**Timeline Perspective:**
Mottice emphasized: "We're really still in kind of like inning one of many here as it relates to global adoption and true institutional adoption and migration of the vast majority of capital flows actually happens in an on-chain environment."

## Key Insights and Implications

### 1. Acquisition Strategy as Competitive Necessity

The episode title "Everyone Needs a Stablecoin Acquisition Strategy" reflects a fundamental market shift. Companies cannot build comprehensive stablecoin capabilities organically fast enough to remain competitive. The specialized expertise required across custody, wallet infrastructure, regulatory compliance, and payment orchestration necessitates M&A activity.

### 2. Ledgering as Critical Infrastructure

The emphasis on ledgering systems, particularly in the context of the Synapse collapse, reveals a often-overlooked but essential component of stablecoin infrastructure. Modern Treasury's positioning of their ledger database as a "first class concern" rather than an afterthought represents a maturation of the industry's understanding of operational requirements.

### 3. Regulatory Licensing as Moat

ZeroHash's extensive licensing across jurisdictions (MTL licenses, New York licenses, global coverage) represents a significant competitive advantage and barrier to entry. This regulatory infrastructure takes years to build and explains the premium valuation in potential acquisitions.

### 4. Abstraction as Product Strategy

Both acquisitions emphasize abstracting complexity away from developers and end-users. The goal of enabling Web2 developers to implement stablecoin functionality "within five minutes without knowing anything about crypto" represents a fundamental shift from crypto-native to mainstream adoption.

### 5. Geographic Payment Gaps Drive Adoption

The most compelling use case for stablecoins is not replacing well-functioning payment corridors (US, Europe) but addressing markets where traditional rails provide inconsistent service levels and high costs (Indonesia, Philippines, Africa, Latin America). This creates a clear value proposition beyond ideological arguments about decentralization.

### 6. Decoupling Signals Market Maturity

The separation of stablecoin volume growth from cryptocurrency price speculation indicates genuine utility-driven adoption. This represents a transition from stablecoins as trading instruments to stablecoins as payment infrastructure.

### 7. Payment Network Competition Intensifying

Mastercard's reported interest in ZeroHash and BVNK, combined with Visa's growing stablecoin-linked card volumes, suggests major payment networks view stablecoin infrastructure as strategically essential rather than experimental. This validates the technology's long-term viability.

### 8. Enterprise Adoption Accelerating

The shift from crypto-native companies to traditional remittance providers (Ria, MoneyGram) and Web2 platforms seeking to pay global contributor bases indicates mainstream enterprise adoption is underway, not merely anticipated.

## Definitions and Terminology

**Stablecoin**: A cryptocurrency designed to maintain a stable value relative to a reference asset, typically the US dollar, through various mechanisms including fiat backing, algorithmic controls, or collateralization.

**On-Ramp/Off-Ramp**: The process of converting between fiat currency and cryptocurrency (on-ramp) or cryptocurrency to fiat currency (off-ramp). The industry is moving toward abstracting these terms away as the process becomes seamless.

**Orchestration Layer**: Infrastructure that coordinates and manages transactions across multiple payment rails and networks, handling routing, conversion, and settlement logic.

**RTP (Real-Time Payments)**: A US instant payment system operated by The Clearing House that enables immediate funds transfer between participating financial institutions.

**FedNow**: The Federal Reserve's instant payment service launched in 2023, providing real-time payment and settlement infrastructure.

**Visa Direct**: Visa's real-time push payment platform that enables funds to be sent directly to eligible cards, accounts, and digital wallets.

**Push to Card**: A payment method that sends funds directly to a recipient's debit card, typically settling within minutes.

**FBO Account (For Benefit Of Account)**: A bank account held by one party for the benefit of another, commonly used by fintechs to hold customer funds.

**MTL (Money Transmitter License)**: State-level licenses required in the US to operate as a money transmitter, involving rigorous compliance and capital requirements.

**MPC (Multi-Party Computation)**: A cryptographic technique that allows multiple parties to jointly compute a function over their inputs while keeping those inputs private, used in wallet security.

**Embedded Wallet**: A cryptocurrency wallet integrated directly into an application's user interface, allowing users to interact with blockchain functionality without leaving the app or managing separate wallet software.

**Non-Custodial Wallet**: A wallet where the user maintains control of their private keys, as opposed to custodial wallets where a third party holds the keys.

**Ledger/Ledgering**: The system of record-keeping that tracks all financial transactions, balances, and account states. In the context of stablecoin operations, robust ledgering prevents discrepancies between actual funds and recorded balances.

**L1 (Layer 1)**: A base blockchain network (like Ethereum, Solana, or Tempo) that processes and finalizes transactions on its own blockchain, as opposed to Layer 2 solutions that build on top of existing blockchains.

**Gas Payments**: Transaction fees paid on blockchain networks to compensate for the computational energy required to process and validate transactions.

**Corridor**: In payments terminology, a specific route between two geographic locations or currencies (e.g., US to Philippines corridor).

**SLA (Service Level Agreement)**: Contractual commitments regarding service performance metrics such as transaction speed, uptime, and reliability.

## References and Citations

### Direct Quotations

**On Infrastructure Convergence:**
> "Fintech rails and crypto rails are pretty much like the same rails, right? They need to be intertwined. And over time, they're going to be more and more intertwined, right?" - Itai Turbahn

**On Market Validation:**
> "We see our customers who are fintechs moving money in the US, like escrow businesses, for example, coming to us every day asking about stablecoins. So it's very real. It's not tied to the asset prices." - Matt Marcus

**On Adoption Timeline:**
> "We're really still in kind of like inning one of many here as it relates to global adoption and true institutional adoption and migration of the vast majority of capital flows actually happens in an on-chain environment." - Dan Mottice

**On Abstraction Goals:**
> "We have lost the plot if we start talking to folks about gas payments or on-ramps or anything of that sort, right? And so the goal is to abstract more and more of that away, move that behind the veil." - Itai Turbahn

**On Geographic Payment Gaps:**
> "You want to push money to people in Indonesia and Philippines and in Africa or in Latin Americans and countries it's far from being solved and you would get like different SLAs and different cost structures and that variable user experience or variable SLA is part of the reasons why it's pushing them to look into stable coins as a first order solution." - Michael Shaulov

### Episode Details
- **Publication Date**: November 3, 2025
- **Show**: Tokenized (Episode 55)
- **Host**: Simon Taylor (GTM @ Tempo)
- **Guests**: Dan Mottice (Beam), Itai Turbahn (Dynamic), Matt Marcus (Modern Treasury), Michael Shaulov (Fireblocks)

### Sponsors Referenced
- Visa (Tokenized Assets Platform - VTAP)
- Bridge (Stripe company)
- Fireblocks

### External References
- Andreessen Horowitz 2025 Annual Crypto Report (stablecoin volume decoupling data)
- Fortune reporting on Mastercard-ZeroHash acquisition talks
- Money 2020 conference (Las Vegas, referenced as recent event)
- Synapse collapse (ledgering failure case study)
- Vocalink acquisition by Mastercard (UK Faster Payments)

### Acquisition Details
- **Modern Treasury acquires Beam**: Reported $40 million
- **Mastercard potential acquisition of ZeroHash**: Reported $1.5-2 billion (unconfirmed)
- **Fireblocks acquires Dynamic**: Terms not disclosed

### Growth Metrics
- Visa stablecoin-linked card volumes: 4x quarter-over-quarter growth
- Fireblocks monthly stablecoin volume: Over $100 billion
- Modern Treasury customer transaction volume: Hundreds of billions of dollars
- IBM mainframe coverage: 70% of world's money movement