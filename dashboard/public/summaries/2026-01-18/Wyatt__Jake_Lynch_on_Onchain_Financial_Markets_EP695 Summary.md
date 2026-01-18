# Wyatt & Jake Lynch on Onchain Financial Markets (EP.695)

**Citation:** "Wyatt & Jake Lynch on Onchain Financial Markets (EP.695)." *On The Brink with Castle Island*, 12 Jan. 2026, <https://castleisland.libsyn.com/wyatt-jake-lynch-on-onchain-financial-markets-ep695>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [DeFi Business Model Framework](#defi-business-model-framework)
   - [Lending Markets as Sustainable Infrastructure](#lending-markets-as-sustainable-infrastructure)
   - [Evolution of Lending Use Cases](#evolution-of-lending-use-cases)
   - [Leverage and Looping Strategies](#leverage-and-looping-strategies)
   - [The October 10 Market Washout](#the-october-10-market-washout)
   - [Illiquidity and Asset Valuation Challenges](#illiquidity-and-asset-valuation-challenges)
   - [Fund Management and Valuation Practices](#fund-management-and-valuation-practices)
   - [DeFi Sector Mapping and Metrics](#defi-sector-mapping-and-metrics)
   - [Revenue, Profitability, and Valuation Multiples](#revenue-profitability-and-valuation-multiples)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [References and Citations](#references-and-citations)

## Executive Summary

This podcast episode features Wyatt Kashushahi and Jake Lynch discussing their report "Total Value Lost," which examines valuation methodologies for DeFi protocols, particularly lending markets. The conversation occurs against the backdrop of significant market volatility, including the October 10, 2024 washout and subsequent altcoin market challenges.

**Main Arguments:**

1. **DeFi lending markets represent one of the most sustainable business models in crypto** because they serve an evergreen need for capital formation, unlike the cyclical nature of swapping and settlement activities.

2. **Total Value Locked (TVL) is an inadequate metric** for assessing lending protocol value; stablecoin availability and actual loan volume are more meaningful indicators.

3. **Leverage in onchain markets is effectively unmeasurable**, creating systemic risk that even protocol operators cannot quantify, as demonstrated by the looping strategies that proliferated before the October washout.

4. **Most crypto assets suffer from severe illiquidity**, with order book depth insufficient to support their nominal market capitalizations, creating valuation distortions.

5. **The crypto market is undergoing sector definition and valuation discovery**, similar to early internet-era debates about appropriate metrics and multiples.

**Key Conclusions:**

The lending market represents a durable business model focused on two forms of capital formation: raising capital (launchpads) and lending. The most sustainable use case remains borrowing stablecoins against Bitcoin collateral—a need previously served by centralized platforms like Celsius and BlockFi. However, newer looping strategies that leverage yield-bearing tokens created dangerous, unmeasurable systemic leverage that contributed to market instability. The industry requires better valuation frameworks based on revenue-generating activities rather than vanity metrics, though current valuations reflect probabilistic bets on future market capture rather than present fundamentals.

## Detailed Analysis

### DeFi Business Model Framework

Jake Lynch establishes a fundamental taxonomy dividing DeFi into two major categories:

**1. Tokenization Activities:** Settlement and swapping—instantaneous, one-time use activities that are "very cyclical" with a "summer aspect" (hence "DeFi summer"). These businesses experience seasonal volatility.

**2. Capital Formation:** An "evergreen business" that represents crypto's unique value proposition. Lynch argues this "is one thing that crypto directly serves the value prop of, and you really can't do this capital formation outside of crypto."

Capital formation manifests in two forms:
- **Raising capital:** Platforms like MetaDAO, PumpFun, and Echo
- **Lending:** The focus of their analysis

This framework positions lending as fundamentally different from trading infrastructure—it serves a persistent need rather than speculative activity that waxes and wanes with market sentiment.

### Lending Markets as Sustainable Infrastructure

Lynch identifies lending markets as having "this really, really sticky user base" fundamentally "seeking yield on their assets. They're trying to turn nonproductive assets into productive assets." He compares this to stablecoin volume: "This doesn't go away with the season. This is constantly something people are seeking to do."

Kashushahi adds critical context about the transition from centralized to decentralized lending. The collapse of Celsius and BlockFi created both a void and "mistrust in those platforms," from which "the DeFi platforms benefited." The core use case these platforms served—"I want to own Bitcoin and as much more Bitcoin as I can and less dollars, but have spendable dollars against that Bitcoin"—remains the most straightforward and durable application.

Lynch provides concrete evidence: Morpho's integration with Coinbase allows borrowing against CBBTC (Coinbase's wrapped Bitcoin), which has grown to "over $1.5 billion of collateral in Bitcoin" and "has just been growing exponentially since they started earlier this year." Critically, "when you look at the TVL chart in the drop-off after October, this has not been hindered at all."

However, Lynch acknowledges ongoing trust issues: "There's still a degree of trust me that goes into the platforms today...you almost need a PhD today to actually understand the risk that you're getting paid for." The lending markets offer rates "as close to the risk-free rate as you can get," but they are definitively "not risk-free."

### Evolution of Lending Use Cases

Lynch traces the evolution of onchain lending: "Originally, if you look at what lending started as, it started as CDPs, where you would put up money and you would get a synthetic dollar essentially against this."

The recent transformation involves "the forms of lending and borrowing use cases that we see on chain have completely changed over the past year to two years." This evolution introduced new strategies and risks that fundamentally altered the lending landscape.

### Leverage and Looping Strategies

Lynch describes the emergence of "looping" as a critical development. The mechanism works as follows:

"I have some yield bearing token. The yield might be coming from any of many sources, treasury yield, right staking yield, basis trade through USD, RWA lending, any of these. And the idea or the realization that lending markets had is they can lend to these at a pretty high LTV. And when you lend to them at a really high LTV, you can actually recycle that capital."

The process: "You put in asset, you borrow against it, stable coin, you buy asset, you put asset back in and you borrow against it. And you continue to do this. And what you can do is you can take a yield from maybe 10% on an unlevered basis and lever it up to call it 25, 30%."

Lynch identifies two frightening aspects of this development:

**1. Unmeasurable Systemic Leverage:** "Although crypto is extremely traceable, it's virtually impossible to identify how levered a system is. It's very possible to go and do this looping on multiple platforms or from multiple accounts." Even more concerning: "We spoke all of the major lending protocols and all of them agreed that they don't know themselves. It's not something that they can measure."

**2. Increasing Risk in Underlying Assets:** While USDE represents "a relatively vanilla strategy" that "commodified" the basis trade, subsequent implementations moved "down the risk curve" into "different vault strategies." Lynch notes that USDE "evaporated the basis trade fund pitch. We stopped seeing them entirely" because it offered the same exposure with "way less friction."

The most dangerous development involved vaults "just cross-depositing into themselves. And this is extremely dangerous because essentially you take one fund and you're spreading the same amount of risk across all the other funds."

Lynch's assessment: "This was a strategy that I think we really rightfully identified as not extremely durable. It was very profitable for a lot of lending protocols. It will continue to be a strategy that lending protocols enable. But this is not what I would consider to be the bet on lending markets, so to speak."

### The October 10 Market Washout

Kashushahi directly asks whether the October 10 washout resulted from this leverage profile. Lynch provides a nuanced answer:

"This risk played a major role in how conservative the perpetual exchanges were with their own risk." Specifically, "leading into 1010, you had call it $6 to $8 billion of USD in Aave. And Aave is by any definition, probably the most systemically important protocol in crypto."

This concentration meant "any tremors in this asset would have huge, huge, huge downstream effects." Aave took the "extreme measure" of pegging USDE to USDT—"I wouldn't recommend hard pegging any asset in a lending market"—but this "turned out to be extremely necessary."

The immediate trigger: "What ended up as far as we can tell causing 1010 was a poor liquidation of USD on Binance, an order in the amount of maybe 60 million that was dumped on an order book that was not $60 million deep. And Binance's Oracle being tied into USD order book on its own platform."

Lynch distinguishes between proximate and ultimate causes: "The direct answer is probably this bad liquidation. But the indirect answer, it could definitely be ascribed to the fear that was around USD, the fear that was around this heavily levered asset."

### Illiquidity and Asset Valuation Challenges

Kashushahi provides a critical analysis of crypto asset liquidity:

"I think the degree of pain felt was because of how thin a lot of the order book depth is on a lot of these assets and across a lot of venues, with the outcome being that you have an asset that let's say it trades at a $200 million market cap, and supposedly it has $5 million a daily volume, but the order book depth within reason is a couple percent."

The practical implication: "Realistically, you can only trade a couple hundred thousand, something like that, of an asset like this without materially moving the market. Probably less, actually."

This creates a fundamental valuation problem: "Someone could easily argue a lot of these assets probably aren't worth what their claimed market cap is in the sense that, yes, the price of the asset as it trades on exchanges times the number of tokens in circulation is that $200 million market cap, but you can only functionally trade $250,000 of the asset per day. And if not, the market moves 10, 20%."

Lynch acknowledges this creates pervasive uncertainty: "When you look at all of the charts today, you have to zoom out because we now have this 95% candle on 10,000. And you're reminded that the fundamental floor is not necessarily there for a lot of assets."

Kashushahi notes the ironic outcome of composability: "For so long, composability or all the apps working well together was such a North Star that people wanted. And lo and behold, as a result of that, you get very composable risk, which means that one of these yield bearing stable coins becomes insolvent. And it's a big problem for the lending protocol. It's a big problem for whoever's curating that lending pool. It's a big problem for assets that are in a vault with those assets."

### Fund Management and Valuation Practices

Kashushahi poses a critical question about fund management: How do you invest in funds holding illiquid tokens they mark at inflated values?

Lynch explains their approach: "This is a strong case for why a fund of funds makes sense in crypto is because we see many funds that will mark a position that we see to be a position, maybe it's FDV is $500 million and it has $25,000 of volume per day. And they'll mark this at the value of $500 million."

Their solution: "With our managers, we have very strict, essentially, valuation policies built in. So for extremely illiquid assets, we're talking about assets that just came into existence that might have a 10% float or something like this. You have to put a massive discount on these assets."

The economic rationale: "We're economically incentivized as allocators to make sure that we're not overpaying in fees. If you take a malicious example here, a fund could easily inflate their NAV and charge you the fees on that performance or on that AUM."

Lynch distinguishes between fund types using Ray's framework: "There's the GBB and GPA. You can, in not so many words, categorize them as whether they want management fees or performance fees."

**The High Watermark Mechanism:**

Performance-fee-focused managers have natural incentives for conservative marking: "If you bring your nav up to 100 and then it drops back down and then it goes up partially to 100, you're not making performance fees on this until you breach what your high watermark was, call it that 100 mark."

The practical consequence: "If you're a manager and you want to incentivize really good talent, you're not going to be able to pay that talent" if the high watermark is artificially elevated.

Lynch provides a concrete example: "It is trivially easy in crypto to go into a token, have a launch, have it go up 10x, but be completely locked for like a year. And then you go to your fund admin and you say it's worth whatever that 10x value is. And all of a sudden, your investors have to pay fees on that unrealized, essentially on what that is."

Smart managers avoid this: "It's in your favor to market conservatively. And once that asset gets to a mature level where you can actually liquidate it safely, that's when you get paid."

### DeFi Sector Mapping and Metrics

Lynch presents a comprehensive DeFi sector map that has achieved "consensus with what everybody sees" over the past two years:

**1. Issuance:** Two forms
   - Issuing existing assets (RWA platforms, Circle)
   - Issuing new assets (launchpads: MetaDAO, Pump, Echo)

**2. Settlement:** Layer 1 blockchains where "you settle your assets on a blockchain"

**3. Swapping:** "If you don't have swapping, you can't do anything else interesting at all in crypto"

**4. Lending:** Enabled by the ability to liquidate assets through swapping

**5. Strategies:** Vault category including Lido—"I want to take an asset that is a nonproductive asset, turn it into a productive asset"

**6. Asset Management/Custody:** Squads, Safe, Copper, Fireblocks—"a lot of C5 DeFi overlaps"

Lynch emphasizes universality: "Broadly speaking, this is every single thing that you're going to do in crypto fits within these categories." Even specialized sectors like gaming, NFTs, and DePIN incorporate these DeFi elements.

**Critical Metric for Lending:**

Lynch argues the key metric is "the availability of stablecoins on that platform. Whether it's USDC, whether it's USDT, these stablecoins are overwhelmingly what is being borrowed."

The logic: "In order for a loan to exist, you need an asset that they're going to borrow against. And very few people want to borrow WBTC because they're effectively going short Bitcoin. Everybody in the world wants to lend WBTC. You see this, there's $10 billion of WBTC sitting on Aave with nobody borrowing it."

His prescription: "What I want to see in the lending protocols going forward is essentially a valuation that is more hinged on how good are these teams at finding dollars...Getting their dollars on platform so that they can be utilized."

**Rejecting Gameable Metrics:**

Lynch critiques historical L1 valuation approaches: "You would look at user metrics and you would look at GitHub commits." Both are "extremely gameable metrics."

User metrics: "As soon as you start looking at it, everybody can fake it."

GitHub commits: "Different companies are at different stages of developing...there are programs out there that will allow you to code how you want your GitHub commits to look."

The alternative: "What's not a gameable metric is revenue paying metrics. At the very end of the day, somebody is paying that revenue."

### Revenue, Profitability, and Valuation Multiples

Kashushahi expresses skepticism: "I think there's very few, if any, crypto platforms that generate revenue that justifies most of the token valuations out there."

Lynch counters by comparing to traditional venture: "Out of the startups that you guys invest in, what percent of the startups you're investing in are profitable at the time of investment?" Kashushahi responds: "At the time of investment, very few. A minority. A vast minority."

Lynch argues: "I don't think investors are looking at these platforms to necessarily be profitable. Revenue generating is an indication that people want to use your platform."

He identifies why crypto demands revenue visibility:

1. "They've been asking for revenue in the form of buybacks because they're desperate for net new buyers of this token and it seems like nobody's buying them."

2. "They don't trust the teams and they want to see the real numbers."

However, Lynch distinguishes between established projects and new launches: "Let's say you're a team that goes through the MetaDell launchpad and it's day one after the launchpad, you just got your first funding in. I think it's unreasonable to expect this team to be turning on big revenue numbers after day one."

**Valuation as Probabilistic Future Capture:**

Lynch frames valuations as forward-looking: "A lot of the valuations are really a function of the expectation of future revenues rather than the presence of current revenues. So it's the idea that does this company have a probability of succeeding in capturing a market? And if it captures that what is that market worth?"

He acknowledges DCF limitations: "If that market's in five years or eight years, sure, you can do your DCF and try to figure out what it's going to be worth, but you don't know what the size of anything is in five or eight years. So your DCF is going to be just as good as the valuation that the market is willing to buy and sell it at."

**Supply-Demand Dynamics:**

Lynch identifies structural pricing pressure: "The supply of flow that is out there for quality projects is so low. And the demand for these safe assets is so high that you have premiums and you have to pay a premium."

He provides concrete examples of valuation dispersion based on team quality:
- Good team with traction: $12.5 million valuation
- Good team, no traction: $30 million valuation  
- Great team, no traction: $50 million valuation

"What you see in how these VCs are funding these things is they're paying a huge premium for the talent, because the talent is the scarce thing."

**Investment Horizon Dependency:**

Lynch acknowledges valuation depends critically on time horizon: "I think that they're underpriced, but not categorically. And I think you have to have a five-year investment horizon for that to be the case. But if you put in a two or three-year investment horizon and do my model, it will tell you that you're going to be overpaying."

Kashushahi poses the aggregation question: "If you combine the market caps of all those $200 million protocols...of the layer ones, of the leading lending protocols, and you compile them into the winning cohort in five years, which numbers more? Because you would argue if Aave becomes big enough, it's a trillion dollar token or a hundred billion dollar token. As long as that exceeds the total value that everyone's paying for these things today, then you can justify that probabilism."

Lynch suggests much current valuation represents dead capital: "Probably the reason that these things are at this value, not like this is changing hands often. The reason that they're at this value is because the holders either lost their coins or they can't do anything with the money anyways. Maybe it's dark money."

For active DeFi protocols: "If you look at any of the teams that are shipping in DeFi, and you look at the collective valuation of these, I think you would look at this valuation and be like, this is not even close to what the TAM is if this thing succeeds."

**Ceiling Valuation Problem:**

Lynch addresses the Ethereum valuation question: "Somebody asked me, they said, do you think Ethereum is really worth $300 billion? And this is a tough question to answer because Ethereum, there's nobody above it when you look at smart contracts. So this is the ceiling."

He references Seep's Monad analysis: "What's the probability Monad becomes the next Ethereum, the valuation be some percentage of that? What he's not asking is, what is Ethereum worth? He's just saying the market values that this consider the market to be completely sane."

**Capital Supply Constraints:**

Kashushahi offers an alternative framing: "I'm to some extent a believer that a lot of these valuations applied are just based on the supply of capital. And the supply of capital is saying that whether it is Ethereum or something else, that's the amount of capital that's going to go into the premium L1 or L1s."

He identifies structural headwinds: "I think stablecoins, tokenized assets, and memecoins, frankly, a broader range of tokens, are materially detrimental to altcoins from this liquidity perspective."

## Key Insights and Implications

### 1. The Unmeasurability of Systemic Leverage Creates Existential Risk

The most alarming finding is that even major lending protocol operators cannot measure total system leverage. This represents a fundamental difference from traditional finance, where regulatory reporting and consolidated balance sheets provide visibility. The composability that makes DeFi powerful also makes it opaque at the system level.

**Implication:** Future market stress events are likely to be more severe than anticipated because participants cannot accurately assess their exposure to cascading liquidations.

### 2. TVL as a Metric Incentivizes Value Destruction

The focus on TVL has created perverse incentives, as evidenced by platforms like Turtle Club and Royco explicitly designed to inflate this metric. The looping strategies that dominated pre-October 2024 were profitable for protocols in the short term but created systemic fragility.

**Implication:** The industry requires a shift toward metrics that measure actual economic activity (loan origination, stablecoin availability) rather than capital accumulation.

### 3. The Centralized-to-Decentralized Lending Transition Remains Incomplete

While DeFi lending captured market share from failed centralized platforms, it has not solved the fundamental trust and complexity problems. Users still require "a PhD today to actually understand the risk that you're getting paid for."

**Implication:** A significant opportunity exists for platforms that can provide the transparency of DeFi with the user experience and risk clarity of traditional finance.

### 4. Composability Creates Composable Risk

The interconnection of DeFi protocols means that a failure in one yield-bearing stablecoin propagates through lending protocols, vaults, and derivative positions. This represents a fundamental architectural challenge.

**Implication:** Future DeFi infrastructure may require circuit breakers, isolation mechanisms, or other risk containment features that sacrifice some composability for stability.

### 5. Illiquidity Premium Distorts All Crypto Valuations

The gap between nominal market cap and actual tradeable value is pervasive. Assets with $200 million market caps may only support $250,000 in daily trading without significant price impact.

**Implication:** Traditional valuation frameworks based on market cap multiples are fundamentally broken for most crypto assets. Liquidity-adjusted valuations would show dramatically different rankings.

### 6. Fund Incentive Structures Determine Valuation Honesty

The distinction between management-fee and performance-fee funds creates divergent incentives around marking illiquid positions. High watermarks naturally encourage conservative valuation.

**Implication:** LPs should strongly prefer performance-fee structures in crypto, where the temptation and ability to inflate NAV through illiquid token markings is highest.

### 7. Talent Scarcity Drives Valuation More Than Fundamentals

The 4x valuation difference between teams of different quality ($12.5M to $50M) with identical traction (none) demonstrates that crypto valuations primarily reflect talent acquisition competition.

**Implication:** The industry is in a talent-constrained rather than capital-constrained phase, suggesting that team quality is the primary investment criterion.

### 8. Investment Horizon Determines Whether Current Prices Are Rational

Lynch's acknowledgment that lending protocols are overvalued on a 2-3 year horizon but potentially undervalued on a 5-year horizon reveals the temporal nature of valuation disputes.

**Implication:** Much of the debate about crypto valuations reflects different time horizons rather than different analytical frameworks.

### 9. The October 10 Event Demonstrated Oracle Fragility

The triggering event—a $60 million liquidation on an order book lacking sufficient depth, with Binance's oracle tied to its own order book—reveals dangerous circularity in price discovery mechanisms.

**Implication:** Oracle design and order book depth are critical infrastructure concerns that require industry-wide standards and redundancy.

### 10. Stablecoins and Tokenized Assets Fragment Altcoin Liquidity

The proliferation of alternative crypto assets (stablecoins, tokenized securities, memecoins) divides the available capital, creating a zero-sum competition for liquidity.

**Implication:** The altcoin market may face structural headwinds as capital flows into these alternative categories, potentially validating current pessimistic sentiment.

## Data and Figures

### Lending Market Metrics

- **Morpho-Coinbase CBBTC collateral:** Over $1.5 billion, growing exponentially since launch
- **USDE in Aave (pre-October):** $6-8 billion
- **WBTC on Aave:** $10 billion in deposits with minimal borrowing
- **Borrow yield on WBTC:** 8 basis points

### Leverage Ratios

- **Unlevered yield:** ~10%
- **Levered yield through looping:** 25-30%
- **USDE concentration in Aave:** ~20% of lending pool

### October 10 Washout

- **Triggering liquidation size:** ~$60 million USDE
- **Order book depth:** Insufficient to absorb $60 million without significant slippage
- **Price impact:** 95% drawdown candle on affected assets

### Valuation Comparisons

- **Team quality premium examples:**
  - Good team with traction: $12.5M valuation
  - Good team without traction: $30M valuation
  - Great team without traction: $50M valuation
  - Premium ratio: 4x based purely on team quality

### Illiquidity Metrics

- **Hypothetical asset example:**
  - Market cap: $200 million
  - Daily volume: $5 million (claimed)
  - Actual tradeable depth: ~$250,000 without significant price impact
  - Liquidity ratio: ~0.125% of market cap

### Ceiling Valuations

- **Ethereum market cap:** $300 billion (referenced as the smart contract platform ceiling)

## Definitions and Terminology

**Total Value Locked (TVL):** The aggregate value of assets deposited in a DeFi protocol. Lynch and Kashushahi argue this metric is misleading for lending protocols because it measures capital accumulation rather than productive economic activity.

**Looping:** A leverage strategy where users deposit yield-bearing tokens, borrow stablecoins against them, purchase more yield-bearing tokens, and repeat the cycle to amplify returns. Can increase a 10% yield to 25-30% through recursive borrowing.

**Collateralized Debt Position (CDP):** The original DeFi lending model where users deposit collateral to mint synthetic dollars (stablecoins) against their position.

**High Watermark:** The highest net asset value a fund has achieved. Performance fees are only charged on gains above this level, creating incentives for conservative valuation of illiquid positions.

**Loan-to-Value (LTV):** The ratio of borrowed amount to collateral value. High LTV ratios enable more aggressive looping strategies but increase liquidation risk.

**Order Book Depth:** The volume of buy and sell orders at various price levels. Shallow depth means large orders cause significant price movement.

**Fully Diluted Valuation (FDV):** Market cap calculated using total token supply rather than circulating supply, often dramatically higher than realized market cap.

**Composability:** The ability of DeFi protocols to interoperate and build on each other. While enabling innovation, it also creates "composable risk" where failures cascade across interconnected systems.

**Basis Trade:** A market-neutral strategy capturing the spread between spot and futures prices. USDE commodified this strategy, making it accessible to retail users.

**Vault Strategies:** Automated investment strategies where users deposit tokens into smart contracts that execute trading or yield-generation strategies on their behalf.

**Capital Formation:** Lynch's term for DeFi activities that create or allocate capital, including both fundraising (launchpads) and lending, distinguished from transactional activities like swapping.

**Performance Fees vs. Management Fees:** Performance fees are charged on profits above the high watermark; management fees are charged on assets under management regardless of performance. The former creates better alignment on valuation practices.

**Product-Market Fit (PMF):** Evidence that a product satisfies strong market demand, typically demonstrated through revenue generation or user growth.

**Dino Coins:** Older cryptocurrencies from previous cycles (NEO, Bitcoin Cash, Hedera Hashgraph) that maintain high nominal valuations despite minimal activity.

## References and Citations

### Direct Quotations

**On lending market durability:**
> "The lending markets to me are specifically interesting in crypto because they are one of the most sustainable businesses...With capital formation, this is like an evergreen business. This is one thing that crypto directly serves the value prop of, and you really can't do this capital formation outside of crypto." — Jake Lynch

**On unmeasurable leverage:**
> "Although crypto is extremely traceable, it's virtually impossible to identify how levered a system is...we spoke all of the major lending protocols and all of them agreed that they don't know themselves. It's not something that they can measure." — Jake Lynch

**On the October 10 trigger:**
> "What ended up as far as we can tell causing 1010 was a poor liquidation of USD on Binance, an order in the amount of maybe 60 million that was dumped on an order book that was not $60 million deep. And Binance's Oracle being tied into USD order book on its own platform." — Jake Lynch

**On illiquidity:**
> "You have an asset that let's say it trades at a $200 million market cap, and supposedly it has $5 million a daily volume, but the order book depth within reason is a couple percent. So realistically, you can only trade a couple hundred thousand, something like that, of an asset like this without materially moving the market." — Wyatt Kashushahi

**On composable risk:**
> "For so long, composability or all the apps working well together was such a North Star that people wanted. And lo and behold, as a result of that, you get very composable risk, which means that one of these yield bearing stable coins becomes insolvent. And it's a big problem for the lending protocol." — Wyatt Kashushahi

**On valuation methodology:**
> "What's not a gameable metric is revenue paying metrics. At the very end of the day, somebody is paying that revenue." — Jake Lynch

**On the key lending metric:**
> "The most important metric in lending is really the availability of stablecoins on that platform. Whether it's USDC, whether it's USDT, these stablecoins are overwhelmingly what is being borrowed." — Jake Lynch

**On investment horizons:**
> "I think that they're underpriced, but not categorically. And I think you have to have a five-year investment horizon for that to be the case. But if you put in a two or three-year investment horizon and do my model, it will tell you that you're going to be overpaying." — Jake Lynch

### Source Document

**Title:** Wyatt & Jake Lynch on Onchain Financial Markets (EP.695)  
**Published:** January 12, 2026  
**Show:** On The Brink with Castle Island  
**Primary Report Referenced:** "Total Value Lost" by Wyatt Kashushahi, Jake Lynch, and Henry (published late October 2024)

### Referenced Entities and Platforms

**Lending Protocols:** Aave, Morpho, Celsius (defunct), BlockFi (defunct)  
**Stablecoins/Yield Tokens:** USDE, USDC, USDT  
**Wrapped Assets:** CBBTC (Coinbase wrapped Bitcoin), WBTC  
**Launchpads:** MetaDAO, PumpFun, Echo  
**Capital Raising Tools:** Turtle Club, Royco  
**Other Protocols:** Lido, Uniswap (implied), Squads, Safe  
**Exchanges:** Binance, Coinbase  
**Layer 1s:** Ethereum, Solana (implied via Fire Dancer reference), Monad  
**Custody/Infrastructure:** Copper, Fireblocks  
**Companies:** Circle, Figure  

### Podcast References

The discussion references a previous podcast with Henry and Corin about vaults, and mentions Felipe's discussion of high watermarks in a prior episode.