# Ethereum Beast Mode - Scaling L1 to 10k and Beyond | Justin Drake

**Citation:** "Ethereum Beast Mode - Scaling L1 to 10k and Beyond | Justin Drake." *Bankless*, 12 Nov. 2025, <https://episode.flightcast.com/01K9SB8RF8XJ682AF0B9J1V3G6.mp3>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Lean Ethereum: Beast Mode and Fort Mode](#lean-ethereum-beast-mode-and-fort-mode)
   - [Current State and Scaling Goals](#current-state-and-scaling-goals)
   - [Rationale for L1 Scaling](#rationale-for-l1-scaling)
   - [Decentralization vs. Performance Trade-offs](#decentralization-vs-performance-trade-offs)
   - [SNARKs: The Cryptographic Foundation](#snarks-the-cryptographic-foundation)
   - [Lean Execution Architecture](#lean-execution-architecture)
   - [The Prover Role and Block Production](#the-prover-role-and-block-production)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [Methodology](#methodology)
7. [References and Citations](#references-and-citations)

## Executive Summary

Justin Drake of the Ethereum Foundation presents "Lean Ethereum," a comprehensive scaling proposal that aims to increase Ethereum's Layer 1 (L1) throughput by approximately 500x while simultaneously improving decentralization. The plan centers on two complementary objectives: **Beast Mode** (aggressive scaling to 10,000 TPS on L1 and 10 million TPS across L2s) and **Fort Mode** (enhanced security, decentralization, and post-quantum resistance).

The core technological enabler is SNARKs (Succinct Non-interactive Arguments of Knowledge), cryptographic proofs that allow validators to verify block validity without executing transactions. This paradigm shift—from execution to verification—removes the primary bottleneck to L1 scaling while reducing hardware requirements to consumer-grade devices (potentially as low as an $8 Raspberry Pi Pico).

Key targets include:
- **L1 scaling**: From current 2 megagas/second to 1 gigagas/second (500x increase)
- **L2 aggregate capacity**: 1 teragas/second through enhanced data availability
- **Validator requirements**: Reduction from laptop-class hardware to smartphone/smartwatch capability
- **Proving requirements**: 10 kilowatt on-premises proving (equivalent to a Tesla home charger)
- **Finality**: Reduction from 10-20 minutes to seconds via the Fossil protocol

The proposal represents a strategic pivot from the roll-up-centric roadmap, acknowledging that SNARK technology has matured sufficiently to enable L1 scaling without compromising Ethereum's core value proposition as decentralized money. Drake argues this is essential for Ethereum to serve as the primary settlement layer and monetary base for global finance, positioning it to absorb innovation that has fragmented across competing L1 chains.

## Detailed Analysis

### Lean Ethereum: Beast Mode and Fort Mode

Lean Ethereum represents a dual-pronged approach to blockchain optimization, leveraging SNARK cryptography to achieve seemingly contradictory goals: massive throughput increases alongside enhanced decentralization.

**Beast Mode** encompasses:
- **L1 execution scaling**: Target of 1 gigagas per second, translating to approximately 10,000 transactions per second (assuming 100,000 gas per transaction average)
- **L2 data availability**: Enhanced to support 1 teragas per second aggregate across all rollups
- **Practical capacity**: Sufficient for 0.1 transactions per human per day at L1, scaling to 100 transactions per human per day when including L2s

Drake frames this as "having enough throughput for all of finance," acknowledging that while L1 capacity alone is insufficient, it provides the foundation for a comprehensive scaling solution when combined with L2 infrastructure.

**Fort Mode** focuses on security and resilience:
- **Uptime**: Maintaining Ethereum's 100% uptime record since genesis
- **Decentralization**: Lowering validator hardware requirements to maximize participation
- **Post-quantum security**: Transitioning cryptographic primitives to quantum-resistant alternatives
- **MEV decoupling**: Cleanly separating MEV extraction from validator operations
- **Fast finality**: Reducing finality time from 10-20 minutes to seconds through the Fossil protocol

The terminology deliberately evokes offensive (beast) and defensive (fort) military strategies, reflecting Ethereum's dual mandate to compete for market share while maintaining its security guarantees. Drake emphasizes that the same SNARK technology enables both modes: by allowing validators to verify small proofs rather than execute full blocks, the system can simultaneously increase throughput and reduce hardware barriers.

### Current State and Scaling Goals

Ethereum's current execution capacity stands at approximately 2 megagas per second, with a gas limit that has grown only 50% over four years (from 30 million to 45 million gas per block). This translates to roughly 20 simple transactions per second, far below the requirements for global financial infrastructure.

**The 500x Gap:**

Current state:
- Gas limit: ~45 million gas per 12-second slot
- Effective rate: 2 megagas/second
- Simple transactions: ~20 TPS
- Complex transactions (DEX swaps): ~4 TPS

Target state:
- Effective rate: 1 gigagas/second (1,000 megagas)
- Simple transactions: ~10,000 TPS
- Complex transactions: ~2,000 TPS
- Per-capita capacity: 0.1 transactions/human/day

Drake contextualizes this target using powers of ten: with roughly $10^{10}$ (10 billion) people on Earth and approximately $10^5$ (100,000) seconds per day, achieving $10^9$ gas per second enables $0.1$ transactions per human per day. While acknowledging this is "a great start," he emphasizes it's insufficient for comprehensive financial activity, necessitating the L2 scaling layer.

The L2 target of 1 teragas per second ($10^{12}$ gas/second) would provide 100 transactions per human per day, which Drake considers adequate for "all of finance" when accounting for both human and automated (robot) transactions.

**Historical Context:**

The modest 50% increase over four years reflects Ethereum's prioritization of decentralization over raw performance. Drake notes this growth rate has "underperformed even Moore's law and hardware improvements," characterizing it as "not very beastly." This conservative approach was necessitated by the lack of cryptographic tools to scale without centralizing validator operations.

### Rationale for L1 Scaling

The decision to aggressively scale L1 represents a strategic shift from the roll-up-centric roadmap, raising questions about why L1 scaling is necessary when L2s were intended to handle execution.

**Primary Justifications:**

1. **Technological Enablement ("Because We Can"):**
   Drake acknowledges this represents "a change" and "a pivot" from previous strategy. The key unlock is SNARK maturity: "we have now technology that allows us to scale while preserving decentralization." He suggests that had ZKVMs been available five years earlier, L1 scaling would have been the default path, though L2 data availability would still have been necessary for millions of TPS.

2. **Hub Functionality:**
   For Ethereum to serve as the primary settlement layer, it requires minimum viable scale. Drake identifies critical L1 use cases:
   - Asset minting and primary issuance
   - Cross-chain bridging operations
   - Forced withdrawal mechanisms (escape hatches)
   - High-value settlement transactions
   - Deep liquidity pools

   Without adequate L1 capacity, these functions become prohibitively expensive, potentially pricing out legitimate use cases. The 0.1 transactions per human per day target represents "the highest density economic transactions that can make it," with others "potentially priced out."

3. **Competitive Positioning:**
   Drake argues that Ethereum's failure to scale L1 has caused innovation fragmentation: "To a large extent, the reason why we have so much fragmentation at L1 is because Ethereum hasn't grown fast enough to absorb all of the innovation." With a credible L1 scaling roadmap, Ethereum can "absorb the entirety" of blockchain innovation rather than ceding market share to competing chains.

**The Store-of-Value Thesis:**

When pressed on specific use cases requiring maximum decentralization, Drake identifies "store of value" and "moneyness" as paramount. He points to empirical market validation: Ethereum's market capitalization and DeFi total value locked demonstrate that "robustness, fort mode, uptime, credible neutrality, moving slowly, having these long-term guarantees are things that are extremely important."

Drake distinguishes between crypto-native bearer instruments (primarily ETH) and custodial assets (like USDC), arguing that store-of-value properties are most critical for the former. He frames Ethereum's primary application as "being money," from which "all of the applications derive"—loans, exchanges, prediction markets all depend on "this strong money."

This leads to a winner-take-most argument: monetary premium concentrates in the most legitimate asset, and maintaining that legitimacy requires never being "disqualified" through downtime or security failures. Drake controversially suggests that Bitcoin will eventually be "disqualified" due to its "dwindling issuance" (currently 99.5% of miner revenue comes from issuance rather than fees), while Solana has already been disqualified by its "10 outages over a handful of years."

### Decentralization vs. Performance Trade-offs

The discussion addresses a fundamental tension: other L1 chains (Solana, Monad, BNB Chain) achieve higher throughput today, raising questions about whether Ethereum's constraints are necessary or represent a "skill issue."

**Competing Approaches:**

High-performance L1s typically employ:
- **Limited validator sets**: ~100 validators (Monad), <1,000 (Solana)
- **Data center requirements**: High-bandwidth connections, substantial RAM, fast CPUs, large state storage
- **Geographic concentration**: Drake notes that many Solana validators are "in two data centers that are just a few dozens of kilometers apart from each other in Europe"

Ethereum's self-imposed constraints:
- **Home internet connections**: No assumption of data center bandwidth
- **Commodity hardware**: Laptop-class devices (historically "Raspberry Pi" as the meme)
- **Geographic distribution**: Maximizing resistance to coordinated attacks
- **Validator count**: Currently ~10,000 independent operators (distinct from the millions of logical 32 ETH validators)

**The Liveness Argument:**

Drake articulates Ethereum's extreme paranoia: "We want to have a security model where even if all data center operators in the world decide to attack Ethereum simultaneously, it still has uptime." With approximately 100 major data center operators globally, this threat model is "not totally far-fetched."

This explains Ethereum's 100% uptime since genesis, contrasted with recent AWS outages that took down various competing chains. Drake characterizes this as refusing to "cut corners" for performance gains, prioritizing long-term resilience over short-term competitiveness.

**The Engineering vs. Evolution Distinction:**

David Hoffman frames competing chains as "engineering first"—optimizing software to run efficiently in data centers. Ethereum, by contrast, is undergoing "something closer to an evolution rather than an engineering upgrade." The SNARK-enabled path represents not merely better engineering but a fundamentally different approach enabled by cryptographic advances.

This distinction is crucial: Ethereum's scaling strategy was "always kind of been in the back pocket... from day one" as "the theoretical scaling strategy," but only recently has "this path become clear to us" as SNARK technology matured.

**Generational Preferences:**

Hoffman observes a generational divide in crypto: pre-2021 participants prioritize "fort mode" (decentralization, security), while post-2021 entrants disproportionately value "beast mode" (throughput, user experience). He notes that "user preferences has been shifting away from fort mode and into beast mode as blockchains become mainstream adopted."

Drake counters that "beast mode without fort mode" produces "very shallow activity," citing Solana's 10+ million meme coins with aggregate market cap under $10 billion—"an absolute drop in the bucket" compared to single Ethereum use cases like Tether ($100+ billion) or ETH itself (50x larger than all Solana meme coins combined).

### SNARKs: The Cryptographic Foundation

SNARKs represent the technological breakthrough enabling Lean Ethereum, but understanding their role requires context on blockchain cryptography evolution.

**Cryptographic Primitives:**

Bitcoin and Ethereum have relied on "Stone Age cryptography":
1. **Hash functions**: Enable blockchain structure (linking blocks) and Merkle trees (state commitments)
2. **Digital signatures**: Authenticate ownership and authorize transactions

These primitives, while robust, offer limited design space for scaling. Drake characterizes them as "extremely primitive" relative to modern cryptography.

**SNARK Properties:**

The acronym breaks down as:
- **S**uccinct: Proofs are small (constant size regardless of computation)
- **N**on-interactive: No back-and-forth communication required
- **AR**gument of **K**nowledge: Cryptographic proof of correct computation

Drake simplifies: "SNARK is nothing more than a small proof."

The "ZK" (zero-knowledge) terminology, while ubiquitous in "ZKEVMs," is technically misleading for scaling applications. Zero-knowledge refers to privacy properties (proving something without revealing information), but Ethereum's scaling use case doesn't leverage this feature. Drake confirms they "should be called SNARK EVMs" but acknowledges "it's a lost fight" in terminology.

**Historical Development:**

- **Theoretical origins**: ~30 years of academic research
- **Practical deployment**: Zcash (2016) as first production use, ~9 years ago
- **Early risks**: Drake characterizes early Zcash as "cryptographic DGENs... building rockets" that "could explode in their face"
- **Critical bug**: Zcash experienced a vulnerability allowing arbitrary token minting; due to privacy features, it's unknown if this was exploited
- **Maturation**: Last 1-2 years have seen emergence of ZKVMs, enabling practical Ethereum integration

**Security Approach:**

Ethereum plans two complementary strategies:

1. **Diversity**: Deploy five different SNARK implementations with "uncorrelated failures," accepting blocks as valid if 3-of-5 proofs verify correctly. This mirrors existing execution/consensus client diversity.

2. **Formal verification**: Mathematically prove SNARK implementation correctness, eliminating bugs through rigorous proof rather than testing. The Ethereum Foundation launched a $20 million formal verification program led by Alex Hicks, with Drake expecting "end-to-end formally verified SNARK, which has zero bugs" by 2029-2030.

**ZKVM Abstraction:**

Early SNARK applications (like Zcash) required "custom circuits"—hand-crafted cryptographic constructions requiring deep expertise. Modern ZKVMs provide abstraction layers allowing standard developers (e.g., Rust programmers) to write normal code that compiles to SNARK-provable execution.

This is critical for Ethereum because it enables taking existing EVM implementations (Reth, Geth, Nethermind, etc.) written in various languages (Rust, Go, C#) and compiling them to ZKVMs. This preserves implementation diversity while adding SNARK provability.

**Requirements for Ethereum:**

Drake outlines stringent requirements beyond basic SNARK functionality:

1. **Real-time proving**: Proofs must be generated within one Ethereum slot (under 12 seconds) to avoid delaying block production
2. **Diversity**: Five independent ZKVM implementations to prevent single points of failure
3. **On-premises proving**: Provers must operate outside data centers, targeting 10 kilowatt power consumption (equivalent to 10 toasters or a Tesla home charger)
4. **Post-quantum security**: Long-term cryptographic sustainability against quantum computing threats

These requirements significantly constrain the design space but are deemed essential for Ethereum's security model.

### Lean Execution Architecture

The core innovation of Lean Ethereum is shifting validators from **execution** to **verification**, fundamentally changing the validator role and enabling massive scaling.

**Traditional Validator Requirements:**

Current validators must:
1. **Download blocks**: Bandwidth-intensive, especially for large blocks
2. **Maintain state**: Store ~100+ GB of current Ethereum state (potentially terabytes with higher gas limits)
3. **Execute transactions**: Requires multi-core CPUs and substantial RAM
4. **Maintain mempool**: Track pending transactions and peer connections
5. **Store history**: Hundreds of gigabytes of historical data

Drake characterizes this as "extremely intensive" and "crazy machinery" that creates the primary bottleneck to scaling.

**SNARK-Enabled Verification:**

With SNARKs, validators instead:
1. **Download small proofs**: Constant size regardless of block size
2. **Verify proofs**: Computationally lightweight operation
3. **No state storage**: "Stateless" verification
4. **No history storage**: "History-less" operation
5. **Minimal RAM**: ~100 kilobytes instead of gigabytes
6. **Single weak core**: No multi-core requirement

**The Raspberry Pi Pico Vision:**

Drake introduces a new hardware target: the Raspberry Pi Pico, an $8 microcontroller (versus ~$100 for a standard Raspberry Pi). He believes "at least as a fun experiment, we can have a validator run on a Raspberry Pi Pico."

This implies validators could run on:
- Smartphones
- Smartwatches
- Embedded devices
- Any consumer electronics with basic computing capability

**User Sovereignty:**

Beyond validator benefits, SNARK verification enables direct user verification of Ethereum state within browser tabs or mobile apps. Currently, users rely on intermediaries (Infura, MetaMask, Etherscan) to access Ethereum state, creating trust dependencies and censorship vectors.

With lightweight verification:
- **Resilience**: Users can transact even if Infura goes down
- **Censorship resistance**: Intermediaries cannot filter OFAC-sanctioned transactions
- **Security**: Malicious front-ends (e.g., compromised Etherscan) cannot misrepresent state
- **Sovereignty**: Users directly verify chain validity without trusted third parties

Drake frames this as "more sovereignty over what is the valid state of the chain," reducing dependence on infrastructure providers.

**The Dual Achievement:**

SNARKs simultaneously enable:
1. **Beast Mode**: Removing execution bottleneck allows 500x throughput increase
2. **Fort Mode**: Reducing hardware requirements increases decentralization beyond current levels

This "double-edged sword" resolves the traditional scaling trilemma by using cryptography rather than economic or engineering trade-offs.

### The Prover Role and Block Production

While validators shift to verification, execution must still occur. This introduces a new actor: the **prover**.

**Prover Responsibilities:**

Provers generate SNARK proofs demonstrating correct block execution. This is computationally intensive, requiring:
- Significant processing power
- Specialized hardware (potentially ASICs or FPGAs)
- ~10 kilowatt power consumption for on-premises operation
- Sub-12-second proof generation (real-time proving requirement)

**Deployment Phases:**

1. **Optional Proofs (Current/Near-term):**
   - Relies on altruism: actors voluntarily generate proofs
   - Validators opt-in to verify proofs
   - Serves as proof-of-concept
   - No economic incentives

2. **Mandatory Proofs (Target State):**
   - Block producers must include proofs
   - Blocks without valid proofs are invalid (excluded from canonical chain)
   - Economic incentives: block producers earn fees/MEV and face penalties for missed blocks
   - Rational actors will ensure proof generation to capture rewards

**Block Production Pipeline:**

Current structure (with Proposer-Builder Separation):
1. **Proposer**: Randomly selected validator for each slot
2. **Builder**: Sophisticated entity constructing economically optimal blocks
3. **MEV-Boost**: Middleware facilitating proposer-builder separation

Future structure (with provers):
1. **Proposer**: Unchanged (randomly selected validator)
2. **Builder**: Constructs blocks and coordinates proving
3. **Prover**: Generates SNARK proofs (potentially outsourced by builder)
4. **Validator**: Verifies proofs rather than executing blocks

**Centralization Concerns:**

The builder landscape is "fairly centralized," raising questions about whether adding provers introduces new centralization vectors. Drake addresses this through the **honesty assumption framework**:

- **Consensus (validators)**: Requires 50% honest participants (extremely high bar)
  - Current: ~10,000 independent operators
  - Target: Maintain or increase through lower hardware requirements

- **Proving**: Requires only **1-of-N** honest prover (much lower bar)
  - Acceptable to have higher hardware requirements
  - Centralization less problematic due to different trust model
  - Even if 99% of provers are malicious/offline, one honest prover suffices

This asymmetry justifies different hardware requirements: validators must be maximally accessible (Raspberry Pi Pico), while provers can require more substantial infrastructure (10 kilowatt on-premises setups) without compromising security.

**Vertical Integration vs. Separation:**

Drake expects builders will initially bundle proving (vertical integration) but anticipates eventual separation of concerns, with specialized proving markets emerging. This mirrors the evolution from integrated mining to specialized mining pools in proof-of-work systems.

The 10 kilowatt target for on-premises proving is deliberate: it matches residential electrical capacity (equivalent to a Tesla home charger), enabling home-based proving operations rather than forcing data center deployment. Drake argues that if "millions of home chargers" exist worldwide, similar prover distribution is achievable.

## Key Insights and Implications

### Strategic Repositioning

Lean Ethereum represents Ethereum's first credible "beast mode" offensive strategy after years of defensive fort-building. This acknowledges that while decentralization and security are necessary, they are insufficient for market leadership without competitive throughput. The timing reflects SNARK maturity rather than strategic error in the roll-up-centric roadmap.

### Monetary Premium as North Star

Drake's emphasis on "moneyness" and store-of-value properties clarifies Ethereum's core value proposition. The argument that Bitcoin will be "disqualified" by dwindling issuance (currently 99.5% of miner revenue) while Solana has already been disqualified by downtime positions Ethereum as the only credible long-term monetary base layer. This frames L1 scaling not as feature competition but as ensuring the monetary layer has sufficient capacity for settlement and high-value transactions.

### Cryptography as the Scaling Primitive

The distinction between cryptographic scaling (SNARKs) and engineering scaling (optimized data center nodes) is fundamental. Drake's principle that "the true way blockchain scale is with cryptography" reflects a belief that sustainable scaling must preserve decentralization properties rather than trade them away. This positions Ethereum's delayed scaling as strategic patience waiting for cryptographic maturity rather than technical inability.

### The 1-of-N vs. 50% Honesty Asymmetry

The different trust models for validators (50% honest) versus provers (1-of-N honest) is underappreciated but crucial. It justifies asymmetric hardware requirements and explains why prover centralization is less concerning than validator centralization. This insight enables the entire Lean Ethereum architecture: validators can use minimal hardware because they only verify, while provers can use substantial hardware because only one honest prover is needed.

### User Sovereignty Through Verification

The vision of browser-based or smartphone-based direct state verification represents a paradigm shift in blockchain interaction. Current reliance on infrastructure providers (Infura, Alchemy) creates centralization at the user interface layer even when the base layer is decentralized. Lightweight SNARK verification could eliminate this dependency, genuinely enabling "don't trust, verify" for end users.

### Generational Divide in Blockchain Values

The observation that pre-2021 crypto participants prioritize decentralization while post-2021 entrants prioritize throughput reflects a maturing market. Ethereum's strategy of achieving both simultaneously through SNARKs attempts to bridge this divide, potentially capturing both security-conscious institutional capital and throughput-demanding consumer applications.

### The Shallow Activity Critique

Drake's characterization of high-throughput chains producing "shallow activity" (Solana's 10M+ meme coins totaling <$10B versus single Ethereum applications exceeding this) challenges the narrative that throughput alone drives value. This suggests that fort mode (security, decentralization) is prerequisite for deep economic activity, with beast mode enabling scale once security is established.

### Post-Quantum as Existential Requirement

The emphasis on post-quantum security, including replacing KZG commitments in data availability sampling, reflects long-term thinking. While quantum computing threats remain distant, the difficulty of cryptographic transitions means planning must begin years in advance. This positions Ethereum as the only major chain with credible post-quantum roadmap.

### The Absorption Thesis

Drake's argument that Ethereum can "absorb the entirety" of blockchain innovation with adequate L1 scaling challenges the multi-chain thesis. This suggests current fragmentation reflects Ethereum's capacity constraints rather than fundamental need for multiple L1s, implying potential market consolidation as Ethereum scales.

## Data and Figures

### Current State Metrics

- **Gas limit**: 45 million gas per 12-second slot
- **Effective throughput**: 2 megagas/second
- **Simple transactions**: ~20 TPS (at 21,000 gas each)
- **Complex transactions**: ~4 TPS (at 100,000 gas each)
- **State size**: ~100+ GB
- **Validator count**: ~10,000 independent operators
- **Historical growth**: 50% increase over 4 years (30M to 45M gas limit)

### Target State Metrics

**L1 Scaling:**
- **Target throughput**: 1 gigagas/second (1,000 megagas/second)
- **Scaling factor**: 500x increase
- **Simple transactions**: ~10,000 TPS
- **Complex transactions**: ~2,000 TPS
- **Per-capita capacity**: $0.1$ transactions/human/day

**L2 Aggregate Scaling:**
- **Target throughput**: 1 teragas/second ($10^{12}$ gas/second)
- **Effective L2 multiplier**: ~1,000x relative to L1
- **Per-capita capacity**: $100$ transactions/human/day

**Hardware Requirements:**

Validators (verification):
- **Target device**: Raspberry Pi Pico ($8)
- **RAM**: ~100 kilobytes
- **CPU**: Single weak core
- **Storage**: Minimal (stateless, history-less)

Provers (execution):
- **Power consumption**: 10 kilowatts
- **Proving latency**: <12 seconds (one Ethereum slot)
- **Deployment**: On-premises (home/garage/office)
- **Honesty assumption**: 1-of-N (only one honest prover needed)

### Comparative Metrics

**Competing Chains:**
- **Solana**: ~1,000 user TPS average, <1,000 validators, majority in data centers
- **Monad**: ~100 validators (projected)
- **BNB Chain**: <100 validators

**Economic Comparisons:**
- **Solana meme coins**: 10M+ tokens, <$10B aggregate market cap
- **Tether on Ethereum**: >$100B (single stablecoin)
- **ETH market cap**: ~50x all Solana meme coins combined

**Bitcoin Security:**
- **Fee revenue**: ~0.5% of total miner revenue
- **Issuance revenue**: ~99.5% of total miner revenue
- **Daily fee security**: ~3 BTC/day

### Timeline Projections

- **DevConnect demo**: ~25 days from recording (demonstration of ZKEVM client)
- **Formal verification**: Expected completion 2029-2030
- **ZKVM maturity**: Last 1-2 years of development
- **Zcash launch**: 2016 (~9 years of production SNARK usage)

## Definitions and Terminology

**Beast Mode**: Ethereum's aggressive scaling strategy targeting 10,000 TPS on L1 and 10 million TPS across L2s through SNARK-enabled execution.

**Fort Mode**: Ethereum's defensive strategy emphasizing security, decentralization, uptime, post-quantum resistance, and fast finality.

**SNARKs (Succinct Non-interactive Arguments of Knowledge)**: Cryptographic proofs that are small (constant size) and enable verification of correct computation without re-executing it. The "zero-knowledge" property is not used for Ethereum scaling.

**ZKEVMs**: More accurately "SNARK EVMs"—implementations of the Ethereum Virtual Machine that generate SNARK proofs of correct execution. The "ZK" terminology is misleading as zero-knowledge properties aren't leveraged for scaling.

**Lean Execution**: The architectural shift from validators executing all transactions to validators verifying SNARK proofs, removing execution as a bottleneck.

**Gigagas**: $10^9$ (one billion) gas units, representing Ethereum's L1 throughput target per second.

**Teragas**: $10^{12}$ (one trillion) gas units, representing aggregate L2 throughput target per second.

**Real-time Proving**: The requirement that SNARK proofs be generated within one Ethereum slot (under 12 seconds) to avoid delaying block production.

**On-premises Proving**: Generating SNARK proofs using home-based hardware (target: 10 kilowatt power consumption) rather than data center infrastructure.

**Proposer-Builder Separation (PBS)**: The architectural pattern where randomly selected validators (proposers) delegate block construction to sophisticated builders, mediated by MEV-Boost.

**Prover**: New actor in the block production pipeline responsible for generating SNARK proofs of correct execution, potentially outsourced by builders.

**1-of-N Honesty Assumption**: Security model requiring only one honest participant among N total participants, contrasted with consensus requiring 50%+ honest participants.

**Stateless Verification**: Validating blocks without maintaining a copy of Ethereum's state, enabled by SNARK proofs that include necessary state commitments.

**Formal Verification**: Mathematical proof of software correctness, eliminating bugs through rigorous logical proof rather than testing. Ethereum has a $20M program targeting end-to-end formally verified SNARKs by 2029-2030.

**Post-Quantum Security**: Cryptographic primitives resistant to attacks by quantum computers, necessary for long-term blockchain sustainability.

**Fossil**: Protocol providing seconds-level finality for Ethereum, reducing current 10-20 minute finality times.

**Moneyness**: The property of an asset serving as money, including store of value, medium of exchange, and unit of account functions.

**Mandatory Proofs**: The target regime where blocks without valid SNARK proofs are considered invalid and excluded from the canonical chain, contrasted with optional proofs relying on altruism.

## Methodology

This document is a transcript of a podcast conversation between Justin Drake (Ethereum Foundation researcher), Ryan Sean Adams, and David Hoffman (Bankless hosts). The methodology is conversational and exploratory rather than formally structured.

**Discussion Structure:**
The conversation follows a logical progression:
1. High-level vision (Beast Mode and Fort Mode)
2. Current state and scaling targets
3. Rationale for L1 scaling
4. Trade-offs and competing approaches
5. Technical foundations (SNARKs)
6. Architectural details (Lean Execution)
7. Implementation specifics (provers, block production)

**Information Sources:**
- Drake's direct involvement in Ethereum Foundation research
- References to ongoing development work (EthProofs, formal verification program)
- Comparative analysis of competing chains (Solana, Monad, BNB Chain)
- Historical context (Zcash, Bitcoin, Ethereum's evolution)
- Upcoming demonstrations (DevConnect in ~25 days)

**Analytical Approach:**
The discussion employs:
- **First principles reasoning**: Starting from cryptographic primitives and building up
- **Comparative analysis**: Contrasting Ethereum's approach with competing chains
- **Economic reasoning**: Analyzing incentives for provers, builders, and validators
- **Historical perspective**: Tracing cryptographic evolution from Bitcoin to SNARKs
- **Quantitative targets**: Specific metrics (500x scaling, 10kW power, <12s proving)

**Limitations:**
- Conversational format may lack systematic coverage of all technical details
- Some implementation specifics are forward-looking and subject to change
- Timeline projections (e.g., 2029-2030 formal verification) are estimates
- Competitive chain metrics (validator counts, centralization) are approximate

## References and Citations

### Direct Quotations

**On Lean Ethereum's Core Vision:**
> "Lean Ethereum is the conviction that we can use this very powerful technology called SNARKs, this magical cryptography, to bring Ethereum to the next level, both in terms of performance and scale, but also in terms of security and decentralization."

**On Scaling Targets:**
> "That's 10,000 TPS on the L1, 10 million TPS on the L2s. And if you were to summarize this in one sentence, it's basically having enough throughput for all of finance."

**On the Strategic Pivot:**
> "I'd say, yes, it is a change. It is a pivot because we have now technology that allows us to scale while preserving decentralization."

**On Ethereum's Primary Application:**
> "I would agree with you that Ethereum's most important application is being money. And that's from which all of the applications derive."

**On Bitcoin's Future:**
> "I think in a few years, Bitcoin will get disqualified because of its blockchain as well. Not because it failed beast mode, but because it failed fort mode. It will not be able to secure itself with the dwindling issuance."

**On Shallow Activity:**
> "If you have beast mode without fort mode, it's very shallow activity... We have over 10 million meme coins on Solana. And the aggregate market cap of all the meme coins on Solana is less than $10 billion, which is an absolute drop in the bucket."

**On Cryptographic Evolution:**
> "Since Bitcoin, the cryptography that we've been using is extremely primitive... nowadays, looking back in 2025, this is Stone Age cryptography relative to what we have today."

**On Eliminating vs. Optimizing:**
> "The most common error of a smart engineer is to optimize a thing that should instead be eliminated." (Elon Musk quote, applied by David Hoffman)

**On Validator Requirements:**
> "We want to have a security model where even if all data center operators in the world decide to attack Ethereum simultaneously, it still has uptime."

**On the Raspberry Pi Pico Vision:**
> "The new meme that I'm hoping to introduce is that of a Raspberry Pi Pico... this $8 piece of hardware relative to the normal Raspberry Pi, which is about $100."

### Referenced Programs and Initiatives

- **$20 Million Formal Verification Program**: Led by Alex Hicks, targeting end-to-end formally verified SNARKs by 2029-2030
- **EthProofs**: Ongoing development initiative for SNARK-based Ethereum execution
- **DevConnect Demo**: Upcoming demonstration (~25 days from recording) of ZKEVM client replacing Geth
- **MEV-Boost**: Existing middleware facilitating proposer-builder separation
- **Fossil Protocol**: Fast finality mechanism reducing finality time to seconds

### Technical References

- **Zcash**: First production deployment of SNARKs (2016), experienced critical bug allowing arbitrary token minting
- **KZG Commitments**: Current data availability cryptography, not post-quantum secure
- **ZKEVM Implementations**: Reth, Geth, Nethermind, Erigon, ZKsync OS (various languages: Rust, Go, C#)
- **Consensus Clients**: Lighthouse (mentioned as Drake's home setup)
- **Execution Clients**: Geth (mentioned as Drake's current execution client)

### Comparative Chain Data

- **Solana**: ~1,000 user TPS average, <1,000 validators, 10+ outages over several years, many validators in two European data centers
- **Monad**: ~100 validators (projected)
- **BNB Chain**: <100 validators
- **Bitcoin**: ~0.5% of miner revenue from fees, 99.5% from issuance, ~3 BTC/day in fee security

### Episode Metadata

- **Published**: 2025-11-12 (Note: This appears to be a future date, likely a transcription error; should be 2024-11-12)
- **Show**: Bankless
- **Participants**: Justin Drake (Ethereum Foundation), Ryan Sean Adams, David Hoffman
- **Duration**: Approximately 1 hour 44 minutes (based on timestamp range)