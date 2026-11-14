---
title: Project Strands
---
# Project Strands
## Overview

Your final project should aim to answer a research question from a real world dataset. The following strands are inspired by Seattle-area community organizations that have sat down with us and described problems that they cannot currently solve. You are not required to select from these strands, instead they are meant to provide ideas for students who may want to use their final project to tackle a Seattle-area community based problem.

Problems they have described include: a senior services provider whose participants share a room but not a language and often face more than one barrier to the services they need, a refugee and immigrant services agency trying to understand a population that shifts with every change in federal policy, a marine mammal rescue organization with four hundred people on a volunteer waitlist and an empty Wednesday night shift, a residential care facility matching volunteer capabilities to resident needs, and a community development authority that wants to know whether Seattle's policies compare favorably to peer cities.

None of these organizations has a data analyst. Each of them has data.

This document describes five **project strands** built from those conversations. You can choose one, develop your own research questions within it, and complete the standard project sequence — proposal, EDA, report, presentation. The notebook requirements do not change. What changes is that at the end, someone outside this course might actually use what you found.

---

## What makes these projects hard in an interesting way

Every strand shares a property that ordinary practice datasets lack: **the data was produced by an organization for its own purposes, under constraints you will have to reconstruct.**

A Kaggle dataset arrives scrubbed of its origins. A volunteer sign-in log does not. It reflects who the organization recruited, what its shift schedule looked like that year, which policies were in force when, and what the person entering the data thought was worth recording. Yanni Loukissas calls this a **data setting** — the local, situated conditions under which data comes into being. We will spend a lecture on it (Oct 21), and in this project it is not a framing exercise. It is a source of findings.

In each strand below, we name a specific provenance question that we already suspect matters. Answering it is part of the work.

---

## The strands

### Strand A — SCIDpda: Open data and policy comparison

**Partner context.** The Seattle Chinatown International District Preservation and Development Authority works on housing, small business support, and neighborhood preservation in the CID. We have not yet met with SCIDpda directly, which makes this the most open strand — treat the framing below as a starting hypothesis rather than a commission, and expect to define the specific policy domain yourself.

**Anchoring question.** How do Seattle's policies in a chosen domain — small business displacement, cultural district designation, affordable housing production, street use permitting — compare to peer cities, and what do open data records suggest about their effects?

**Data landscape.** Seattle Open Data (`data.seattle.gov`), Seattle City Council legislative records, equivalent open data portals for comparison cities (Portland, Oakland, San Francisco, Boston, Chicago), ACS demographic tables for normalization, and city GIS boundary files.

**Named provenance question.** *Cross-city comparison is where provenance bites hardest.* Two cities recording "small business" are rarely recording the same thing — different thresholds, different NAICS groupings, different update cadences, different definitions of what counts as a closure. Your comparison is only as good as your account of where the categories diverge. Document the divergences; do not smooth them over.

**Challenge goal fit.** **Multiple Datasets** is nearly automatic here. **Messy Data** if you scrape or use an API for legislative records. **Result Validity** if you test whether a difference between cities is distinguishable from noise.

**Scope warning.** Do not attempt to establish that a policy *caused* an outcome. You do not have the design for it. Describe, compare, and be explicit about what a difference between cities can and cannot tell you.

---

### Strand B — Sound Generations: Where language and access barriers overlap

**Partner context.** Sound Generations serves older adults across King County, a linguistically diverse population in which many people face language barriers and access barriers at the same time. In our listening session, staff described participants who want to talk with one another but can't, because language differences are compounded by widespread hearing loss. Since then, funding for some health programming, including blood pressure checks, has been cut, and the services that replaced it increasingly require medical insurance; Sound Generations provides translation and navigation to keep them reachable. Staff have also raised audiology and hearing services as a specific need. Because its programs are free, Sound Generations keeps almost no record of who participates or where they live, which is why this strand runs on public data plus the partner's own list of sites.

