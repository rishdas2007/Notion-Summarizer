# Why Kraken Is Betting Big on Onchain Vaults | John Zettler & Sun Raghupathi

**Citation:** "Why Kraken Is Betting Big on Onchain Vaults | John Zettler & Sun Raghupathi." *Empire*, 26 Jan. 2026,


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [What Are Vaults?](#what-are-vaults)
   - [The Evolution of Vault Infrastructure](#the-evolution-of-vault-infrastructure)
   - [Vault Ecosystem Architecture](#vault-ecosystem-architecture)
   - [Business Models and Revenue Distribution](#business-models-and-revenue-distribution)
   - [DeFi as Backend Infrastructure](#defi-as-backend-infrastructure)
   - [Kraken's Vault Strategy](#krakens-vault-strategy)
   - [Risk Management Framework](#risk-management-framework)
   - [Competitive Dynamics and Market Forces](#competitive-dynamics-and-market-forces)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [References and Citations](#references-and-citations)

## Executive Summary

This podcast episode features John Zettler (Director of Product at Kraken) and Sun Raghupathi (Co-founder of Veda) discussing the emergence of on-chain vaults as a transformative force in decentralized finance (DeFi). The central thesis is that 2026 will be "the year of the vault," with predictions that vault total value locked (TVL) will grow from $6 billion to at least $15 billion, potentially exceeding $50 billion.

**Core Arguments:**

1. **Vaults as DeFi Aggregation Layer**: Vaults package complex DeFi lending and yield strategies into simple, user-friendly products that abstract away the technical complexity of interacting with multiple protocols across different blockchains.

2. **DeFi as Backend Infrastructure**: The future of DeFi lies not in competing directly with traditional fintech companies for users, but in serving as backend infrastructure that powers yield products for established platforms like Kraken, Coinbase, and potentially traditional financial institutions.

3. **Multi-Protocol Superiority**: Vaults that can allocate capital across multiple protocols and chains (like Veda's platform) offer sustainable competitive advantages over single-protocol solutions (like Morpho vaults) by accessing diverse yield opportunities and reducing concentration risk.

4. **Institutional Adoption Catalyst**: The convergence of embedded wallet technology, declining traditional interest rates, and regulatory clarity is creating ideal conditions for mainstream fintech adoption of DeFi yield products.

**Key Outcome**: Kraken launched three vaults on January 27, 2026, using Veda's infrastructure with risk management from Chaos Labs and Centora, offering yields ranging from approximately 2% to 6.5% on stablecoins through non-custodial embedded wallets powered by Privy.

## Detailed Analysis

### What Are Vaults?

Sun Raghupathi provides the foundational definition: **"Vaults are a layer on top of [DeFi primitives] that allows institutions, fintechs, exchanges, anyone with users or capital that wants to offer financial products to their customers to package up the best of DeFi, layer on whatever compliance, whatever risk controls, offer whatever risk return profile they want as a yield product."**

The core problem vaults solve is the inherent user-unfriendliness of primitive DeFi protocols. While DeFi offers powerful financial primitives—lending protocols that match lenders with borrowers, decentralized exchanges (DEXs) that connect traders with liquidity providers—these protocols lack:

- User-friendly interfaces
- Risk controls suitable for institutional deployment
- Compliance frameworks
- Product customization capabilities
- Aggregation across multiple opportunities

John Zettler conceptualizes the DeFi ecosystem as a pyramid structure:

1. **Base Layer**: Liquidity in automated market makers (AMMs) like Uniswap and Curve
2. **Middle Layer**: Borrow-lend protocols (Aave, Compound, Morpho) that rely on the liquidity layer for liquidations
3. **Top Layer**: Vaults that aggregate opportunities across borrow-lend protocols to optimize yield

**Yield Origins**: The yield in vaults ultimately derives from on-chain borrowers who want to leverage their positions. The typical use case involves users posting crypto collateral (e.g., ETH, BTC) to borrow stablecoins (primarily USDC), which they then use to purchase more crypto, creating leveraged long positions. This borrowing demand generates the interest rates that vault depositors earn.

### The Evolution of Vault Infrastructure

The discussion traces three distinct generations of vault technology:

**Generation 1: Aave (Pooled Model)**

Aave pioneered decentralized lending at scale using a pooled model where:
- All supplied assets go into a single global pool
- Multiple collateral types can be deposited
- Borrowers can access any supply token against any accepted collateral
- The Aave DAO sets risk parameters (collateral types, borrow caps, liquidation thresholds)
- No vaults are necessary because there's no choice to make—it's one-size-fits-all

**Generation 2: Morpho (Isolated Markets + Protocol-Specific Vaults)**

Morpho introduced modular lending with isolated markets:
- Each market pairs one collateral type with one loan token (e.g., BTC-USDC, ETH-USDT)
- Markets are siloed without shared liquidity
- Vaults became necessary to aggregate across these fragmented markets
- Morpho vaults allow curators to package multiple isolated markets into unified yield products
- **Limitation**: Morpho vaults can only allocate to Morpho markets, not to other protocols

**Generation 3: Veda (Multi-Protocol, Multi-Chain Vaults)**

Sun Raghupathi articulates Veda's design philosophy: **"The goal is that you should be able to aggregate any form of DeFi, whether it's Morpho, whether it's Aave, whether it's Pendle, it's RWAs, right, packaging up all these things into a single product with the most flexibility possible is the ultimate evolution of vaults."**

Key advantages of the multi-protocol approach:

- **Yield Sustainability**: When yields decline in one protocol due to reduced borrowing demand, capital can flow to higher-yielding opportunities elsewhere
- **Risk Diversification**: Exposure is spread across multiple protocols, reducing the impact of any single protocol failure
- **Institutional Requirements**: Large institutions demand flexibility and don't want vendor lock-in to any single chain or protocol

John Zettler emphasizes this point from Kraken's perspective: **"Multi-protocol, multi-chain, allowing, you know, that simplicity and aggregation in the most, the highest form"** is what will ultimately win institutional adoption.

### Vault Ecosystem Architecture

The vault ecosystem involves three distinct specialized roles:

**1. Infrastructure Providers (e.g., Veda)**

- Build and maintain the vault smart contracts
- Handle technical operations (daily NAV calculations, rebalancing mechanisms)
- Ensure security through audits and battle-testing
- Provide multi-chain, multi-protocol connectivity
- Operate as a SaaS-style business model

**2. Risk Managers/Curators (e.g., Chaos Labs, Centora, Gauntlet, Steakhouse)**

- Design allocation strategies across protocols
- Set risk parameters and exposure limits
- Monitor market conditions and adjust positions
- Identify temporary incentive programs and yield opportunities
- May employ advanced strategies like looping (recursive borrowing/lending)

Key players mentioned:
- **Chaos Labs**: Known for risk management of Aave DAO, institutional-grade expertise
- **Centora**: Institutional-focused, experienced with Veda infrastructure
- **Gauntlet**: Established risk manager, has developed its own vault infrastructure
- **Steakhouse**: Worked with Coinbase on their Morpho vault integration

**3. Distribution Partners (e.g., Kraken, Coinbase, potentially Robinhood, Klarna)**

- Own the end-user relationships
- Provide the user interface and customer experience
- Handle customer support and compliance
- Typically capture the largest share of fees due to owning distribution

Sun Raghupathi notes an emerging trend: **"The largest asset managers in the world already today are becoming interested in diversifying their offerings through these on-chain products."** Traditional asset managers like BlackRock are exploring vault curation, though they face challenges competing with crypto-native firms on technical expertise.

**Vertical Integration Attempts**: Several players are attempting to vertically integrate:
- Gauntlet has launched its own vault infrastructure (though adoption appears limited)
- Aave V4 will include vault functionality
- Hyperliquid has proprietary vaults

Sun's perspective on these efforts: **"Building a successful vault platform is very different than these other things... There's really economies of scale with doubling down on vault infrastructure because it's so complicated."** He predicts that specialized infrastructure providers will outcompete vertically integrated solutions.

### Business Models and Revenue Distribution

The revenue model for vaults typically involves performance fees split among ecosystem participants. For Kraken's launch:

- **Total Performance Fee**: 25% of yield generated
- **Fee Distribution**:
  - **Largest share**: Kraken (distribution partner bringing users and volume)
  - **Infrastructure provider**: Veda (for vault technology and operations)
  - **Risk manager**: Chaos Labs or Centora (for strategy and curation)

The fee flows into a smart contract fee splitter that automatically distributes revenue to the appropriate parties.

Sun Raghupathi explains Veda's business philosophy: **"Our goal is to serve thousands, tens of thousands, hundreds of thousands of vaults, right? And who's going to take the lion's share of the fees that are actually generated in these products? It's going to be the distribution... But our goal is to be, you know, is to serve everyone, right? And so you kind of have this dynamic where the distribution partner always takes a lion's share... The curator comes in and they're kind of competing based on their ability to outperform... and our goal, we operate more like a SaaS company."**

**Token Incentives as Competitive Tool**: A significant behind-the-scenes dynamic involves token incentives. John Zettler notes: **"The borrow lend protocols will go to the risk managers and the curators and be like, well, come deploy with us and we'll incentivize it with our own token."**

Sun observes a shift in how token incentives are used: **"People used to pay for liquidity, that was what token incentives were for. Now token incentives are for paying for distribution, right? It's a very different model."**

Veda, notably, does not have a token, which Sun frames as a competitive advantage: **"VEDA doesn't have a token. That's why we don't have a massive war chest that we can use to throw money around... my view is truly... the best product will win over the long term."**

### DeFi as Backend Infrastructure

A central theme of the discussion is the repositioning of DeFi from consumer-facing applications to backend infrastructure—what the participants call "the DeFi mullet: fintech in the front, DeFi in the back."

**Why DeFi Failed as Direct-to-Consumer**: Sun Raghupathi articulates a crucial realization: **"There was a pipe dream that we would invent this entire independent financial system and just migrate everyone over, like everyone's gonna leave the banks, leave their exchanges and fintechs and move on chain. But that was always a pipe dream, right?"**

The historical user experience problems with DeFi included:
- Difficulty tracking assets across multiple protocols
- Poor wallet experiences (MetaMask, Ledger connectivity issues)
- Fragmented interfaces requiring visits to multiple websites
- Complex gas fee management
- Self-custody burden

**The Backend Model Advantages**:

John Zettler describes the new paradigm: **"Once you have that packaging, that aggregation layer of vaults, and then you have it plugged into a traditional, easy-to-use fintech with a slick native app, you're bringing it right to the user's fingertips without them having to think about much."**

For Kraken's implementation:
- **Embedded Wallets**: Partnership with Privy (acquired by Stripe) provides non-custodial wallets embedded in user accounts
- **User Control**: Each Kraken user has a unique embedded wallet that Kraken cannot access or control
- **Authentication**: One-time passcode (OTP) sent to email for transaction authorization
- **User Experience**: Single-click access to diversified DeFi yield across multiple protocols and chains

Sun emphasizes the complementary nature: **"This is not just beneficial to DeFi and complementary. This is actually the only way that DeFi succeeds."** The backend model brings DeFi's core value propositions—transparency, non-custodial control, competitive yields—to mainstream users through familiar interfaces.

**Value Proposition**: Sun summarizes what users gain: **"You have Kraken users, millions of users on this exchange who with a single button are earning yield on Inc, Ethereum across multiple protocols. They can see their assets at all times, right? It's all on chain. They can get those assets out whenever they want, right? They're getting the best, most competitive yields that exist. That is an amazing product experience."**

### Kraken's Vault Strategy

John Zettler's background provides context for Kraken's approach. He spent five years at Coinbase, where he helped build their staking and DeFi products, including the Coinbase-Morpho vault integration.

**Coinbase Model (First-Party Integration)**:
- Vault provided by Steakhouse
- Built on Morpho (Coinbase Ventures portfolio company)
- Deployed on Base (Coinbase's L2)
- Using USDC (co-owned by Coinbase and Circle)
- Vertically integrated "Apple model" approach
- Free gas for users through server signers
- Peak TVL: ~$475 million on lending side; ~$1.9 billion collateral with ~$1 billion loans on borrow side

Lessons from Coinbase: **"Coinbase wanted to be the most trusted and easiest to use... those are our two differentiators... you always want to hammer and hammer on the user experience, always try to make it easier to use and improve upon it."**

**Kraken Model (Best-of-Breed Integration)**:

John contrasts Kraken's approach: **"The thing I love about Kraken is that we have an opportunity to use providers like Veda, where it's not all just first party products and services, but we can really source the actual best in the industry."**

Strategic advantages:
- **Better Yields**: Multi-protocol access provides "substantially better" yields than single-protocol solutions
- **Sustainability**: Diversification across protocols and chains ensures yields remain competitive long-term
- **Flexibility**: Can add new protocols and strategies without rebuilding infrastructure

**The Arjun Effect**: Jason Yanowitz observes that Kraken's product quality has improved markedly over 18 months, which John attributes to CEO Arjun Sethi's leadership.

John describes Arjun's management philosophy: **"Every leader is very different... one of Arjun's superpowers is that like... you can always move faster, we can always be better, we can always be leaner and we can always be hungrier... it's this constant drive to move faster and to do more with less... it's that feeling you get when you're in a smaller stage startup that's really working, that's in product market fit mode."**

Cultural changes under Arjun:
- No process for process's sake
- No lengthy quarterly planning cycles
- Single OKR: revenue target for the year
- Resource allocation: "Tell me what you need... and mountains can move around you"
- Hiring crypto-native talent with deep DeFi expertise

**Product Approval Process**: The vault product was already in early development when John joined, but lacked clarity on structure and implementation. Sun recalls: **"I remember actually the day that John joined Kraken... we'd been chatting, we'd been working with the Inc team... But I remember John joined and shit just started moving."**

**Launch Details** (as of January 27, 2026):
- Three vaults with yields ranging from ~2% to ~6.5%
- Risk management by Chaos Labs and Centora
- Infrastructure by Veda
- Embedded wallets by Privy
- 25% performance fee split among partners

**Future Vision**: John teases: **"It's just the first of many. There's a whole suite of on-chain DeFi-oriented products coming our way."** He invites risk managers to reach out: **"Anyone who's out there listening to this pod... who has any differentiated strategy they want to pioneer or bring... Come talk to us."**

Selection criteria for new curators:
- Experience doing curation at scale
- Strong security model
- Familiarity with vault infrastructure
- Track record (not just two weeks)
- Explanation of strategy sustainability
- Innovation in identifying new protocols and incentive programs

### Risk Management Framework

The participants identify three primary risk categories for vault products:

**1. Smart Contract / Cyber Security Risk**

John Zettler: **"Could the protocols, could the Aaves, could the Morphos, could they be jeopardized and there could be some critical bug?"** 

Assessment: Given how battle-tested and "Lindy" major protocols like Aave and Morpho have become, this risk is considered relatively low but never zero. Vault infrastructure itself also carries smart contract risk.

Sun Raghupathi notes a recent incident: **"There's a vault exploit this past week from some curve pool that had some pricing issues."** He emphasizes the trade-off: **"There is to some extent a trade-off between how expressive these vaults are and the surface area for where things can go wrong."**

Veda's approach to mitigating this risk: **"It's super important to be battle-tested. It's why we sprinted to get to multi-billion dollar scale and stay that way and prove that our infrastructure is secure because you can't put a price on that."**

**2. Liquidity Risk**

John defines this as: **"Can I get my money back when I want it?"**

Different vaults handle liquidity differently:
- Some allow immediate withdrawals only if liquidity is available in the vault
- Others implement queue systems (e.g., one-day wait time for guaranteed withdrawal)
- Withdrawal windows vary by vault design

**3. Bad Debt Risk**

John identifies this as "probably the most DeFi native" risk and "the real risk" differentiating vaults from traditional products like T-bills.

Mechanism: **"If the hundred bucks that they put down, which is in the form of Bitcoin or something, drops precipitously and faster than the solvers can go out and fill the loan... then you could be in a situation where there ends up with what's called bad debt, where the collateral has sunk so fast that it is now lower than the total amount of loans that are outstanding."**

Different protocols handle bad debt differently:
- **Aave**: "Umbrella insurance" or "umbrella policy" where users can earn yield for serving as a backstop
- **MakerDAO**: MKR token serves as the backstop, getting diluted to cover bad debt
- Each protocol has evolved unique mechanisms

**Diversification Paradox**: Sun notes: **"More diversifying in some sense is not always good, right? If you diversify over garbage, you're in a worse position than if you put all your assets in one secure protocol."** Quality of protocols matters more than quantity.

**Contagion Risk**: Sun describes a recent incident with Stream Finance: **"There was a set of Morpho markets that users just couldn't withdraw from. They incurred bad debt. What ended up happening was that fear spread to all the Morpho markets. And for a period of like... 15 minutes or something... even healthy markets and healthy vaults had liquidity and withdrawal issues."**

This illustrates how fear and FUD can create systemic issues beyond direct economic exposure, reinforcing the value of multi-protocol diversification.

### Competitive Dynamics and Market Forces

**DeFi Vaults vs. CeFi Lending (BlockFi, Celsius)**

Jason raises the critical question about how vaults differ from failed centralized lending platforms. Sun's response highlights the fundamental distinction:

**"The difference is when you gave your money to BlockFi, you had no idea where it was going, right? You had no real claim over those assets. They could do whatever the hell they wanted with it. And they did. They did crazy shit with those assets."**

In contrast, with DeFi vaults:
- **Transparency**: "You know where your assets are at all times, it's all on chain"
- **Verifiable Claims**: "You can see your claim to the set of assets that are in that vault"
- **Non-Custodial**: "Only you can redeem your assets from that vault"
- **Public Auditability**: "It's all public, everyone can see it"

John adds historical context: **"Remember when all of that happened... in 2022... all of DeFi went unscathed. Because it just functioned and operated as it was supposed to. These were over collateralized loans. The collateral was there. The risks were managed."**

**Traditional Finance Entry**

A pivotal moment in Jason's conviction about vaults came at a holiday party: **"One of the largest asset managers in the world was there and they said... to someone else who was at one of the largest [asset manager servicers]... 'Have you heard of these vaults?' The guy says, 'Vaults? We're all over vaults.' They know Steakhouse, they know Gauntlet, they know Morpho... they were deep... they both of them in different ways said they're coming into the vaults business."**

This observation led Jason to predict that traditional asset managers will enter the space in 2026, though their competitive position differs from crypto-native firms:

**Distribution Model Differences**:
- **Crypto Fintechs** (Kraken, Robinhood): Direct user access, one-click deployment
- **Traditional Asset Managers** (BlackRock): Must sell through intermediaries (Charles Schwab, TD Ameritrade, financial advisors)

Sun's perspective: **"They will [succeed] because they have the customers, right?... They have customer relationships, they have assets that they can funnel into their products... If BlackRock comes on chain and says, we want to bring a hundred billion dollars on chain, they can do it."**

However, crypto-native curators maintain advantages in technical expertise. John questions: **"Would a Tarun [founder of Gauntlet] ever go work for a BlackRock? Like, I don't think so... that level of crypto forward individual... would want to go work in one of those big institutions."**

Yet Jason counters with an anecdote about a traditional hedge fund portfolio manager: **"I was like, oh, are you into crypto? He's like, you wouldn't believe the looping that I'm doing... I've got, you know, lever to the nines on Superstate... I'm looping USCC like seven times right now."**

This leads to the conclusion: **"Crypto and traditional capital markets will eventually converge... We'll just call them capital markets one day."**

**Morpho vs. Veda Competition**

The competitive dynamic between Morpho's vault layer and Veda's infrastructure reveals different business models:

**Morpho's Model**:
- Vaults serve as an instrument to drive capital into Morpho's lending protocol
- Permissionless vault creation
- Vaults can only allocate to Morpho markets
- Vault layer appears to be non-monetized (focused on protocol revenue)

**Veda's Model**:
- Vaults as a standalone monetized product
- Curated, managed approach with selected risk managers
- Multi-protocol allocation (including to Morpho)
- Can create "meta-vaults" that allocate to multiple Morpho curators

Sun's competitive assessment: **"Vaults are always secondary [to] protocols, right? They're only as good as they need to be. They're not as good as they should be."** By focusing exclusively on vault infrastructure, Veda can invest more heavily in building superior technology.

Interestingly, Veda vaults can allocate to Morpho vaults, creating a layered structure: **"Let's say you want to allocate to two different Morpho curators, right? How do you do that? Well, that's available... it's the beauty of Veda."**

**Token Incentive Wars**

Behind the scenes, protocols compete for vault allocations through token incentives. Sun notes: **"A lot of projects, token projects have large amounts of their token supply earmarked for these kinds of deals."**

The competitive tactics include:
- Protocols offering tokens to risk managers who deploy capital to their markets
- Infrastructure providers offering equity stakes for major partnerships
- Distribution partners (exchanges, fintechs) being courted with various incentive structures

Sun describes the intensity: **"I've seen people offer insane amounts of equity for a single deal with zero guaranteed revenue ever. And it's very common. And honestly, it might be worth it... because this is ultimately about trust... These large institutions, they want someone who is de-risking. They want someone who's done it before."**

## Key Insights and Implications

### 1. DeFi's Existential Pivot

The most significant insight is that DeFi's path to success requires abandoning the original vision of replacing traditional finance with a parallel decentralized system. Sun's frank assessment—**"There was a pipe dream that we would invent this entire independent financial system and just migrate everyone over... But that was always a pipe dream"**—represents a fundamental recalibration of DeFi's role.

**Implication**: DeFi protocols should optimize for institutional integration rather than direct consumer acquisition. Success metrics shift from user counts to TVL from institutional partners and API integration quality.

### 2. The Distribution Moat

The discussion reveals that distribution—not technology—captures the majority of economic value in the vault ecosystem. Kraken takes the "lion's share" of the 25% performance fee despite Veda building the infrastructure and risk managers designing the strategies.

**Implication**: Pure technology plays in crypto face structural disadvantages in value capture. The most defensible positions are either owning distribution (exchanges, fintechs) or achieving such technical superiority and scale that switching costs become prohibitive (Veda's strategy).

### 3. Multi-Protocol as Sustainable Competitive Advantage

Both John and Sun emphasize that single-protocol vaults face an inherent sustainability problem. When borrowing demand decreases in one protocol, yields compress, TVL leaves, creating a negative feedback loop.

John's prediction: **"There's other products out there that have... already started to see some of those decreases in their TVL because the yields are now falling to like... three and a half or sub three percent."**

**Implication**: Vault providers locked into single protocols (like Morpho-only vaults) will face increasing pressure to expand or risk becoming commoditized. The market will likely consolidate around multi-protocol infrastructure providers.

### 4. The Embedded Wallet Unlock

The technical maturity of embedded wallet solutions (particularly Privy's acquisition by Stripe) represents a critical infrastructure milestone that enables mainstream vault adoption.

**Implication**: The combination of embedded wallets + vault infrastructure + established fintech distribution creates a complete stack for DeFi-powered products. This stack is now mature enough for rapid scaling, supporting the bullish TVL predictions.

### 5. Regulatory Arbitrage Through Non-Custody

The non-custodial nature of vault products provides a potential regulatory advantage. As John emphasizes: **"We Kraken can't touch it. We can't move the funds. We can't influence it. We can't do anything about it."**

**Implication**: This structure may allow exchanges and fintechs to offer yield products without triggering securities regulations or custody requirements that applied to BlockFi and Celsius. However, this remains legally untested at scale.

### 6. The Borrowing Demand Question

John raises a critical concern: **"Will there be enough borrowed demand on the other side that the yields continue to stay high and competitive?"** If massive TVL inflows from fintechs aren't matched by borrowing demand, yields will compress.

His hypothesis: **"When that happens it just kind of spurs the market... more borrow products that are built on DeFi... if borrowing starts becoming very cheap in DeFi, what are all the new use cases that will come from that?"**

**Implication**: The vault boom may catalyze innovation in DeFi borrowing products. Cheap, accessible leverage could enable new use cases beyond simple leveraged long positions, potentially including working capital loans, consumer credit, or structured products.

### 7. User Base Transformation

Sun observes: **"The user base historically in DeFi has been like a thousand people. Like realistically, you look at the capital. It's like, you know, Justin Sun and a couple other people."**

The shift to millions of retail users through fintech platforms fundamentally changes market dynamics.

**Implication**: DeFi markets will become less volatile and more stable as capital becomes diversified. This enables more sophisticated financial products that require predictable liquidity. The "Justin Sun risk" (concentration in a few large holders) diminishes.

### 8. Traditional Finance Convergence Timeline

The anecdote about traditional asset managers discussing vaults at a holiday party signals that institutional adoption is further along than publicly visible. These institutions are already deep in due diligence on Morpho, Gauntlet, Steakhouse, and vault infrastructure.

**Implication**: 2026 may see announcements from major traditional asset managers entering the vault curation space. The "caliber of companies" offering vault products will increase dramatically, even if absolute TVL growth is harder to predict.

### 9. The Specialization Imperative

The failure of vertical integration attempts (Gauntlet's vault infrastructure, protocol-specific vaults) suggests that specialization wins in the vault ecosystem.

Sun's observation: **"Building a successful vault platform is very different than these other things... There's really economies of scale with doubling down on vault infrastructure because it's so complicated."**

**Implication**: The vault ecosystem will likely maintain distinct layers (infrastructure, curation, distribution) rather than consolidating into vertically integrated players. This creates opportunities for specialized providers in each layer.

### 10. Risk Management as Emerging Profession

The discussion reveals risk management/curation as a rapidly growing professional category. The skills required—deep DeFi protocol knowledge, real-time market monitoring, strategy design—represent a new type of financial expertise.

**Implication**: Expect significant hiring and team-building in this category. Traditional finance risk managers will need to acquire crypto-native skills, while DeFi natives will need to develop institutional risk management frameworks. Educational programs and certifications may emerge.

## Data and Figures

### TVL Metrics and Projections

- **Current Vault TVL**: Approximately $6 billion (as of early 2026)
- **Jason's Prediction**: Growth to $15 billion by end of 2026
- **John's Prediction**: "I'll take the over" on $15 billion
- **Sun's Prediction**: Expects "a fatter second half of the year" with growth accelerating

- **Veda Peak TVL**: $6 billion (during Plume Network height)
- **Veda Current TVL**: Approximately $2 billion
- **Coinbase DeFi Borrow**: $1.9 billion in collateral, ~$1 billion in loans issued
- **Coinbase DeFi Lend**: Peak of ~$475 million TVL (declined as yields compressed)

### Yield Ranges

- **Kraken Vault Yields** (at launch): Ranging from approximately 2% to 6.5% APY
- **Competitive Yields**: Some single-protocol vaults have declined to 3.5% or below
- **Historical Context**: During DeFi Summer 2020, yields were significantly higher (specific numbers not provided)

### Fee Structures

- **Performance Fee**: 25% of yield generated
- **Fee Distribution**: 
  - Largest share: Distribution partner (Kraken)
  - Smaller shares: Infrastructure provider (Veda) and Risk manager (Chaos Labs/Centora)
  - Exact percentages not disclosed

### Collateralization Ratios

- **Typical Over-Collateralization**: Users post $100 in collateral to borrow $50 (2:1 ratio mentioned as example)
- **Liquidation Threshold**: Varies by protocol and collateral type (specific numbers not provided)

### Market Concentration

- **Historical DeFi User Base**: Sun estimates "like a thousand people" held the majority of capital
- **Justin Sun's Position**: "I think he had like a billion dollars in one of our vaults at one point"
- **Future User Base**: Projected to reach "millions of users" through fintech integrations

### Funding

- **Veda Series A**: $18 million raised, led by Coinfund (timing: early-mid 2025)

## Definitions and Terminology

**Vault**: A smart contract-based product that aggregates DeFi yield opportunities across multiple protocols and chains, packaging them into simplified investment products with defined risk parameters and liquidity terms.

**DeFi (Decentralized Finance)**: As defined by Sun: "A set of financial primitives that allow peer-to-peer coordination" through programmable, public, on-chain protocols.

**Borrow-Lend Protocol**: DeFi protocols (e.g., Aave, Compound, Morpho) that match lenders (who supply capital to earn yield) with borrowers (who post collateral to access liquidity).

**Over-Collateralized Lending**: Lending model where borrowers must post collateral worth more than the loan amount (e.g., $100 collateral for $50 loan) to protect lenders from default risk.

**Liquidation**: The automated process of selling a borrower's collateral when its value falls below a threshold, ensuring loans remain over-collateralized.

**TVL (Total Value Locked)**: The total dollar value of assets deposited in a DeFi protocol or vault.

**APY (Annual Percentage Yield)**: The annualized rate of return on deposited assets, including compound interest effects.

**Risk Manager/Curator**: Entities that design vault allocation strategies, set risk parameters, and actively manage capital deployment across DeFi protocols.

**Infrastructure Provider**: Companies like Veda that build and maintain the technical vault infrastructure (smart contracts, NAV calculations, rebalancing mechanisms).

**Distribution Partner**: Platforms like Kraken or Coinbase that own end-user relationships and provide the interface through which users access vault products.

**Embedded Wallet**: A non-custodial cryptocurrency wallet integrated directly into an application (like Kraken's app) that users control but don't need to separately manage.

**Looping**: A strategy where users recursively borrow and re-deposit assets to amplify exposure and yield (e.g., deposit ETH, borrow USDC, buy more ETH, repeat).

**Bad Debt**: Occurs when a borrower's collateral value falls below their loan amount before liquidation can occur, leaving the protocol with uncollateralized loans.

**Isolated Markets**: Morpho's model where each market pairs one specific collateral type with one loan token, without shared liquidity across markets.

**Pooled Model**: Aave's model where all assets are deposited into a single shared pool that any borrower can access against any accepted collateral.

**LST (Liquid Staking Token)**: Tokens representing staked assets (e.g., stETH for staked Ethereum) that can be used as collateral while still earning staking rewards.

**LRT (Liquid Restaking Token)**: Tokens representing restaked assets in protocols like EigenLayer, providing additional yield layers.

**NAV (Net Asset Value)**: The per-share value of a vault, calculated by dividing total vault assets by total shares outstanding.

**Lindy Effect**: The concept that the longer something has survived, the longer it's likely to continue surviving; used here to describe battle-tested protocols.

**DeFi Mullet**: The architectural pattern of "fintech in the front, DeFi in the back"—traditional user interfaces powered by DeFi infrastructure.

**RWA (Real World Assets)**: Traditional financial assets (bonds, real estate, commodities) tokenized and brought on-chain.

**Solver**: Entities that execute liquidations by purchasing under-collateralized positions and selling the collateral to repay loans.

## References and Citations

### Key Quotations

**On Vault Definition**:
> "Vaults are a layer on top of [DeFi primitives] that allows institutions, fintechs, exchanges, anyone with users or capital that wants to offer financial products to their customers to package up the best of DeFi, layer on whatever compliance, whatever risk controls, offer whatever risk return profile they want as a yield product." — Sun Raghupathi

**On DeFi's Evolution**:
> "There was a pipe dream that we would invent this entire independent financial system and just migrate everyone over, like everyone's gonna leave the banks, leave their exchanges and fintechs and move on chain. But that was always a pipe dream, right?" — Sun Raghupathi

**On Multi-Protocol Advantage**:
> "The thing I love about Kraken is that we have an opportunity to use providers like Veda, where it's not all just first party products and services, but we can really source the actual best in the industry." — John Zettler

**On DeFi as Backend**:
> "This is not just beneficial to DeFi and complementary. This is actually the only way that DeFi succeeds." — Sun Raghupathi

**On Vaults vs. CeFi**:
> "The difference is when you gave your money to BlockFi, you had no idea where it was going, right? You had no real claim over those assets. They could do whatever the hell they wanted with it. And they did. They did crazy shit with those assets." — Sun Raghupathi

**On Arjun's Leadership**:
> "One of Arjun's superpowers is that... you can always move faster, we can always be better, we can always be leaner and we can always be hungrier... it's this constant drive to move faster and to do more with less." — John Zettler

**On Traditional Finance Entry**:
> "The largest asset managers in the world already today are becoming interested in diversifying their offerings through these on-chain products." — Sun Raghupathi

**On Token Incentives**:
> "People used to pay for liquidity, that was what token incentives were for. Now token incentives are for paying for distribution, right? It's a very different model." — Sun Raghupathi

**On Risk Management**:
> "Building a successful vault platform is very different than these other things... There's really economies of scale with doubling down on vault infrastructure because it's so complicated." — Sun Raghupathi

**On Future Vision**:
> "2026 is going to be the year of the vault." — Sun Raghupathi

### Referenced Companies and Protocols

**DeFi Protocols**: Aave, Compound, Morpho, Yearn Finance, Synthetix, Curve, Uniswap, Pendle, Euler, Hyperliquid, MakerDAO

**Vault Infrastructure**: Veda, Morpho Vaults, Gauntlet (vault product)

**Risk Managers/Curators**: Chaos Labs, Centora, Gauntlet, Steakhouse

**Exchanges/Fintechs**: Kraken, Coinbase, Robinhood, Klarna, Revolut, Neobank

**Infrastructure Providers**: Privy (embedded wallets, acquired by Stripe), Zapper, Zerion

**Blockchain Networks**: Base (Coinbase L2), Inc (Kraken-associated), Ethereum, Plume Network

**Stablecoins**: USDC, USDT, DAI, USCC (Superstate)

**Traditional Finance**: BlackRock, Charles Schwab, TD Ameritrade

### Podcast Details

- **Show**: Empire
- **Published**: January 26, 2026
- **Guests**: John Zettler (Director of Product, Kraken), Sun Raghupathi (Co-founder, Veda)
- **Host**: Jason Yanowitz
- **Product Launch**: Kraken vaults went live January 27, 2026 (day after podcast release)

### Social Media References

- John Zettler: @JohnZettler
- Sun Raghupathi: @sunandr_
- Jason Yanowitz: @JasonYanowitz
- Empire Podcast: @theempirepod

### Related Content

- 2026 Predictions Episode referenced (featuring Santiago and Rob)
- Arjun Sethi (Kraken CEO) previous Empire podcast appearance mentioned