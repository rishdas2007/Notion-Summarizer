# What Ethereum Will Look Like When It Implements Its New Privacy Focus - Ep. 959

**Citation:** "What Ethereum Will Look Like When It Implements Its New Privacy Focus - Ep. 959." *Unchained*, 25 Nov. 2025, <https://unchainedcrypto.com/podcast/what-ethereum-will-look-like-when-it-implements-its-new-privacy-focus/>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [The Privacy Cluster Initiative](#the-privacy-cluster-initiative)
   - [Common Misconceptions About Crypto Privacy](#common-misconceptions-about-crypto-privacy)
   - [Evolution of Privacy Stewards of Ethereum (PSE)](#evolution-of-privacy-stewards-of-ethereum-pse)
   - [Institutional Privacy Task Force (IPTF)](#institutional-privacy-task-force-iptf)
   - [Why Privacy Matters in Crypto](#why-privacy-matters-in-crypto)
   - [Technical Approaches to Privacy](#technical-approaches-to-privacy)
   - [Private Identities and Zero-Knowledge Proofs](#private-identities-and-zero-knowledge-proofs)
   - [Privacy User Experience](#privacy-user-experience)
   - [The Kohaku SDK](#the-kohaku-sdk)
   - [Relationship with Other Privacy Efforts](#relationship-with-other-privacy-efforts)
   - [Regulatory Considerations](#regulatory-considerations)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Definitions and Terminology](#definitions-and-terminology)
5. [References and Citations](#references-and-citations)

## Executive Summary

In October 2025, the Ethereum Foundation announced the formation of the Privacy Cluster, a coordinated effort involving 47 researchers, engineers, and cryptographers aimed at establishing privacy as a "first-class property of the Ethereum Ecosystem." This initiative represents a significant evolution of Ethereum's longstanding privacy efforts, now refocused specifically on the Ethereum ecosystem rather than broader privacy research.

The Privacy Cluster encompasses two main organizational components: Privacy Stewards of Ethereum (PSE), which has been operating since 2019 and focuses on developing privacy primitives and applications, and the newly formed Institutional Privacy Task Force (IPTF), which addresses the specific privacy requirements of financial institutions and enterprises seeking to build on public blockchains.

**Key objectives include:**

- Making privacy a default feature rather than an opt-in addition
- Developing privacy solutions across multiple dimensions: private reads (metadata privacy), private writes (on-chain transaction privacy), and private proving (bridging Web2 data to Web3)
- Creating institutional-grade privacy solutions that meet regulatory compliance requirements
- Improving user experience to make privacy tools accessible to mainstream users
- Establishing standards and reference implementations through initiatives like the Kohaku SDK

The initiative comes at a critical juncture when privacy has emerged as the primary blocker preventing institutional adoption of public blockchains, surpassing even regulatory concerns. The timing coincides with increased market attention to privacy coins and growing recognition that blockchain's default transparency creates significant security, financial, and personal risks for users.

## Detailed Analysis

### The Privacy Cluster Initiative

The Privacy Cluster represents a focused reorganization of Ethereum Foundation's privacy efforts. According to Andy Guzman, PSE Lead at the Ethereum Foundation, the cluster is "this very focused effort on trying to make Ethereum more private, on bringing more and make it a default." The initiative involves increased resources, personnel, and coordination compared to previous efforts.

The cluster operates within a broader Ethereum Foundation restructuring that includes three main divisions: the protocol cluster (focused on Layer 1), the ecosystem development cluster, and the privacy cluster. This organizational structure reflects the foundation's recognition that privacy requires dedicated, coordinated attention rather than being treated as a secondary concern.

The Privacy Cluster was coordinated by Igor Baranov, founder of BlockScout and XTI, and brings together 47 specialists. Importantly, this initiative had been in development throughout 2025, particularly in the second half of the year, predating the market surge in privacy coin interest that began with Zcash in late September 2025.

### Common Misconceptions About Crypto Privacy

A fundamental challenge addressed by the Privacy Cluster is widespread misunderstanding about blockchain privacy. Andy Guzman emphasized: "One of the misconceptions that many people have even just like starting in the space is like thinking that by default crypto is private, which is not or it's anonymous and it's not right. It's pseudonymous."

The reality is that transactions on public blockchains like Ethereum and Bitcoin are recorded permanently and transparently. This creates multiple risk categories:

- **Legal risks**: Permanent records of all transactions can create future legal exposure
- **Personal security risks**: Address linkage to real-world identities enables targeted attacks
- **Financial risks**: Complete transaction history visibility allows front-running and exploitation

Guzman noted: "Whenever you do an action on blockchains like Ethereum or Bitcoin or most of the other public blockchains, those actions get recorded forever. And that could be like legal real show that could be personal risk, that could be like financial risk as well. Just leaking all your information and storing it that in a blockchain where you cannot delete it, you cannot edit it."

### Evolution of Privacy Stewards of Ethereum (PSE)

PSE has a rich history dating back to 2018-2019, when it began as a small group of cryptographers and researchers exploring zero-knowledge proofs. The team grew from a handful of researchers to 50-60 people at its peak, pioneering multiple critical technologies:

- **Early rollup exploration**: PSE was among the first teams exploring rollups as a scaling solution
- **ZK-EVM development**: The team included pioneers in zero-knowledge Ethereum Virtual Machines
- **TLS Notary support**: PSE supported development of TLS Notary, pioneering ZK-TLS technology
- **Privacy and identity primitives**: Development of systems for proving identity without revealing personal details

Historically, PSE operated somewhat independently from the Ethereum Foundation, exploring use cases broadly across both privacy and scalability. The 2025 restructuring brought PSE fully into the foundation and refocused it exclusively on privacy for Ethereum, rather than general privacy research.

Oskar Thorén explained the shift: "What is new this year is that it sort of focuses mission a little bit and focusing on privacy on Ethereum specifically and not sort of privacy broadly in sort of the ecosystem. So I think that is the main shift."

### Institutional Privacy Task Force (IPTF)

The IPTF represents a new initiative, formed only 2-3 months before the interview (approximately August-September 2025). Oskar Thorén, Technical Lead of IPTF, described its mission: "Basically what we're trying to do is we're trying to get institutions to build on top of public blockchains like Ethereum specifically, with the focus on solving their privacy Requirements."

The formation of IPTF reflects a critical market insight: privacy has become the primary blocker for institutional adoption. Thorén stated: "It used to be that regulation was the primary blocker but nowadays, or especially this year and the last few years, privacy is actually the main blocker in terms of these institutions moving on-chain."

**IPTF's approach involves:**

1. **Requirements gathering**: Engaging with major financial institutions to document specific business and privacy needs
2. **Mapping exercises**: Connecting institutional requirements to existing Ethereum ecosystem solutions
3. **Vendor neutrality**: Maintaining credible neutrality by not favoring specific vendors while helping institutions navigate options
4. **Legal framework analysis**: Understanding how different regulatory jurisdictions (US, Europe, Japan, Singapore, Hong Kong) affect privacy requirements
5. **Translation services**: Converting business requirements into technical specifications that developers can implement

The team includes members with extensive financial industry experience, including former Goldman Sachs employees, combined with protocol researchers and cryptographers. This blend enables effective communication between institutional stakeholders and the technical community.

### Why Privacy Matters in Crypto

The guests articulated multiple dimensions of why privacy is essential for cryptocurrency adoption:

**Individual User Protection:**
Privacy protects users from various attack vectors. Thorén cited real-world examples: "When addresses got leaked, it had like very real world consequences in terms of like, people's address being leaked, and that was like led attacks or physical attacks." He referenced "wrench attacks" in Paris and Miami as concrete examples of how blockchain transparency creates physical security risks.

**Cash-like Properties:**
Thorén drew parallels to traditional cash: "If I buy a coffee here, they can't see my entire sort of my income or my assets. I just, all they know is like bearer asset like cash." Public blockchains lack this fundamental privacy property, exposing users' complete financial histories with every transaction.

**Geographic Disparities:**
While privacy may seem less critical in developed countries like the US and Sweden, Thorén noted: "In lots of parts of the world, there are more adversarial circumstances where it matters a lot more. And I think as the world is moving more towards usage of blockchain technology, even you see attacks in Paris and Miami, it's very much a real problem."

**Institutional Requirements:**
For institutions, privacy is a "table stakes requirement," according to Guzman. Without privacy, institutions either fail to meet regulatory requirements or face unacceptable business risks, including loss of competitive advantage through transaction visibility and client data exposure.

**Philosophical Alignment:**
Privacy connects to crypto's cypherpunk origins and core values of self-sovereignty and freedom. Guzman emphasized: "All this cypherpunk movement, all this like start of this industry came from self-suffering individuals and had like really strong ties to privacy technology in itself."

### Technical Approaches to Privacy

The Privacy Cluster works across multiple technical dimensions, each addressing different aspects of privacy:

**Private Reads (Metadata Privacy):**
Guzman explained: "Private reads, I would say, is all this privacy that you want to ensure whenever you query the blockchain. So whenever you read the blockchain, so if this was a book, you don't want people to know which pages you are reading particularly or which sentences because you might leak information about who you are and what you are interested or what are your intentions."

This addresses the problem that even querying blockchain data can reveal user interests and intentions, creating metadata that can be exploited.

**Private Writes (On-Chain Privacy):**
This encompasses privacy for all on-chain actions: "Whenever you take an action like, you know, writing or whenever you do any action on the chain, right? So things like voting, things like delegating, things like purchasing NFTs, tokens, things like doing transactions, things like DeFi. All of these will have your actions recorded forever."

Private writes ensure that transactions cannot be linked back to specific addresses or identities, protecting users from permanent exposure.

**Private Proving:**
This involves technologies that allow users to prove facts about Web2 data without revealing the underlying information. Guzman provided examples: "If you have a driver's license, if you have a bank account and you want to prove that you have more than a certain amount of funds in your bank account, you can already prove this with technologies that we're developing."

This bridges the gap between traditional systems and blockchain, enabling verification without data exposure.

**Technology Families:**

The guests outlined several cryptographic primitive families:

- **Zero-knowledge proofs**: Allowing proof of statements without revealing underlying data
- **Multi-party computation (MPC)**: Enabling collaborative computation without exposing individual inputs
- **Fully homomorphic encryption (FHE)**: Operating on encrypted data without decryption
- **Trusted Execution Environments (TEEs)**: Hardware-based privacy guarantees

**Trade-off Considerations:**

Guzman outlined key trade-off dimensions:

- **Cost**: Transaction fees for privacy-preserving operations
- **Speed**: Time required to generate proofs or complete private transactions
- **User experience**: Complexity of using privacy tools
- **Trust assumptions**: Number of parties that must collude to break privacy
- **Hardware requirements**: Whether solutions run on mobile devices or require specialized infrastructure

Different use cases require different trade-offs. High-net-worth transactions might prioritize maximum privacy despite higher costs, while daily payments might favor speed and low cost over extreme privacy guarantees.

### Private Identities and Zero-Knowledge Proofs

Private identity represents a major application area for zero-knowledge technology. The challenge is enabling users to prove specific facts about themselves (age, residency, nationality) without revealing complete personal information.

**Current Problems:**
Traditional KYC (Know Your Customer) processes require users to share complete identity documents with every service provider, creating multiple risks:
- Data breach exposure at each provider
- Identity theft vulnerability
- Unnecessary data collection
- Permanent records of sensitive information

**Zero-Knowledge Solutions:**
ZK proofs enable selective disclosure. As Guzman explained: "How can I make zero knowledge proofs in particular and prove specific facts about me without disclosing all this information, without me having to send the document, the picture on everything, right?"

**Implementation Approaches:**

The team distinguishes between "Brownfield" and "Greenfield" implementations:

**Brownfield (Retrofitting Existing Systems):**
Many countries already have digital identity systems. India's Aadhaar system serves 1.3 billion users. Projects like AnonAadhaar retrofit zero-knowledge proofs onto existing infrastructure, allowing users to prove identity facts without exposing complete records.

**Greenfield (Building from Scratch):**
The Kingdom of Bhutan provides a notable example, building their digital identity system directly on Ethereum. Guzman described it as "trying to provide the most secure, most sovereign digital identities to their citizens. And they built their digital identity system on top of Ethereum."

Ethereum serves as a trusted registry where cryptographic keys can be verified as legitimate government-issued credentials, while actual identity data remains with users on their personal devices.

**Security Mechanisms:**

To address concerns about stolen or compromised identities, the system employs multiple safeguards:

1. **Revocation lists**: Stolen credentials can be reported and added to revocation lists, causing verification checks to fail
2. **Expiration dates**: Credentials have limited validity periods, requiring periodic renewal
3. **Liveness checks**: Systems can verify that the person presenting a credential is the legitimate holder
4. **Short-lived proofs**: Single-use or time-limited proofs reduce exposure windows

**Industry Adoption:**
Major technology companies are moving in this direction. Guzman noted: "Google also released their own stack a few months ago, earlier this year. And I know Microsoft as well. So there's a trend, right? There's a real need about having strong privacy-preserving digital identity systems."

### Privacy User Experience

Privacy has historically been difficult for average users to understand and implement. The Privacy Experience initiative addresses this adoption barrier.

**Current Challenges:**
Guzman identified the core problem: "Historically, privacy has been a very difficult topic to use for end user, for normal person in the street, like just trying to learn how to use these systems, how to keep your keys secure, how to not leak information."

The complexity extends beyond technical implementation to conceptual understanding. Users must grasp:
- Different privacy guarantees and their trade-offs
- Security implications of various choices
- Proper key management
- When and how to use privacy tools

**Improvement Strategies:**

The initiative focuses on multiple dimensions:

1. **Terminology standardization**: Creating consistent, understandable language for privacy concepts
2. **Visual indicators**: Developing icons and visual cues that communicate privacy properties quickly
3. **Education**: Building literacy around privacy concepts and best practices
4. **Simplified interfaces**: Reducing complexity without compromising security

Thorén emphasized the disconnect between technical and user communities: "There's like a certain language that people, how people talk about these things, and that's disconnected from how normal people live their lives. And you're trying to sort of make that connection."

**Key Management Evolution:**

Thorén highlighted significant progress in key management UX: "It used to be that because so much of this was like cutting edge research...it was a bit hard and you had things like hardware wallets but now the ux is improving more and more so for example you can tie it to your device so you use kind of face id and pass keys."

Modern solutions include:
- Device-based authentication (Face ID, biometrics)
- Multi-signature wallets
- Time-locked recovery mechanisms
- Social key recovery (requiring multiple trusted contacts to attest identity)

This evolution makes self-sovereign key management accessible to non-technical users while maintaining security.

### The Kohaku SDK

Kohaku represents a practical implementation strategy for accelerating privacy adoption across the Ethereum ecosystem. Guzman described it as "this good effort to try to bring privacy to wallets and make it much easier for wallets to adopt."

**Core Concept:**
Kohaku is a reference implementation and software development kit (SDK) that packages multiple privacy protocols into an easily integrable format. Rather than each wallet developer needing to understand and implement complex privacy primitives independently, they can integrate Kohaku as a complete solution.

**Strategic Rationale:**
The Ethereum Foundation's role is not to compete with wallet providers but to enable them. Guzman explained: "The intention would not be to for the Ethereum Foundation to run, you know, a wallet and try to get end users and try to get adoption, because that's much rather something that we would like the ecosystem to run and do business with."

**Value Propositions:**

1. **Reduced Integration Complexity**: Thorén noted that privacy tools require "specific expertise" and "it's not always easy to do that." Kohaku provides working examples and integration patterns.

2. **Demonstration of Possibilities**: By showing how different privacy primitives work together, Kohaku helps developers understand what's achievable and how components combine.

3. **Standards Promotion**: Kohaku establishes reference implementations that can become de facto standards across the ecosystem.

4. **Ecosystem Coordination**: It provides a focal point for collaboration between privacy researchers, protocol developers, and application builders.

Thorén emphasized the educational value: "What Kohaku is also doing is showing how you can do it, it's showing examples of it...there's all these amazing resources and open source products and so on that exist in the space but it's not always obvious to people like how do you put them together."

### Relationship with Other Privacy Efforts

The Privacy Cluster exists within a rich ecosystem of existing privacy initiatives, both within Ethereum and in other blockchain ecosystems.

**Relationship with Zcash:**

The guests emphasized philosophical alignment and collaboration rather than competition. Thorén stated: "Zcash and Ethereum are very much philosophically aligned. And the communities, especially this privacy part of the Ethereum community...it's like a lot of collaboration in terms of actual code and research and so on."

The two ecosystems have taken different developmental paths:
- **Zcash approach**: Privacy first, then usability, then scaling
- **Ethereum approach**: Decentralization first, then usability and scaling, now privacy

Guzman noted: "There's a lot of things that we can learn from the Zcash ecosystem. There's a lot of things that now they will want to learn from us as well. How do they scale and how do they bring usability from like the layer-centric roadmaps."

Both guests emphasized that the privacy market is large enough for multiple approaches, with the real competition being traditional Web2 systems rather than other crypto projects.

**Ethereum Layer 2 Privacy Solutions:**

Multiple Layer 2 solutions focus on privacy, including Aztec's new Ignition chain and StarkNet. The Privacy Cluster views these as complementary rather than competitive.

Guzman explained the Layer 2 advantage: "Layer 2s continues to be key for the Ethereum scaling roadmap...Layer 2s would always have an advantage in terms of innovation, just because they're smaller, they're more concentrated teams. They can't just stop and start a new, even from scratch, architecture."

The relationship is symbiotic:
- Layer 2s can experiment with novel privacy architectures
- Layer 1 privacy provides baseline guarantees for all users
- Both benefit from shared research and primitive development

**Coordination Role:**

The Ethereum Foundation acts as a coordinator and neutral party. Guzman provided an example: "There are 20-something, 30-something teams building zero-knowledge virtual machines, CKVMs, and in a way, they all claim that theirs are the best and the fastest or the most scalable."

The foundation's role includes:
- Benchmarking different approaches objectively
- Identifying overlooked areas needing development
- Facilitating collaboration between teams
- Providing neutral guidance to institutions evaluating options

Thorén emphasized: "EF tends to take a more subjective approach. So if the ecosystem is solving a problem, there's no need for us to meddle with it. We're trying to work on the things that are overlooked."

### Regulatory Considerations

The regulatory landscape significantly shapes privacy development, particularly following the Tornado Cash sanctions in 2022.

**Tornado Cash Impact:**

The OFAC sanctions against Tornado Cash created widespread uncertainty and "chilling effects" across the ecosystem. Thorén recalled: "At the time I was running an R&D lab and we had researchers working on similar types of protocols. And it definitely had a chilling effect. People were afraid of working on certain technology."

However, the incident also catalyzed important conversations. Guzman noted: "There was also good understandings and maturation and even conversation that sparked of what does privacy protocols that can also be compliant looks like in the future."

**Spectrum of Approaches:**

The guests acknowledged that privacy solutions exist on a spectrum from maximally compliant to maximally permissionless. Guzman stated: "There is a spectrum, right? And from one side, it's like the most compliant, the most like government, the most like, you know, practical or responsible privacy. And on the other side is like the most cypherpunk, the most permissionless."

Ethereum's credible neutrality allows both approaches to coexist: "In a permissionless layer, anybody can build anything at the end of the day. So as Oscar was saying, both will coexist."

**Compliance Mechanisms:**

For institutions requiring regulatory compliance, several design patterns enable privacy with accountability:

1. **Viewing keys**: Designated parties (auditors, regulators) can access specific transaction details
2. **Audit logs**: Selective disclosure mechanisms for compliance purposes
3. **Time-delayed access**: Regulators gain access after specified periods
4. **Threshold access**: Multiple parties must collaborate to access private data

**Self-Regulation Approaches:**

The ecosystem is exploring mechanisms to address illicit activity concerns:

- **Allow/deny lists**: Addresses suspected of illicit activity could be flagged
- **Zero-knowledge KYC**: Users prove compliance without revealing identity
- **Know Your Transaction (KYT)**: Risk scoring for transactions without full transparency
- **Compliance attestations**: Proving adherence to regulations without exposing business logic

**Jurisdictional Variations:**

Privacy requirements vary significantly across jurisdictions. The IPTF specifically addresses this by mapping requirements for different regulatory environments (US, Europe, Japan, Singapore, Hong Kong) and connecting them to appropriate technical solutions.

**Ethereum Foundation's Position:**

The foundation maintains a research and development focus rather than operating production systems. Thorén explained: "The way EF thinks about it is that we are more, I guess, on the R&D side of things. We're not necessarily running things in production. That's not our role. We're trying to facilitate and enable that."

This positioning allows the foundation to explore privacy technologies while individual projects make their own choices about compliance approaches.

**Evolving Landscape:**

The regulatory environment continues to evolve. Recent developments include:
- Stablecoin Act progress in the US
- MiCA implementation in Europe
- Clarity emerging in Japan, Hong Kong, and Singapore

Thorén noted: "We're in a much better spot now than we were a few years ago. There's definitely like a lot of work to be done on the policy side and so on. So it's definitely not a work in progress...but for example things like stable coins and so on now there's at least some kind of regulatory clarity."

## Key Insights and Implications

### Privacy as Infrastructure, Not Feature

The Privacy Cluster represents a fundamental shift in how Ethereum approaches privacy—from optional add-on to core infrastructure. This mirrors the evolution of HTTPS on the internet, which Thorén referenced: "Eventually everyone goes, oh, it's actually a great idea. We want HTTPS because that's how you do payments online. Otherwise you can't buy something from Amazon."

### Institutional Adoption Depends on Privacy

A critical insight is that privacy has surpassed regulation as the primary blocker for institutional adoption. This represents a significant market signal that privacy solutions are not merely ideological but economically necessary for Ethereum's growth.

### Technology Maturity Enables New Possibilities

The timing of the Privacy Cluster reflects genuine technological maturity rather than market opportunism. Zero-knowledge proofs, multi-party computation, and related technologies have evolved from research curiosities to production-ready tools. This maturity enables use cases that were impossible just a few years ago.

### Complementary Rather Than Competitive Ecosystem

The relationship between Ethereum's privacy efforts and other privacy-focused projects (Zcash, Aztec, etc.) is fundamentally collaborative. The market is large enough that different approaches serve different needs, and shared research benefits all participants.

### User Experience as Critical Bottleneck

Technical capability alone is insufficient for adoption. The Privacy Experience initiative recognizes that privacy tools must be accessible to non-technical users to achieve mainstream adoption. This represents a maturation from pure research focus to product thinking.

### Regulatory Compliance and Privacy Can Coexist

The institutional privacy work demonstrates that privacy and regulatory compliance are not mutually exclusive. Through careful design (viewing keys, audit mechanisms, selective disclosure), systems can provide strong privacy guarantees while meeting institutional requirements.

### Ethereum's Neutral Infrastructure Advantage

Ethereum's credible neutrality allows it to serve both cypherpunk and institutional use cases simultaneously. This positions Ethereum uniquely compared to privacy-specific chains or permissioned systems.

### Privacy Enables New Use Cases

Beyond protecting existing activities, privacy unlocks entirely new applications. The guests mentioned voting systems, reputation mechanisms, and institutional DeFi as examples that become viable only with adequate privacy guarantees.

## Definitions and Terminology

**Zero-Knowledge Proofs (ZK Proofs)**: Cryptographic methods that allow one party to prove to another that a statement is true without revealing any information beyond the validity of the statement itself.

**Pseudonymous**: A system where users operate under persistent identifiers (addresses) that are not directly linked to real-world identities but can potentially be linked through analysis. Distinct from anonymous (no identifier) or private (identifier cannot be linked).

**Private Reads**: Privacy protections for querying blockchain data, preventing observers from determining what information a user is accessing (metadata privacy).

**Private Writes**: Privacy protections for on-chain transactions and actions, preventing observers from linking transactions to specific users or addresses.

**Private Proving**: Technologies that enable users to create cryptographic proofs about data from traditional (Web2) systems without revealing the underlying data.

**ZK-EVM (Zero-Knowledge Ethereum Virtual Machine)**: An implementation of the Ethereum Virtual Machine that can generate zero-knowledge proofs of computation, enabling private or scalable execution of smart contracts.

**ZK-TLS (Zero-Knowledge Transport Layer Security)**: Technology that allows users to prove facts about encrypted web connections (like proving you accessed a specific website or that a website returned specific data) without revealing the full content.

**Multi-Party Computation (MPC)**: Cryptographic protocols that enable multiple parties to jointly compute a function over their inputs while keeping those inputs private.

**Fully Homomorphic Encryption (FHE)**: Encryption schemes that allow computation on encrypted data without decrypting it, enabling privacy-preserving computation on servers.

**Trusted Execution Environment (TEE)**: Hardware-based security features that provide isolated execution environments, protecting code and data from external access even by privileged system software.

**Credibly Neutral**: A system or platform that demonstrably does not favor any particular participant or use case, enabling diverse applications to coexist.

**Layer 2 (L2)**: Scaling solutions built on top of Ethereum's base layer (Layer 1) that process transactions off the main chain while inheriting Ethereum's security guarantees.

**Revocation List**: A list of credentials or identities that have been invalidated (due to loss, theft, or expiration), checked during verification to ensure credentials remain valid.

**Viewing Keys**: Cryptographic keys that allow designated parties to view private transaction details without having the ability to spend funds or modify transactions.

**KYC (Know Your Customer)**: Regulatory requirements for financial institutions to verify customer identities, traditionally requiring collection of personal information.

**KYT (Know Your Transaction)**: Risk assessment of transactions based on their characteristics and history, used for compliance and fraud prevention.

**Brownfield Implementation**: Retrofitting new technology onto existing systems and infrastructure.

**Greenfield Implementation**: Building new systems from scratch without constraints from existing infrastructure.

**Wrench Attack**: Physical coercion or violence used to force cryptocurrency holders to transfer their assets, enabled by knowledge of their holdings through blockchain analysis.

## References and Citations

### Direct Quotations

**On crypto privacy misconceptions:**
> "One of the misconceptions that many people have even just like starting in the space is like thinking that by default crypto is private, which is not or it's anonymous and it's not right. It's pseudonymous." - Andy Guzman

**On institutional privacy needs:**
> "It used to be that regulation was the primary blocker but nowadays, or especially this year and the last few years, privacy is actually the main blocker in terms of these institutions moving on-chain." - Oskar Thorén

**On PSE's evolution:**
> "What is new this year is that it sort of focuses mission a little bit and focusing on privacy on Ethereum specifically and not sort of privacy broadly in sort of the ecosystem." - Oskar Thorén

**On privacy as table stakes:**
> "It's a table stakes requirement for institutions where if they don't, either they don't meet regulation or there's, like, big financial or business risk, right, of losing all their practice at their client." - Andy Guzman

**On Ethereum-Zcash relationship:**
> "Zcash and Ethereum are very much philosophically aligned. And the communities, especially this privacy part of the Ethereum community...it's like a lot of collaboration in terms of actual code and research and so on." - Oskar Thorén

**On the spectrum of privacy approaches:**
> "There is a spectrum, right? And from one side, it's like the most compliant, the most like government, the most like, you know, practical or responsible privacy. And on the other side is like the most cypherpunk, the most permissionless." - Andy Guzman

### Referenced Projects and Initiatives

- **Privacy Cluster**: Announced October 2025, coordinated by Igor Baranov
- **Privacy Stewards of Ethereum (PSE)**: Operating since 2018-2019
- **Institutional Privacy Task Force (IPTF)**: Formed approximately August-September 2025
- **Kohaku SDK**: Reference implementation for wallet privacy integration
- **AnonAadhaar**: Privacy-preserving implementation for India's Aadhaar identity system
- **Kingdom of Bhutan Digital Identity**: Ethereum-based national identity system
- **Aztec Ignition Chain**: Layer 2 privacy-focused blockchain
- **TLS Notary**: Pioneer in ZK-TLS technology

### Timeline References

- **2018-2019**: PSE begins operations exploring zero-knowledge proofs
- **2022**: Tornado Cash OFAC sanctions create regulatory uncertainty
- **Late September 2025**: Zcash experiences market resurgence
- **Early October 2025**: Ethereum Foundation announces Privacy Cluster
- **August-September 2025**: IPTF formation (approximately 2-3 months before interview)
- **November 2025**: Interview conducted at Ethereum DevConnect

### External Context

The episode references broader industry developments including:
- Google's release of privacy-preserving identity stack (2025)
- Microsoft's similar initiatives
- Regulatory developments: Stablecoin Act (US), MiCA (Europe)
- Regulatory clarity emerging in Japan, Hong Kong, and Singapore

### Podcast Information

- **Show**: Unchained
- **Host**: Laura Shin
- **Episode Number**: 959
- **Published**: November 25, 2025
- **Guests**: Andy Guzman (PSE Lead, Ethereum Foundation) and Oskar Thorén (Technical Lead, IPTF, Ethereum Foundation)
- **Sponsor**: Uniswap