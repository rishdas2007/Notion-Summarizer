# Vault Curation and On-Chain Asset Management with Steakhouse Financial

**Citation:** "Vault Curation and On-Chain Asset Management with Steakhouse Financial." *Your uploads*, 03 Feb. 2026, <https://www.youtube.com/watch?v=nSbOtntTuXw>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Steakhouse Financial's Business Model and Evolution](#steakhouse-financials-business-model-and-evolution)
   - [Vault Architecture and Non-Custodial Guarantees](#vault-architecture-and-non-custodial-guarantees)
   - [Coinbase Integration: A Case Study](#coinbase-integration-a-case-study)
   - [Cryptographic vs. Social Guarantees](#cryptographic-vs-social-guarantees)
   - [Comparison with Decentralized Stablecoin Models](#comparison-with-decentralized-stablecoin-models)
   - [Future Evolution and Scaling Potential](#future-evolution-and-scaling-potential)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [References and Citations](#references-and-citations)

## Executive Summary

This document presents a comprehensive discussion with Adrian Vasiljevic and Sébastien Derivaux, co-founders of Steakhouse Financial, an internet-native asset manager specializing in non-custodial, on-chain investment products for stablecoins. The conversation explores vault curation as a transformational primitive for asset management, positioning it as both a complement and competitor to traditional financial instruments like ETFs.

**Core Thesis:** Vaults represent a fundamental innovation in financial infrastructure by offering cryptographically enforced guarantees that enable institutional-grade risk management without custodial risk. Steakhouse currently manages approximately $4 billion in assets under management (AUM), with roughly half allocated to asset-liability management for the Sky ecosystem and half to vault curation across platforms like Morpho and Coinbase.

**Key Arguments:**
- Non-custodial vaults provide superior transparency, risk management, and user protections compared to traditional financial products
- The vault model enables "internet-native asset management" that aligns with an economy increasingly denominated in stablecoins
- Cryptographic guarantees can replace or supplement traditional fiduciary responsibilities through smart contract logic
- The vault ecosystem is positioned for significant growth as fintechs, custodians, and eventually banks integrate DeFi yield products

**Strategic Vision:** Steakhouse views the global economy as "stablecoinizing rapidly" and positions vaults as the foundational infrastructure for this transition, enabling credit markets, yield generation, and asset allocation without traditional banking intermediaries.

## Detailed Analysis

### Steakhouse Financial's Business Model and Evolution

Steakhouse Financial has evolved through three distinct phases: individual contributors at MakerDAO, DAO advisory and consulting services, and finally their current incarnation as an internet-native asset manager. This progression reflects the maturation of DeFi infrastructure and the emergence of viable business models around vault curation.

**Background and Expertise:**
- Adrian Vasiljevic brings experience from Goldman Sachs and Bain & Company
- Sébastien Derivaux created the first decentralized Core Unit at MakerDAO, focusing on Real-World Assets (RWA) and financial reporting
- Both founders pioneered concepts like treating DeFi protocols as entities with balance sheets requiring financial statement analysis

**Current Operations:**
Steakhouse manages approximately $4 billion across two primary mandates:

1. **Asset-Liability Management ($2 billion):** Development of the Grove protocol for the Sky ecosystem, creating "stars" as dynamic asset allocation mechanisms constrained by governance processes
2. **Vault Curation ($2 billion):** Unconstrained product development focusing on foundational credit layers, primarily prime repo markets channeling DeFi's risk-free rate

The vault business serves predominantly institutional clients, including hedge funds, individual LPs, fintechs, custodians, and exchanges seeking earning products for their stablecoin platforms.

### Vault Architecture and Non-Custodial Guarantees

The technical architecture of Steakhouse vaults implements multiple layers of protection to minimize counterparty risk while maintaining operational flexibility.

**Core Protective Mechanisms:**

1. **Guardian Veto Rights:** Users can veto curator decisions through a guardian mechanism. For example, before adding new collateral types, there is a seven-day timelock during which the guardian can block the change. This protects depositors from unilateral risk profile alterations.

2. **Hard-Coded Parameters:** Investment mandates are enforced through smart contract logic rather than social agreements. Parameters include:
   - Eligible collateral types (e.g., CBBTC, wrapped ETH)
   - Loan-to-value (LTV) ratios (typically 86%, with some at 77%)
   - Concentration limits on individual collateral types
   - Platform restrictions (e.g., Morpho V1 vaults can only lend on Morpho)

3. **Transparency and Liquidity:** Full on-chain visibility into curator actions and underlying strategy liquidity enables real-time risk assessment by depositors.

**Product Segmentation:**
Steakhouse distinguishes between "prime" and "high yield" products:
- **Prime products:** Target rates slightly above the risk-free rate (referenced as "35% repo market rate" in the discussion, though this appears to be 3.5% based on context), emphasizing liquidity and low-risk collateral
- **High yield products:** Accept higher risk profiles with correspondingly higher returns, requiring more sophisticated underwriting

### Coinbase Integration: A Case Study

The Coinbase partnership exemplifies how vault curation can bridge traditional fintech platforms and DeFi infrastructure while maintaining non-custodial properties.

**Integration Architecture:**

1. **Collateral Side:** Coinbase users can use CBBTC (Coinbase's Bitcoin representation on Base network) as collateral to borrow USDC
2. **Lending Side:** Users deposit USDC into Steakhouse vaults directly through the Coinbase application without leaving the platform
3. **User Experience:** The integration channels DeFi functionality through Coinbase's familiar interface while maintaining true non-custodial properties

**Technical Implementation:**
- Deposits flow into Steakhouse vaults on the Base network
- Funds are allocated to collateralized lending against crypto assets (CBBTC, wrapped ETH, and similar quality assets)
- Users retain withdrawal rights and veto power over strategy changes
- Coinbase serves as the exclusive provider of these vault solutions on their platform

**Strategic Significance:**
This integration demonstrates that major custodians can offer DeFi yield products without taking custody of user funds, addressing regulatory concerns while providing competitive earning opportunities. As Adrian notes, "users actually experience DeFi, just channel through the user experience of Coinbase."

### Cryptographic vs. Social Guarantees

A central philosophical distinction in Steakhouse's approach is the prioritization of cryptographic guarantees over social guarantees (legal and reputational mechanisms).

**Conceptual Framework:**

**Social Guarantees:**
- Legal constructs like fiduciary responsibility
- Require threat of legal action to prevent malicious behavior
- Depend on regulatory enforcement and reputation
- Examples: traditional asset management, fund structures

**Cryptographic Guarantees:**
- Mathematically enforced through smart contract logic
- Make malicious behavior technically impossible rather than legally prohibited
- Enable trustless interactions between parties
- Examples: hard-coded LTV limits, timelock mechanisms, guardian vetoes

**Steakhouse's Hybrid Approach:**

While maximizing cryptographic guarantees, Steakhouse acknowledges that complete elimination of social guarantees is neither possible nor always desirable. Their strategy involves:

1. **Minimizing Social Layer:** Reducing social guarantees to primarily brand reputation—the promise that "a Prime Vault will always be a Prime Vault"
2. **Cryptographic Enforcement:** Implementing technical controls that make it impossible for curators to unilaterally alter risk profiles
3. **User Empowerment:** Providing depositors with veto rights and exit options that don't depend on curator cooperation

**Competitive Advantage:**

Adrian articulates the value proposition: "In order for a DeFi product to be successful, it needs to be able to make these strong, mathematically enforced guarantees to the user if it wants to be competitive with a traditional financial product."

This approach addresses the October-November credit crunch referenced in the discussion, where excessive reliance on social guarantees led to user losses even in supposedly low-risk repo lending markets.

### Comparison with Decentralized Stablecoin Models

The discussion contrasts vault curation with the Sky (formerly MakerDAO) model, highlighting different approaches to decentralization and risk management.

**Sky/MakerDAO Model:**

**Characteristics:**
- Fully automated collateralized lending/minting
- Decentralized governance requiring on-chain votes for all decisions
- Multiple contributors and companies participating
- "Regulatory immunity" through persistent on-chain existence
- Greater flexibility through collective governance preventing malicious actions

**Advantages:**
- Cannot be shut down; exists as long as blockchain operates
- Distributed decision-making reduces single points of failure
- Social layer (governance) provides security through collective oversight
- Less need for cryptographic guarantees due to governance checks

**Disadvantages:**
- Slower decision-making requiring coordination
- More complex governance processes
- Serves stablecoin liability side with different constraints

**Vault Curation Model:**

**Characteristics:**
- Single curator (e.g., Steakhouse) with defined mandate
- Faster execution with limited flexibility
- Clear counterparty for users to contact
- Cryptographic guarantees compensate for centralized curation
- Narrower application as building blocks rather than full ecosystems

**Advantages:**
- Rapid innovation and strategy adjustment
- Clear accountability and operational efficiency
- Strong cryptographic protections for specific use cases
- Modular design enabling composition with other protocols

**Disadvantages:**
- Company could cease operations (unlike perpetual on-chain protocols)
- Requires more cryptographic safeguards due to centralized control
- Counterparty risk on curator (though minimized through design)

**Complementary Relationship:**

Rather than competing, these models serve different purposes. As Adrian explains: "USDS is a stablecoin. So it has network effects and it has a funding cost that's necessary to raise the utility of that stablecoin... where the asset liability management equation for makers in the service of the users of USDS as a stablecoin." Vaults, by contrast, are "building blocks" with narrower applications that can integrate with stablecoin ecosystems.

Steakhouse's creation of vaults denominated in USDS exemplifies this complementarity, bridging "the more collective world or decentralized organization world to the more privately owned corporation that are managing vaults."

### Future Evolution and Scaling Potential

The discussion outlines a vision for vault evolution extending beyond current collateralized lending models toward more sophisticated financial operations.

**Current State:**
- Predominantly crypto-collateralized lending (prime repo markets)
- Limited integration of tokenized real-world assets
- Approximately $4 billion AUM across Steakhouse vaults
- Institutional adoption primarily through fintech and exchange integrations

**Evolutionary Trajectory:**

**1. Modular Decomposition:**
Following Morpho's approach, the future involves "decompos[ing] individual financial operations into the smallest possible unit, and then re-aggregat[ing] the liquidity around them in a modular way." This contrasts with vertically integrated product stacks that may lose network effects.

**2. Beyond Borrow-Lend:**
Expansion into additional financial primitives:
- Fixed-rate markets (Morpho's upcoming offerings)
- Pendle tokens for yield tokenization
- Leverage and carry strategies
- Duration exposure products
- Maturity-based instruments

**3. Risk Segmentation:**
Better separation of user risk appetites to avoid mixing prime and high-yield depositors in the same pools. The Stream Finance incident (involving Elixir and Stream collateral) demonstrated the dangers of inadequate risk segmentation, where "users who were looking for slightly more risk than prime mixed in with users that were comfortable lending to borrowers who were speculating with dog shit."

**4. Real-World Asset Integration:**

**Two Directional Flows:**

*Crypto to Real World:*
- Examples: Daylight, USDAI
- GPU lending for data centers (meeting real financing needs)
- DeFi-first origination models
- "Meeting a very real economic need by raising balance sheet in DeFi and allocating it into the real world"

*Real World to Crypto:*
- Initial phase: Capital accumulation (traditional finance seeking DeFi AUM)
- Mature phase: Thoughtful products leveraging stablecoin advantages
- Long-term winners will ask: "What are the inherent advantages of stablecoins to the way that we do business?"

**Scaling Pathways:**

**Wave 1 (Current):** Wealthy crypto natives and early adopters

**Wave 2 (Emerging):** Centralized exchanges and fintechs
- Coinbase integration as template
- Kraken and other exchanges following
- Universal fintech adoption of DeFi yield products

**Wave 3 (Near-term):** Custodians and digital asset treasuries
- Regulated custodians seeking yield on idle assets
- Preference for DeFi over failed centralized lenders (Celsius, BlockFi)
- Transparency advantage: "The only one that didn't add significant losses were DeFi because everything was transparent"

**Wave 4 (Medium-term):** Banks
- Driven by stablecoin competition and regulatory clarity
- Genius Act and Clarity Act creating framework for bank participation
- Banks as intermediaries or service providers rather than direct competitors

**Scaling Projections:**

While acknowledging that "40 million tomorrow" is unrealistic, Sébastien suggests that "over the next few years it's not impossible to see this kind of order of magnitude" (implying 10x growth from current $4 billion to $40 billion).

**Stablecoinization Thesis:**

The ultimate vision posits complete economic transformation: "Our long term direction of travel view is eventually the entire economy will stablecoinize." This includes scenarios where "a generation of children born today have to have a bank account in 18 years when they could, for example, open a wallet or open a social media app with a wallet balance."

### Vaults as Transformational Financial Instruments

The discussion positions vaults as comparable in transformational potential to ETFs, which disrupted mutual funds through aggregation, simplification, access, and lower fees.

**Vault Advantages Over Traditional Products:**

1. **Transparency:** Full on-chain visibility into curator actions and underlying positions
2. **Liquidity Exposure:** Real-time insight into strategy liquidity
3. **Scalability:** Potential to scale faster than ETFs due to programmable infrastructure
4. **Non-Custodial Security:** Users maintain control without trusting intermediaries
5. **Composability:** Modular design enabling integration across platforms

**Competitive Positioning:**

Vaults are "to a degree competitive, but largely complementary" to ETFs. The key differentiator is the value proposition for stablecoin-native users: "In a world where more people are native to stablecoins, it'll be the first and most obvious use of those stablecoins rather than, you know, off-ramping them into an ETF."

**Addressing Banking Sector Concerns:**

The vault model challenges the "deposit flight" anxiety in banking and central banking circles. Adrian argues this concern is "overwrought" because vaults demonstrate that "even when you have a system within forced narrow banking, like with stablecoins... you can still create a vibrant credit economy on top with a lot of origination taking place."

This positions vaults within the broader trend of private credit funds capturing market share from traditional bank lending, particularly in the U.S. market.

## Key Insights and Implications

### 1. Cryptographic Guarantees as Competitive Moat

The emphasis on mathematically enforced protections represents a fundamental rethinking of trust in financial services. Rather than relying on legal frameworks and reputation, Steakhouse demonstrates that smart contract logic can provide superior guarantees. This has profound implications for regulatory frameworks, which may need to recognize cryptographic enforcement as equivalent or superior to traditional fiduciary structures.

### 2. The Stablecoin Economy as Parallel Financial System

The vision of comprehensive "stablecoinization" suggests not merely incremental adoption but wholesale replacement of traditional banking infrastructure. The pathway from fiat bank accounts directly into DeFi vaults (bypassing traditional intermediaries) represents a structural threat to banking business models while potentially expanding credit availability.

### 3. Modular Finance as Design Philosophy

The Morpho-inspired approach of decomposing financial operations into atomic units and reaggregating them represents a paradigm shift from vertically integrated financial products. This modularity enables rapid innovation, better risk segmentation, and more efficient capital allocation—potentially addressing long-standing inefficiencies in traditional finance.

### 4. Risk Segmentation as Critical Success Factor

The Stream Finance incident and subsequent discussion highlight that vault success depends on proper risk segmentation. Mixing user risk appetites in undifferentiated pools creates adverse selection problems and potential losses. Future vault evolution must prioritize clear product differentiation between prime, high-yield, and specialized strategies.

### 5. Real-World Asset Integration Requires DeFi-First Thinking

The distinction between capital accumulation (traditional finance seeking DeFi AUM) and thoughtful product design (leveraging stablecoin advantages) suggests that successful RWA integration will come from projects that understand DeFi's unique properties rather than simply tokenizing existing products. Examples like GPU lending demonstrate how DeFi can address real-world financing gaps that traditional systems struggle to serve.

### 6. Institutional Adoption Follows Infrastructure Maturity

The progression from crypto whales to exchanges to custodians to banks reflects infrastructure maturation rather than mere marketing success. Each wave requires specific technical capabilities, regulatory clarity, and demonstrated track records. The Coinbase integration represents a template for how major platforms can offer DeFi exposure while maintaining user experience and regulatory compliance.

### 7. Complementarity Between Decentralized and Curated Models

Rather than viewing decentralized protocols (like Sky) and curated vaults as competitors, the discussion reveals them as complementary infrastructure serving different needs. Decentralized protocols provide persistent, censorship-resistant base layers, while curated vaults enable rapid innovation and specialized strategies. This suggests a layered financial ecosystem rather than winner-take-all competition.

## Data and Figures

### Assets Under Management

- **Total Steakhouse AUM:** $\approx \$4 \text{ billion}$
- **Asset-Liability Management (Sky/Grove):** $\approx \$2 \text{ billion}$
- **Vault Curation:** $\approx \$2 \text{ billion}$

### Vault Parameters

**Loan-to-Value Ratios:**
- Standard LTV: $86\%$
- Conservative LTV: $77\%$

**Guardian Timelock:**
- Veto period for collateral additions: $7 \text{ days}$

**Target Yields:**
- Prime vault target: "slightly above" risk-free rate (context suggests $\approx 3.5\%$ based on "35% repo market rate" likely being a transcription error)

### Projected Growth

**Scaling Trajectory:**
- Current AUM: $\$4 \text{ billion}$
- Potential medium-term target: $\$40 \text{ billion}$ (10x growth)
- Timeframe: "next few years"

### Market Context

**Stablecoin Regulatory Framework:**
- Genius Act (referenced for U.S. stablecoin regulation)
- Clarity Act (potential changes to yield restrictions)
- European regulations restricting native stablecoin yields

## Definitions and Terminology

**Vault:** A smart contract-based investment vehicle that pools user deposits and allocates them according to a defined strategy, with cryptographic guarantees protecting depositors from curator malfeasance.

**Vault Curation:** The practice of managing vault strategies, including collateral selection, risk management, and capital allocation, while operating within cryptographically enforced constraints.

**Non-Custodial:** A property of financial products where users maintain control of their assets without transferring custody to an intermediary. In vault context, this means curators cannot unilaterally withdraw or misappropriate user funds.

**Cryptographic Guarantees:** Protections enforced through smart contract logic and blockchain consensus mechanisms, making certain actions mathematically impossible rather than merely legally prohibited.

**Social Guarantees:** Protections that depend on legal frameworks, reputation, and threat of enforcement action rather than technical impossibility.

**Guardian:** A mechanism in vault architecture that allows designated parties (often representing depositors) to veto curator decisions during a timelock period, providing an additional layer of protection.

**Prime Vault:** A vault strategy focused on low-risk, highly liquid collateral (typically major crypto assets like BTC and ETH) targeting returns near the risk-free rate.

**High Yield Vault:** A vault strategy accepting higher-risk collateral or more complex strategies in exchange for higher expected returns.

**Repo Market:** Short for "repurchase agreement market," referring to collateralized lending where borrowers provide assets as security for short-term loans. In DeFi context, this typically means lending stablecoins against crypto collateral.

**LTV (Loan-to-Value):** The ratio of loan amount to collateral value, expressed as a percentage. An 86% LTV means borrowers can borrow up to 86% of their collateral's value.

**Morpho:** A DeFi lending protocol that provides the infrastructure for vault creation, emphasizing modularity and efficient capital allocation.

**USDS:** The stablecoin issued by Sky (formerly MakerDAO), designed to maintain a 1:1 peg with the U.S. dollar through overcollateralization.

**CBBTC:** Coinbase's Bitcoin representation on the Base network, a tokenized version of Bitcoin that can be used as collateral in DeFi protocols.

**Stablecoinization:** The hypothesized process by which stablecoins become the dominant medium of exchange and store of value in the economy, potentially replacing traditional bank deposits and payment systems.

**Asset-Liability Management (ALM):** The practice of managing the relationship between a protocol's assets (what it owns/invests in) and liabilities (what it owes to users/depositors) to ensure solvency and optimize returns.

**Real-World Assets (RWA):** Traditional financial assets (bonds, loans, real estate, etc.) that have been tokenized for use in DeFi protocols.

**Timelock:** A smart contract mechanism that delays the execution of certain actions, providing a window during which stakeholders can review and potentially veto changes.

## References and Citations

### Direct Quotations

**On Steakhouse's Identity:**
> "Steakhouse is today an internet native asset manager... What we do is we focus on building products for stablecoins that have very strong non-custodiality guarantees."

**On Non-Custodial Value Proposition:**
> "Non-custodiality is a very, very strong value proposition and frankly, one of the few, if not only reasons anyone would use these products as opposed to using a traditional financial product like an ETF."

**On Cryptographic vs. Social Guarantees:**
> "In the DeFi space, one of the value propositions is that you can actually not necessarily do away with fiduciary responsibility, but enforce it cryptographically in enough variables to make it actually impossible for the curator to be malicious."

**On Vault Transformation Potential:**
> "We view vaults as to a degree competitive, but largely complementary product in relation to ETFs that simply offers a different value proposition."

**On Smart Contracts as Agreements:**
> "Smart contracts is a clunky term for a script that runs on a blockchain, but it's kind of what it ends up looking like. It's an agreement between two parties that meet each other and they agree to a set of rules."

**On Stablecoinization Vision:**
> "Our long term direction of travel view is eventually the entire economy will stablecoinize. We think it's such a superior form of moving money in any currency that it will eventually take over."

**On Future Banking:**
> "There's no reason why a generation of children born today have to have a bank account in 18 years when they could, for example, open a wallet or open a social media app with a wallet balance or something similar and simply participate in the economy that way."

**On DeFi's Resilience:**
> "Every lender or every asset manager like Celsius, a BlockFi, all those kind of middlemen or shallow banking, they all blew up. So the only one that didn't add significant losses were DeFi because everything was transparent."

### Organizational Structure

This document follows a thematic rather than strictly chronological structure, organized around key conceptual areas:
1. Business model and positioning
2. Technical architecture and mechanisms
3. Specific implementation examples
4. Philosophical frameworks
5. Comparative analysis with alternative models
6. Future trajectory and scaling potential

The conversation itself was semi-structured, with the host guiding discussion through specific topics while allowing for organic exploration of related concepts. Time markers in the original document indicate approximate discussion points but were not strictly followed in this analysis, which prioritizes conceptual coherence over temporal sequence.