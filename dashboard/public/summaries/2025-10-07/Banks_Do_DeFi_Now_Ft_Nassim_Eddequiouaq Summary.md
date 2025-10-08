# Banks Do DeFi Now: Stablecoin Adoption and Institutional Integration

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Data and Figures](#data-and-figures)
5. [Definitions and Terminology](#definitions-and-terminology)
6. [References and Citations](#references-and-citations)

## Executive Summary

This podcast episode documents a significant inflection point in stablecoin adoption, characterized by major financial institutions and technology companies launching proprietary stablecoin products and integrating with decentralized finance (DeFi) protocols. The discussion centers on three primary developments: Visa Direct's integration of stablecoins for cross-border payment funding, Stripe's Open Issuance platform enabling businesses to launch custom stablecoins, and Société Générale's deployment of stablecoins on DeFi lending protocols.

The participants—Simon Taylor (Tempo), Cuy Sheffield (Visa), and Nassim Eddequiouaq (Bastion)—identify a fundamental shift in stablecoin market structure. Rather than a handful of dominant stablecoins serving all use cases, the market is fragmenting into specialized, branded stablecoins that offer issuers control over economics, smart contract functionality, and user experience. This proliferation creates new interoperability challenges but also unlocks business models previously unavailable to financial services companies.

Key drivers for proprietary stablecoin issuance include: capturing reserve yield economics, controlling mint/burn fees, implementing custom security features (transaction reversal, fraud detection), and building closed-loop ecosystems. The discussion reveals that stablecoins are evolving from payment instruments into platforms for financial product innovation, particularly in lending and corporate treasury management.

The episode documents early adoption patterns: self-custodial wallets (MetaMask, Phantom) launching branded stablecoins to monetize their distribution, B2B neobanks (Brex, Ramp) integrating stablecoin payments for corporate clients, and traditional banks (Société Générale) deploying stablecoins on DeFi protocols to access on-chain credit markets. These developments suggest stablecoins are transitioning from crypto-native infrastructure to mainstream financial tools.

## Detailed Analysis

### Visa Direct Stablecoin Integration: Solving Cross-Border Funding Constraints

Cuy Sheffield describes Visa Direct as operating "one of the largest global money movement platforms" capable of reaching "about 11 billion endpoints" including cards, accounts, and wallets. The traditional constraint involves funding requirements: to enable a payout in Mexico funded from the US, companies must pre-fund during banking hours, creating weekend liquidity prediction challenges.

The stablecoin integration addresses this by enabling "seven days a week, 24-7" funding without requiring fiat pre-positioning. The architecture involves clients sending stablecoins to Visa, which converts them and enables "local fiat payments all across the world." This represents a settlement layer upgrade rather than a consumer-facing product change—the end recipient still receives local fiat currency.

The business rationale centers on operational flexibility for remittance companies and financial institutions that use Visa Direct. By accepting stablecoin funding, Visa reduces client working capital requirements and eliminates weekend funding gaps. This positions stablecoins as infrastructure optimization rather than a new payment rail competing with existing systems.

### Stripe Open Issuance: Democratizing Stablecoin Creation

Stripe's Open Issuance platform represents a significant reduction in barriers to stablecoin issuance. The platform promises stablecoin launch "with just a few lines of code" and includes reserve management, customizable smart contracts, and control over mint/burn fees. Stripe is also applying for a federal banking charter to comply with anticipated US stablecoin regulations.

A distinctive feature is "out of the box interoperability with other stablecoins that are open issuance"—meaning stablecoins issued through the platform for different clients (e.g., DoorDash and Cloudflare) would be interoperable because they share the same underlying issuer and reserves. This creates a network effect within Stripe's ecosystem while maintaining brand differentiation for clients.

Launch partners include Phantom (self-custodial wallet with 25 million users), Hyperliquid (DeFi platform), MetaMask, and Dakota (corporate spend management). The diversity of partners—spanning wallets, DeFi protocols, and B2B fintech—indicates broad market demand across different use cases.

### Stablecoin Issuance Models: Full-Stack vs. Wrapped

Nassim Eddequiouaq identifies two primary stablecoin architectures emerging in the market:

**Full-stack stablecoins**: Issuers maintain their own reserves, banking relationships, and accounts. This provides maximum control over economics and functionality but requires building distribution and liquidity from scratch. Larger enterprises and institutions prefer this model for risk management and regulatory control.

**Wrapped stablecoins**: These take existing stablecoins and wrap them, leveraging the underlying asset's liquidity and distribution. The M0 protocol exemplifies this approach, reportedly powering MetaMask's stablecoin to "defragment liquidity" and achieve stability faster. Small to medium-sized businesses favor this model to access established networks without full infrastructure buildout.

The market is developing hybrid approaches where issuers can "start maybe in one and then move to the other" or leverage "cross stablecoin issuance network effects" where the same issuer manages multiple stablecoins, enabling liquidity sharing.

### Business Rationale for Proprietary Stablecoins

The discussion identifies multiple drivers beyond simple payment facilitation:

**Economic control**: Issuers capture reserve yield (currently substantial given interest rates), control redemption and mint fees, and avoid sharing economics with third-party stablecoin providers. As Nassim notes, "you can only go so far by partnering with an existing issuer" due to "limitations in terms of the economics that you get on the reserves."

**Smart contract customization**: Proprietary issuance enables integration with existing fraud detection and security systems. Nassim describes working with "one of the largest companies in the world" that wants "to be able to undo transactions and revert transactions in a way that is fully integrated into their own security system." This level of control is unavailable when using third-party stablecoins.

**Product expansion**: Stablecoins function as platforms enabling rapid product iteration. Nassim observes that companies can "build on top of stablecoins instead" of APIs and SDKs, providing "not only the economics, but also the extensibility" to launch new products and partnerships while maintaining economic participation.

**Closed-loop ecosystems**: For companies with significant transaction volume, proprietary stablecoins enable value capture across the entire customer lifecycle—from onboarding through spending, lending, and yield generation.

### Interoperability Challenges and Solutions

The proliferation of stablecoins creates fragmentation challenges. Cuy Sheffield frames the core question: "how do you enable interoperability between Bastion stablecoins and Stripe stablecoins and Paxos stablecoins? Like, what does it look like cross-provider instead of just within provider?"

Current solutions include:

**Automated Market Makers (AMMs)**: Platforms like Tempo provide liquidity pools enabling stablecoin swaps, though this adds friction and cost.

**Shared issuer models**: Stripe's approach where multiple branded stablecoins share underlying reserves, enabling seamless interoperability within the ecosystem.

**Bridging protocols**: Cross-chain infrastructure enabling stablecoin movement between different blockchain networks, though this introduces additional complexity and risk.

The discussion acknowledges this remains "super, super early" with significant "value created in figuring that out" for companies that solve cross-provider interoperability.

### Self-Custodial Wallets as Stablecoin Issuers

Both MetaMask and Phantom launching stablecoins represents a significant market development. These wallets have massive distribution (Phantom: 25 million users) but face unique challenges compared to custodial neobanks.

Cuy Sheffield identifies the key distinction: custodial neobanks "can just use their interface and use the distribution that they have to try and create financial products and convince their customers to move over" but cannot force conversion. Users maintain control over existing USDC or USDT holdings. The question becomes "how successful can these self-custodial wallets be in converting what likely is billions of dollars of existing stablecoins that are sitting on those wallets today over to the self-custodial wallet branded stablecoin."

The business model depends on offering superior yield, rewards, or functionality to incentivize voluntary switching. This contrasts with custodial platforms that can auto-convert deposits into their proprietary stablecoin on the backend, creating guaranteed adoption.

### B2B Neobank Stablecoin Integration: Brex and Ramp

Brex's announcement enabling stablecoin payment of corporate card balances and stablecoin receipt represents pragmatic integration focused on existing customer needs. Simon Taylor observes this differs from Ramp's approach: "Ramp's proposition was about expanding the markets they could operate in, whereas Brex is about serving the customers they have today that want to move in stablecoins."

The use case centers on corporate treasury management. Companies increasingly hold stablecoins in treasury, and Brex serves "a number of crypto companies" using "stablecoins as kind of a core part of their corporate treasury." Enabling instant settlement of credit card balances with stablecoins provides immediate value without requiring customers to change operational workflows.

Cuy Sheffield notes crypto companies are "growing really quickly" with substantial fundraising and revenue, making them "an attractive client segment" for B2B neobanks. The regulatory environment has clarified sufficiently that serving crypto businesses is now viable, and updating capabilities to accommodate stablecoin payments becomes "a really logical thing to do that then grows the core business."

The instant settlement capability is particularly valuable for global companies needing to "move money across different subsidiaries to then pay a corporate credit card balance" where stablecoins enable immediate transfer "versus paying in fiat."

### Société Générale and DeFi: Banks Enter On-Chain Lending

SG Forge deploying euro and dollar stablecoins (EURCV and USDCV) on Uniswap and Morpho represents traditional financial institutions directly participating in DeFi protocols. Morpho users can now lend out SG stablecoins and borrow against them, with Morpho recently hitting "$1 billion in Bitcoin backed loans."

Cuy Sheffield characterizes this as "a big deal that a bank or a subsidiary of a large bank is directly participating and interacting with a DeFi protocol." He reframes DeFi as evolving into "on-chain credit and on-chain finance" rather than purely decentralized systems—the focus shifts to "new infrastructure that's emerging that is leveraging the properties of smart contracts to enable things like better lending platforms."

Morpho functions as a protocol connecting lenders and borrowers without being a lender itself, now embedded in multiple applications (Coinbase, Crypto.com). This creates "shared infrastructure layer that many crypto wallets are using to very quickly iterate around lending and financial products inside their platform."

The significance extends beyond crypto: Sheffield predicts "this is going to be one of the biggest stories of 2026. We're going to see more traditional financial institutions, not just looking at stablecoins for payments, but looking at stablecoins for on-chain credit." The efficiency gains over "managing loan books with spreadsheets and old legacy infrastructure" could be "10x better than existing solutions."

### Composability and Competitive Collaboration

The Morpho integration demonstrates a novel market structure where direct competitors (Coinbase and Crypto.com) share underlying lending infrastructure. Sheffield describes the dynamic: "you might actually have a crypto.com customer depositing a stablecoin to earn yield that ends up funding the loan of a Coinbase customer that's borrowing against their Bitcoin. And these are competitors."

This composability is enabled by "neutral infrastructure" creating liquidity concentration and market efficiency. The modular approach dramatically reduces time-to-market: rather than securing credit facilities, building ledgers, and establishing margin systems, companies "integrate into it" and launch products rapidly.

Simon Taylor observes: "If you want to see what most banks are going to be doing in five years' time, look at what Coinbase is doing today." The pattern of crypto buy/sell/hold becoming standard bank features suggests stablecoin lending may follow similar adoption curves.

### Bank Advantages in On-Chain Lending

The discussion identifies unique advantages banks bring to DeFi lending:

**Leverage capability**: Banks can lend up to $10 for every dollar in deposits, making them "highly levered lenders" and "very good levered risk managers." This provides structural advantages in providing liquidity to lending protocols.

**Deposit collection**: Issuing stablecoins backed by bank deposits creates a new deposit acquisition channel. SG Forge's approach enables collecting deposits "in a completely different way by issuing a stablecoin that is backed by your deposits."

**Balance sheet deployment**: Banks can deploy balance sheet into DeFi protocols either directly through lending or indirectly through stablecoin issuance, without necessarily competing with their traditional lending businesses.

Nassim emphasizes the speed advantage: "A bank like SG should not be able, even like a sub arm that is smaller, faster, more lean, typically does not move as fast as what we're seeing them do. And that's really, in my opinion, because of the enablement of stablecoins and then DeFi."

### Euro Stablecoin Demand Dynamics

An interesting aside addresses limited euro stablecoin adoption. Nassim notes: "The one thing that is puzzling me is still like the euro stablecoin. I haven't seen that much demand for it to this day."

Cuy Sheffield offers a hypothesis: "Arguably, there'll be more demand for Eurostable coins in a lending context than in a payments context." The logic: European borrowers and lenders prefer euro-denominated products, whereas euro payment stablecoins face limited demand given dollar dominance in cross-border transactions.

This suggests stablecoin demand may bifurcate by use case, with dollar stablecoins dominating payments while local currency stablecoins serve lending and regional financial products.

### SWIFT Blockchain Initiative

The episode briefly addresses SWIFT's blockchain project with 30 global banks. The participants express cautious optimism, with Nassim emphasizing the importance of "integrations for each one of those large banking institutions that will enable the same format, ideally, of money and make it interoperable with the ones that everyone is building currently in the stablecoin space or even the tokenized deposit space."

Cuy Sheffield notes many in crypto "don't even know what SWIFT does" while positioning it as an enemy to beat. He identifies SWIFT's role as a messaging layer and raises implementation questions: "Is this using Linea? Is this a SWIFT L2 with SWIFT as a single sequencer? Is it entirely permissioned? Are the banks going to run nodes?"

Simon Taylor suggests the optimal outcome would be "something that allows you to turn an ISO message and very quickly have a standard way of turning that into some sort of tokenized deposit and or be interoperable with the universe of stablecoins." SWIFT's advantage lies in enabling large banks to provide credit lines to smaller banks globally, facilitating correspondent banking without high pre-funding costs—a model potentially applicable to stablecoin infrastructure.

## Key Insights and Implications

### The Stablecoin Boom Business Model

The episode reveals stablecoin proliferation is driven by a new economic model analogous to the US fintech boom built on Durbin Amendment interchange arbitrage. Just as neobanks partnered with small banks to capture higher interchange rates, companies now issue stablecoins to capture reserve yield and fee economics previously unavailable. Simon Taylor suggests: "I wonder if we'll look back on the GENIUS Act as creating this explosion of innovation."

### Stablecoins as Platforms, Not Just Payment Instruments

A fundamental reframing emerges: stablecoins function as platforms enabling rapid product development rather than merely payment rails. Nassim states: "stablecoins are platforms. A lot of companies are moving away from building on top of APIs and SDKs and starting to build on top of stablecoins instead." This enables both economic participation and extensibility—partners can build on the stablecoin rather than integrating via API, creating network effects.

### The Payments-to-Lending Pivot

While stablecoins initially focused on payments, the discussion reveals lending as potentially more compelling for traditional financial institutions. Simon Taylor observes: "most banks don't get a positive business case out of stablecoins necessarily" for payments, but "here's this giant lending opportunity that's incredibly efficient." Banks possess structural advantages in lending (leverage, risk management expertise) that translate effectively to on-chain credit markets.

### Composability Enables Competitive Collaboration

The Morpho example demonstrates competitors sharing infrastructure while maintaining product differentiation—a market structure uncommon in traditional finance. This "neutral infrastructure" concentrates liquidity and improves efficiency while enabling rapid innovation. The implication: financial services may evolve toward shared infrastructure layers with competition occurring at the application and distribution layers.

### Self-Custodial Wallet Monetization Challenge

MetaMask and Phantom face a unique challenge: they cannot force users to adopt their stablecoins despite having massive distribution. Success depends on offering superior products that incentivize voluntary switching from established stablecoins. This contrasts with custodial platforms that control the user experience end-to-end and can default users into proprietary stablecoins.

### Speed of Iteration as Competitive Advantage

Multiple participants emphasize unprecedented development velocity enabled by stablecoin standardization. Nassim references the decade-long integration of PayPal and Venmo despite common ownership, contrasting this with current rapid iteration. The principle: "you only need to solve every single problem once" in open systems, enabling fast-follower advantages once initial solutions emerge.

### Regulatory Clarity Unlocking Institutional Adoption

The GENIUS Act and broader regulatory clarity enable traditional financial institutions to serve crypto businesses and deploy stablecoin products. Cuy Sheffield notes that "a few years ago, it might have been more challenging to be able to onboard and serve crypto businesses. Now, when you have a regulatory environment that's pretty clear, you could serve businesses that are in the crypto ecosystem."

### The Interoperability Paradox

Stablecoin proliferation creates value for issuers but fragments liquidity and complicates user experience. The market is "super, super early" in solving cross-provider interoperability. Solutions will likely combine technical infrastructure (AMMs, bridges) with business model innovation (shared issuer platforms like Stripe's Open Issuance).

### Smart Contract Customization Underexplored

The discussion reveals smart contract functionality—particularly freeze/seize mechanisms and transaction reversal—as an underutilized area. Historically used only for compliance and law enforcement, these capabilities could enable customer service improvements (recovering funds sent to wrong addresses) and fraud prevention integration. However, increased complexity introduces security risks and larger attack surfaces.

### Growth Rate Acceleration in Stablecoin Infrastructure

Simon Taylor cites BVNK reaching $20 billion annual processed volume (doubling from $10 billion earlier in the year) as evidence of accelerating growth. Nassim confirms: "the growth rate is real. Yeah. And that's what surprised people." This suggests the market is past early adoption and entering rapid expansion phase.

## Data and Figures

- **Visa Direct reach**: Approximately $11$ billion endpoints globally (cards, accounts, wallets)
- **Phantom wallet users**: $25$ million users
- **Morpho Bitcoin-backed loans**: $\$1$ billion milestone reached
- **Coinbase Morpho yield**: Up to $10.6\%$ APY for lending collateral
- **BlackRock Bitcoin ETF revenue**: $\$260$ million annually
- **BVNK processed volume**: $\$20$ billion annual run rate (doubled from $\$10$ billion earlier in 2025)
- **Fireblocks stablecoin volume**: Over $\$100$ billion monthly
- **SWIFT daily volume**: $\$5$ trillion in daily transactions
- **Bank lending leverage**: Banks can lend up to $\$10$ for every $\$1$ in deposits
- **PayPal-Venmo integration timeline**: Approximately one decade despite common ownership

## Definitions and Terminology

**Stablecoin**: A cryptocurrency designed to maintain stable value relative to a reference asset (typically US dollar), backed by reserves of fiat currency or other assets.

**DeFi (Decentralized Finance)**: Financial services built on blockchain infrastructure using smart contracts, operating without traditional intermediary institutions.

**White-label stablecoin**: A stablecoin issued by one entity but branded and operated by another, enabling companies to offer stablecoins without building full infrastructure.

**Mint and burn fees**: Charges applied when creating new stablecoin tokens (minting) or redeeming them for underlying assets (burning).

**Smart contract**: Self-executing code on a blockchain that automatically enforces agreement terms without intermediaries.

**Freeze and seize mechanism**: Smart contract functionality enabling issuers to prevent token transfers (freeze) or reclaim tokens (seize), typically for compliance or security purposes.

**Automated Market Maker (AMM)**: A DeFi protocol that enables automated trading between different assets using liquidity pools rather than traditional order books.

**Morpho**: A DeFi lending protocol that connects lenders and borrowers without itself being a lender, embedded in multiple crypto applications.

**Composability**: The ability to combine different protocols and applications like building blocks, enabling rapid innovation through shared infrastructure.

**Nostro account**: A bank account held in a foreign country by a domestic bank in the foreign country's currency, used for facilitating foreign exchange and international trade.

**GENIUS Act**: US legislation establishing regulatory framework for stablecoins (referenced in discussion regarding rulemaking and white-label models).

**ISO message**: Standardized message format used in financial services for payment instructions and information exchange (ISO 20022 standard).

**Tokenized deposit**: Bank deposits represented as blockchain tokens, maintaining deposit insurance and regulatory protections while enabling blockchain functionality.

**Self-custodial wallet**: A cryptocurrency wallet where users control their private keys directly, as opposed to custodial wallets where a third party manages keys.

**Correspondent banking**: A banking relationship where one bank provides services on behalf of another, typically for cross-border transactions.

**Private credit**: Lending by non-bank financial institutions to companies, typically involving direct loans rather than publicly traded debt.

## References and Citations

### Direct Quotations

**On stablecoin issuance demand:**
> "Every single company, I think, that you've been talking to, that we've been talking to, is thinking about issuing their own stablecoin." — Nassim Eddequiouaq

**On economic control:**
> "You want to have full control over the economics of every single dollar, and you need the value flowing through your ecosystem. You want to have control not only over that, but the redemption fees and the mint fees as well, without being pushed into certain directions based on the issuer that you work with." — Nassim Eddequiouaq

**On limitations of partnering:**
> "You can only go so far by partnering with an existing issuer. That's the reality, right? You have limitations in terms of the economics that you get on the reserves." — Nassim Eddequiouaq

**On stablecoins as platforms:**
> "Stablecoins are platforms. A lot of companies are moving away from building on top of APIs and SDKs and starting to build on top of stablecoins instead." — Nassim Eddequiouaq

**On DeFi evolution:**
> "DeFi is really evolving into what I like to think about as like on-chain credit and on-chain finance. It's not even just about it being decentralized." — Cuy Sheffield

**On bank participation in DeFi:**
> "I think this is going to be one of the biggest stories of 2026. We're going to see more traditional financial institutions, not just looking at stablecoins for payments, but looking at stablecoins for on-chain credit." — Cuy Sheffield

**On competitive collaboration:**
> "You might actually have a crypto.com customer depositing a stablecoin to earn yield that ends up funding the loan of a Coinbase customer that's borrowing against their Bitcoin. And these are competitors." — Cuy Sheffield

**On future bank behavior:**
> "If you want to see what most banks are going to be doing in five years' time, look at what Coinbase is doing today." — Simon Taylor

**On speed of iteration:**
> "The beauty about open source software is that you only need to solve every single problem once." — Nassim Eddequiouaq (attributed to Naval or similar source)

**On bank velocity:**
> "A bank like SG should not be able, even like a sub arm that is smaller, faster, more lean, typically does not move as fast as what we're seeing them do. And that's really, in my opinion, because of the enablement of stablecoins and then DeFi." — Nassim Eddequiouaq

### Company and Product References

- **Visa Direct**: Cross-border payment platform integrating stablecoin funding
- **Stripe Open Issuance**: Platform enabling custom stablecoin creation
- **Bridge** (Stripe company): Stablecoin infrastructure provider
- **Bastion**: Regulated stablecoin issuer (New York limited purpose trust charter)
- **Phantom**: Self-custodial wallet launching Cash stablecoin
- **MetaMask**: Self-custodial wallet with stablecoin product
- **Hyperliquid**: DeFi platform with USDH stablecoin
- **Dakota**: Corporate spend management platform with native stablecoin
- **Brex**: B2B neobank enabling stablecoin corporate card payments
- **Ramp**: B2B neobank launching stablecoin-linked cards
- **Meow**: B2B platform integrating stablecoin payments
- **SG Forge**: Société Générale's crypto subsidiary
- **Morpho**: DeFi lending protocol
- **Uniswap**: Decentralized exchange and AMM
- **M0**: Protocol for wrapped stablecoins
- **Paxos**: White-label stablecoin provider (issued PYUSD for PayPal)
- **Tempo**: Automated market maker platform
- **Coinbase**: Crypto exchange embedding Morpho
- **Crypto.com**: Crypto exchange embedding Morpho
- **Centrifuge**: DeFi protocol for real-world asset lending
- **BVNK**: Stablecoin payment infrastructure provider
- **SWIFT**: Global financial messaging network
- **ConsenSys**: Blockchain technology company (working with SWIFT)
- **Linea**: Layer 2 blockchain by ConsenSys

### Regulatory and Industry Context

- **GENIUS Act**: US stablecoin legislation establishing regulatory framework
- **Durbin Amendment**: Dodd-Frank Act provision affecting interchange fees, cited as analogy for stablecoin economics
- **ISO 20022**: Financial messaging standard referenced in SWIFT discussion
- **Federal banking charter**: Stripe's application for regulatory compliance
- **New York limited purpose trust charter**: Bastion's regulatory structure

---

**Validation Note**: This summary captures all major discussion topics from the transcript including Visa Direct integration, Stripe Open Issuance, stablecoin business models, interoperability challenges, wallet and neobank adoption, SG Forge's DeFi deployment, and SWIFT's blockchain initiative. Technical details regarding smart contracts, lending protocols, and market structure are preserved. Participant perspectives from all three speakers are represented with direct quotations. The organizational structure follows the podcast's thematic progression rather than strict chronology, as appropriate for a conversational format.