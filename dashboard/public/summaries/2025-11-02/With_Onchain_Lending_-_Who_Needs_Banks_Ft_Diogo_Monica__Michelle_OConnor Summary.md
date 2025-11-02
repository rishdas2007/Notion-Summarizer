# With Onchain Lending - Who Needs Banks? Ft. Diogo Monica & Michelle O'Connor

**Citation:** "With Onchain Lending - Who Needs Banks? Ft. Diogo Monica & Michelle O'Connor." *Tokenized*, 27 Oct. 2025, <https://tokenized.simplecast.com/episodes/with-onchain-lending-who-needs-banks-ft-diogo-monica-michelle-oconnor-xxTqERH_>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Tempo's $500M Funding and Strategic Positioning](#tempos-500m-funding-and-strategic-positioning)
   - [The Rise of Vertically Integrated Payment Blockchains](#the-rise-of-vertically-integrated-payment-blockchains)
   - [Blockchain Decentralization Spectrum and Design Trade-offs](#blockchain-decentralization-spectrum-and-design-trade-offs)
   - [Ripple's Corporate Treasury Strategy](#ripples-corporate-treasury-strategy)
   - [On-Chain Treasury Management Challenges](#on-chain-treasury-management-challenges)
   - [Federal Reserve's Payment Account Proposal](#federal-reserves-payment-account-proposal)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Definitions and Terminology](#definitions-and-terminology)
5. [References and Citations](#references-and-citations)

## Executive Summary

This episode of the Tokenized podcast examines the evolving landscape of on-chain finance, focusing on three major developments: Tempo's $500M funding round and acquisition strategy, Ripple's $1B acquisition of G Treasury for corporate treasury management, and the Federal Reserve's proposed "payment account" signaling regulatory openness to crypto infrastructure.

**Main Arguments:**

1. **Payment-specific blockchains represent a new category** of infrastructure optimized for reliability, speed, and user experience rather than maximum decentralization, addressing the needs of the "99%" who don't currently use stablecoins.

2. **Corporate treasury management is emerging as a critical use case** for on-chain finance, with major companies seeking solutions for multi-currency, multi-bank complexity through stablecoins and tokenized assets.

3. **Regulatory harmonization remains the primary barrier** to global adoption, despite increasing openness from U.S. regulators, as different jurisdictions maintain incompatible frameworks.

**Key Participants:**
- **Simon Taylor** (GTM @ Tempo)
- **Cuy Sheffield** (Head of Crypto @ Visa)
- **Diogo Monica** (GP @ Haun Ventures, former Anchorage founder)
- **Michelle O'Connor** (Founder @ The Digital Future, former VP @ TaxBit)

The discussion reveals tension between crypto's original ethos of sovereign resistance and the practical requirements of payment systems serving mainstream users. Participants debate whether new payment chains represent genuine innovation or "not-invented-here syndrome," ultimately concluding that multiple approaches will coexist as the industry matures.

## Detailed Analysis

### Tempo's $500M Funding and Strategic Positioning

Tempo announced a $500M funding round led by GreenOaks and Thrive Capital, coinciding with two significant acquisitions: hiring Dankrad Feist (prominent Ethereum researcher) and acquiring Ithaca, led by Georgios Konstantopoulos. Ithaca has been a premier contributor to the Ethereum ecosystem, building the Porto client and Reth, focused on EVM performance and scalability.

**Strategic Rationale:**

Simon Taylor emphasized that Tempo is assembling world-class talent to build a payments-native blockchain. The company has identified product-market fit and aims to solve real problems through specific design choices:

- **Native account abstraction** at the chain level, eliminating the need for separate smart contracts to remove gas fees for users
- **Enshrined AMM (Automated Market Maker)** built into the protocol
- **Support for memo fields** and other payment-specific features as first-class citizens
- **Focus on reliability** comparable to traditional payment systems, where "payroll not happening" is unacceptable

Taylor acknowledged feeling "massively out of my depth" surrounded by technical talent, but emphasized the importance of product mindset: "thousands of tiny little decisions that add up to one great experience." He drew parallels to Stripe's success in making payment acceptance accessible through "seven lines of code," arguing that similar simplification is needed for on-chain payments.

**Decentralization Path:**

Taylor clarified that Tempo intends to be "decentralized, permissionless over time, starting with a closed validator set," following a path established by other successful chains. The platform will be "fully open to every single competitor in the Stripe stack," including Bridge competitors, Privy competitors, and other payments companies.

### The Rise of Vertically Integrated Payment Blockchains

Diogo Monica framed the emergence of payment chains as companies creating "their own ecosystems based on the blockchain," where they provide Oracle services, API services, and payment services, allowing developers to build within their ecosystem. He noted: "Before an ecosystem was a set of APIs, maybe dozens, and a documentation page that showed you how to use them. Maybe now the new actual ecosystems are just smart contract languages running on these blockchains."

**Key Characteristics:**

Monica highlighted surprising design choices in emerging payment chains:
- Some don't include smart contracts at all, prioritizing speed over generalizability
- Single-purpose focus on stablecoin payments or FX
- Vertical integration of services previously offered through separate APIs

**Market Structure Uncertainty:**

Monica acknowledged: "We don't know what the market structure is gonna be. These things are new." However, he observed that "very great companies with great brands and great engineering teams are putting serious money behind new vertically integrated blockchains."

**The "Death Star" Competition:**

Monica humorously noted that before Tempo, "it was pretty easy to identify the Death Star of crypto, which was absolutely Coinbase. And now there's competition for the Death Star." This metaphor captures the concentration of resources and talent in emerging payment infrastructure companies.

### Blockchain Decentralization Spectrum and Design Trade-offs

The discussion revealed fundamental tensions around blockchain design philosophy, particularly regarding decentralization versus performance.

**The Decentralization Spectrum:**

Monica articulated a spectrum view: "If I want to go very fast throughput, high availability, amazing engineering teams, I can go to something like Tempo, which, you know, is more corporate. There's going to be more SLAs, that type of like behavior. And if I want something on the fully centralized spectrum, I can go towards something more like Ethereum."

He argued that the crypto industry has been "chipping away at" the original requirement of sovereign resistance: "The main requirement that you're taking away that the crypto community started out with, with Bitcoin was sovereign resistance. And sovereign resistance just leads you to a totally different set of solutions."

**The NIH (Not-Invented-Here) Syndrome Debate:**

Monica provocatively suggested that 80% of new chain development represents NIH syndrome: "It's 80% it, where it was not invented here. And thus, I don't want to use it because I'm an engineer and I can actually build it myself."

Taylor pushed back, noting that Tempo's leadership (Liam and Georgios) "tried L2s and sort of found them wanting in terms of performance." He emphasized solving requirements "not yet solved" rather than removing requirements, specifically targeting "internet scale infrastructure" that doesn't currently exist.

**L1 vs. L2 Debate:**

Sheffield raised the question of why payment chains are predominantly L1s rather than L2s built on existing infrastructure. Michelle O'Connor deflected predictions but emphasized: "What's exciting is really the ability for wider adoption and testing and experimentation."

She cautioned against getting lost in technical debates: "We get in our own way so much. And we get in Twitter spats that are sometimes so interesting. And if you watch it, you just go, why are we down here in the weeds? And someone outside of the industry watching goes, what the hell are they even talking about?"

**Making Defaults Different:**

Taylor argued that "making the default different is powerful," suggesting that enshrining payment-specific features at the protocol level changes user behavior: "Nobody kind of uses it but if you enshrine it and you make it a part of how you do every single payment, you make the default different."

### Ripple's Corporate Treasury Strategy

Ripple acquired G Treasury for $1 billion, marking their third major acquisition in 2025. G Treasury's clients include American Airlines, Goodyear, and Volvo, processing $12.5 trillion in payments volume (timeframe unclear from reporting).

**Historical Context:**

O'Connor provided historical perspective, noting she started at BitReserve (now Uphold) in 2014, where founder Halsey Miner's vision was corporate treasury because "he couldn't be banked because he was a billionaire who'd had a few blips and bankruptcies." She observed: "Fast forward a decade plus later, it's really interesting to see this run of acquisitions that Ripple has had."

**The RLUSD-XRPL-XRP Question:**

Sheffield identified a critical strategic ambiguity: "What's not clear yet is how RLUSD translates to XRPL, translates to XRP." He noted that the majority of RLUSD supply runs on Ethereum, not XRPL, raising questions about the role of Ripple's native chain and token.

The acquisition strategy appears focused on distribution: "If you own the interface you own the distribution you're orchestrating payments or the prime brokerage business that they have, being able to embed RLUSD as the default in interesting ways."

**Monica's Assessment:**

Monica offered a blunt evaluation: "I think my take is that they don't even know themselves. That's what's happening. And it is primarily a currency or cryptocurrency that has gained mind share and it's a marketing engine that is now being turned to M&A into an actual business."

However, he praised Ripple's impact on the industry: "Before 2025, I believe there was exactly zero over a billion dollar M&A crypto. Zero. And then in 2025 alone, we've already had four, maybe five acquisitions over a billion dollars." This shift has changed VC conversations "from tokens are the thing that matters in crypto to, oh, it turns out equity actually has a lot of value."

**Distribution Hypothesis:**

Monica articulated Ripple's likely strategy: "If you have the customer relationship, if you have the flow, if you have the assets for custody, management, administration, then you'll be able to actually influence which stablecoin is appointing."

### On-Chain Treasury Management Challenges

The discussion identified corporate treasury as a critical emerging use case, with significant technical and regulatory barriers.

**The Value Proposition:**

Taylor explained the appeal for large corporations: "If I'm Netflix or if I'm Coca-Cola and I have to deal with lots of markets and lots of long-tail currencies, that gets really expensive and really hard. People think this is a fees problem. It's mostly a complexity issue."

The vision: "One wallet to rule them all per legal entity, where all of the deposits from all of the banks and all of my stable coins can just sit in a single pane of glass is like Nirvana to most CFOs."

**Privacy Concerns:**

Sheffield reported that privacy emerged as a top concern in treasury team discussions: "You're telling me that there might be a hedge fund that is able to detect that these wallets are supplier payments and figure out how much of these goods that we're buying over time? That's insane. It's the last thing that I want."

He concluded: "Privacy is probably going to be a major area that has to be solved if you're going to see the Coca-Colas of the world, like moving billions and billions of dollars on chain."

**FX and Multi-Currency Challenges:**

Sheffield identified foreign exchange as a critical gap: "I operate in a bunch of currencies. Right now I look at stablecoins and I only see dollars. And so when we have to convert from dollars to other currencies, well, then you have to go back off chain."

The liquidity question remains unresolved: "What's the liquidity of going USDC to MXN versus going USD to MXN? And so I think we're a ways from getting to the on-chain FX side."

**Regulatory Fragmentation:**

O'Connor highlighted the complexity of global operations: "You have different banks, different entities, different legal entities, different countries, different geographies, different regulatory bodies have different requirements, reporting, tax, etc. So it becomes something that should be very easy, moving instantly across borders to solve time, velocity scale, save money, have more insight into what you have becomes really challenging."

Taylor noted that "the lack of harmonization of regulatory regimes was going to be the major problem," citing this as the reason he named his 2017 initiative "Global Digital Finance": "On-chain is natively global, but regulation is not."

**Adoption Timeline:**

Sheffield predicted: "I will be surprised if there are a lot of things happening in the next six to 12 months, but I would be shocked if there's not a lot of things happening in three years."

**Ant Financial as Bellwether:**

Taylor pointed to Ant Financial as showing the future: "They have their own L2. They've been pushing all of the banks to tokenize. They've been pushing them to do FX. They're starting to issue their own treasury management token outside of Europe itself. That is like a typical Chinese company, three to five years ahead of everybody else."

### Federal Reserve's Payment Account Proposal

Federal Reserve Governor Waller signaled a major policy shift, proposing a "payments account" or "skinny version of a master account" for payment-focused entities.

**Key Quotes from Waller:**

"I wanted to send a message that this is a new era for federal reserve in payments. The DeFi industry is not viewed with suspicion or scorn. Distributed ledges in crypto are increasingly becoming woven into the fabric of payment financial systems."

**Master Account Benefits:**

Monica, having obtained Fed master account access twice (at Anchorage and currently), explained the value: "Fedmaster account allows you to have access directly to the banking system. The Fedwire system allows you to have your own accounts and essentially park money at the Fed. You also, in many cases, have access to the overnight window."

He noted the irony of his experience: "The first thing that they said when i came to this meeting was like, Diogo, welcome back. And I don't know exactly how to feel about this right now."

**The Narrow Banking Connection:**

Monica drew a fascinating historical parallel: "When the first narrow bank was actually being proposed it was shot down by the Fed. And the complaints from the traditional banks was that if there was a narrow bank and you had straight liabilities from the Fed, wouldn't this mean that everybody would just take their deposits away from the fractional reserve and just go straight to it?"

His conclusion: "Somehow crypto created a narrow bank called Stablecoins. And here we are. Now we sort of like backdoored into it."

**Systemic Implications:**

Monica argued this development "removes leverage from the system. It makes the banking system safer in general." He suggested traditional banks "are going to defend their own business. That's basically all I have to say about it, regardless of what the truth on the ground is."

**Significance Assessment:**

Sheffield concluded: "This seems like a really big deal," though the conversation was cut short at this point in the transcript.

## Key Insights and Implications

### 1. Payment Chains Represent a Distinct Category

Payment-specific blockchains are not simply "faster Ethereum" but represent a different design philosophy prioritizing reliability, user experience, and payment-specific features over maximum decentralization. This suggests the blockchain landscape will fragment into specialized infrastructure rather than converging on general-purpose platforms.

### 2. The Decentralization Spectrum is Widening

The industry has moved from a binary "decentralized vs. centralized" framework to a spectrum where different use cases demand different trade-offs. Monica's observation that "we started with sovereign resistance and we're sort of like chipping away at like the requirements" suggests the industry is maturing beyond ideological purity toward pragmatic problem-solving.

### 3. Corporate Treasury is the Next Major Use Case

Multiple participants identified corporate treasury management as a critical application area, but one that requires solving privacy, FX, regulatory compliance, and interoperability challenges. The 3-5 year timeline suggests this is a medium-term opportunity rather than immediate.

### 4. Regulatory Arbitrage Through Stablecoins

Monica's insight that "crypto created a narrow bank called Stablecoins" and "backdoored into it" reveals how the industry achieved through market innovation what was denied through regulatory channels. This pattern may repeat in other areas.

### 5. Distribution Trumps Technology

Ripple's acquisition strategy and Tempo's focus on user experience over pure technical performance suggest that distribution and product design may matter more than underlying technology for mainstream adoption. As Sheffield noted: "If you own the interface you own the distribution."

### 6. The M&A Market Signals Maturity

The emergence of billion-dollar+ acquisitions in crypto (zero before 2025, four-five in 2025) represents a fundamental shift in how value is captured and realized in the industry, moving from pure token appreciation to equity value creation.

### 7. Privacy is Non-Negotiable for Institutions

The repeated emphasis on privacy concerns from corporate treasury teams suggests that public blockchain transparency is a fundamental barrier to institutional adoption, requiring either privacy-preserving technologies or permissioned alternatives.

### 8. Global Regulatory Fragmentation is the Primary Barrier

Despite technical progress, the lack of harmonized regulatory frameworks across jurisdictions emerged as the most significant obstacle to realizing on-chain finance's global potential.

## Definitions and Terminology

**Master Account**: Direct access to Federal Reserve banking infrastructure, including Fedwire system and the ability to park money at the Fed. Provides access to overnight lending windows and core banking infrastructure without intermediaries.

**Payment Account**: Proposed "skinny version" of a master account specifically for payment-focused entities, representing potential regulatory accommodation for crypto infrastructure.

**NIH Syndrome (Not-Invented-Here)**: Engineering tendency to rebuild existing solutions rather than adopt them, often driven by belief that custom solutions will be superior. Monica estimates this accounts for 80% of new blockchain development.

**Sovereign Resistance**: The original Bitcoin design goal of creating financial infrastructure resistant to government control or censorship. Requires maximum decentralization and censorship resistance.

**Narrow Banking**: Banking model where deposits are fully backed by safe assets (typically central bank reserves or government securities) rather than lent out, eliminating fractional reserve risk. Historically opposed by traditional banks and regulators.

**Enshrined AMM**: Automated Market Maker functionality built directly into blockchain protocol rather than implemented as a separate smart contract layer.

**Account Abstraction**: Blockchain feature allowing smart contract wallets to pay gas fees on behalf of users, eliminating the need for users to hold native tokens for transaction fees.

**Memo Fields**: Payment metadata fields allowing additional information to be attached to transactions, standard in traditional payment systems but often lacking in blockchain implementations.

**VTAP (Visa Tokenized Assets Platform)**: Visa's platform using smart contracts and cryptography to help banks bring fiat currencies on-chain through tokenized assets.

**RLUSD**: Ripple's stablecoin (Ripple USD), currently deployed primarily on Ethereum despite Ripple's ownership of the XRPL blockchain.

**XRPL**: XRP Ledger, Ripple's native blockchain platform.

**L1 (Layer 1)**: Base blockchain protocol (e.g., Bitcoin, Ethereum, Solana).

**L2 (Layer 2)**: Secondary protocol built on top of a Layer 1 blockchain to improve scalability while inheriting security from the base layer.

**TEE (Trusted Execution Environment)**: Hardware-based security technology that creates isolated execution environments for sensitive computations, increasingly used for privacy in blockchain applications.

## References and Citations

### Episode Information
- **Title**: "With Onchain Lending - Who Needs Banks? Ft. Diogo Monica & Michelle O'Connor"
- **Show**: Tokenized (Episode 54)
- **Published**: 2025-10-27
- **Hosts**: Simon Taylor (GTM @ Tempo), Cuy Sheffield (Head of Crypto @ Visa)
- **Guests**: Diogo Monica (GP @ Haun Ventures), Michelle O'Connor (Founder @ The Digital Future)

### Key Sources Referenced
- Fortune Crypto reporting on Tempo's $500M funding round
- Federal Reserve Governor Waller's speech on payment accounts
- Ripple's acquisition announcements (Hidden Road, G Treasury)
- BIS (Bank for International Settlements) regulatory harmonization analysis

### Companies and Projects Mentioned
- **Tempo**: Payment-focused blockchain backed by Stripe
- **Ithaca**: Ethereum infrastructure company acquired by Tempo, builders of Porto client and Reth
- **Ripple**: Blockchain payments company, issuer of RLUSD stablecoin
- **G Treasury**: Corporate treasury management platform acquired by Ripple for $1B
- **Hidden Road**: Ripple acquisition for over $1B
- **Anchorage**: Digital asset bank founded by Diogo Monica
- **Ant Financial**: Chinese fintech with proprietary L2 (Jovi) focused on corporate treasury
- **Coinbase**: Referenced as the previous "Death Star of crypto"
- **Base**: Coinbase's L2 blockchain
- **Hyperliquid**: Referenced as example of decentralization spectrum
- **Solana**: General-purpose L1 blockchain
- **Ethereum**: General-purpose L1 blockchain
- **TaxBit**: Tax and accounting software for digital assets (O'Connor's former employer)
- **Global Digital Finance**: Industry organization founded by Taylor in 2017

### Sponsors
- **Visa**: Tokenized assets platform (VTAP)
- **Bridge** (a Stripe company): Stablecoin orchestration platform
- **Centrifuge**: DeFi platform for institutional finance products with over $1B TVL

---

**Validation Note**: This summary covers all major discussion topics from the transcript. The conversation was cut short during the Federal Reserve payment account discussion, so that section may be incomplete. All direct quotes are preserved with attribution. Technical terminology has been explained in context and in the definitions section. The summary maintains the conversational and sometimes contentious tone of the original discussion while organizing content thematically for clarity.