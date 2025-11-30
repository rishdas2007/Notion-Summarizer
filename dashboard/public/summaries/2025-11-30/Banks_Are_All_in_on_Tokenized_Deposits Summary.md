# Banks Are All in on Tokenized Deposits

**Citation:** "Banks Are All in on Tokenized Deposits." *Tokenized*, 24 Nov. 2025, <https://tokenized.simplecast.com/episodes/banks-are-all-in-on-tokenized-deposits-ylYTw99_>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [JPMorgan's JPMD on Base: A Watershed Moment](#jpmorgans-jpmd-on-base-a-watershed-moment)
   - [DeFi Consumer Products and Accessibility](#defi-consumer-products-and-accessibility)
   - [Institutional Staking Products](#institutional-staking-products)
   - [Tokenized Deposits vs. Stablecoins](#tokenized-deposits-vs-stablecoins)
   - [Regulatory Evolution and Node Operation](#regulatory-evolution-and-node-operation)
   - [Layer 2 Solutions and Control vs. Decentralization](#layer-2-solutions-and-control-vs-decentralization)
   - [User Experience and Wallet Infrastructure](#user-experience-and-wallet-infrastructure)
   - [Privacy Challenges and Solutions](#privacy-challenges-and-solutions)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Definitions and Terminology](#definitions-and-terminology)
5. [References and Citations](#references-and-citations)

## Executive Summary

This episode of the Tokenized podcast, hosted by Cuy Sheffield (Head of Crypto at Visa), features Sam McIngvale (Head of Product at Optimism Labs) and Lesley Chavkin (Ribbit Capital, former Head of Global Policy at Paxos) discussing the institutional adoption of blockchain technology, particularly focusing on tokenized deposits and their implications for traditional banking.

**Main Themes:**

1. **Major institutional adoption milestone**: JPMorgan executed the first live transaction of JPMD (JPMorgan deposit token) on Base, an OP Stack Layer 2 blockchain, at Singapore FinTech Fest—a conference run by regulators. This represents a significant shift in institutional comfort with public blockchains.

2. **Tokenized deposits emergence**: Major banks including JPMorgan, HSBC, Citibank, and others are racing to launch tokenized deposit products, primarily targeting corporate clients initially.

3. **Regulatory clarity improving**: The regulatory environment has evolved significantly, with clearer guidance on node operation, gas fee payments, and the distinction between money transmission and blockchain validation.

4. **DeFi accessibility**: New consumer-facing products like Aave's high-yield savings app (offering 5-9% returns with up to $1 million insurance) are abstracting blockchain complexity to reach mainstream users.

5. **Privacy as next frontier**: As blockchain adoption scales, privacy solutions are becoming critical for both consumer expectations and enterprise requirements, with various technical approaches under development.

The discussion reveals a fundamental shift from ideological debates about crypto to pragmatic implementation of blockchain as financial infrastructure, with institutions recognizing tangible business value in on-chain operations.

## Detailed Analysis

### JPMorgan's JPMD on Base: A Watershed Moment

The episode opens with Sheffield describing a pivotal moment at Singapore FinTech Fest where JPMorgan's Naveen (who leads Kinexys, formerly Onyx) conducted the first live transaction of JPMD on Base. Sheffield emphasizes the significance: **"to see one of, if not the largest financial institution in the world, transacting on base, paying a gas fee in ETH to be able to send a deposit token, JPMD, from one address to another Was pretty cool at a conference run by a regulator."**

This development represents multiple breakthroughs:

- **Public blockchain adoption**: JPMorgan is comfortable representing deposits on a public chain, contradicting earlier assumptions that banks would only use private or permissioned blockchains
- **Gas fee payments**: The bank paid transaction fees in ETH, addressing previous regulatory uncertainty about whether institutions could hold and use cryptocurrency for operational purposes
- **Regulatory acceptance**: The demonstration occurred at a regulator-run conference, signaling official comfort with these activities

The Office of the Comptroller of the Currency (OCC) subsequently confirmed bank authority to hold certain crypto assets to pay gas fees, providing additional regulatory clarity.

### DeFi Consumer Products and Accessibility

The discussion examines Aave's new consumer-facing application, which offers 5-9% yields on deposits with up to $1 million in insurance coverage. This product represents an evolution in DeFi accessibility by:

**Addressing complexity barriers**: Chavkin identifies two major DeFi adoption barriers from a regulatory perspective: complexity and trust. The Aave app addresses complexity by eliminating the need for users to manage self-custodial wallets or interact directly with decentralized protocols.

**Insurance as trust mechanism**: The "balance protection mechanism" provides insurance coverage that mimics FDIC protection, though it comes from Aave's corporate treasury rather than government backing. McIngvale notes that while insurance may be relevant for crypto-native users aware of DeFi risks, new users are likely more attracted to the headline yield rates, similar to Robinhood Gold's success in aggregating deposits.

**Blockchain abstraction**: The product abstracts away blockchain complexity entirely, with users potentially unaware of the underlying technology. Sheffield questions whether this represents a "DeFi mullet"—traditional interface with DeFi backend—though McIngvale suggests it may simply be a DeFi company expanding distribution.

**Regulatory positioning**: Aave is pursuing licensing in certain markets (including Europe) to operate as a regulated entity handling on-ramps while maintaining on-chain protocol backends. This hybrid approach attempts to satisfy regulatory requirements while preserving blockchain benefits.

### Institutional Staking Products

The episode discusses a 15% yield product from Figment, OpenTrade, and Crypto.com that combines Solana staking with perpetual futures to neutralize price volatility. While the exact mechanics remain somewhat opaque to the participants, the structure appears designed to:

**Separate yield from price volatility**: Traditional staking requires purchasing and holding a native token (like SOL), exposing holders to price fluctuations. The yield earned is also denominated in the volatile token. Sheffield explains: **"you could stake, which is generating yield, but then have some hedging of the price of the asset. So it doesn't matter whether the sole price goes up or down, you're still earning more of a steady yield."**

**Address liquidity concerns**: Staking typically involves lock-up periods where tokens cannot be accessed. McIngvale notes this creates a "liquidity premium" that institutions must consider. The product appears structured as "USDC in, USDC out whenever you want," eliminating this friction.

**Provide institutional-grade custody**: Assets are held in segregated custody by Crypto.com with compliance features, meeting institutional mandates and legal requirements.

**Aggregate deposits**: McIngvale suggests the 15% rate may be subsidized, as crypto institutions are willing to pay high prices to aggregate institutional deposits, similar to how traditional banks compete for deposits.

Chavkin observes that this structure allows institutions to participate in staking indirectly, in a "more simplified" and "institution-friendly" manner compared to direct staking operations.

### Tokenized Deposits vs. Stablecoins

A central theme is the distinction between tokenized deposits and stablecoins, with major banks including JPMorgan, HSBC, Citibank, BNY Mellon, and Standard Chartered launching or planning tokenized deposit products.

**Market size advantage**: McIngvale notes that global bank deposits vastly exceed stablecoin supply, making it logical for banks to tokenize existing deposit bases rather than create new stablecoin products: **"I'm guessing there's way, way, way, way, way more bank deposits in the world. And I expect that folks like JP Morgan, Alibaba, who have banking entities that have large bank deposits, sort of look at the TAM available to them of doing something with their existing Bank deposits versus doing something with stable coins."**

**Regulatory clarity**: Following passage of the GENIUS Act, banks have emphasized tokenized deposits. Chavkin observes: **"I wish I could see a chart of how many times banks talked about tokenized deposits before and after the Genius Act passed, because I feel like once it was passed and it was like, who needs Stable coins? We're going to tokenize deposits."**

**Structural differences**: Current tokenized deposit implementations include allow-lists in smart contracts, restricting transfers to KYC'd customers within the bank's ecosystem. Sheffield questions whether deposits could circulate more freely: **"can a tokenized deposit be transferred outside the bank? If JPMD wanted to, could they just take the allow list off of it? And could they let a JPMD deposit circulate globally the same way that a stablecoin would and be traded on an exchange and not be tied to a customer?"**

**Potential convergence**: Under the GENIUS Act, deposits are included as high-quality liquid assets that can back stablecoins. Sheffield raises the question: if a bank issues a stablecoin 100% backed by deposits, what distinguishes it from a tokenized deposit?

**Coexistence model**: Chavkin argues they are "fundamentally different products" that can coexist, with tokenized deposits potentially more suitable within a bank's ecosystem and stablecoins better for inter-institutional transfers.

**Reserve asset transparency**: Tokenized reserves could enable real-time monitoring of stablecoin backing, with products like Buidl and SuperState already being used as collateral.

### Regulatory Evolution and Node Operation

The discussion reveals significant regulatory evolution regarding blockchain node operation and validation:

**Historical concerns**: Sheffield recalls that 1-2 years ago, there were serious questions about whether banks could use public blockchains, whether node operators needed money transmitter licenses, and whether processing transactions from sanctioned jurisdictions created liability.

**Money transmission clarity**: Chavkin describes the evolution: **"if you think back a few years ago, Senator Warren had a proposal out there that any node operator be a money transmitter, right? And you saw some of that even under the last Treasury Department."** This position has largely been abandoned, with regulators moving toward recognizing that node operation provides a specific technical service distinct from money transmission.

**Developer protections**: Current market structure legislation drafts include clear developer protections, preventing prosecution as money transmitters. Chavkin expects this will extend to node operators.

**Existential importance**: McIngvale emphasizes this is potentially existential for public blockchains: **"if every node was required to register and to KYC, every wallet entity sending them a transaction before they verify and check the signatures, that seems like that just wouldn't be Feasible."**

**Internet infrastructure analogy**: McIngvale draws parallels to internet service providers, which don't face similar compliance burdens despite forming internet backbone infrastructure.

### Layer 2 Solutions and Control vs. Decentralization

McIngvale articulates Optimism's philosophy on balancing control with decentralization through Layer 2 architecture:

**Control for user experience**: Entities building products want control to deliver optimal experiences and meet compliance requirements: **"what they really want is control to deliver the best product experience they can to their customers. They also have compliance requirements, privacy requirements, all sorts of other stuff they have to deal with. But the best way to deliver really like uncompromising UX is probably to invest in a really beefy and bespoke sequencer."**

**Inherited decentralization**: Layer 2s on Ethereum can maintain a centralized sequencer for performance while inheriting Ethereum's decentralization properties for security and censorship resistance: **"you can kind of get the best of both worlds where folks can, you know, have all the crypto ideology that they want and, you know, sort of get transactions included on that L2 by leveraging Ethereum's decentralization."**

**Avoiding walled gardens**: McIngvale critiques current real-world asset tokenization where assets are tokenized but never move due to allow-lists: **"A lot of real-world assets that get tokenized, get tokenized into a smart contract and never move because there is an allow list or they're not able to go do anything yet."** He questions the value of blockchain integration without intention to leverage on-chain liquidity and composability.

**Network diversity**: Chavkin emphasizes that compliance burdens on nodes would "destroy the growth of these networks" by limiting participation to large institutions, undermining the value of diverse, geographically distributed validator sets.

### User Experience and Wallet Infrastructure

The discussion explores how tokenized deposits might change user interfaces and wallet experiences:

**Bring-your-own-wallet potential**: Sheffield suggests tokenized deposits could enable users to hold deposits from multiple banks alongside stablecoins and other assets in a single wallet (MetaMask, Coinbase Wallet, etc.), rather than being locked into each bank's proprietary interface.

**DeFi mullet model**: McIngvale predicts most users will access blockchain-based financial products through "DeFi mullets"—polished, bank-like interfaces with blockchain backends they don't see: **"I strongly suspect the future is DeFi mullets, where I don't even really know there's a blockchain in the back end, I'm just getting a better yield. I'm getting more assets to trade. I can borrow different stuff against my existing assets."**

**Ejection capability**: While most users may prefer integrated experiences, McIngvale emphasizes the importance of "eject buttons" allowing sophisticated users to exit to self-custody: **"what I hope exists is that there are eject buttons from these various apps that would allow the power user, the sophisticated user, or someone who is fed up or not getting served the Right way from their financial partner to eject out easily."** This optionality creates competitive pressure on financial institutions.

**Onboarding pathways**: McIngvale expects most new blockchain users will come through specific apps (Coinbase, Robinhood, neobanks) rather than directly to wallet interfaces, as these companies prioritize user experience control.

**Infrastructure vs. ideology**: Sheffield and McIngvale agree that framing blockchain as "financial infrastructure" or "financial technology" rather than emphasizing "permissionless" or "DeFi" terminology resonates better with traditional financial institutions, avoiding ideological baggage while focusing on practical benefits.

### Privacy Challenges and Solutions

Privacy emerges as a critical challenge for scaling blockchain-based financial products:

**Transparency trade-offs**: Chavkin notes that blockchain transparency benefits law enforcement compared to physical cash, but creates privacy concerns for average users: **"the average person probably doesn't want the world to be able to figure out how many times they've ordered from DoorDash, right? Like they don't want that out there. That's not what they have with their current financial products and services."**

**Enterprise requirements**: Sheffield observes that tokenized deposits create unprecedented transparency into bank operations, with transactions visible on block explorers. Large enterprises require privacy for competitive and operational reasons.

**Balancing act**: The challenge is providing basic privacy protections while maintaining law enforcement access with appropriate legal process (court orders, warrants).

**Technical readiness**: McIngvale asserts **"I think we're basically there"** regarding technical solutions. The OP Stack supports multiple privacy approaches:
- Fully shielded transactions
- Selectively shielded transaction elements
- Privacy pools integrated into protocols
- Selective revelation to trusted parties (sequencers, validators, regulators)

**Experimentation phase**: Financial institutions recognize privacy importance but haven't determined exact requirements. Multiple experiments are running on the OP Stack to develop practical privacy solutions.

**Preferred approach**: McIngvale favors selectively shielded transaction data that can be revealed to specific entities while keeping most blockchain information public, preserving transparency benefits while protecting sensitive details.

## Key Insights and Implications

### Institutional Adoption Drivers

The discussion reveals that institutional blockchain adoption is driven by **utility recognition** rather than ideology. Chavkin emphasizes: **"I actually think it's driven by the utility that regulated players are seeing in this space, right? Even when it was really difficult under the last administration for regulated institutions to engage in any kind of activity on permissionless chains, they were interested, right?"** Institutions maintained interest despite regulatory obstacles, and now face "FOMO" as they catch up on experimentation.

### Regulatory Environment Transformation

The regulatory landscape has undergone dramatic transformation. Proposals that would have required node operators to register as money transmitters—which would have been existential threats to public blockchains—have been largely abandoned. Current legislative drafts include developer protections, and regulators increasingly distinguish between technical infrastructure provision and financial services.

### Terminology and Framing Matter

The shift from "crypto" and "DeFi" terminology to "on-chain" and "financial infrastructure" language facilitates institutional conversations. McIngvale notes: **"The language that we found resonates best with sort of fintechs, banks, existing financial institutions, is just financial infrastructure or financial technology."** This reframing avoids ideological baggage while emphasizing practical benefits: 24/7 operation, native auditability, cross-border functionality, and composability.

### Tokenized Deposits as Competitive Response

The rush to tokenized deposits following the GENIUS Act suggests banks view this as competitive necessity rather than optional innovation. Multiple major institutions (JPMorgan, HSBC, Citi, BNY Mellon, Standard Chartered) are launching products simultaneously, indicating strategic importance.

### Privacy as Adoption Bottleneck

Privacy emerges as a critical requirement for mainstream adoption. Current blockchain transparency is incompatible with both consumer expectations (transaction privacy) and enterprise requirements (competitive confidentiality). While technical solutions exist or are near deployment, standardization and regulatory acceptance remain works in progress.

### Hybrid Models Dominating

The "DeFi mullet" model—traditional interfaces with blockchain backends—appears to be the dominant path for mainstream adoption rather than direct wallet-based interactions. This preserves user experience quality while enabling blockchain benefits, with "ejection" capabilities providing competitive pressure and user optionality.

### Stablecoins and Deposits as Complementary

Rather than competing, stablecoins and tokenized deposits appear to serve complementary functions. Deposits may be optimal within institutional ecosystems, while stablecoins facilitate inter-institutional and retail transactions. The potential for deposits to back stablecoins creates additional integration opportunities.

## Definitions and Terminology

**Tokenized Deposit**: A bank deposit represented as a token on a blockchain, maintaining the legal structure of a traditional deposit (FDIC insured, subject to banking regulations) while gaining blockchain properties (programmability, 24/7 availability, composability). Currently implemented with allow-lists restricting transfers to KYC'd customers.

**JPMD**: JPMorgan Deposit token, JPMorgan's tokenized deposit product that operates on Base (an OP Stack Layer 2 blockchain). Represents USD deposits and can be transferred between allow-listed addresses.

**Base**: A Layer 2 blockchain built on the OP Stack (Optimism's technology) and secured by Ethereum. Developed by Coinbase, it provides lower transaction costs and higher throughput than Ethereum mainnet.

**OP Stack**: Optimism's modular blockchain development framework that allows entities to deploy customized Layer 2 blockchains while inheriting Ethereum's security properties.

**DeFi Mullet**: A product design pattern combining a traditional, user-friendly interface ("business in the front") with decentralized finance protocols as the backend ("party in the back"). Users interact with familiar interfaces while benefiting from blockchain infrastructure.

**Gas Fee**: Transaction fees paid to blockchain validators/sequencers for processing transactions. On Ethereum and Layer 2s, typically paid in ETH or the chain's native token.

**Staking**: The process of locking cryptocurrency tokens to participate in blockchain validation and consensus, earning rewards in return. In Proof-of-Stake networks, stakers validate transactions and secure the network.

**Sequencer**: In Layer 2 blockchains, the entity responsible for ordering and executing transactions before they're batched and submitted to the Layer 1 blockchain (typically Ethereum). Can be centralized for performance or decentralized for censorship resistance.

**Allow-list**: A smart contract feature restricting token transfers to pre-approved addresses, typically used for compliance purposes to ensure all token holders have completed KYC/AML verification.

**GENIUS Act**: Federal legislation providing regulatory framework for stablecoins, including requirements for reserve assets, issuer licensing, and operational standards. Specifies high-quality liquid assets (including deposits) that can back stablecoins.

**Real-World Assets (RWAs)**: Traditional financial assets (real estate, bonds, commodities, etc.) that have been tokenized and represented on blockchains, enabling on-chain trading and composability.

**Perpetual Futures (Perps)**: Derivative contracts without expiration dates that track the price of an underlying asset, commonly used in crypto markets for hedging or speculation.

**OFAC**: Office of Foreign Assets Control, a U.S. Treasury Department agency that administers and enforces economic sanctions, including restrictions on transactions with sanctioned individuals and jurisdictions.

**KYC/AML**: Know Your Customer / Anti-Money Laundering—regulatory compliance processes requiring financial institutions to verify customer identities and monitor for suspicious activities.

## References and Citations

### Key Quotes

**On JPMorgan's milestone:**
> "to see one of, if not the largest financial institution in the world, transacting on base, paying a gas fee in ETH to be able to send a deposit token, JPMD, from one address to another Was pretty cool at a conference run by a regulator." — Cuy Sheffield

**On institutional motivation:**
> "I actually think it's driven by the utility that regulated players are seeing in this space, right? Even when it was really difficult under the last administration for regulated institutions to engage in any kind of activity on permissionless chains, they were interested, right?" — Lesley Chavkin

**On effective terminology:**
> "The language that we found resonates best with sort of fintechs, banks, existing financial institutions, is just financial infrastructure or financial technology." — Sam McIngvale

**On user experience future:**
> "I strongly suspect the future is DeFi mullets, where I don't even really know there's a blockchain in the back end, I'm just getting a better yield." — Sam McIngvale

**On privacy requirements:**
> "the average person probably doesn't want the world to be able to figure out how many times they've ordered from DoorDash, right? Like they don't want that out there." — Lesley Chavkin

**On Layer 2 design philosophy:**
> "you can kind of get the best of both worlds where folks can, you know, have all the crypto ideology that they want and, you know, sort of get transactions included on that L2 by leveraging Ethereum's decentralization." — Sam McIngvale

### Products and Announcements Referenced

- **Aave consumer app**: High-yield savings product offering 5-9% returns with up to $1 million insurance
- **JPMD on Base**: JPMorgan's tokenized deposit operating on Coinbase's Layer 2 blockchain
- **Figment/OpenTrade/Crypto.com staking product**: 15% yield institutional product combining SOL staking with perpetual futures
- **HSBC tokenization expansion**: Planned launch of tokenized deposits for US and UAE corporate clients
- **Alibaba/JPM Kinexys partnership**: Using tokenized deposits for cross-border B2B payments
- **OCC guidance**: Confirmation of bank authority to hold crypto assets for gas fee payments

### Regulatory Context

- **GENIUS Act**: Federal stablecoin legislation establishing regulatory framework
- **Senator Warren's historical proposal**: Previous suggestion that node operators be classified as money transmitters (now largely abandoned)
- **Market structure legislation**: Current Congressional drafts including developer protections
- **Singapore FinTech Fest**: Regulator-run conference where JPMD demonstration occurred

### Technical Infrastructure

- **OP Stack**: Optimism's Layer 2 framework used by Base and other chains
- **Ethereum**: Layer 1 blockchain providing security for Layer 2 solutions
- **Privacy solutions**: Various approaches including fully shielded transactions, selective shielding, and privacy pools

### Sponsors Mentioned

- **Visa**: Tokenized assets platform (VTAP) for banks to bring fiat currencies on-chain
- **Stripe/Bridge**: Infrastructure for stablecoin payments and cross-border transactions
- **Centrifuge**: Platform for tokenizing real-world assets with over $1 billion total value locked