We offered Sound Generations three possible directions. They chose this one: data that helps them understand where language and access barriers overlap. Everyone in this strand works on some version of that question.

**Anchoring question.** Where in King County do language barriers and access barriers overlap for older adults, and how does that geography compare to where language-matched programming and relevant services are located?

**Making it yours.** Everyone in this strand shares a question, so what distinguishes your project is how you cut it. Three choices define a cut.

*Which access barrier.* "Access" is broad. Public data measures hearing difficulty, insurance coverage, vehicle access, and poverty by age, all at the tract level. Hearing connects most directly to what staff raised. Choose one or two barriers and justify the choice in your Motivation.

*Which languages.* Participants speak many languages, and the only census table that separates out older adults sorts them into four broad groups (see below). If you speak a language participants speak, or know a particular community well — where people gather, which organizations they trust, which neighborhoods they have moved to or from — that knowledge is a legitimate basis for your cut. It is also exactly what will distinguish your project at panels.

*Which services.* Sound Generations' own sites, audiology and hearing providers, or other services the partner's navigation work connects people to.

**Data landscape.** American Community Survey 5-year estimates at the census tract level, from data.census.gov or the Census Data API, which requires a free key. Request one before you need it.

- `B16004`: age by language spoken at home by ability to speak English. The only language table that separates out adults 65 and older, and it sorts languages into four groups: Spanish, other Indo-European, Asian and Pacific Island, and all other languages.
- `C16001`: language spoken at home, with twelve language categories (Chinese, Vietnamese, Korean, Tagalog, and Arabic among them), but for all ages combined.
- `B18102`: hearing difficulty by sex and age, with bands for 65–74 and 75 and over.
- `B27010`: types of health insurance coverage by age. Use `B27001` if you need the 55–64 band.
- `B25045`: vehicles available by age of householder.
- `B17020`: poverty status by age.

Beyond those: the ACS Public Use Microdata Sample (PUMS) for person-level records (see the provenance question below; PUMA boundaries were redrawn and first used in 2022 data, so a multi-year file can span both versions); 2020 TIGER/Line tract boundaries for King County; Sound Generations' site list with languages offered, supplied once by the partner and shared across the strand; provider locations from the CMS NPI Registry API, where audiologists are taxonomy code `231H00000X` and addresses need geocoding; and King County Metro's published transit data if you want reachability rather than straight-line distance.

**Named provenance question.** *Overlap on a map is not overlap in a person.* The Census Bureau publishes small-area data only as separate tallies: this many older adults in a tract speak English less than "very well," this many have hearing difficulty. Person-level records, where you could see one person facing both barriers, are published only for Public Use Microdata Areas of at least 100,000 people. That is a privacy decision. The Bureau trades geographic resolution for protection against identifying individuals, and the trade determines what can be known. A tract-level map can show that barriers co-locate. It cannot show that they fall on the same people, and a tract can rank high on both measures while the two barriers belong to entirely different residents. Sound Generations asked where barriers overlap, so your answer has to say which kind of overlap it shows. The strongest projects will compute both, co-location across tracts and person-level overlap from PUMS for the same part of the county, and report where the two pictures disagree.

**What else the tables hide.** Three more places to look. None is required, and any of them could become your provenance finding.

