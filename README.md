# World Population, Birth Rates & Long-Term Projections

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/pandas-analysis-150458.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/matplotlib-charts-11557C.svg)](https://matplotlib.org/)

A multi-source demographic research project built on the **UN World Population Prospects 2024**, **Our World in Data**, the **World Bank**, **Gapminder**, the **CIA World Factbook**, and three Kaggle datasets. It cleans and harmonizes ~40 datasets into tidy CSVs and produces 19 publication-style charts covering world, continental, and country-level population and fertility trajectories through 2100.

**The full written analysis with every finding, table, and chart is in [`reports/report.md`](reports/report.md).**

A companion study on the consequences of low fertility and what can be done about it is in [`reports/consequences_and_solutions.md`](reports/consequences_and_solutions.md).

## Formats & live site

- **Read online**: the full site (landing page + both reports, all charts) is served via GitHub Pages at **https://rishibagale.github.io/population**
- **PDF**: [`reports/population_report.pdf`](reports/population_report.pdf) (3.0 MB) and [`reports/consequences_and_solutions.pdf`](reports/consequences_and_solutions.pdf) (1.9 MB) — print-ready versions with charts
- **Markdown**: [`reports/report.md`](reports/report.md) and [`reports/consequences_and_solutions.md`](reports/consequences_and_solutions.md)
- To rebuild the site locally: `pip install markdown` then `python build_site.py` (writes `docs/`)

---

## Contents

- [Headline findings](#headline-findings)
- [Consequences & solutions](#consequences--solutions)
- [Repository layout](#repository-layout)
- [Charts](#charts)
- [Data sources](#data-sources)
- [Reproducibility](#reproducibility)
- [License](#license)
- [Report an issue](#report-an-issue)

---

## Consequences & solutions

A second, dedicated study: what happens when births fall far below replacement — depopulation of working-age cohorts, pension and care burden, shrinking tax bases, innovation slowdown, rural hollowing — and an evidence-based menu of responses (pro-natal policy and what it can realistically achieve, labor-force participation, migration, automation/AI productivity, pension reform), with honest trade-offs and which countries are already testing each approach. Findings include: pro-natal packages reliably lift TFR only ~0.1–0.3 (France 1.8, Korea ~1.3 despite $230B since 2006); a 10pp-higher 55–64 employment rate can offset roughly a third of a decade of workforce shrinkage; and age-based pension reform vs. higher productivity is a quantified trade-off (each +1pp in the 65+ dependency share historically costs about 0.2–0.3pp of per-capita GDP growth absent offsetting gains).

---

## Headline findings

- The world reached **8.16 billion in 2024**; under the UN Medium scenario it peaks at **~10.3 billion in the mid-2080s**, then declines. The 2100 High–Low spread (14.4B vs 7.0B) is wider than today's entire population.
- Global fertility collapsed from **4.85 children per woman (1950)** to **~2.25 today**, crossing below replacement (2.1) in the 2050s and ending near **1.84 by 2100**.
- The **65+ population triples** from 0.83B to 2.44B by 2100; the under-15 cohort never grows again.
- **Africa takes the baton**: 1.52B → 3.82B, the only region still growing at 2100. Asia peaks at 5.29B in 2054; Europe's 2100 population is *smaller* than its 1950 population.
- China shrinks **1.42B → 0.63B (−55%)** by 2100; India peaks at ~1.70B around 2061.
- Birth rates are already below replacement in **77 of 179** developing countries and **36 of 58** high-income countries — the fertility transition has reached most of the Global South.

---

## Repository layout

```
├── charts/          19 PNG charts (150 dpi), numbered by report section
├── data/
│   ├── raw/         original source files (not committed — see sources table)
│   └── processed/   26 tidy CSVs produced by scripts/
├── docs/            GitHub Pages site (index.html + HTML reports, built by build_site.py)
├── reports/
│   ├── report.md                            the full analysis, section by section
│   ├── consequences_and_solutions.md        the companion low-fertility study
│   ├── population_report.pdf                print-ready full report
│   └── consequences_and_solutions.pdf       print-ready companion study
├── build_site.py    builds docs/ HTML from the reports (pip install markdown)
├── scripts/         pandas + matplotlib pipelines (see Reproducibility)
├── LICENSE          MIT
└── README.md
```

---

## Charts

### World population & projection uncertainty

![World population by projection variant](charts/01_world_population_variants.png)

*Historical growth 1950–2024 (solid) with Low / Medium / High WPP variants (dashed). All projection statements in this repo are Medium-scenario-conditional.*

![UN Medium vs Worldometers projection](charts/08a_un_vs_worldometers_projection.png)

*Independent tracker lineage: Worldometers lands 690M above UN Medium at 2100, driven by slower assumed fertility decline.*

### Fertility transition

![Global total fertility rate](charts/02_global_tfr.png)

![World TFR, UN/OWID vs Worldometers](charts/08b_world_tfr_sources.png)

![World TFR, UN WPP 2024 Medium](charts/12_world_tfr_medium.png)

*Fertility halves in two generations and crosses replacement (~2.1) in the 2050s — the single curve that every continental future flows from.*

### Birth rates: source convergence & country extremes

![World crude birth rate, three sources](charts/03_world_cbr_sources.png)

*Three fully independent pipelines (UN-derived, World Bank, Gapminder) agree on the world crude birth rate, which has fallen to one-third of its 1950 value.*

![Country birth rate trends, selected countries](charts/05_country_birth_rate_trends.png)

![Top 15 countries by birth rate, 2025 (CIA)](charts/06_cia_top15_birth_rate_2025.png)

*Somalia 46.4 vs South Korea 4.3 births per 1,000 — a 10x gap, the widest in recorded demographic history.*

### Age structure & regions

![Age structure evolution, Medium scenario](charts/04_age_structure_evolution.png)

![Regional population, Medium scenario](charts/07_regional_population.png)

![Continental populations 1950-2100](charts/09_continents_1950_2100_medium.png)

### Country futures: developed vs developing

![Top 10 countries, Medium variant](charts/10_top10_countries_medium.png)

![Developed vs developing world](charts/11_developed_vs_developing.png)

![Top 40 country trajectories](charts/13_country_grid_focus.png)

*Two futures dominate the developed world: immigration-sustained growth (US, Canada, Australia, Gulf states) and demographic contraction (Korea −58% by 2100, Japan −38%). Of 237 countries, only 75 are still growing at 2100.*

### Fertility & birth-rate trajectories, 1950–2100

![Top 20 TFR trajectories](charts/14_top20_tfr_grid.png)

![Top 20 CBR trajectories](charts/15_top20_cbr_grid.png)

![Continental TFR, WPP Medium](charts/16_continents_tfr.png)

![Continental CBR, WPP Medium](charts/17_continents_cbr.png)

*Top-20 country grids (developing = green, high income = blue; dashed = projection; dotted gray = replacement level) and continental trajectories. Africa is the only region above 2.5 in 2100; world CBR halves twice, 36.8 → 16.2 → 10.4.*

---

## Data sources

| Source | Coverage | Notes |
|--------|----------|-------|
| [UN WPP 2024](https://population.un.org/wpp/) | All countries + regions, 1950–2100 | Gold standard; Medium variant + variants; age/sex detail. Data files published under CC BY 3.0 IGO |
| [Our World in Data](https://ourworldindata.org/fertility-rate) | Countries, 1950–2100 | Harmonized UN/GM/IHME series (CC BY) |
| [World Bank](https://data.worldbank.org/indicator/SP.DYN.CBRT.IN) `SP.DYN.CBRT.IN` | Countries, ~1960–2023 | CC BY 4.0 |
| [Gapminder](https://www.gapminder.org/data/) | Countries, 1800–2100 | Longest historical horizon; estimates pre-1950 (CC BY 4.0) |
| [CIA World Factbook](https://www.cia.gov/the-world-factbook/) | 275 countries, 1990–2025 | Current-year birth-rate estimates (public domain) |
| [Kaggle: world-population-19512020](https://www.kaggle.com/datasets/sandhyakrishnan02/world-population-19512020) | World, 1955–2023 + projection | Worldometers lineage (CC0-1.0) |
| [Kaggle: population-time-series-data](https://www.kaggle.com/datasets/census/population-time-series-data) | US, 1900–2019 (POP/POPH) | US Census Bureau (public domain) |
| [Kaggle: ivanchvez/fertility](https://www.kaggle.com/datasets/ivanchvez/fertility) | 201 countries, survey TFR ~1950–2018 | UN World Fertility Dataset 2019 (CC0-1.0) |

> **Raw data is not committed** (it is freely downloadable from the links above and totals ~500 MB). Download to `data/raw/` following the layout in `scripts/` to reproduce.

---

## Reproducibility

Run the scripts in order with Python 3.10+ (`pandas`, `matplotlib`):

```bash
pip install pandas matplotlib
python scripts/process_data.py            # WPP/OWID/WB/Gapminder/CIA → data/processed/
python scripts/process_geography.py       # country & continent population futures
python scripts/process_kaggle.py          # Kaggle validation datasets
python scripts/process_birth_fertility.py # top-20 TFR/CBR series (WPP backbone, no fills needed)
python scripts/make_charts.py             # charts 01–07, 12
python scripts/make_chart08.py            # charts 08a/08b/08c
python scripts/make_charts_geo.py         # charts 09–13
python scripts/make_charts_tfr_cbr.py     # charts 14–17
python scripts/verify_geo.py              # sanity checks
```

Processing gotchas are documented in [`reports/report.md` §14](reports/report.md#14-reproducibility) — notably that WPP `PopTotal` is in **thousands**, region `LocID`s differ from common assumptions (Asia = 935, Africa = 903), and the WPP Demographic Indicators file carries an all-NaN placeholder row per entity for year 2101.

---

## License

Code in this repository is released under the [MIT License](LICENSE).

Processed and chart outputs are derived from the sources above; each retains its original terms (UN WPP: CC BY 3.0 IGO; OWID / World Bank / Gapminder: CC BY; Kaggle datasets: CC0 or CC BY as noted; CIA Factbook: public domain). Attribution to the original sources is preserved in the `reports/report.md` source table.

---

## Report an issue

Found an error in the analysis, a data-processing bug, or a chart that looks wrong? Please [open an issue](https://github.com/rishibagale/population/issues) with the affected chart or CSV name and the source in question. Corrections to headline numbers are especially welcome.
