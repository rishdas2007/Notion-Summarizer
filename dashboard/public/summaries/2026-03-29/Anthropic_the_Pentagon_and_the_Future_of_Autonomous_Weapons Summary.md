# Anthropic, the Pentagon, and the Future of Autonomous Weapons

**Citation:** "Anthropic, the Pentagon, and the Future of Autonomous Weapons." *Odd Lots*, 28 Mar. 2026, <https://omny.fm/shows/odd-lots/anthropic-the-pentagon-and-the-future-of-autonomous-weapons>.


## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Analysis](#detailed-analysis)
   - [The Anthropic-Pentagon Controversy](#the-anthropic-pentagon-controversy)
   - [Defining Autonomous Weapons: A Spectrum of Control](#defining-autonomous-weapons-a-spectrum-of-control)
   - [Current AI Applications in the Iran Conflict](#current-ai-applications-in-the-iran-conflict)
   - [The Human-in-the-Loop Problem](#the-human-in-the-loop-problem)
   - [Historical Context and Policy Development](#historical-context-and-policy-development)
   - [The Commercial-Military AI Divide](#the-commercial-military-ai-divide)
3. [Key Insights and Implications](#key-insights-and-implications)
4. [Definitions and Terminology](#definitions-and-terminology)
5. [References and Citations](#references-and-citations)

## Executive Summary

This podcast episode from Odd Lots, published March 28, 2026, examines the intersection of artificial intelligence and military applications through the lens of a recent controversy between Anthropic and the Pentagon. The discussion occurs against the backdrop of an ongoing war with Iran, where AI systems have reportedly been deployed in military operations.

The central tension explored is the disagreement between Anthropic and the Department of Defense regarding the use of AI models in "fully autonomous weapons or domestic surveillance." Despite this public dispute, reporting indicates that Anthropic's technology was utilized at the start of hostilities with Iran, raising critical questions about what constitutes autonomous weaponry, how AI is currently being used in warfare, and the ethical boundaries of such applications.

Guest Paul Scharre, executive vice president at the Center for a New American Security and author of two books on AI in warfare, provides expert analysis. Scharre previously worked inside the Department of Defense developing policy on autonomy in weapons systems around 2011, making him uniquely positioned to discuss both the technical and policy dimensions of autonomous weapons.

The episode reveals that current military AI applications exist on a spectrum rather than as binary autonomous/non-autonomous systems. AI is being used primarily for data processing, target identification through image classification, and planning support—with humans still making final targeting decisions. However, significant concerns emerge about whether human oversight remains meaningful when AI systems process vast amounts of data and generate recommendations that humans may simply "rubber stamp."

## Detailed Analysis

### The Anthropic-Pentagon Controversy

The episode opens by establishing the temporal context: just before the Iran war began, the dominant news story concerned the "collapse in the relationship between the Pentagon and Anthropic." Anthropic objected to potential use of its models in two specific areas:

1. Fully autonomous weapons systems
2. Domestic surveillance

This disagreement became immediately more relevant when the war started, as "reporting that Anthropic's technology was in fact utilized at the start of hostilities" emerged. The hosts note the irony that this was not a disagreement about AI use in war generally, but specifically about "the degree to which AI could be used for autonomous weapon systems on their own without a human in the loop."

The controversy highlights a fundamental tension between corporate AI developers and military applications. As Tracy Alloway notes, there are "questions over exactly how places like the Department of Defense, not only how they define it, but once they have those definitions, whether or not certain companies trust them to sort of stick to those policies."

Joe Weisenthal frames another dimension of the debate: "here's a technology and the government says, we believe that we can use this to make the country safer. What, you're not going to let us do it? Like private corporation, there's some very interesting questions about the role of corporate power vis-a-vis the government."

### Defining Autonomous Weapons: A Spectrum of Control

Paul Scharre addresses the definitional challenge directly: "there is not a unified definition that everyone agrees on. The Defense Department has their definition that's written in their policy." Conceptually, he defines an autonomous weapon as "a weapon that is choosing its own targets on the battlefield."

Critically, Scharre emphasizes this is "not where we are today. Right now today, people are choosing those targets. But it is kind of a spectrum because we do have examples of weapons that have some measure of autonomy."

He employs the self-driving car analogy to illustrate the spectrum:

> "A good analogy might be self-driving cars where conceptually, like, okay, a self-driving car would be where the AI is driving the car. But then you get into an actual car today, and a lot of them have intelligent cruise control, automatic braking, automated self-parking. They have all these like automated features that are kind of creeping you in this direction where the AI is taking over more and more control for what the vehicle can do. And it's actually a pretty similar thing in the military space as well."

Joe Weisenthal provides a concrete example of where autonomy seems acceptable: missile defense systems where human decision-making would be too slow. He suggests "everyone's probably OK with that level of autonomy," but notes that "a lot of this discussion, and maybe it's core to what Anthropic and the Department of Defense were disagreeing on, I have a feeling a lot of this is going to come down to definitions."

### Current AI Applications in the Iran Conflict

Scharre identifies two distinct categories of AI currently being used by the Pentagon in the Iran conflict:

**1. Narrow AI Systems (Image Classification)**

These systems have been operational for over a decade, originating with "the military's original Project Maven almost a decade ago where they took machine learning image classifiers to sift through drone video feeds and satellite images to identify objects. OK, here's a building, here's a person, here's a vehicle. That's pretty mature technology."

**2. Large Language Models and AI Agents**

More recently, and notably during the Iran conflict, the military has deployed LLMs including Anthropic's technology. Scharre explains: "in the midst of this huge, messy public breakup between Anthropic and the Pentagon, we found out that, in fact, Anthropic's AI tools are being used by the US military to help plan the war against Iran."

These tools serve a different function: "It's really helping intel analysts sift through just the massive amount of data that the U.S. Military has."

Scharre describes the operational challenge:

> "You can imagine the problem that the military is facing right now when they're looking at targets in Iran. U.S. Military has flown over 6,000 sorties against Iran. The Iranian military architecture is degraded in a lot of ways. U.S. Military has already bombed a lot of targets. There are mobile targets, senior Iranian commanders, mobile missile launchers, and air defense systems, and drone launchers. U.S. Military has got to bring all that information together and find out where are these targets right now and where is there an aircraft that has the right bombs on it to take these targets out."

**Integration Architecture**

The AI tools are integrated through "an existing system called the Maven Smart System, which is built by Palantir, and that fuses all this data together." This system brings together multiple data sources: "satellite imagery, geolocation data, signals intelligence, other forms of information."

LLMs function as an interface layer, allowing analysts to "task a large language model to say, okay, here's a bunch of data I'm giving you. I want you to look for a place where we have satellite imagery and some other forms of intelligence that can help identify the location of some missile launcher, for example."

Scharre emphasizes the human-directed nature of current usage: "the AI is definitely being used to help understand the battle space and to plan operations, but in, I would say, ways that are pretty narrowly directed by people. It's not quite as simple as dump all this data into a context window for LLM and then say, oh, AI, figure it out. People are asking the AI some really specific questions."

### The Human-in-the-Loop Problem

Tracy Alloway raises what Scharre later acknowledges as "a really important question": how meaningful is human oversight when AI systems process vast amounts of data and generate recommendations?

Alloway frames the concern: "I'm imagining if you're an intelligence officer and you're getting reams and reams of data from Iran and you ask the AI to pick out certain patterns or identify potential strategic targets, how much due diligence are you actually doing on what that model spits out? Because of course, the tendency when a lot of people use LLM certainly is just you accept what it shows you on the screen."

Scharre identifies this as "one of the possible failure modes, if you will, of AI and how we use it":

> "You could end up in a place where humans are nominally in the loop and you could say, well, it's not an autonomous weapon and humans making these decisions. But if the human is not meaningfully engaged and they're just kind of rubber stamping some kind of decision, then that's not really what we're looking for."

He notes this has been "a longstanding concern for many years about people worried about autonomous weapons. I think that's a very real risk with how AI is used."

**The School Bombing Incident**

Joe Weisenthal introduces a concrete example: "in the early days of the war, we hit that school." According to New York Times reporting, this resulted from "outdated data provided by the Defense Intelligence Agency."

Scharre provides analysis of this failure:

> "That school was a fixed object. And so that's likely something that should have clearly been much more vetted prior to the war kicking off, someone could have identified that that building that was struck had actually been at one point in time part of an Iranian military compound. But you could see based on publicly available satellite imagery that it had been moved out of that compound some time ago and had been converted to a school. And it would appear based on what's been reported in the Times that that information had never been updated in this DIA targeting database."

This incident highlights "this underlying challenge of how good is the data going into this AI system and how thoroughly are people vetting it." Scharre notes that while "in principle, AI might be able to help you with those things, but you've got to use it the right way and people still have to be meaningfully engaged in these decisions."

The incident raises questions about the scalability of human oversight: "when you're talking about thousands of targets, what's the degree of vetting that's gone into all of that information?"

### Historical Context and Policy Development

Scharre provides historical context for Pentagon policy on autonomous weapons, dating to his own work "around, say, 2011" when he "led an effort inside the Pentagon, when I worked at the Office of the Secretary of Defense, on developing the Pentagon's policy on the role of autonomy in weapons, the one that's still in effect today."

**The Accidental Robotics Revolution**

The impetus came from what Scharre calls "this accidental robotics revolution during the wars in Iraq and Afghanistan, where the military deployed thousands of air and ground robots, drones in the air and ground robots for diffusing bombs."

At that time, the technology was far more primitive: "the military had kind of woken up to" the potential but "we weren't at all where the military is now in terms of integrating AI tools. I mean, these types of large language models just didn't exist at the time."

The military began considering "having more autonomy in these systems, the ability to not be totally reliant on a human remotely controlling them, which was really the case at the time. But that raised all these obviously thorny questions about like, well, how much autonomy should they have? And what are the legal and ethical implications of that?"

This led to the policy directive still in effect today, though the technological landscape has evolved dramatically since its creation.

### The Commercial-Military AI Divide

Scharre identifies a fundamental structural difference between AI and traditional military technologies:

> "AI is really different than a lot of traditional military technologies because it's coming out of the commercial sector. So in a way, it's kind of like the opposite of stealth technology that was invented in secret defense labs and doesn't have a lot of commercial applications. AI is all of these different applications. It's not being invented by the military. The military is having to import it in."

**Historical Precedent: Project Maven and Google**

Tracy Alloway asks whether Scharre encountered contractor resistance during his Pentagon work. He responds that "not at that time," but notes that "later, after the U.S. Military launched Project Maven, there was a big dust up when it came out publicly that Google had been a part of Project Maven and a number of Google employees signed an open letter protesting that. And Google eventually discontinued their work on Project Maven."

This establishes a pattern: "there are certainly some similarities in terms of a disconnect between how some people in the AI community are thinking about how their technology ought to be used in war and how the military is thinking about it."

The episode characterizes this as "a pivotal point in, I guess, the history of the military-industrial complex," where commercial AI companies with broad societal applications must navigate ethical questions about military use that traditional defense contractors never faced.

## Key Insights and Implications

1. **Definitional Ambiguity as Strategic Challenge**: The lack of unified definitions for "autonomous weapons" creates space for both policy disagreement and potential mission creep. What constitutes meaningful human control remains contested, allowing for gradual expansion of AI decision-making authority.

2. **The Rubber Stamp Problem**: The most significant near-term risk may not be fully autonomous weapons but rather nominally human-controlled systems where AI recommendations are accepted without adequate scrutiny due to data volume and complexity. This represents a de facto autonomy that maintains the appearance of human oversight.

3. **Data Quality as Critical Vulnerability**: The school bombing incident reveals that AI systems amplify rather than mitigate data quality problems. Outdated or incorrect information in databases becomes operationalized through AI-assisted targeting, with potentially catastrophic consequences.

4. **Commercial-Military Tension**: The commercial origins of AI technology create unprecedented friction in the military-industrial complex. Unlike purpose-built military technologies, AI companies serve broad civilian markets and face employee and public pressure regarding military applications.

5. **Scale and Speed Pressures**: The operational context described—6,000+ sorties, mobile targets, degraded enemy infrastructure—creates enormous pressure to process information quickly. This pressure inherently favors increased automation and may erode meaningful human oversight over time.

6. **Policy Lag**: Current Pentagon policy on autonomous weapons dates to 2011, developed in a pre-LLM era. The technological capabilities have evolved far beyond the policy framework designed to govern them.

7. **Spectrum Rather Than Binary**: The self-driving car analogy effectively illustrates that autonomy exists on a continuum. Military systems are accumulating autonomous features incrementally, making it difficult to identify a clear threshold where a system becomes "autonomous."

## Definitions and Terminology

**Autonomous Weapon**: According to Scharre, conceptually "a weapon that is choosing its own targets on the battlefield." The Defense Department has its own formal definition in policy, but no universally agreed-upon definition exists.

**Project Maven**: The U.S. military's original initiative (approximately a decade old as of 2026) to apply machine learning image classifiers to drone video feeds and satellite imagery for object identification. This project became controversial when Google's involvement became public, leading to employee protests and Google's withdrawal.

**Maven Smart System**: Built by Palantir, this is the existing data fusion architecture that integrates multiple intelligence sources (satellite imagery, geolocation data, signals intelligence) and now incorporates LLM interfaces for analyst interaction.

**Human-in-the-Loop**: A system design where humans maintain decision-making authority, particularly for critical functions like target selection. The meaningful implementation of this concept is contested, as humans may nominally be "in the loop" while effectively rubber-stamping AI recommendations.

**Sortie**: A military term for a single aircraft mission or deployment. The episode references over 6,000 sorties flown against Iran.

**Large Language Models (LLMs)**: AI systems like Anthropic's Claude that can process natural language queries and interact with large datasets. In military applications, these serve as interfaces between analysts and complex data fusion systems.

**Narrow AI**: Specialized AI systems designed for specific tasks, such as image classification, as opposed to general-purpose AI systems.

**DIA (Defense Intelligence Agency)**: The U.S. military intelligence agency responsible for maintaining targeting databases, implicated in the school bombing incident due to outdated data.

## References and Citations

**Publication Details**:
- **Title**: Anthropic, the Pentagon, and the Future of Autonomous Weapons
- **Published**: 2026-03-28T08:00:00.000+00:00
- **Show**: Odd Lots
- **Hosts**: Joe Weisenthal and Tracy Alloway
- **Guest**: Paul Scharre, Executive Vice President and Director of Studies, Center for a New American Security

**Paul Scharre's Credentials and Works**:
- Author of *Four Battlegrounds: Power in the Age of Artificial Intelligence* (most recent)
- Author of *Army of None: Autonomous Weapons and the Future of War*
- Former Office of the Secretary of Defense (led autonomy policy development circa 2011)
- Former Army Ranger

**Key Quotations**:

On defining autonomous weapons: "I think conceptually, I think the distinction really is a weapon that is choosing its own targets on the battlefield. And it's not where we are today. Right now today, people are choosing those targets."

On current AI usage: "The AI is definitely being used to help understand the battle space and to plan operations, but in, I would say, ways that are pretty narrowly directed by people."

On the rubber stamp problem: "You could end up in a place where humans are nominally in the loop and you could say, well, it's not an autonomous weapon and humans making these decisions. But if the human is not meaningfully engaged and they're just kind of rubber stamping some kind of decision, then that's not really what we're looking for."

On AI's commercial origins: "AI is really different than a lot of traditional military technologies because it's coming out of the commercial sector... it's kind of like the opposite of stealth technology that was invented in secret defense labs and doesn't have a lot of commercial applications."

**External References**:
- New York Times reporting on the school bombing incident (specific article not cited in transcript)
- Pentagon policy directive on autonomy in weapons (developed circa 2011, still in effect as of 2026)
- Google's withdrawal from Project Maven following employee protests

**Operational Context**:
- Over 6,000 sorties flown against Iran as of the recording date (March 24, 2026)
- Anthropic's technology confirmed to be in use despite public disagreement with Pentagon
- Integration through Palantir's Maven Smart System