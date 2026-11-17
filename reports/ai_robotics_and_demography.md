# AI, Physical AI & Robotics in an Aging World

**Can technology offset demographic decline — and will it change fertility itself?**

A companion report to `report.md` (global population and birth-rate projections) and `consequences_and_solutions.md` (low-fertility consequences and policy responses). Research cut-off: **17 November 2026**.

---

## Scope, method, and confidence labels

This report asks two questions:

1. **Can AI, physical AI, and robotics offset the economic effects of a shrinking, aging workforce?**
2. **Could AI itself change fertility and family decisions — and if so, in which direction?**

It synthesizes **188 distinct verified sources** gathered by four parallel research streams: economist/institutional estimates (31 sources), physical AI/robotics/care (53), fertility/testimonials (61), and GitHub repositories/prediction markets (43). Every claim below was checked against an issuing institution, primary paper, platform page, or reputable report. Confidence tags are used throughout:

| Tag | Meaning |
|---|---|
| **HIGH** | Primary source or peer-reviewed record; exact title/date/numbers retrieved. |
| **MEDIUM** | Reputable secondary source quoting a named primary source, or a version-specific figure. |
| **LOW** | Aggregator, undated, or time-sensitive figure; useful for triangulation, not standalone quotation. |
| **CONTESTED** | The source is real, but the magnitude, date, or definition is disputed or version-dependent. |

A central warning: **exposure is not unemployment**, **forecasts are not order books**, **headcount is not labor input**, and **company-announcement prediction markets are not capability forecasts**.

---

## 1. Executive summary

- **The demographic pressure is mechanical and already visible.** The UN's 2024 Medium projection has world population peaking at ~10.3B in the mid-2080s and falling to ~10.2B by 2100, with global TFR at ~2.25 and the 65+ cohort tripling from 0.83B to 2.44B. The probability of a peak this century is put at ~80% [HIGH] ([UN WPP 2024](https://population.un.org/wpp/assets/Files/WPP2024%5FSummary-of-Results.pdf)). This report's companion studies establish the underlying trajectory; here the question is what technology can and cannot do about it.

- **Digital AI's aggregate macro effect is real but highly uncertain.** Credible estimates span an order of magnitude: Acemoglu's **≤0.66% TFP over ten years** (≤0.53% for hard-to-learn tasks) versus Goldman Sachs' **+7% global GDP / +1.5pp annual productivity growth** over a decade; the OECD's central range is **0.25–0.6pp annual TFP**; Penn Wharton's 2025 estimate is **+1.5% GDP by 2035, +3.7% by 2075**. Early macro data are close to zero: Danish administrative data find **precise null effects on earnings and hours** two years after ChatGPT [HIGH]. The honest central reading is **modest, delayed, and uneven** — not nothing, not magic.

- **Physical AI is real in factories but nascent in humanoids.** The IFR counted **542,076 industrial robot installations in 2024** and **4.66M operational units**; global robot density was ~177 per 10,000 manufacturing workers in the September 2025 report, revised to **132** in April 2026 after China changed its employment denominator [HIGH]. Humanoid shipments, however, were only **~13,000 units in 2025** (Omdia), against bank forecasts of **6.48M units / $138B by 2035** (Goldman, revised 2026) and **~1B units / $5T by 2050** (Morgan Stanley) [MEDIUM–HIGH, scenarios not orders]. The gap between actuals and forecasts is where most capital risk sits.

- **Care robots are the clearest test of "offsetting" demography, and the evidence is genuinely mixed.** Ethnographic work in Japan finds robots often *create more work* for caregivers [HIGH]. A 2026 Health Affairs Review study using robot-subsidy variation finds adoption associated with **+28% care workers, +39% nurses, +26% total employment**, but entirely among **non-regular** staff and with no hours/FTE data [HIGH]. A separate lottery-based study finds a **small reduction** in care workers [HIGH]. PARO seal-robot RCTs show engagement/mood benefits but meta-analyses rate the evidence low and find no significant effects on cognition, agitation, or quality of life in several outcomes [HIGH]. Verdict: **complement, not replacement — with weak cost-saving evidence**.

- **AI can push fertility in both directions.** Chinese survey studies find AI development and robot exposure associated with **lower ideal fertility and delayed marriage** [HIGH]; US evidence finds robot exposure reduced marital fertility and increased nonmarital births [HIGH]. Remote-work studies conflict: one finds both partners working from home associated with **+0.32 to +0.45 children**, another finds a **−2% birth-rate effect** [HIGH, contested]. Online dating changes *who partners with whom* more than *whether people partner* [HIGH]. The net aggregate effect on fertility is **unknown**, and no credible source claims AI will reliably raise TFR back to replacement.

- **What economists actually consider highly likely:** widespread *exposure*; task-level productivity gains concentrated among novices; delayed aggregate effects; distributional consequences; that aging and technology interact through policy. What they do **not** consider highly likely: imminent mass unemployment (a Chicago Booth panel was ~two-thirds uncertain) or a quick technological reversal of below-replacement fertility.

- **Tech leaders are more bullish than the evidence.** Jensen Huang calls robots "AI immigrants" to fill a labor gap of "tens of millions"; Eric Schmidt says "we are not having enough children" and argues for productivity; Elon Musk calls low birth rates a top threat; James Liang warns fewer people means yielding "control to AI." Demographers Wolfgang Lutz and Ronald Lee are more nuanced: productivity can substantially offset fewer workers, but "technology is not a substitute for sound public policies."

---

## 2. The demographic baseline technology would have to offset

| Indicator | Value | Source |
|---|---|---|
| World population 2024 | 8.16–8.2B | UN WPP 2024 [HIGH] |
| Peak (Medium) | ~10.3B in mid-2080s | UN WPP 2024 [HIGH] |
| 2100 population | ~10.2B | UN WPP 2024 [HIGH] |
| Global TFR 2024 | ~2.25; 2.3 in 2023 | UN WPP 2024 / OWID [HIGH] |
| Global TFR 1950s | 4.85–4.9 | UN WPP / OWID [HIGH] |
| 65+ population 2024→2100 | 0.83B→2.44B | UN WPP 2024 [HIGH] |
| Ultra-low fertility (<1.4) | nearly 1/5 of countries; return to ≥2.1 in 24 peak countries within 30 years has 0.1% probability | UN WPP 2024 [HIGH] |

