# The $300 Trillion Dollar Whoopsie Ft. Morgan Krupetsky & Raagulan Pathy

**Citation:** "The $300 Trillion Dollar Whoopsie Ft. Morgan Krupetsky & Raagulan Pathy." *Tokenized*, 20 Oct. 2025, <https://tokenized.simplecast.com/episodes/the-300-trillion-dollar-whoopsie-ft-morgan-krupetsky-raagulan-pathy-jIQrStOh>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [The Crypto Flash Crash Event](#the-crypto-flash-crash-event)
   - [Market Structure and Synthetic Stablecoin Mechanics](#market-structure-and-synthetic-stablecoin-mechanics)
   - [Institutional Perspectives on Market Maturity](#institutional-perspectives-on-market-maturity)
   - [M&A Activity: BVNK Acquisition Dynamics](#ma-activity-bvnk-acquisition-dynamics)
   - [Corporate Treasury and Stablecoin Adoption](#corporate-treasury-and-stablecoin-adoption)
   - [Bank-Issued Stablecoins and Tokenized Deposits](#bank-issued-stablecoins-and-tokenized-deposits)
   - [The PayPal PYUSD Minting Error](#the-paypal-pyusd-minting-error)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [References and Citations](#references-and-citations)

## Executive Summary

This episode of the Tokenized podcast, published October 20, 2025, features Simon Taylor (GTM at Tempo), Morgan Krupetsky (VP of Business Development for Onchain Finance at Ava Labs), and Raagulan Pathy (Founder & CEO at KAST) discussing critical developments in cryptocurrency markets and stablecoin infrastructure. The conversation centers on three major themes: the recent crypto flash crash and its implications for market structure, the growing institutional adoption of stablecoins for corporate treasury management, and the challenges facing bank-issued stablecoins versus existing solutions.

The flash crash, triggered by geopolitical tensions and exacerbated by thin weekend liquidity, represented the largest liquidation event in crypto market history. Despite initial concerns about Ethena's USDE synthetic dollar de-pegging, the panelists clarify that the issue stemmed from oracle feed problems rather than actual collateral impairment. The discussion reveals both the fragility of current crypto market infrastructure and its remarkable resilience—with recovery occurring within hours rather than the days or weeks typical of traditional finance crises.

The episode also examines significant M&A activity, particularly the potential $2 billion acquisition of stablecoin infrastructure provider BVNK by either Coinbase or Mastercard, and explores why major banks are announcing G7 currency stablecoin initiatives despite skepticism about their viability. Throughout, the panelists emphasize the growing importance of B2B payments and corporate treasury management as the primary growth driver for stablecoins, surpassing consumer-focused use cases.

## Detailed Analysis

### The Crypto Flash Crash Event

The flash crash occurred on a Friday following a late-evening tweet from President Trump threatening 100% tariffs on Chinese imports and export controls on critical software. The timing proved catastrophic: U.S. markets were closing, global markets were already closed for the weekend, and liquidity was naturally thin during this period.

**Cascade of Events:**

Morgan Krupetsky provides a detailed breakdown of the "perfect storm" that unfolded in under 30 minutes:

1. **Initial Price Collapse**: Altcoins fell 60-80% in near-vertical drops as market makers pulled support due to extreme volatility and trading API instability
2. **Liquidity Evaporation**: Market depth disappeared almost instantly, forcing liquidation engines to dump positions into markets with effectively no bids
3. **Oracle Desynchronization**: Funding and index oracles desynced, with perpetual contracts showing prices significantly lower than actual spot markets, reinforcing the downward liquidation spiral
4. **Infrastructure Congestion**: Chain and exchange API congestion prevented traders from deploying capital to shore up margin positions in time, resulting in liquidations of even conservatively leveraged positions (2x on top 10 coins)
5. **Insurance Fund Depletion**: The speed of liquidations depleted exchange insurance funds, triggering auto-deleveraging (ADL)—a last-resort mechanism where exchanges liquidate traders' profitable positions, something "unheard of in TradFi"

The event was characterized as a "10 Sigma event" and represented the biggest liquidation of positions in crypto market history. However, once liquidations cleared, prices quickly bounced back, though not to pre-crash levels.

### Market Structure and Synthetic Stablecoin Mechanics

A critical aspect of the discussion centered on Ethena's USDE, which was initially reported to have de-pegged but actually maintained its peg. The confusion arose from fundamental differences between synthetic dollars and traditional stablecoins.

**USDE Mechanics and Controversy:**

Raagulan Pathy, drawing on his experience running Circle's Asia business during the USDC de-peg, clarifies the distinction: "A de-peg is a situation similar to where you've got USDC. Like if you've got a billion dollars of USDC, there's a billion dollars of cash sitting underneath it, right? So it's only if there's like a removal of that cash that there's an actual de-peg versus in the case of USDE, there's not a billion dollars of cash for a billion dollars of USDE. It's a long, short position."

The apparent de-peg was actually a Binance oracle feed issue. Binance's USDE oracle referenced its own relatively illiquid internal order book rather than the deepest pools of liquidity, which existed on-chain. This created the appearance of collateral impairment for traders using USDE as collateral, triggering further liquidations.

**Reserve Adequacy Concerns:**

Pathy raises a critical concern about USDE's reserve structure: Ethena maintains only $66 million in reserves against $13-14 billion of USDE outstanding (less than 0.5% coverage). He contrasts this with Circle's position during the USDC de-peg, where Circle had approximately $1 billion in cash plus Coinbase's $7 billion against $45 billion of USDC (roughly 20% coverage).

Pathy notes: "If there was a scenario in which the perp trading or short faltered and that default was bigger than 66 million then you'll be into an actual de-peg scenario because you would have less money there than actually it was quoted and then you get this like downward spiral that happens."

Morgan Krupetsky adds important context: Ethena refers to USDE as a "synthetic dollar" rather than a stablecoin, and USDE is pegged to USDT on DeFi money market funds, adding additional complexity to the risk profile.

### Institutional Perspectives on Market Maturity

The flash crash exposed significant immaturity in crypto market infrastructure, but the panelists note important differences from traditional finance crises.

**Comparative Analysis with 2008:**

Simon Taylor emphasizes a crucial distinction: "Think about how different this was from 2008 where fundamentally 2008 we had a 'is anybody solvent' question and where is the collateral and what's the collateral made of—that was not the problem here. Crypto Twitter solved this thing in less than two, three hours. Binance had started refunding people within what, 20 hours."

**Infrastructure Gaps:**

Krupetsky identifies several areas requiring institutional-grade improvements:

- Standardized price discovery mechanisms
- Enhanced risk controls
- Potential circuit breakers (though challenging in decentralized contexts)
- Regulation of centralized exchanges to ensure standardization in collateral maintenance

She notes: "The amount of money that it took to see this price action wasn't a lot. And so to your point, it doesn't instill that much confidence. And I think it proved that Bitcoin is an institutional asset and that TradFi was willing to kind of go in and bid it back. But otherwise, it's still really developing."

**Anti-Fragility Argument:**

Pathy introduces the concept of anti-fragility: "These de-pegs actually make you stronger because people see that you went through it and you did positive actions and you survived it. I think also it will probably wake them up to some risks that even if they've thought through all the risks, maybe there's some more that they need to do."

**Transparency Advantages:**

Krupetsky highlights a key advantage of on-chain infrastructure: "At least on-chain, you can see transparently like what's going to get liquidated at what price and when and what that looks like. It's a little bit more opaque, I think, from a centralized exchange perspective, which is why I think there does need to be some kind of standardization."

### M&A Activity: BVNK Acquisition Dynamics

Fortune reported that both Coinbase and Mastercard held advanced talks to acquire stablecoin infrastructure provider BVNK for approximately $2 billion—double the $1 billion Stripe paid for Bridge. The timing was notable, coming 24 hours after BVNK announced a strategic investment from Citibank.

**Strategic Rationale:**

Pathy outlines multiple motivations for such acquisitions:

1. **Speed to Market**: "These companies, Coinbase is now a 12, 13-year company, right? So they don't move as quick as you once would think. And so maybe it's easy just to buy a team that can move faster."

2. **Licensing and Distribution**: "I can't build this team quick enough, I can't get the licenses. I can't get the customers. And I can't, by the way, reinvent my culture quickly enough as well."

3. **De-risking**: "If you become part of a bigger org... for their partners, their banking partners, they're also like, oh, you're part of Stripe now. Okay, well, that's a little bit safer. We're not going to debank you as easily because that's a much bigger conversation because I'm debanking Stripe now."

**Orchestrator Vulnerability:**

The discussion reveals significant challenges facing orchestration layer companies:

- **Disintermediation Risk**: Pathy notes, "The biggest problem that these providers have is that they can get disintermediated. You know, for us, for example, if we get enough scale in a single market, we just start doing it ourselves."

- **Price Competition**: "My inbox on X and LinkedIn is filled every day with a new partner saying, hey, I'll give you the same rails for cheaper."

- **Banking Relationship Fragility**: The constant threat of being debanked creates existential risk for independent operators.

**Buyer-Specific Motivations:**

For Coinbase, the acquisition would complement their 80 million consumer base and strengthen their infrastructure play with Base and institutional services. For Mastercard, it represents an effort to maintain relevance as blockchain-based payment rails potentially disrupt traditional card networks. Krupetsky notes: "If this tech overtakes adoption, both globally and locally, obviously it's no secret. The credit card networks kind of might decrease from a relevance perspective."

### Corporate Treasury and Stablecoin Adoption

A significant theme throughout the discussion is the shift from consumer-focused stablecoin use cases to B2B and corporate treasury management.

**Growth Trajectory:**

Taylor highlights BVNK's announcement that since regulatory clarity emerged (Genius Act passage), the majority of their growth came from the United States and companies managing dollar-denominated cross-border treasury operations. This aligns with Artemis data showing B2B as the fastest-growing stablecoin use case.

**Institutional Demand Drivers:**

Krupetsky observes: "The B2B cross-border wholesale payments, treasury management conversation has really heated up over the past six to nine months... I think we'll see a lot more of that. And obviously, there's a lot more to it than just launching your own stablecoin in terms of seeing it win."

**Distribution Challenges:**

The panelists emphasize that distribution remains the critical challenge. Krupetsky notes: "The one thing that is very difficult to build in which some more crypto-native companies might take for granted is distribution... a lot of these companies, whether it is Coinbase or MasterCard or Citi or whoever it is, already has distribution."

**Scale Comparison:**

BVNK announced approximately $20 billion in total processed volume. While this pales compared to Stripe's $1.4 trillion, Taylor notes it represents significant traction for pure stablecoin payments infrastructure and took Stripe considerable time to achieve comparable early-stage volumes.

### Bank-Issued Stablecoins and Tokenized Deposits

The announcement that UBS, Santander, Bank of America, Barclays, BNP Paribas, Citi, Deutsche, Goldman, MUFG, and TD Bank are jointly exploring reserve-backed stablecoins for G7 currencies on public blockchains generated significant debate.

**Skeptical Perspective:**

Pathy offers a blunt assessment: "I think it's dead on arrival." His reasoning includes:

1. **Market Concentration**: "99% of stablecoins are just four stablecoins, right? And that is USDC, USDT, USDE, and DAI, right? And then 99% of stablecoins are USD."

2. **Permissionless Requirement**: "The major feature of stablecoins is because banks are just ridiculously permissioned and got more and more permissioned over the years, made people's lives pretty much hell. And so the biggest feature of a stablecoin is that it's largely permissionless, right? And I just did not see a world in which one bank, let alone a group of banks, are going to successfully launch something on the public Internet that's as permissionless as a USDC or USDT."

3. **Execution History**: Multiple failed bank consortium blockchain projects suggest low probability of success.

**Alternative Interpretation:**

Taylor reframes the initiative: "If we change the definition of what they're doing, because if they were building a stable coin, that would be ridiculous... What they're building is a settlement instrument between deposit tokens."

He explains the fundamental challenge: "My deposit token can't show up in somebody else's wallet. Because once it's done that, it's left the bank and it's not my deposit anymore. So what does that mean? How do I have a deposit that lives on chain outside of the bank—that's a legal question that has not been resolved."

**Existing Tokenized Deposit Activity:**

Taylor references JPMorgan's appearance on the show where they disclosed doing "trillions in italics" of total processed volume with tokenized deposits internally. The challenge is making these systems "open loop" to meet corporate client demands.

**Client-Driven Pressure:**

Taylor cites Eric from Velocity, who reported that in a previous role, corporates like Ant Financial demanded: "Yeah, you won't have our business anymore unless you start letting us move tokens around 24-7."

**Technical Efficiency Debate:**

Pathy, drawing on his Amazon Web Services background, questions the technical necessity: "I know how efficient databases are. So I don't like I love blockchains, but I don't love building blockchains for the sake of building."

Taylor counters with practical banking reality: "The amount of mainframes they have in the amount of different countries, and you could roll in the best database you want in the world. But my God, trying to get those to talk to each other is an absolute bleated nightmare."

**Integration Requirements:**

Krupetsky emphasizes that launching a stablecoin is insufficient: "You need to obviously ensure there's sufficient liquidity. You have to do business development to create integrations on and off ramps, custodians, exchanges, all that stuff and use cases... the effort needs to be made to actually integrate them into banks, enterprises, companies, operational flows, which is another question, which I don't think can be driven by the innovation and blockchain teams of these companies."

**Settlement Efficiency:**

The discussion highlights that the real inefficiency lies in settlement rather than FX trading. Krupetsky, drawing on 10 years at a large bank's FX desk, notes: "It's really post-trade that all the kind of scary things come to light."

Pathy adds a striking observation from his Circle experience: "One of the greatest innovations is just being able to settle dollars. It's amazing how few banks, pretty much almost none, can settle all of their countries in just dollars between the one bank itself, right? We used to often say to move money from Singapore to London, via Circle was often faster than a bank's own internal treasury system."

### The PayPal PYUSD Minting Error

In what the episode title references as a "$300 trillion dollar whoopsie," PayPal's blockchain partner Paxos accidentally minted $300 trillion PYUSD—more than double the world's entire GDP of $117 trillion.

**Operational Context:**

Pathy explains typical minting operations: "A lot of minting and burning is just done like a bank operation. Most of it's automated with obviously some daily reconciliation and et cetera. So I don't, I honestly don't even know how it happened. Like unless there was like a system error, et cetera, right? It's very unusual."

He notes he had never witnessed such an error during his time at Circle.

**Resolution and Controls:**

The error was quickly corrected through burn mechanisms: "All the issuers, various risk controls still can burn and control these things if needed, which happened in this case. And so I don't think it's a major issue apart from there's going to be quite a few memes going around about it."

**Comparative Context:**

Taylor provides perspective: "There was the example from I think it was Citibank who accidentally credited a client with $81 trillion dollars once so it's not a uniquely crypto thing—a fat finger error—but what is uniquely crypto is I think again how quickly it was fixed."

**Process Implications:**

Krupetsky emphasizes that manual processes exist in both Web2 and Web3: "Web3 companies have manual processes too in some way, shape or form. So I think that's just more of like a general kind of question around ensuring that you have your processes mapped end to end and robust risk and controls in place."

Taylor identifies the core concern for skeptics: "How do you want to one link to those underlying assets? How do you know where they are? How's that automated? How's that audited? And it's still a risk and control process. So there is a trust element there that I think we have to overcome."

## Key Insights and Implications

### Market Structure Evolution

The flash crash revealed that crypto markets, despite significant growth, remain small and immature relative to traditional finance. The amount of capital required to trigger such dramatic price action was relatively modest, indicating vulnerability to institutional-scale flows. However, the rapid recovery demonstrates a form of anti-fragility absent in traditional finance, where similar crises require regulatory intervention and extended resolution periods.

### Synthetic vs. Cash-Backed Stablecoins

The USDE controversy highlights critical distinctions in stablecoin design that are poorly understood by many market participants. Synthetic dollars using delta-neutral hedging strategies operate fundamentally differently from cash-backed stablecoins, with different risk profiles and reserve requirements. The adequacy of reserve ratios becomes increasingly critical as these instruments scale—USDE's 0.5% reserve ratio may have been sufficient at smaller scale but presents systemic risk at $13-14 billion outstanding.

### Oracle Reliability as Systemic Risk

The Binance oracle feed issue demonstrates that pricing infrastructure represents a critical vulnerability in crypto markets. When a dominant exchange (50%+ market share) references its own order book rather than deeper on-chain liquidity pools, it can create cascading liquidations based on inaccurate price signals. This suggests a need for standardized, multi-source oracle feeds with transparent methodologies.

### Orchestration Layer Commoditization

The willingness of orchestration layer companies to exit at relatively early stages (BVNK at $20 billion processed volume vs. Stripe's $1.4 trillion) suggests founders perceive limited defensibility in their position. Disintermediation risk, price competition, and banking relationship fragility create a ceiling on independent orchestrator valuations. Companies with existing distribution (Coinbase, Mastercard, Stripe) can acquire these capabilities more efficiently than building them organically.

### B2B Treasury Management as Primary Use Case

The shift from consumer-focused narratives to corporate treasury management represents a maturation of the stablecoin market. The inefficiency of cross-border dollar settlement—even within a single bank's global operations—creates immediate value propositions that don't require speculative adoption curves. This use case is being driven by client demand rather than supplier push, suggesting more durable adoption.

### Bank Tokenization Paradox

Banks face a fundamental paradox: they possess the distribution and client relationships to make tokenized assets successful, but their organizational structure, risk culture, and regulatory constraints make them poorly suited to execute. The legal ambiguity around deposit tokens that exist outside bank balance sheets remains unresolved. Bank consortium projects have a poor track record, yet client pressure is forcing banks to attempt solutions.

### Permissionless vs. Permissioned Tension

The core value proposition of stablecoins—permissionless access—directly conflicts with banks' operational and regulatory requirements. Any bank-issued stablecoin will necessarily be more permissioned than USDC or USDT, potentially limiting its utility. However, if banks are building settlement instruments for tokenized deposits rather than true stablecoins, the permissionless requirement may be less critical.

### Integration Over Innovation

Multiple panelists emphasize that launching a stablecoin or tokenized deposit is insufficient—the critical work lies in integration with operational flows, liquidity provision, and distribution channel development. This work cannot be accomplished by innovation or blockchain teams alone but requires coordination across treasury, operations, compliance, and business units.

### Speed as Competitive Advantage

The rapid resolution of both the flash crash and the PYUSD minting error demonstrates that 24/7 operation and transparent on-chain activity enable faster problem identification and resolution than traditional finance. This speed advantage may be more important than absolute stability in attracting institutional adoption.

## Data and Figures

### Flash Crash Metrics

- **Liquidation Scale**: Largest liquidation event in crypto market history
- **Duration**: Under 30 minutes for primary cascade
- **Price Impact**: Altcoins fell 60-80% in near-vertical drops
- **Leverage Threshold**: Even 2x leveraged positions on top 10 coins were liquidated
- **Recovery Time**: Prices began bouncing back within 2-3 hours; Binance refunds initiated within 20 hours
- **Statistical Characterization**: Described as a "10 Sigma event"

### Stablecoin Reserve Ratios

- **USDE**: $66 million reserves against $13-14 billion outstanding = 0.5% coverage
- **USDC (during de-peg)**: ~$8 billion available liquidity (Circle + Coinbase) against $45 billion outstanding = ~18% coverage

### Market Concentration

- **Binance Trading Volume**: Historically >80% of total crypto trading volume; currently ~50%
- **Stablecoin Concentration**: 99% of stablecoin value in four assets (USDC, USDT, USDE, DAI)
- **Currency Concentration**: 99% of stablecoins denominated in USD

### M&A Valuations

- **Bridge Acquisition**: $1 billion (Stripe, ~12 months prior)
- **BVNK Valuation Range**: $1.5-2.5 billion (reported)
- **BVNK Processing Volume**: ~$20 billion total processed volume
- **Stripe Processing Volume**: $1.4 trillion (for comparison)

### Tokenized Deposit Activity

- **JPMorgan**: "Trillions in italics" of total processed volume with internal tokenized deposits

### Minting Error Scale

- **PYUSD Accidental Mint**: $300 trillion
- **World GDP**: $117 trillion (for comparison)
- **Ratio**: Accidental mint was 2.56x global GDP

### Exchange Market Share

- **Top Three Exchanges**: Binance, OKEx, Bybit
- **Daily Volume**: Tens to potentially hundreds of billions of dollars daily

### Coinbase Scale

- **User Base**: 80 million consumers

### FX Efficiency

- **G7 Currency FX Spreads**: 1-3 basis points
- **Margin Characterization**: ~99% margin for banks on these transactions

## Definitions and Terminology

**Auto-Deleveraging (ADL)**: A last-resort mechanism used by exchanges when insurance funds are depleted, involving the forced liquidation of traders' profitable positions to cover losses from liquidated accounts. Described as "unheard of in TradFi."

**Synthetic Dollar**: A dollar-pegged instrument that maintains its peg through financial engineering (such as delta-neutral hedging strategies) rather than direct cash backing. Ethena's USDE uses long-short positions rather than holding $1 in reserves for each token.

**Delta-Neutral Hedge**: A trading strategy that combines offsetting positions to eliminate directional price risk, used by USDE to maintain its dollar peg without holding equivalent cash reserves.

**De-peg**: A situation where a stablecoin's market price diverges from its intended peg (typically $1.00). The panelists debate whether this term applies to synthetic dollars like USDE, which by design may trade slightly off-peg.

**Oracle Feed**: A data source that provides external information (such as asset prices) to blockchain smart contracts. The Binance oracle feed issue involved referencing the exchange's internal order book rather than deeper on-chain liquidity pools.

**Perpetual Contracts (Perps)**: Derivative contracts without expiration dates that allow traders to speculate on asset prices with leverage. These were heavily implicated in the flash crash liquidations.

**Tokenized Deposit**: A blockchain-based representation of a bank deposit that remains on the bank's balance sheet, distinct from a stablecoin. The legal framework for deposits that exist "on-chain outside of the bank" remains unresolved.

**Orchestration Layer**: Infrastructure companies that aggregate multiple services (licenses, on-off ramps, custody, liquidity, wallet services) to enable stablecoin and crypto payment flows. Examples include Bridge and BVNK.

**On-Off Ramp**: Services that facilitate conversion between fiat currency and cryptocurrency/stablecoins.

**Fat Finger Error**: A trading or operational error caused by human mistake, typically involving incorrect order sizes or quantities. The $300 trillion PYUSD mint is an extreme example.

**Circuit Breaker**: A mechanism that temporarily halts trading when prices move too rapidly, used in traditional markets but challenging to implement in decentralized systems.

**Insurance Fund**: Capital maintained by exchanges to cover losses from liquidated positions when traders' collateral is insufficient.

**Market Depth**: The volume of buy and sell orders at various price levels; deeper markets can absorb large orders without significant price impact.

**Funding Rate**: In perpetual contracts, the periodic payment between long and short position holders to keep the contract price aligned with the spot price.

**G7 Currencies**: Currencies of the Group of Seven nations (USD, EUR, JPY, GBP, CAD, CHF, and historically ITL before the euro).

**Total Processed Volume (TPV)**: The total value of transactions processed through a payment system, a key metric for payments companies.

**Total Value Locked (TVL)**: The total value of assets deposited in a DeFi protocol, a metric the panelists contrast with TPV as less relevant for payments use cases.

## References and Citations

### Direct Quotations

**On the flash crash mechanism:**
> "Market depth totally evaporated almost instantly and really forced kind of a wave of liquidations, again, largely in perps, which really kind of triggered a death spiral." — Morgan Krupetsky

**On USDE's structure:**
> "A de-peg is a situation similar to like where you've got USDC. Like if you've got a billion dollars of USDC, there's a billion dollars of cash sitting underneath it, right? So it's only if there's like a removal of that cash that there's an actual de-peg versus in the case of USDE, there's not a billion dollars of cash for a billion dollars of USDE. It's a long, short position." — Raagulan Pathy

**On reserve adequacy:**
> "One of the weak things about USDE, as much as I love the Athena guys, I'm a big holder of Eno myself, is that they only have 66 million in reserves against 13, 14 billion dollars of USDE, which is less than 0.5%." — Raagulan Pathy

**On crypto vs. 2008:**
> "Think about how different this was from 2008 where fundamentally 2008 we had a 'is anybody solvent' question and where is the collateral and what's the collateral made of—that was not the problem here. Crypto Twitter solved this thing in less than two, three hours." — Simon Taylor

**On bank stablecoin viability:**
> "I think it's dead on arrival... The major feature of stablecoins is because banks are just ridiculously permissioned and got more and more permissioned over the years, made people's lives pretty much hell. And so the biggest feature of a stablecoin is that it's largely permissionless, right?" — Raagulan Pathy

**On settlement efficiency:**
> "One of the greatest innovations is just being able to settle dollars. It's amazing how few banks, pretty much almost none, can settle all of their countries in just dollars between the one bank itself, right? We used to often say to move money from Singapore to London, via Circle was often faster than a bank's own internal treasury system." — Raagulan Pathy

**On acquisition rationale:**
> "If you become part of a bigger org... for their partners, their banking partners, they're also like, oh, you're part of Stripe now. Okay, well, that's a little bit safer. We're not going to debank you as easily because that's a much bigger conversation because I'm debanking Stripe now." — Raagulan Pathy

### Source Attribution

- **Episode**: Tokenized Podcast, Episode 53
- **Publication Date**: October 20, 2025
- **Participants**: Simon Taylor (GTM @ Tempo), Morgan Krupetsky (VP of Business Development for Onchain Finance @ Ava Labs), Raagulan Pathy (Founder & CEO @ KAST)
- **Sponsors**: Visa, Bridge (a Stripe company), Fireblocks
- **External Sources Referenced**: 
  - Fortune magazine (BVNK acquisition reporting)
  - Engadget (PYUSD minting error)
  - Artemis (stablecoin use case data)
  - Blockworks Das (flash crash coverage)

### Timestamp References

Key discussion segments occurred at:
- 02:23 - Flash crash and market liquidations
- 07:41 - Market structure and synthetic stablecoin risks
- 13:14 - Institutional perspective on crypto market maturity
- 18:19 - Coinbase and Mastercard potential acquisition of BVNK
- 24:54 - Corporate treasury as growing stablecoin use case
- 30:26 - Major banks exploring G7 currency stablecoins
- 32:36 - Debate on bank-issued stablecoins vs. tokenized deposits
- 39:10 - Inefficiencies in traditional cross-border dollar settlement
- 40:31 - $300 trillion PYUSD accidentally minted