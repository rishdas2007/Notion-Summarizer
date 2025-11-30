# Breaking Down Uniswap's Fee Switch and UNIfication Proposal | Hayden Adams & Jesse Walden

**Citation:** "Breaking Down Uniswap’s Fee Switch and UNIfication Proposal | Hayden Adams & Jesse Walden." *Bell Curve*, 26 Nov. 2025,


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [Historical Context: The Gensler Era](#historical-context-the-gensler-era)
   - [The UNIfication Proposal Structure](#the-unification-proposal-structure)
   - [Fee Implementation Mechanics](#fee-implementation-mechanics)
   - [Strategic Decision: Removing Frontend Fees](#strategic-decision-removing-frontend-fees)
   - [Legal Framework: DUNA and Governance](#legal-framework-duna-and-governance)
   - [Investor Alignment and Business Model Shift](#investor-alignment-and-business-model-shift)
   - [Retroactive Token Burn](#retroactive-token-burn)
   - [Future Considerations: Labs vs. DATs](#future-considerations-labs-vs-dats)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [References and Citations](#references-and-citations)

## Executive Summary

This episode of Bell Curve features Hayden Adams (founder of Uniswap) and Jesse Walden (early investor) discussing Uniswap's "UNIfication" proposal, which represents a fundamental restructuring of how the protocol generates and distributes value. The proposal addresses the long-discussed "fee switch" mechanism while simultaneously removing frontend fees from Uniswap Labs' interface, establishing a new legal structure through Wyoming's DUNA framework, and implementing a retroactive token burn.

**Core Objectives:**
- Activate protocol fee switches across Uniswap V2, V3, V4, and Unichain
- Redirect all protocol fees to burn UNI tokens rather than distribute to holders
- Eliminate frontend fees to align Labs' incentives with protocol growth
- Establish Uniswap governance as a DUNA (Decentralized Unincorporated Nonprofit Association)
- Create a service provider relationship between Uniswap Labs and the DAO
- Execute a symbolic 100 million UNI retroactive burn

**Key Arguments:**
The proposal represents a strategic pivot from monetizing products (frontend interfaces) to maximizing protocol adoption and usage. Adams and Walden argue this approach follows the "commoditize your complement" strategy, where making the product layer free drives exponentially greater value to the underlying protocol. The timing reflects both the end of the restrictive "Gensler era" of crypto regulation and the maturation of legal frameworks (DUNA) that enable practical DAO governance structures.

## Detailed Analysis

### Historical Context: The Gensler Era

Uniswap experienced "meteoric rise" during DeFi summer 2020, growing from $10 million to over $1 billion in daily trading volume within months. This growth occurred against a backdrop of regulatory uncertainty that would define the subsequent four years.

**Regulatory Constraints:**
Adams explains that during SEC Chair Gary Gensler's tenure, Uniswap Labs operated under severe restrictions regarding governance participation. The regulatory approach shifted from the earlier "sufficient decentralization" framework (exemplified by Ethereum's treatment) to what Adams characterizes as a stance where "anything that anyone does at all is bad." This created an environment where "if you build and create things that are valuable, if you build and launch things like, you know not supposed to do that."

**Internal Policy Response:**
Uniswap Labs adopted internal policies that severely limited governance participation. Adams notes: "part of the internal approach we took to governance is that we weren't going to put forward any proposals during that kind of previous era." The UNIfication proposal marks "my first governance proposal" despite founding the protocol.

**Continued Development:**
Despite restrictions, Labs continued building critical infrastructure including Uniswap V3 (described as "the most used trading protocol and in our spot trading Protocol in crypto history"), V4, and Unichain. Adams frames this as infrastructure investment: "the uniswap protocol is critical infrastructure for the products that we're building...our products don't work if the protocol isn't what it is and isn't able to be improved."

**Governance Evolution:**
During this period, independent governance structures emerged. Ken Ng, formerly of the Ethereum Foundation, submitted a proposal to create an independent grants program. Subsequently, Devin Walsh left Labs to join Ng in establishing the Uniswap Foundation, an entity "fully independent from Labs that was meant to be focused more around the ecosystem and the governance System."

### The UNIfication Proposal Structure

The proposal encompasses multiple interconnected components designed to align all stakeholders around protocol growth.

**Fee Switch Activation:**
Adams clarifies a common misconception: "People have always been like, when fee switch? It's actually like there's Uniswap V2, there's Uniswap V3, there's Uniswap V4. There's Uniswap X has a fee switch as well on each version of it." The proposal initially activates fees on Ethereum mainnet for V2 and V3, with subsequent proposals planned for V4 and other chains.

**Smart Contract Infrastructure:**
The proposal introduces new smart contracts with "cool names like TokenJar and FirePit." The TokenJar contract "fills up with thousands of tokens from across all different UniSwap pools. And then essentially when the jar becomes valuable enough, anyone can withdraw everything from the jar as long as they burn a certain amount of uni."

**Unichain Integration:**
Unichain represents a unique opportunity for value capture. Adams notes: "you can imagine there were periods where it was a billion dollars a year in ETH being burned just from usage of Uniswap on L1." On Unichain, "as much value is internalized to the protocol as can be" through the fee mechanism.

### Fee Implementation Mechanics

The proposal introduces sophisticated mechanisms for fee collection and value distribution.

**Protocol Fee Discount Auctions:**
Adams describes this as "a very funny, beautiful thing that happened" after years of exploring MEV internalization. The mechanism works by "auctioning off the right not to pay" protocol fees. Adams explains: "There's just something very funny about that."

**Technical Rationale:**
The discount auction addresses a fundamental tension in AMM design. Liquidity providers (LPs) lose money to "impermanent loss" during price divergence but earn fees from volatility and trading activity. Swap fees create arbitrage barriers—larger fees mean smaller price movements become unprofitable to arbitrage.

By introducing protocol fees that can be auctioned off, the system enables more granular arbitrage: "if LP fees are 30 bps and protocol fees are zero, and then you have LP fees are now 25 bps and protocol fees are five, You can kind of, by auctioning off the right to ignore the five, you can actually make arbitrage trades to within 25 bps instead of 30."

**Value Flow:**
This mechanism redirects value from MEV searchers to the protocol while potentially improving LP returns: "you're sort of like allowing for more and smaller arbitrage trade along the way which can improve lp profits...and then like the sort of auction is is uh the auction to not pay that fee is is sort of um how the value Ultimately still flows to the to the or the how the fees still kind of flow to the burn contracts."

**Parameter Space:**
Adams acknowledges this creates "an interesting design space and requires lots of thinking and parameterization and exploration in the future." The initial implementation represents the beginning of ongoing optimization.

### Strategic Decision: Removing Frontend Fees

The decision to eliminate frontend fees while activating protocol fees represents a fundamental strategic reorientation.

**Alignment Rationale:**
Adams articulates the core motivation: "from kind of like a what is the top line metric that we're tracking? I don't want that to be fees in our front end. I want it to be usage of the Uniswap protocol." He emphasizes: "we wanted to make it clear that like our full focus is on the protocol."

**Historical Criticism:**
The proposal addresses longstanding concerns about misalignment. As the host notes, "one of the criticisms, fair or not, about Uniswap for years was that there's this misalignment of incentives between equity holders of the labs entity and then the token Holders of the protocol."

**Commoditize Your Complement Strategy:**
Walden provides the theoretical framework, referencing Joel Spolsky's concept. He traces Uniswap's history: "He invented the Uniswap protocol, and then he also built the first front-end interface on top." The original interface, designed by Cal, created "this buttery experience of one token to another. It was like a vending machine" that made the complex AMM mechanism accessible.

**Bootstrap Then Commoditize:**
Walden explains the strategy: "if you're building a novel protocol, you also need to go and build the first product On top, make sure that product solves a problem for users, and use that product to bootstrap the network effects on the underlying protocol." Once bootstrapped, "the Uniswap Labs front end is not dominant in terms of market share. In fact, a lot of the flow going through the protocol is coming from third parties."

**Positive-Sum Dynamics:**
Walden distinguishes crypto's implementation from traditional "commoditize your complement" strategies: "I think it's actually very different in the case of decentralized protocols. And that's why the strategy works even better in this context...this game can be much more positive sum."

The key difference: "underlying protocol is permissionless, decentralized, that can't rug you, and you can own a piece of it." Third-party integrators "can own a piece of the token or a piece of the network that they're integrating by virtue of buying the token. And that token is going to accrue fees if that, or accrue value if the protocol or the proposal passes."

**Competitive Stance:**
Adams clarifies the approach isn't about brutal competition: "sometimes the phrase commoditize your compliment kind of implies a little bit of almost brutal. We're going to completely compete anyone building on top of the protocol to zero, which is really not our goal...if you build a really good interface, you have a really, really loyal user base that trades through the user protocol and you charge fees, we're happy for you."

### Legal Framework: DUNA and Governance

The proposal's legal structure represents a novel approach to DAO governance enabled by recent Wyoming legislation.

**DUNA Creation:**
Adams explains: "a lot of this proposal is built on this DUNA thing, which was actually Like, you know, a new type of entity that was created through a Wyoming law that was passed in the past like two years." DUNA stands for Decentralized Unincorporated Nonprofit Association.

**Legal Clarity:**
The DUNA framework addresses multiple governance concerns that blocked previous fee switch proposals. Adams notes historical objections: "things like A6 and Z saying, hey, we're worried about tax liability. We're worried about, oh, this Uki-Dao case and where governance participants got sued."

The DUNA provides "some level of understanding around how tax would be viewed within this, what gave some level of understanding around, you know, The liability of governance participants."

**Service Provider Relationship:**
A novel aspect is the contractual relationship between Labs and the DAO. Adams describes it as "almost like an end like it almost Allows like the the dow itself to like have or in governance itself to have like contractual relationships and stuff like that and so so part of this proposal include you know as part Of this like creation of the growth fund etc like includes like a service provider and contractual relationship between us and the dow."

**Balanced Decentralization:**
Walden frames this as solving the DAO coordination problem: "what we learned through The era of dows back in like 2021 when there was tons of experimentation going on um is is like too much decentralization it like it is really hard for a startup to to operate under because You know you need you do need to make forward progress um and decision by committee is kind of a slow run."

The solution: "this proposal, I think, lands in a very sweet spot where you still have governance, like the token holders, but you also have the service provider relationship that codifies How Uniswap Labs can be incentive aligned with all the token holders."

**Separation of Concerns:**
Adams emphasizes the distinction between protocol and governance decentralization: "the protocol itself is like immutable smart contracts and it's kind of like automatically works it automatically you know uh burns burns fees...governance is like very limited to specific parameters."

He adds: "we're like a software development Firm and like i don't think that like token holders shouldn't be voting on day to day technical decisions from a software development firm."

**Ultimate Resilience:**
Adams highlights the protocol's fundamental robustness: "imagine if like all like token governance and labs were both horrible, like Uniswap would still Survive because the protocol itself doesn't rely, like doesn't, you know, ultimately rely on either of these entities to continue to function."

### Investor Alignment and Business Model Shift

The transition from frontend fee revenue to protocol-aligned incentives required navigating complex stakeholder dynamics.

**Investor Composition:**
Adams notes: "the majority of my investors have been around for a long time. Most of them are also stakeholders in the broader Uniswap ecosystem. There's not a perfect mapping, but I'd say that, generally speaking, the investor group has been pretty supportive."

**CEO Decision-Making:**
Adams frames the decision in terms of avoiding local maxima: "I think one of the biggest jobs of a CEO and I've been learning this on the job as I go is like almost like thinking about like there's sort of like Local Maxima...avoiding like the local Maxima trap where like something feels like safe and stable. And so you just do that forever versus like thinking about like bigger opportunities and how you kind of traverse to them."

Frontend fees represented stability: "yes, front-end fees were a stable business. But I think that...the big opportunity of Uniswap is the Uniswap protocol success. And so I want to kind of align our upside to making the protocol successful and not just these front end products."

**Investor Perspective:**
Walden provides the investor viewpoint: "in my view, this is how it sort of always should have been. The thing that we really invested in, again, was Hayden and what they built with the protocol and the product on top. But I think at the time that we invested, product on top wasn't being monetized the expectation was all the values in this in the protocol."

The original thesis: "all the world's value is Going to get tokenized all that value is going to need a place to be exchanged and uniswap protocol is the exchange...And and there's gonna be many products on top um but the protocol will be the kind of canonical center of all that liquidity."

**Funding Mechanism:**
The proposal includes a growth fund from the treasury to support Labs development: "the proposal includes a, you know, a kind of like a growth fund from the treasury that labs will be, you know, that will fund a lot of the development here."

### Retroactive Token Burn

The proposal includes a symbolic 100 million UNI burn addressing historical community sentiment.

**Rationale:**
Adams explains: "part of what happened Though over the past four years it's not just like us fighting legal battles there's also like a community sentiment thing that happened which was like a lot of frustration over a long Time people like like not everyone like understood what was happening not people you know not everyone had called context."

The community "had like kind of like long expressed like you know a wish that the protocol fees had been turned on earlier um And you know in like uniswap protocol did four trillion dollars in trading during the period where the fee switch was off which is like a mind-boggling number."

**Calculation Methodology:**
The 100 million figure came from data analysis: "we ran different data queries on like how many, and it's like, honestly, like, like there's like a lot, it's debatable on how you parametrize it. But like they kind of came out in the range of like 100 million uni it kind of depends on the exact period like the exact levels like there's no perfect number and you can't like retroactively Perfectly calculate."

**Symbolic Significance:**
Adams connects it to Uniswap's history of innovation: "uniswap like pioneered the retroactive airdrop Um and so like there's sort of people are used to like uniswap surprising or like not to, it's almost like we've surprised with a retroactive thing in the past. And when we did the Uniairdrop, it hadn't really been done in the way that we'd done it. And it kind of really kickstarted this as almost a broader industry phenomenon."

**Investor Perspective on Burns:**
Walden offers a nuanced view: "I think it's great, especially for a mature protocol like Uniswap. And yet, I also think that crypto trader writ large is too myopically focused on...burning tokens. Given that most protocols are not as mature as Uniswap, and they're high growth startups, high growth startups need to be profitable, but they generally are not distributing dividends To token owners."

His advice: "Grow the pie like many orders of magnitude bigger in terms of adoption and usage before we focus on, you know, yeah, making number go up, you know, in a kind of like more forced artificial Way."

### Future Considerations: Labs vs. DATs

The discussion addresses potential future structures and the relationship to Decentralized Autonomous Trusts (DATs).

**Current Stance:**
Adams is clear about priorities: "that's certainly not like our focus or area in terms of like, I also say like, like, you swap labs is pretty different from a DA in terms of like, you know, that's tend to, you know, What they're essentially doing is like buying, you know, raising money, buying a ton of tokens."

He adds: "To me, it would feel like a distraction to do this right now...It would also be like massive confusion to this, you know, this unification story."

**Conditional Openness:**
Adams leaves the door open conditionally: "the only way that I would, you know, be excited to kind of do something in that direction would be if I felt like it really like contributed to this alignment story And was like really additive to it."

**Structural Similarities:**
Walden identifies key parallels: "Labs is an equity entity whose primary sort of value accrual mechanism now, today, or if the proposal passes, is like Uni on the balance sheet...if you think about what a DAT is, it is an equity entity that is like, you know, primary value accrual mechanism is tokens per share, tokens on the balance sheet. So there is that similarity."

**Critical Differences:**
Walden notes: "most stats are not full of... The founders of the protocols are not at the data, so that's one key difference here. And most stats are not shipping new versions of the protocol. That's another key difference here."

**DAT Evolution:**
Walden predicts: "many of the stats that don't have any kind of functional value to add to the ecosystems they're in may not last very long. The ones that stick around will probably have to find a way to do that in order to stand out in the market...if DATs continue to exist in three, four years, which I think they will, they will look very different than they look currently. They might look more like operating companies that actually do things that contribute value."

**Operating Model Distinction:**
Adams notes current DAT characteristics: "people are like, want like very low operating costs, you know, because you're kind of like minimizing, Like if people just want like exposure to, you know, to the underlying tokens, essentially, in a lot of these stats. And so that wouldn't, that wouldn't be a model that would make sense here."

## Key Insights and Implications

### Industry Precedent Setting

Uniswap's historical role as an industry standard-setter suggests the UNIfication proposal could catalyze broader changes. Adams observes: "it seems to be true that the things that we do are copied or kind of standard in the industry in the sense that we did this airdrop and then suddenly everyone was doing airdrops. Our protocol has been forked 5,000 times. Our front end has been forked 5,000 times at least."

Walden frames the potential impact: "if if this works it'll prove Like a really big point which is that the you know protocol growth as the north star focus is how you actually create way more value right than any single product can create." The implication: "the protocols are growing many orders of magnitude bigger in terms of usage and adoption and integrations."

### Regulatory Environment Shift

The proposal's viability reflects fundamental changes in the regulatory landscape. The contrast between the "sufficient decentralization" framework and the Gensler-era approach highlights how regulatory uncertainty constrained innovation. The emergence of legal frameworks like DUNA represents infrastructure development that enables practical DAO governance.

Adams emphasizes Uniswap's unique position: "from like a brand perspective, from a name perspective, we're like the Largest, most kind of, uh, you know, like things we do get the most attention of, of any part of the industry." This visibility necessitated conservative approaches: "we've sort of always been at the forefront of what gets the most attention, that gets the most scrutiny. We also, you know, have kind of always held ourselves a very high standard."

### Protocol vs. Product Value Capture

The strategic shift from product monetization to protocol value capture represents a fundamental thesis about value creation in crypto. Walden's "DeFi mullet" thesis—business in the front, protocol in the back—suggests protocols can achieve orders of magnitude greater scale than any single product interface.

The positive-sum dynamics enabled by token ownership distinguish crypto from traditional "commoditize your complement" strategies. Third-party integrators can simultaneously compete with and benefit from protocol growth through token ownership.

### Governance Structure Innovation

The DUNA-enabled service provider relationship represents a novel solution to the DAO coordination problem. By separating protocol immutability from development governance, the structure maintains decentralization benefits while enabling effective execution.

Walden's observation about DAO evolution is significant: "we swung too far towards like total decentralization, flat decision making like that in my view just doesn't work because, you know, start startups need leadership." The UNIfication structure provides a template for balancing decentralization with operational effectiveness.

### Token Value Accrual Mechanisms

The burn mechanism represents a specific approach to value accrual that differs from dividend-style distributions. The choice reflects both technical considerations (simplicity, gas efficiency) and philosophical alignment with protocol growth over immediate yield.

Walden's caution about myopic focus on burns for early-stage protocols highlights an important distinction: mature protocols like Uniswap can prioritize value return, while growth-stage protocols should prioritize adoption and usage expansion.

## Data and Figures

### Trading Volume Growth
- **DeFi Summer 2020**: Uniswap grew from $10 million to over $1 billion in daily trading volume
- **Historical Volume**: $4 trillion in trading volume during the period when fee switches were off

### Fee Structure Parameters
- **Example LP Fees**: 30 basis points (bps)
- **Example Protocol Fees**: 5 bps (subtractive from LP fees, resulting in 25 bps to LPs)
- **Discount Auction Mechanism**: Enables arbitrage to within 25 bps instead of 30 bps

### Retroactive Burn
- **Amount**: 100 million UNI tokens
- **Rationale**: Symbolic representation of fees that would have been collected if switches had been activated earlier
- **Calculation**: Based on data queries across different time periods and fee levels, though "there's no perfect number"

### Value Capture Historical Example
- **Ethereum L1 Burns**: Periods where Uniswap usage resulted in approximately $1 billion per year in ETH being burned

### Adoption Metrics
- **Protocol Forks**: Approximately 5,000 forks on GitHub
- **Frontend Forks**: Approximately 5,000 forks
- **Governance Participation**: The UNIfication snapshot vote achieved the highest participation in Uniswap governance history

## Definitions and Terminology

**Fee Switch**: A parameter in Uniswap smart contracts that, when activated, diverts a portion of trading fees from liquidity providers to the protocol. Multiple fee switches exist across different Uniswap versions (V2, V3, V4, X).

**DUNA (Decentralized Unincorporated Nonprofit Association)**: A legal entity type created by Wyoming law within the past two years, designed specifically for crypto protocols. Provides clarity on tax treatment and liability for governance participants while enabling contractual relationships between DAOs and service providers.

**Protocol Fee Discount Auctions**: A mechanism where the right to avoid paying protocol fees is auctioned off. Enables more granular arbitrage opportunities while still capturing value for the protocol through the auction process.

**TokenJar and FirePit**: Smart contracts implementing the fee collection and burn mechanism. TokenJar accumulates diverse tokens from trading fees; FirePit executes the burn when sufficient value accumulates.

**Impermanent Loss**: The price risk liquidity providers face when token prices diverge significantly from entry to exit. LPs lose money on price divergence but earn fees from trading activity and volatility.

**MEV (Maximal Extractable Value)**: Value captured by searchers who identify and execute profitable arbitrage opportunities. The protocol fee discount auction mechanism aims to internalize some of this value.

**Commoditize Your Complement**: A business strategy where a company makes complementary products free or cheap to drive demand for its core product. In Uniswap's case, making frontend interfaces free to drive protocol adoption.

**DeFi Mullet**: "Business in the front, protocol in the back"—a strategy where protocols maintain decentralization while products built on top handle user-facing business functions.

**DAT (Decentralized Autonomous Trust)**: An equity entity whose primary value accrual mechanism is tokens on the balance sheet, typically with low operating costs and focused on token exposure rather than active development.

**Service Provider Relationship**: A contractual arrangement between Uniswap Labs and the Uniswap DAO (via DUNA) that defines Labs' responsibilities, funding, and accountability while maintaining DAO governance authority.

**Sufficient Decentralization**: A regulatory framework articulated pre-Gensler era, suggesting that sufficiently decentralized networks (like Ethereum) are not securities. Based on network decentralization rather than governance structure.

## References and Citations

### Governance Proposals
- **UNIfication Proposal**: https://gov.uniswap.org/t/unification-proposal/25881
- **DUNA Establishment Proposal**: https://gov.uniswap.org/t/governance-proposal-establish-uniswap-governance-as-duni-a-wyoming-duna/25770

### Key Quotes

**On Regulatory Constraints:**
> "in this Gensler era, there was a very different approach which was taken, which was anything that anyone does to create any, or to kind of like, you Know, like almost like anything that anyone does at all is bad. And that was sort of like, you know, if you build and create things that are valuable, if you build and launch things like, you know not supposed to do that." — Hayden Adams

**On Strategic Focus:**
> "from kind of like a what is the top line metric that we're tracking? I don't want that to be fees in our front end. I want it to be usage of the Uniswap protocol." — Hayden Adams

**On Positive-Sum Dynamics:**
> "the key difference in crypto is like this game can be much more positive sum. And that's because like underlying protocol is permissionless, decentralized, that can't rug you, and you can own a piece of it." — Jesse Walden

**On Governance Balance:**
> "this proposal, I think, lands in a very sweet spot where you still have governance, like the token holders, but you also have the service provider relationship that codifies How Uniswap Labs can be incentive aligned with all the token holders." — Jesse Walden

**On Protocol Resilience:**
> "imagine if like all like token governance and labs were both horrible, like Uniswap would still Survive because the protocol itself doesn't rely, like doesn't, you know, ultimately rely on either of these entities to continue to function." — Hayden Adams

### Historical Context
- **DeFi Summer**: Summer 2020 period of explosive DeFi growth
- **SushiSwap Vampire Attack**: Historical event referenced as example of community governance importance
- **Unisocks**: Early Uniswap NFT project demonstrating protocol innovation
- **Retroactive Airdrop**: Uniswap pioneered this distribution mechanism, which became an industry standard

### Participants
- **Hayden Adams**: Founder of Uniswap, CEO of Uniswap Labs
- **Jesse Walden**: Early Uniswap investor, crypto strategy commentator
- **Mike Ippolito**: Host, Bell Curve podcast
- **Ken Ng**: Former Ethereum Foundation grants lead, co-founder of Uniswap Foundation
- **Devin Walsh**: Former Uniswap Labs employee, co-founder of Uniswap Foundation
- **Cal**: Early Uniswap Labs designer responsible for iconic interface