*What the language question records.* The ACS asks about each person's language, but one household member usually fills out the form for everyone, so an older adult's English ability is often reported by a child or grandchild. People who speak several non-English languages can write in more than one, but the Bureau processes only the first ([Mejia, 2026](https://www.census.gov/library/working-papers/2026/demo/sehsd-wp2026-02.html)). Limited English proficiency is a line drawn by convention at speaking English less than "very well." The categories flatten, too. At the tract level, Somali, Amharic, Tigrinya, and Oromo have no category of their own; they fall into "other" in both `B16004` and `C16001`, and the detailed table that names more languages, `B16001`, is not published for tracts or counties. That matters in King County, home to established Somali- and Amharic-speaking communities. Finally, the household-level measure counts a household as limited English speaking only when no one 14 or older speaks English very well, so a monolingual Cantonese-speaking grandmother living with an adult grandchild who speaks English very well appears in `B16004` and disappears from the household measure. Which table you use decides who is visible.

*What the hearing measure counts.* `B18102` counts people reported as deaf or having "serious difficulty hearing," again often by someone else in the household. That is a family member's judgment of severity, not an audiological measurement, and it will miss hearing loss that nobody at home would call serious.

*Small numbers, wide margins.* A tract-level estimate for one language group among adults 65 and older rests on a small sample of households, and its margin of error can approach the size of the estimate itself. The ACS publishes a margin of error for every estimate. Use it, or aggregate until the numbers can bear the weight you put on them.

**A note on insurance.** Medicare covers nearly everyone 65 and older, so a map of uninsured older adults will mostly show noise. The barrier Sound Generations described is what insurance covers and requires, not its absence. Original Medicare, for instance, does not pay for hearing aids or the exams to fit them ([Medicare.gov](https://www.medicare.gov/coverage/hearing-aids)). Some Medicare Advantage plans do, and the ACS does not ask which kind of Medicare a person has. Coverage type in `B27010` (Medicare alone, or Medicare with Medicaid) is a more meaningful layer, as is the 55–64 band if the partner serves that age group. Ask before assuming.

**Other directions from our conversations.** Our conversations with Sound Generations also produced ideas about building occupancy for emergency planning, the participation record the organization doesn't keep, and an archive of paper surveys. None is supported as a strand project this term. Each depends on documents or staff time the partner hasn't committed, and they have told us the access map is what would help. If one of them is what draws you, it is possible only as an inverted-variant or independent project, with instructor approval before the proposal deadline. Volunteer tracking came up as well, but there is no record to analyze; Strands D and E have volunteer records.

**Challenge goal fit.** **Multiple Datasets** is close to automatic: ACS tables, tract boundaries, the partner's site list, and provider locations, joined. **Result Validity** follows directly from the provenance question, whether by checking tract-level co-location against person-level overlap in PUMS or by testing whether your map's patterns survive the margins of error. **Messy Data** if you pull data through the Census Data API or the NPI Registry API. **New Library** for routing and accessibility analysis.

**Scope warnings.** The Mapping homework joins Washington tract geometry to food access data, and your project cannot rest on a course assignment's dataset. The ACS tables above are different data; say so explicitly in your proposal. And do not reuse the homework's tract shapefile. It uses older tract boundaries, current ACS estimates use 2020 tracts, and a join on tract IDs across the two will silently drop or misplace every tract whose boundaries changed. Separately, this is a four-person team with no data staff, and every student in this strand depends on the same handoff. Route requests through the instructor.

---

### Strand C — ReWA: Resettlement shifts and programming footprint

**Partner context.** The Refugee Women's Alliance serves a population whose composition changes with federal policy, world events, and funding cycles. Staff described the difficulty of planning programming for a community whose needs they can only partially anticipate.

**Anchoring question.** How have the countries of origin, languages, and geographic distribution of arrivals in Washington shifted since 2015, and where is ReWA's programming footprint relative to that shift?

**Data landscape.** Federal refugee arrivals data, Washington state refugee and immigrant assistance reporting, ACS language and nativity tables, ReWA program site locations. Expect large volume and uneven quality — this is the strand where the data is most abundant and least tidy.

**Named provenance question.** *The categories are administrative, not descriptive.* Refugee, asylee, Special Immigrant Visa holder, humanitarian parolee — these are legal statuses that determine which dataset a person appears in, not facts about who they are or what they need. The categories themselves change over time. Discontinuities in your time series will often turn out to be policy events (a travel ban, the 2021 Afghanistan evacuation, the 2022 Ukraine parole program) rather than changes in the underlying population. Identify them and say so. If you use ACS language tables, Strand B's notes on what they record apply here with more force: many of the languages in recent arrival data have no category of their own at the tract level.

**Challenge goal fit.** **Messy Data** is a strong fit given format inconsistency across reporting years. **Multiple Datasets** for joining arrivals to ACS to program locations. **Result Validity** for testing whether an apparent trend survives a change in category definitions.

**Scope warning.** Do not use individual-level client records. Aggregate published data only.

---

### Strand D — SR3: Volunteer retention, absence, and reach

**Partner context.** SR3 responds to marine mammal strandings and runs a rehabilitation facility. Over 200 hands-on volunteers, roughly 400 on the waitlist. Training runs late spring and early summer; the season is summer-centric. Volunteer records live in Volunteer Impact, where each profile carries a `DatabaseUserID` that links across report types.

SR3's volunteer coordinator has been specific about what is and isn't worth asking. **They have advised against framing this as "how are volunteers used and where could they be reallocated"** — that question is hard to answer from their records and hard to act on. They pointed instead toward volunteer feedback, absence and call-out patterns, and retention. The tracks below follow their steer.

**D1 — Call-outs and absence.** *When do volunteers who have committed to a shift not appear, and what distinguishes those shifts?*

The distinction to build on first: a shift nobody signed up for and a shift someone claimed and then called out of are different failures with opposite interventions. One is a recruitment or scheduling problem, the other a commitment or burnout problem. They produce identical coverage gaps.

From there: call-out rates by day of week, slot, and point in the season; whether call-outs cluster in individuals or spread across the corps; whether they rise as the season progresses; and whether they differ by role, since roles carry different duties and different shift minimums.

*Data:* shift schedules and call-out tracking.

**D2 — The volunteer pipeline.** *Where in the process do people leave?*

SR3 laid out the stages: application → orientation → role-specific training → first shift → season completion → return the following year. Each transition is a conversion rate, and someone lost between training and first shift is a different problem from someone lost mid-season.

`DatabaseUserID` makes person-level linkage possible across Volunteer Impact reports, so this is a genuine funnel rather than a set of stage totals. Note where that guarantee stops — see the provenance questions below.

*Data:* application records, orientation and training rosters, shift records, multi-year participation.

**D3 — Applicant and supporter geography.** *Where do volunteer applicants and donors come from, and who is structurally out of reach?*

The only Family 1 track in this strand. The version worth doing is the inverse of how it sounds: not where applicants live, but which parts of the region generate essentially none, and whether that tracks travel time to the facility, shift timing that presumes a car, or the channels through which SR3 recruits. A 400-person waitlist looks like abundant supply until you ask where it draws from.

*Data:* applicant records with ZIP codes, ACS demographic and vehicle-access tables, ZCTA boundaries, transit layers.

**Named provenance question.** *The standard for "retained" has been rising the whole time.* SR3 has always had a shift requirement, but it has increased steadily — from two shifts per summer to three per month for Husbandry — and as new roles were added, each got its own minimum. There is no clean before-and-after to control for. The bar drifts year over year and differs across roles within a year.

The consequences are concrete. A volunteer who "completed the season" in an early year cleared a bar several times lower than one who completed it recently, so any multi-year retention trend is partly a measurement of escalating requirements rather than changing volunteer behavior. If retention fell, the bar rising is a candidate explanation before anything about volunteers is. And cross-role comparison in a single year compares people held to different standards. Reconstruct the requirement history and carry it as a covariate, or restrict your comparison to a window where the standard held still.

A second, narrower one: *`DatabaseUserID` solves linkage inside Volunteer Impact, which relocates the question rather than closing it.* Ask at what point in the pipeline a person first receives one. If applicants only get a profile on acceptance, then the application → orientation transition — often the largest drop in the funnel — is the one place you cannot follow individuals, and apparent attrition there may partly be people who exist in one system and not the other. Establish where the identifier starts before interpreting the first conversion rate.

**Survey data.** SR3 named volunteer feedback as a priority, and will share **themes and noteworthy points** from the mid-point survey (distributed August 15) rather than raw responses. Two consequences. First, someone else has already done the interpretive coding, which is itself a data setting worth naming — you are analyzing a reading of the responses, not the responses. Second, the **end-of-season survey goes out in November or December and will not exist in time for this project.** Do not plan around it.

Be realistic about what this course can do with qualitative material. Survey themes work well as the thing that motivates a quantitative question or complicates a quantitative finding — if volunteers report schedule conflicts, does the call-out data show it? — but not as the spine. The exception is an inverted-variant project treating the survey instrument itself as the object of study. Talk to the instructor.

**Two things that are not available.** Session records do not note which tasks a volunteer performed, so any skill-decay or refresher analysis is off the table — roles are tracked, individual duties are not. And hours reporting is already well served by SR3's own system; use it for a denominator if you need one, but it is not a project.

**Challenge goal fit.** **Multiple Datasets** for D2 (funnel stages across report types) and D3 (applicant records joined to census and transit data). **Messy Data** for reconstructing the shift-requirement history across years and roles, which will not arrive as a tidy table. **Result Validity** throughout, particularly for conversion rates on small stage counts. **Machine Learning** is a poor fit at this scale.

**Scope warnings.** Do not build a shift allocation optimizer — SR3 has specifically waved off the reallocation framing, and an optimizer presumes exactly the question they said is hard to act on. Training video production, hardware documentation, and corporate sponsorship packages are real organizational needs and none is a data analysis project.

---

### Strand E — Bailey Boushay House: Volunteer capability and coverage gaps

**Partner context.** Bailey Boushay House provides residential and outpatient care, and operates a shelter. Its volunteer corps is unusually diverse — students, medical professionals, retirees, people in career transition. New volunteers complete a "gifts and talents form" at intake describing their strengths. Staff match volunteers to residents based on language, communication style, and interest, and described the difficulty of responding when gaps open unexpectedly.

**Anchoring question.** Where do gaps open between volunteer capabilities — languages, skills, availability windows — and the coverage the house needs?

A second question worth pursuing: which volunteer cohorts returned after 2020 and which did not? Staff described a lasting change in volunteer culture after COVID.

**Data landscape.** Gifts and talents form responses, volunteer shift and hours records. Multi-select capability fields reshape into indicator columns; coverage becomes a groupby heatmap; matching supports an object model.

**Named provenance question.** *A self-report instrument measures vocabulary as much as capability.* A form asking people to name their own strengths systematically over-represents volunteers who are fluent in the language of professional skills and misses those whose capabilities have no entry on the form. Reconstruct where the form came from and what it renders visible.

**Challenge goal fit.** **Messy Data** for multi-select and free-text field parsing. **Other** for an allocation or matching model with complexity analysis. **Multiple Datasets** if you bring in public context data.

**Hard constraint — read this before choosing this strand.** Bailey Boushay House serves a population whose records include HIV status, other diagnoses, substance use history, and housing status. **No project in this strand may use resident data of any kind.** This is not a judgment call: course policy prohibits datasets that cannot be shared with course staff, including confidential medical information, and resident records here cannot be shared. Volunteer data only.

If volunteer records are not available in usable form, a **documented synthetic dataset** is acceptable in this strand only, with instructor approval. You must write the generator programmatically, state clearly in your Data Setting section that the data is synthetic, describe what real distributions informed it, and confine every claim in your Results to what a synthetic dataset can support — which is a statement about your method, not about Bailey Boushay House.

---
### Concluding Remarks
You are not required to select one of these strands for the final project. You are welcome to select a data set unrelated to any of these strands. Instead, these are here for anyone who wants to apply their data analysis and programming skills to a problem within our local communities.