Wilmoth: "the probability that the world's population will peak within the current century is quite high – about 80%" [HIGH] ([AP, 2024-07-11](https://apnews.com/article/un-world-population-growth-e2adab27719bb94ea19626dc53c57384)). Ronald Lee warns that forecasters "work well when the future is similar to the past, but our methods can be blind-sided by real change" [HIGH] ([Population and Development Review, 2025](https://onlinelibrary.wiley.com/doi/10.1111/padr.12674)).

The offset question is not "will there be fewer people?" but **how much output and care per person can rise before dependency ratios outrun productivity gains**.

---

## 3. Digital AI and productivity: the estimate map

### 3.1 The headline range

| Source | Estimate | Horizon | Confidence |
|---|---|---|---|
| [Acemoglu, *Simple Macroeconomics of AI*](https://www.nber.org/papers/w32487) | TFP **+0.66%**, ≤**0.53%** for hard tasks; GDP +0.93–1.56% | 10 yrs | HIGH |
| [Goldman Sachs, Briggs & Kodnani](https://www.gspublishing.com/content/research/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.pdf) | Global GDP **+7% / ~$7T**; US productivity **+1.5pp/yr**; 300M jobs exposed | 10 yrs | HIGH |
| [McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier) | **$2.6–4.4T/yr** across 63 use cases; productivity +0.1–0.6%/yr through 2040 | to 2040 | HIGH |
| [IMF SDN/2024/001](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf) | **~40%** global jobs exposed; 60% advanced economies, 40% EM, 26% LIC | current | HIGH |
| [WEF Future of Jobs 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf) | 170M created, 92M displaced, +78M net, 22% churn | by 2030 | HIGH |
| [OECD, *Miracle or Myth?*](https://www.oecd.org/en/publications/miracle-or-myth-assessing-the-macroeconomic-productivity-gains-from-artificial-intelligence_b524a072-en.html) | TFP **+0.25–0.6pp/yr**; **~1pp/yr if robotics exposes manual tasks** | 10 yrs | HIGH |
| [Penn Wharton 2025](https://budgetmodel.wharton.upenn.edu/p/2025-09-08-the-projected-impact-of-generative-ai-on-future-productivity-growth/) | GDP +1.5% by 2035, ~3% by 2055, +3.7% by 2075 | decades | HIGH |
| [Baily, Brynjolfsson & Korinek](https://www.brookings.edu/articles/machines-of-mind-the-case-for-an-ai-powered-productivity-boom/) | 18% productivity level boost; Level+Growth near-doubling in 20 yrs | 10–20 yrs | HIGH, illustrative |
| [Brynjolfsson, Rock & Syverson](https://www.aeaweb.org/articles?id=10.1257/mac.20180386) | Productivity J-curve: adjusted TFP 15.9% above official by 2017 | historic | HIGH |
| [Humlum & Vestergaard](https://www.nber.org/papers/w33777) | Precise nulls on earnings/hours; 2.8% time saved | 2 yrs post-ChatGPT | HIGH |
| [Bick, Blandin & Deming](https://www.nber.org/papers/w32966) | Current usage implies +1.1% aggregate productivity | current | HIGH |
| [CBO](https://www.cbo.gov/publication/61147) | "Varies greatly"; no discrete AI boost in baseline; only 5% of businesses use AI to produce goods/services | current | HIGH |

Richmond Fed's Hornstein provides the synthesis: conclusions "range from less than 1 percent to 20 percent, which would correspond to annual growth rates of 0.1 to 2.0 percent" [HIGH] ([Economic Brief 24-19](https://www.richmondfed.org/publications/research/economic_brief/2024/eb_24-19)).

### 3.2 Task-level gains are the most robust finding

- [Brynjolfsson, Li & Raymond, *Generative AI at Work*](https://academic.oup.com/qje/article/140/2/889/7990658) (QJE 2025): AI assistance raised chats resolved per hour by **15%** among 5,172 customer-support agents; novices gained **30–36%** [HIGH].
- [Noy & Zhang, *Science*](https://www.science.org/doi/10.1126/science.adh2586): 453 professionals; writing time **−40%**, quality **+18%**, inequality between workers fell [HIGH].
- [Dell'Acqua et al., *Organization Science*](https://pubsonline.informs.org/doi/full/10.1287/orsc.2025.21838): inside the AI frontier, 758 consultants completed **12.2% more tasks, 25.1% faster**, quality ~32%; outside it, AI users were **19% less likely** to be correct [HIGH].
- [Eloundou et al., *GPTs are GPTs*](https://www.science.org/doi/10.1126/science.adj0998): 80% of US workers could have ≥10% of tasks affected; 19% could have ≥50% affected; tooling assumptions push this to 46% [HIGH/CONTESTED].
- [Bick et al.](https://www.stlouisfed.org/on-the-economy/2025/feb/impact-generative-ai-work-productivity): workers are 33% more productive in hours they use GenAI, but aggregate effect is only ~1.1% because usage is shallow [HIGH].

The consistent pattern: **large gains for inexperienced workers on tasks inside the model's frontier, weak pass-through to wages and aggregate statistics**.

### 3.3 Why the macro data lag

The Productivity J-curve means investment in intangible complements is counted as current cost before benefits show up. Brynjolfsson et al. found measured TFP understated by 15.9% by 2017 for software/hardware intangibles [HIGH]. Humlum & Vestergaard's Danish data show adoption was rapid but time savings only 2.8%, with 3–7% of gains passing to wages [HIGH/MEDIUM]. CBO notes actual outcomes are not yet observed and "the conclusions of current studies... are preliminary" [HIGH].

**Demographic relevance:** if the J-curve is long, an aging society may need productivity gains *before* the dependency ratio worsens — precisely when measured gains look absent. This is an argument for patience, not for assuming rescue.

---

## 4. What economists say is "highly likely"

Based on the primary sources and two Chicago Booth expert panels, the following are the best-supported propositions:

| Proposition | Assessment | Evidence |
|---|---|---|
| AI exposure is widespread, but most exposure is *partial* and complementary | **HIGHLY LIKELY** | IMF 40%/60%; Goldman two-thirds of US jobs; OpenAI 80% with ≥10% tasks |
| Task-level productivity gains are real, often large for novices | **HIGHLY LIKELY** | QJE +15%; Noy–Zhang −40% time/+18% quality; BCG 12.2%/25.1% |
| Aggregate productivity effects are delayed and much smaller than task gains | **HIGHLY LIKELY** | J-curve; Humlum nulls; Bick +1.1%; CBO caution |
| The magnitude of long-run GDP growth is deeply uncertain | **HIGHLY LIKELY** | Estimates 0.53% to 7%; Richmond Fed 0.1–2.0pp annual range |
| AI will worsen within-country and between-country inequality without policy | **LIKELY / HIGHLY LIKELY** | IMF; Acemoglu; WEF 12% expect positive wage effect; Lu: "surplus not yet reaching consumers" |
| Mass technology-driven unemployment within ten years | **CONTESTED, NOT HIGHLY LIKELY** | Chicago Booth: ~two-thirds uncertain, quarter disagree, <10% agree |
| AI will substantially raise high-skilled workers' earnings | **CONTESTED** | Booth panel >50% agree/strongly agree on negative effect on some high-skilled; Acemoglu uncertain |
| Returns to education will become more uncertain | **HIGHLY LIKELY** | Booth panel nearly 70% agree |
| AI/robots will fully offset aging-driven labor loss | **NOT SUPPORTED** | OECD ~1pp/yr only if physical tasks exposed; Acemoglu low estimates; mixed care evidence |
| AI will restore replacement fertility | **NOT SUPPORTED** | Fertility studies point both ways; no primary source claims reliable TFR restoration |

Individual expert votes illustrate the split: Acemoglu "Disagree" on US per-capita growth acceleration, Chad Syverson "Strongly Agree," William Nordhaus "Disagree," Olivier Blanchard and Ricardo Reis "Agree" for Europe [CONTESTED dates; Clark Center surveys](https://kentclarkcenter.org/surveys/ai-and-growth/).

---

## 5. Physical AI and robotics

### 5.1 The installed base is substantial — but it is not humanoids

| Metric | Value | Source |
|---|---|---|
| Industrial robots installed 2024 | **542,076** | [IFR World Robotics 2025](https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf) [HIGH] |
| Operational stock 2024 | **~4.664M** (+8.9%) | IFR [HIGH] |
| Global robot density 2024 | 177 (Sep 2025) → **132** (Apr 2026 denominator revision) | IFR [HIGH] |
| Highest density | Korea **1,220** per 10,000; Singapore 818; Japan 446 | IFR [HIGH] |
| China installations 2024 | 295,000 (54% of global) | IFR [HIGH] |
| Forecast 2025/2028 | 575,000 / >700,000 installations | [IFR press release](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years) [HIGH] |

This is the relevant baseline for demographic offset: **robots already work at scale in structured manufacturing**, but the labor they replace is not the same as the labor that is scarce in aging societies (care, services, construction, logistics).

### 5.2 Humanoids: forecasts vs. shipments

| Source | Forecast | Confidence |
|---|---|---|
| [Goldman Sachs, 2026 revision](https://www.investing.com/news/stock-market-news/goldman-sachs-raises-humanoid-robot-forecast-sees-auto-role-93CH-4882346) | **6.48M units / $138B by 2035** (prior: 1.38M / $38B); 75k units 2026, 890k 2030 | MEDIUM |
| [Morgan Stanley, 2025](https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050) | **>1B units / $5T by 2050** incl. supply chain; adoption slow until mid-2030s | HIGH |
| [Citi GPS, 2024](https://www.citigroup.com/global/insights/the-rise-of-ai-robots) | **~650M humanoids / $7T by 2050**; 1.3B AI-robots by 2035 | HIGH |
| [Omdia, 2026](https://www.agibot.com/article/231/detail/33.html) | **2.6M units by 2035** | MEDIUM |
| BofA / UBS / RBC (via [comparison](https://blog.robozaps.com/b/market-size-for-humanoid-robots)) | 10M by 2035; 300M by 2050; $9T addressable | LOW/MEDIUM |

Actual 2025 shipments: **~13,000 humanoids** (Omdia; 13,317 precise), with China producing 87%; leaders AgiBot 5,168, Unitree 4,200, UBTech 1,000, Tesla/Figure/Agility ~150 each [HIGH/MEDIUM]. IFR's narrower industrial/professional count is ~7,000 [LOW]. Tesla began "early production" on its Fremont Optimus line in October 2026 but has published **no cumulative build count**; Musk's "20,000/week" is a target "at least a year" away [HIGH/MEDIUM]. Unitree's IPO prospectus reports **5,632 humanoid robots sold 2023–2025**, >5,500 shipped in 2025, and average humanoid price falling from ~¥260,700 (2024) to ~¥167,600 (9M 2025) [HIGH].

**Interpretation:** the industrial base is real; the humanoid trajectory is a **scenario bet**. The read-through for demographic decline is that physical substitution is plausible in structured settings first, not in homes or care.

### 5.3 The enabling stack

- NVIDIA GR00T N1/N1.5/N1.6/N1.7: open foundation models for humanoid reasoning; GR00T-Dreams generated training data in **36 hours** versus ~3 months manual; 24,000 motion trajectories; 76.8% real-world success with full data; 2M+ developers on the robotics stack [HIGH] ([NVIDIA, 2025-05-18](https://nvidianews.nvidia.com/news/nvidia-powers-humanoid-robot-industry-with-cloud-to-robot-computing-platforms-for-physical-ai), [GR00T repo](https://github.com/NVIDIA/Isaac-GR00T)).
- Jetson Thor: 128GB, up to 2,070 FP4 TFLOPs in 130W; 7.5× compute and 3.5× efficiency over Orin [HIGH] ([NVIDIA, 2025-08-25](https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics)).
- Hugging Face **LeRobot**: 28,822 GitHub stars; 16K+ datasets from 2.2K+ contributors by September 2025; training in <100 LOC [HIGH] ([repo](https://github.com/huggingface/lerobot)).
- Care-specific datasets: **OpenRoboCare** (21 occupational therapists, 15 tasks, 315 sessions, 19.8 hours, 44-sensor tactile data) [HIGH]; **ETRI-Activity3D** (112,620 samples, 100 people, 6.47TB) [HIGH]; **NAVER CareCall** (10,500 dialogues) [HIGH].

Jensen Huang's framing: "Physical AI and robotics will bring about the next industrial revolution... from AI brains for robots to simulated worlds to AI supercomputers" [HIGH].

---

## 6. Care robots: the clearest demographic test

### 6.1 The skeptical evidence

James Wright's 18 months of ethnographic fieldwork in Japan found that care robots "tend to end up creating more work for caregivers" — they must be moved, maintained, cleaned, booted, explained, monitored, and stored [HIGH] ([MIT Tech Review, 2023-01-09](https://www.technologyreview.com/2023/01/09/1065135/japan-automating-eldercare-robots)). By 2018 the Japanese government had spent **well over $300M** on R&D for such devices. A 2021 home-care study found only **2% of 444 providers** used them; a 2019 survey of 9,000+ institutions found only ~10% had introduced any care robot [MEDIUM]. A 118-home Japanese survey found high accident/near-miss rates and a gap between managers' efficiency beliefs and workers' agitation concerns [HIGH] ([JINR, 2025](https://www.jstage.jst.go.jp/article/jinr/5/2/5_2025-0012/_pdf/-char/en)).

PARO evidence is mixed but not null. A 415-participant cluster-RCT found improvements in engagement, pleasure, and agitation versus usual care, but PARO was only better than a plush toy on engagement [HIGH] ([JAMDA, 2017](https://www.sciencedirect.com/science/article/pii/S1525861017301895)). A 2022 meta-analysis of 66 studies found **no significant effects** on agitation, cognition, or quality of life [HIGH]; a 2023 meta-analysis (12 articles, 1,461 participants) found small effects on anxiety/agitation/depression but graded evidence **low** [HIGH]. A 2026 cluster-RCT of 85 participants found reduced caregiver burden with thrice-weekly self-directed PARO sessions [HIGH].

### 6.2 The complementary evidence

A 2026 study in *Health Affairs Review* used prefecture-level robot subsidies as an instrument across ~860 Japanese nursing homes and found robot adoption associated with **+28% care workers, +39% nurses, +26% total employment**, reduced retention difficulty, and no lower care quality [HIGH] ([AIMS Press](https://www.aimspress.com/article/doi/10.3934/har.2026001?viewType=HTML), [Stanford Report](https://news.stanford.edu/stories/2026/08/care-robots-japan-employment-labor-shortage-research)). A meaningful caveat: gains were entirely in **non-regular** staff; no hours/FTE data exist, so headcount ≠ labor input. A separate lottery-based natural experiment found a **small reduction** (−1.11 care workers in 2021) [HIGH] ([Research Square preprint](https://assets-eu.researchsquare.com/files/rs-9001048/v1/869988bc-be91-40b7-8a70-9e207b1b940d.pdf)).

Public acceptance is surprisingly high: about **65%** of Japanese respondents chose a robot-using nursing home over an all-human option, and were willing to pay more; mobility aids were most welcome at 70% [HIGH] ([Boston College CRR, 2026-11-03](https://crr.bc.edu/how-do-people-feel-about-robot-caregivers-evidence-from-japan)).

**Verdict:** care robots are best understood as **retention and task-reallocation tools**, not labor-saving replacements. They may expand employment in low-wage, flexible roles while improving some patient outcomes; the fiscal and staffing payoff remains unproven.

---

## 7. AI and fertility / family decisions

### 7.1 Channels identified in scholarship

Adserà (Princeton, 2025) identifies four interlocking channels: labour-market polarization, AI-enabled reproductive medicine and fertility apps, algorithmic partner matching, and algorithmic influence on ideals/information [HIGH] ([Vienna Yearbook of Population Research](https://verlag.oeaw.ac.at/api/download/content/9783700196815_kapitel_59_68.pdf)). Her conclusion is explicitly two-sided: AI may "reinforce educational and other socio-economic barriers to parenthood," while household robots could "ease the path to realising fertility goals."

### 7.2 Evidence that AI/robots may *lower* fertility

- Zou & Chen (2026), using CFPS 2014/2018/2022: AI development "significantly reduces women's ideal number of children," stronger among highly educated women; mitigated by spousal housework and social childcare [HIGH] ([Journal of Finance and Economics](http://qks.sufe.edu.cn/mv_html/j00001/202608/V7f3eSTE-qmQ1-zr67-byme-QltvBYpLsGoS_WEB.htm)).
- He & Li (2026), China GSS 2012–2021: industrial robot adoption "significantly delays first marriage and reduces fertility," stronger for men [HIGH] ([Review of Economics of the Household](https://doi.org/10.1007/s11150-026-09863-z)).
- He & Wang (2026): robot exposure decreases likelihood of childbearing via human-capital investment, employment instability, and inequality [MEDIUM–HIGH].
- Anelli, Giuntella & Stella (2024), US: robot exposure narrowed gender income gaps, increased divorce/cohabitation, reduced marital fertility, increased nonmarital births; overall fertility unchanged [HIGH] ([Journal of Human Resources](http://jhr.uwpress.org/content/59/2/443)).
- A 2025 experiment found robot-support priming *lowered* fertility intentions when robots were seen as substitutes for human support but *raised* them when framed as assistants reducing childrearing costs [MEDIUM] ([Science China Technological Sciences](https://link.springer.com/article/10.1007/s11431-025-2953-y)).

### 7.3 Evidence that flexibility may *raise* fertility

- Bloom et al. (NBER 34963): both partners WFH ≥1 day/week associated with **+0.32 children per woman globally / +0.45 in the US**; interpreted causally, WFH accounts for ~291,000 US births/yr, but "not powerful enough... to reverse trend fertility declines" [HIGH/CONTESTED — ADB abstract says +0.2/+0.18] ([NBER PDF](https://www.nber.org/system/files/working_papers/w34963/w34963.pdf)).
- Singapore FWA survey experiment: all three flexible-work arrangements improved fertility intentions, especially for women and professional/managerial occupations [HIGH].
- Opposite evidence: Johnston (NBER 35881) finds a one-SD increase in teleworkability **reduced birth rates 2%** and notes men's home time did not translate into childcare [HIGH]. UK and Australian studies find no fertility increase from home-based work [HIGH/MEDIUM].

### 7.4 Dating, childcare, and education

Online dating's measurable effect is on **sorting**, not aggregate fertility: mobile-era activity lowered marriage and divorce rates by 0.40% and 0.33% per 1% activity increase in one study [HIGH]; platform use is associated with mixed changes in interracial and educational homogamy [HIGH]. Algorithmic audits of Indian matrimonial platforms found recommendations reinforce gender-based age/income norms [MEDIUM–HIGH]. Interviews with users worry that care robots might disrupt child-parent attachment; parents accept robots as relief from overload, not parental substitutes [MEDIUM].

Andrew Ng's position illustrates the education tension: "frankly, AI models are terrible for learning... retention, their long-term performance is much worse" while one-to-one tutoring has large potential [HIGH transcript]. A field experiment found a standard ChatGPT tutor improved practice grades 48% but left students **17% worse** on exams when access was removed; a guardrailed version avoided the negative effect [MEDIUM].

**Verdict:** AI is more likely to **modify the timing and distribution of births** than to reverse the fertility transition. Its net effect is empirically unresolved.

---

## 8. Testimonials — what leaders actually said

| Speaker | Date | Verbatim / near-verbatim claim | Confidence |
|---|---|---|---|
| Jensen Huang, Nvidia | 2026-01-07 | "Having robots will create jobs." "We need more AI immigrants to help us on manufacturing floors and do work that maybe we've decided not to do anymore." Shortage is "tens of millions" due to demography | HIGH ([France24/AFP](https://www.france24.com/en/live-news/20260107-nvidia-ceo-praises-robots-as-ai-immigrants)) |
| Jensen Huang | 2025-05-09 | "we have a shortage of workers... we can imagine the opportunity to close that gap to put 30-40 million workers back into the workforce" | HIGH ([Milken transcript](https://milkeninstitute.org/sites/default/files/2025-05/new-innovation-economy-conversation-nvidia-ceo-jensen-huang_Transcript_GC25.pdf)) |
| Elon Musk | 2025-09-14 | "Low birth rate is the number one threat to the West. There will be no West if this continues." | MEDIUM–HIGH ([Business Insider](https://www.businessinsider.com/elon-musk-baby-bust-western-governments-taking-action-demographics-2025-9)) |
| Elon Musk | 2026-11-16 | "Hong Kong has had one of the lowest birth rates in the world for a long time. They will be gone soon if that doesn't change." | HIGH ([X post](https://x.com/elonmusk/status/2122216166584435079)) |
| Eric Schmidt | 2023-05-24 | "We are not having enough children... there is a demographic crisis where people who are my age are going to be taken care of by younger generations." | MEDIUM–HIGH ([Fortune](https://fortune.com/2023/05/24/artificial-intelligence-ai-eric-schmidt-demographic-crisis-babies-labor-shortage)) |
| Eric Schmidt | 2025-05-15 | "We, collectively as a society, are not having enough humans... the key problem is getting the people who are productive... to be more productive." | HIGH ([Vanity Fair](https://www.vanityfair.com/news/story/eric-schmidt-ai-ted)) |
| James Liang, Trip.com | 2026-07-07 | "We need more people, otherwise we'll just yield our control to AI." | HIGH ([Fortune](https://fortune.com/2026/07/07/china-japan-korea-birth-rate-innovation-trip-founder-james-liang/)) |
| Demis Hassabis | 2025-08-04 | "it's going to be 10 times bigger than the Industrial Revolution, and maybe 10 times faster" — about AI, **not fertility** | HIGH ([Guardian](https://www.theguardian.com/technology/2025/aug/04/demis-hassabis-ai-future-10-times-bigger-than-industrial-revolution-and-maybe-10-times-faster)) |
| Wolfgang Lutz & Guillaume Marois | 2026-03-02 | "Higher levels of education, increased labor force participation, and rising productivity can offset – and even outweigh – the effects of having fewer births." | HIGH ([IIASA](https://iiasa.ac.at/news/mar-2026/is-low-fertility-really-economic-threat)) |
| Ronald Lee | 2022-06-08 | "may be substantially offset by increased productivity of the smaller labor force" | HIGH ([UC Berkeley](https://www.demog.berkeley.edu/faculty/ronald-demos-lee)) |
| UN DESA / China Daily | 2026-07-11 | "Technology is a powerful enabler, but it is not a substitute for sound public policies, strong institutions and a commitment to human rights." | MEDIUM ([China Daily](http://www.chinadaily.com.cn/a/202607/11/WS6a5215eaa310986e2b464c76.html)) |

---

## 9. Predictions and forecasting — read the resolution criteria

| Source | Claim | Confidence / caveat |
|---|---|---|
| [AI Impacts 2023 survey](https://wiki.aiimpacts.org/ai_timelines/predictions_of_human-level_ai_timelines/ai_timeline_surveys/2023_expert_survey_on_progress_in_ai) (2,778 researchers) | 50% chance of HLMI by **2047**; 50% chance of full automation of labor by **2116**; median 5% extinction risk | HIGH |
| [Metaculus Q5121](https://www.metaculus.com/questions/5121/date-of-artificial-general-intelligence/), 2026-11-17 | General AI median **14 Jun 2030** (Feb 2028–Apr 2036); strict multi-criteria incl. robotic assembly | HIGH snapshot |
| [Metaculus Q3479](https://www.metaculus.com/questions/3479/date-weakly-general-ai-system-is-devised/) | Weakly general AI median **07 Aug 2027** | HIGH snapshot |
| [XPT](https://forum.effectivealtruism.org/posts/KGGDduXSwZQTQJ9xc/what-do-xpt-forecasts-tell-us-about-ai-timelines) | Superforecasters 50% advanced AI by **2060**; domain experts median 2046 | HIGH |
| [Manifold "AGI before 2030"](https://manifold.markets/RemNi/will-we-get-agi-before-2030) | ~50% (play money); resolution edited 2025-11-02 | HIGH snapshot |
| [Polymarket "OpenAI announces AGI before 2027"](https://polymarket.com/event/openai-announces-it-has-achieved-agi-before-2027) | ~7–10%, $382K volume | HIGH; **announcement market** |
| [Kalshi "any company AGI"](https://predictpedia.com/events/JMAJCw/when-will-any-company-achieve-agi) | Before 2030 ~72%, before 2031 ~75.5% | MEDIUM; **announcement market** |

**Critical caveat:** Polymarket/Kalshi contracts resolve when a company *announces* AGI, not when independent tests confirm capability. As NEXTPredict puts it, prices are "a forecast of a statement, not of a technology" [MEDIUM]. Definitions explain much of the spread between 2027 and 2116.

---

## 10. GitHub repository catalog (selected, verified)

| Repository | What it does | Confidence |
|---|---|---|
| [karpathy/jobs](https://github.com/karpathy/jobs) | BLS OOH exploration of 342 occupations / 143M workers; LLM-based exposure scores; "not a serious economic publication" | HIGH |
| [rmmomin/jobs-ai-exposure](https://github.com/rmmomin/jobs-ai-exposure) | Occupation/industry exposure, benchmarked against OpenAI, Yale, Felten, Eisfeldt, Microsoft | HIGH |
| [mathias3/jobs-exposure-atlas](https://github.com/mathias3/jobs-exposure-atlas) | Unified 342-occupation dataset; 143,066,500 workers; theory–reality gap analysis | HIGH |
| [AIOE-Data/AIOE](https://github.com/AIOE-Data/AIOE) | Felten/Raj/Seamans AI occupational, industrial, geographic exposure data | HIGH |
| [EIG-Research/AI-unemployment](https://github.com/EIG-Research/AI-unemployment) | CPS microdata 2015–2025; five exposure measures; most-exposed quintile unemployment +0.30pp vs least-exposed +0.94pp | HIGH |
| [MTJPeterman/eu-ai-exposure-index](https://github.com/MTJPeterman/eu-ai-exposure-index) | Eurostat/ESCO-based EU exposure index | HIGH |
| [tomasoles/AutomationExposureISCO-08](https://github.com/tomasoles/AutomationExposureISCO-08) | Patent-text similarity to ISCO-08 tasks; AI/ML/software/robotics | HIGH |
| [pgmyrek/2025_GenAI_scores_ISCO08](https://github.com/pgmyrek/2025_GenAI_scores_ISCO08) | ILO–NASK Global AI Exposure Index, 427 occupations, 3,265 tasks | HIGH |
| [Siyaovo/robotics-exposure-europe](https://github.com/Siyaovo/robotics-exposure-europe) | 3,039 ESCO occupations; 1 SD robotics exposure ↔ 7.2% lower hourly wages | HIGH |
| [NatLabRockies/DEMOS](https://github.com/NatLabRockies/DEMOS) / [urbansim/LBNL_DEMOS](https://github.com/urbansim/LBNL_DEMOS) | Agent-based demographic microsimulators: birth, death, marriage, migration, labor-force events | HIGH |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | Open robot-learning stack, 28.8K stars, 16K+ datasets | HIGH |
| [awslabs/open-data-registry — OpenRoboCare](https://github.com/awslabs/open-data-registry/blob/main/datasets/open-robo-care.yaml) | Robot-caregiving demonstrations by 21 occupational therapists | HIGH |
| [naver-ai/carecall-corpus](https://github.com/naver-ai/carecall-corpus) | Elder-care dialogue corpus (10,500 dialogues) | HIGH |
| [alejandrozu/population-visualizer](https://github.com/alejandrozu/population-visualizer) | OWID-based demographic scenario simulator | HIGH |
| [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | Open humanoid foundation model; N1.7 GA; Apache 2.0 code | HIGH |

The recurring caveat from these repositories: **exposure is technical potential, not job loss**.

---

## 11. Bottom line

1. **Technology can raise output per worker, but the size and timing are unresolved.** The combined evidence supports a modest, delayed, distributionally uneven productivity lift — not a near-term demographic rescue.
2. **Physical AI helps first where work is structured.** Industrial robots are mature; humanoids are a forecast-heavy, shipment-light sector; care robots are complements with mixed cost evidence.
3. **Aging societies should plan for a longer J-curve.** The productivity needed to offset dependency may arrive after the fiscal pressure peaks.
4. **AI in family life is ambivalent.** It lowers some barriers (childcare tools, flexibility, fertility care) and raises others (income precarity, algorithmic partner sorting, companion substitution). No evidence supports a reliable TFR rebound.
5. **The most defensible policy stance** is to treat AI/robotics as one lever alongside labor-force participation, migration, childcare/housing reform, and pension adaptation — not as a substitute for them. As Lutz & Marois put it, productivity can offset fewer births, but "technology is not a substitute for sound public policies."

---

## 12. Verified source catalog

The sources below are grouped by research stream. Confidence follows the rubric in §0. The catalog is deliberately extensive: 188 distinct items were verified, and the most load-bearing are listed here.

### 12.1 Economists and institutions (31 sources)

| # | Source | Confidence |
|---|---|---|
| 1 | [Acemoglu — NBER WP 32487 / Economic Policy](https://www.nber.org/papers/w32487) | HIGH |
| 2 | [Goldman Sachs — Briggs & Kodnani (full PDF)](https://www.gspublishing.com/content/research/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.pdf) | HIGH |
| 3 | [McKinsey — economic potential of generative AI](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier) | HIGH |
| 4 | [IMF — Georgieva blog](https://www.imf.org/en/blogs/articles/2024/01/14/ai-will-transform-the-global-economy-lets-make-sure-it-benefits-humanity) | HIGH |
| 5 | [IMF SDN/2024/001](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf) | HIGH |
| 6 | [WEF Future of Jobs 2025](https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/) | HIGH |
| 7 | [OECD — Miracle or Myth?](https://www.oecd.org/en/publications/miracle-or-myth-assessing-the-macroeconomic-productivity-gains-from-artificial-intelligence_b524a072-en.html) | HIGH |
| 8 | [Penn Wharton Budget Model — 2025](https://budgetmodel.wharton.upenn.edu/p/2025-09-08-the-projected-impact-of-generative-ai-on-future-productivity-growth/) | HIGH |
| 9 | [Baily, Brynjolfsson & Korinek — Brookings](https://www.brookings.edu/articles/machines-of-mind-the-case-for-an-ai-powered-productivity-boom/) | HIGH |
| 10 | [Brynjolfsson, Rock & Syverson — AEA](https://www.aeaweb.org/articles?id=10.1257/mac.20180386) | HIGH |
| 11 | [Humlum & Vestergaard — NBER 33777](https://www.nber.org/papers/w33777) | HIGH |
| 12 | [Chicago Booth Clark Center — AI and Growth](https://kentclarkcenter.org/surveys/ai-and-growth/) | CONTESTED date |
| 13 | [Goldman Sachs — AI could raise GDP 7%](https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent) | HIGH |
| 14 | [Goldman Sachs — long-run forecast upgrade](https://www.gspublishing.com/content/research/en/reports/2023/10/30/2d567ebf-0e7d-4769-8f01-7c62e894a779.html) | HIGH |
| 15 | [Goldman Sachs — Top of Mind: too much spend?](https://www.goldmansachs.com/insights/top-of-mind/gen-ai-too-much-spend-too-little-benefit) | HIGH |
| 16 | [McKinsey — $4.4T corporate profits release](https://www.mckinsey.com/mgi/media-center/ai-could-increase-corporate-profits-by-4-trillion-a-year-according-to-new-research) | HIGH |
| 17 | [Bick, Blandin & Deming — NBER 32966](https://www.nber.org/papers/w32966) | HIGH |
| 18 | [St Louis Fed — impact of GenAI on productivity](https://www.stlouisfed.org/on-the-economy/2025/feb/impact-generative-ai-work-productivity) | HIGH |
| 19 | [Brynjolfsson, Li & Raymond — QJE](https://academic.oup.com/qje/article/140/2/889/7990658) | HIGH |
| 20 | [Noy & Zhang — Science](https://www.science.org/doi/10.1126/science.adh2586) | HIGH |
| 21 | [Eloundou et al. — GPTs are GPTs](https://openai.com/index/gpts-are-gpts/) | HIGH |
| 22 | [Dell'Acqua et al. — Organization Science](https://pubsonline.informs.org/doi/full/10.1287/orsc.2025.21838) | HIGH |
| 23 | [Richmond Fed — Aggregate Effects of AI Adoption](https://www.richmondfed.org/publications/research/economic_brief/2024/eb_24-19) | HIGH |
| 24 | [CBO — AI and the economy](https://www.cbo.gov/publication/61147) | HIGH |
| 25 | [Wharton WIFPR — macroeconomic implications](https://wifpr.wharton.upenn.edu/wp-content/uploads/2024/10/Paper20241002.pdf) | HIGH |
| 26 | [Sequoia — AI's $600B Question (secondary)](https://www.404media.co/goldman-sachs-ai-is-overhyped-wildly-expensive-and-unreliable/) | CONTESTED |
| 27 | [Tom Cunningham — forecasts crosswalk](https://tecunningham.github.io/posts/2025-10-19-forecasts-of-AI-growth.html) | CONTESTED |
| 28 | [ifo/EconPol — Economic Experts Survey](https://www.ifo.de/DocDL/econpol-forum-2-2026-dietrich-etal-effects-of-AI.pdf) | CONTESTED |
| 29 | [LEAP wave 1](https://leap.forecastingresearch.org/reports/wave1) | CONTESTED |
| 30 | [PEP — AI and labor markets](https://www.pep-net.org/blog/artificial-intelligence-and-labor-markets-navigating-uncertain-and-fast-moving-landscape) | HIGH |
| 31 | [AEI — Pethokoukis on Acemoglu](https://www.aei.org/commentary/are-we-overestimating-ais-potential-economic-oomph/) | CONTESTED |

### 12.2 Physical AI, robotics, and care (53 sources)

Key verified items (full dossiers contain all 53):

- IFR: [World Robotics 2025 executive summary](https://ifr.org/img/worldrobotics/Executive_Summary_WR_2025_Industrial_Robots.pdf), [foreword](https://ifr.org/img/worldrobotics/Foreword_WR_2025_Industrial_Robots.pdf), [2025 press release](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years), [April 2026 density revision](https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas) — HIGH.
- Shipments: [AGIBOT/Omdia](https://www.agibot.com/article/231/detail/33.html), [Xinhua](https://english.news.cn/20260109/bab6612656664145bb5becc3781edd59/c.html), [Forbes](https://www.forbes.com/sites/johnkoetsier/2026/01/09/top-10-humanoid-robot-companies-by-shipments-revealed), [Bloomberg](https://www.bloomberg.com/news/articles/2026-01-08/chinese-firms-dominated-global-humanoid-robot-shipments-in-2025), [SCMP](https://www.scmp.com/tech/tech-trends/article/3339346/chinese-firms-outpace-us-rivals-2025-humanoid-robot-shipments-agibot-takes-lead) — HIGH/MEDIUM.
- Bank forecasts: [Goldman via Investing.com](https://www.investing.com/news/stock-market-news/goldman-sachs-raises-humanoid-robot-forecast-sees-auto-role-93CH-4882346), [Morgan Stanley $5T](https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050), [MS podcast](https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/humanoid-robot-market-rising-adam-jonas-sheng-zhong), [MS Robot Almanac](https://www.morganstanley.com/insights/videos/robot-almanac/industrial-robots-future), [Citi GPS PDF](https://www.citifirst.com.hk/home/upload/citi_research/rsch_pdf_30297368.pdf) — HIGH/MEDIUM.
- NVIDIA: [GR00T platform announcement](https://nvidianews.nvidia.com/news/nvidia-powers-humanoid-robot-industry-with-cloud-to-robot-computing-platforms-for-physical-ai), [Newton/Cosmos](https://nvidianews.nvidia.com/news/nvidia-accelerates-robotics-research-and-development-with-new-open-models-and-simulation-libraries), [Jetson Thor](https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics), [GR00T technical blog](https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1) — HIGH.
- Tesla/Unitree: [Tesla SEC 8-K](https://ir.tesla.com/_flysystem/s3/sec/000162828026066738/tsla-20261021-gen.pdf), [TechCrunch](https://techcrunch.com/2026/10/21/tesla-stars-optimus-robot-production-in-california-as-profit-falls-43/), [Xinhua Unitree IPO](https://english.news.cn/20260810/d1fe25981435453db422ecf41dd9b3e2/c.html), [Reuters](https://www.reuters.com/world/asia-pacific/unitree-plans-shanghai-ipo-testing-interest-humanoid-robots-2026-03-20) — HIGH/MEDIUM.
- Care: [MIT Tech Review](https://www.technologyreview.com/2023/01/09/1065135/japan-automating-eldercare-robots), [METI/MHLW](https://www.meti.go.jp/english/press/2024/0628_004.html), [Reuters AIREC](https://www.reuters.com/technology/artificial-intelligence/ai-robots-may-hold-key-nursing-japans-ageing-population-2025-02-28), [JINR survey](https://www.jstage.jst.go.jp/article/jinr/5/2/5_2025-0012/_pdf/-char/en), [JMIR scoping review](https://aging.jmir.org/2023/1/e42652) — HIGH.
- PARO: [Moyle 2017 RCT](https://www.scienceDirect.com/science/article/pii/S1525861017301895), [2022 meta-analysis](https://www.sciencedirect.com/science/article/pii/S1568163722000757), [2023 meta-analysis](https://www.sciencedirect.com/science/article/abs/pii/S0020748923000950), [2021 systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9292779/), [Inoue 2026](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/alz.71163) — HIGH.
- Stanford/care employment: [Health Affairs Review paper](https://www.aimspress.com/article/doi/10.3934/har.2026001?viewType=HTML), [Stanford Report](https://news.stanford.edu/stories/2026/08/care-robots-japan-employment-labor-shortage-research), [Stanford FSI](https://fsi.stanford.edu/news/robots-ease-elder-care-shortages-without-displacing-workers-or-diminishing-care-quality-study), [lottery counter-study](https://assets-eu.researchsquare.com/files/rs-9001048/v1/869988bc-be91-40b7-8a70-9e207b1b940d.pdf), [Boston College CRR](https://crr.bc.edu/how-do-people-feel-about-robot-caregivers-evidence-from-japan) — HIGH.

### 12.3 Fertility and family decisions (61 sources)

- [Adserà 2025 — AI and fertility inequalities](https://verlag.oeaw.ac.at/api/download/content/9783700196815_kapitel_59_68.pdf) — HIGH.
- [Zou & Chen 2026 — AI and women's fertility intentions](http://qks.sufe.edu.cn/mv_html/j00001/202608/V7f3eSTE-qmQ1-zr67-byme-QltvBYpLsGoS_WEB.htm) — HIGH.
- [Robot-support priming experiment](https://link.springer.com/article/10.1007/s11431-025-2953-y) — MEDIUM–HIGH.
- [npj Women's Health scoping review](https://www.nature.com/articles/s44294-025-00118-3) — HIGH.
- [Bloom et al. — Work from Home and Fertility](https://www.nber.org/system/files/working_papers/w34963/w34963.pdf) — HIGH/CONTESTED.
- [Johnston — Does Remote Work Increase Fertility?](https://www.nber.org/system/files/working_papers/w35881/w35881.pdf) — HIGH.
- [UK home-based work and childbearing](https://www.tandfonline.com/doi/full/10.1080/00324728.2023.2287510) — HIGH.
- [Singapore flexible working and fertility intentions](https://link.springer.com/article/10.1007/s10680-024-09719-1) — HIGH.
- [Ershov, Fong & Yildirim — online dating](https://www.nber.org/system/files/working_papers/w34757/w34757.pdf) — HIGH.
- [IFS — online dating and heterogamous marriage](https://ifs.org.uk/sites/default/files/2025-09/WP202533-The-rise-of-online-dating-and-heterogamous-marriages.pdf) — HIGH.
- [ACM — algorithmic audit of Indian matrimonial platforms](https://dl.acm.org/doi/full/10.1145/3736644) — MEDIUM–HIGH.
- [Vox — AI companions and fertility](https://www.vox.com/politics/491167/ai-smartphones-fertility-crisis-birth-rates) — HIGH (fetch-verified title/date).
- [Andrew Ng transcript](https://ulisten.ai/channels/silicon-valley-girl/andrew-ng-the-biggest-opportunities-in-ai-arent-where-you-th_o-wv_szZ0V0/transcript) — HIGH.
- Demographers: [Lutz 2024](https://epub.oeaw.ac.at/0xc1aa5572%200x003fb946.pdf), [Lutz & Marois 2026](https://iiasa.ac.at/news/mar-2026/is-low-fertility-really-economic-threat), [Lutz 2023](https://epub.oeaw.ac.at/0xc1aa5572%200x003fa366.pdf), [Lee 2025](https://onlinelibrary.wiley.com/doi/10.1111/padr.12674), [Lee 2003](https://pubs.aeaweb.org/doi/10.1257/089533003772034943), [UC Berkeley Lee](https://www.demog.berkeley.edu/faculty/ronald-demos-lee), [Wilmoth/UN News](https://news.un.org/en/story/2023/04/1135967) — HIGH.

### 12.4 Repositories, predictions, and surveys (43 sources)

- [Metaculus general AI](https://www.metaculus.com/questions/5121/date-of-artificial-general-intelligence/) and [weakly general AI](https://www.metaculus.com/questions/3479/date-weakly-general-ai-system-is-devised/) — HIGH snapshots.
- [Polymarket OpenAI AGI 2027](https://polymarket.com/event/openai-announces-it-has-achieved-agi-before-2027), [NEXTPredict crosswalk](https://nextpredict.io/prediction-markets/technology/agi-timeline/), [PredictPedia Kalshi](https://predictpedia.com/events/JMAJCw/when-will-any-company-achieve-agi) — HIGH/MEDIUM.
- [AI Impacts 2023 ESPAI](https://wiki.aiimpacts.org/ai_timelines/predictions_of_human-level_ai_timelines/ai_timeline_surveys/2023_expert_survey_on_progress_in_ai) — HIGH.
- [IGM/Clark Center — AI and the Labor Market](https://kentclarkcenter.org/surveys/ai-and-the-labor-market/), [AI and Productivity Growth](https://kentclarkcenter.org/surveys/ai-and-productivity-growth-2/), [XPT](https://forum.effectivealtruism.org/posts/KGGDduXSwZQTQJ9xc/what-do-xpt-forecasts-tell-us-about-ai-timelines) — HIGH/MEDIUM.
- All GitHub repositories listed in §10 plus [EIG-Research/EIG-ai-unemp-she-wrote](https://github.com/EIG-Research/EIG-ai-unemp-she-wrote), [emilesilvis/eu-jobs](https://github.com/emilesilvis/eu-jobs), [jamiemaguiredotnet/AIJobExposure](https://github.com/jamiemaguiredotnet/AIJobExposure), [ETRI-Activity3D](https://ai4robot.github.io/etri-activity3d/) — HIGH.

---

*Confidence labels and exact figures follow the four research dossiers compiled 17 November 2026. Where sources disagree, both figures are reported rather than silently reconciled. This report is a synthesis, not a forecast.*
