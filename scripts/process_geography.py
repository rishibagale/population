import sys
import os
import gzip

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"C:\Users\rushi\OneDrive\Desktop\random_projects\population_reserch"
RAW = os.path.join(ROOT, "data", "raw")
PROC = os.path.join(ROOT, "data", "processed")

# World Bank high-income economies (current classification, ISO3)
HIGH_INCOME = set(
    """AND ARE AUS AUT BHS BHR BRB BLZ BRN CAN CHE CHL CYP CZE DEU DNK ESP EST FIN FRA
GBR GRC HKG HRV HUN IRL ISL ISR ITA JPN KOR KWT LIE LUX LVA LTU MAC MCO MLT MNE NLD
NOR NZL OMN PAN POL PRT QAT ROU SAU SGP SMR SVK SVN SWE TWN USA URY""".split()
)

# The 7 aggregate LocIDs we keep for the region file: World + 6 continents
REGION_IDS = {900: "World", 903: "Africa", 935: "Asia", 908: "Europe",
              904: "Latin America and the Caribbean", 905: "Northern America",
              909: "Oceania"}

print("== load TotalPopulationByVariant (Medium) ==")
pop = pd.read_csv(os.path.join(PROC, "un_wpp_total_population_by_variant.csv"),
                  usecols=["LocID", "ISO3_code", "Location", "Variant", "year",
                           "population_thousands"])
med = pop[pop["Variant"] == "Medium"].copy()

countries = med[med["ISO3_code"].notna()].copy()
countries = countries.sort_values(["ISO3_code", "year"])
countries = countries[["ISO3_code", "Location", "year", "population_thousands"]]
countries.columns = ["iso3", "location", "year", "population_thousands"]
countries.to_csv(os.path.join(PROC, "country_population_medium_1950_2100.csv"), index=False)
print("country rows:", len(countries), "| countries:", countries["iso3"].nunique())

regions = med[med["LocID"].isin(REGION_IDS.keys())].copy()
regions["continent"] = regions["LocID"].map(REGION_IDS)
regions = regions.sort_values(["continent", "year"])
regions = regions[["continent", "LocID", "year", "population_thousands"]]
regions.columns = ["region", "locid", "year", "population_thousands"]
regions.to_csv(os.path.join(PROC, "region_population_medium_1950_2100.csv"), index=False)
print("region rows:", len(regions))

print("== load Demographic Indicators (Medium) ==")
cols = ["ISO3_code", "Location", "Time", "TPopulation1July", "TFR", "Births",
        "Deaths", "PopGrowthRate", "NetMigrations", "MedianAgePop"]
demo = pd.read_csv(
    os.path.join(RAW, "WPP2024_Demographic_Indicators_Medium.csv.gz"),
    usecols=cols, dtype={"ISO3_code": str})
demo_countries = demo[demo["ISO3_code"].notna()].copy()
demo_countries = demo_countries.rename(columns={
    "ISO3_code": "iso3", "Location": "location", "Time": "year",
    "TPopulation1July": "population_1july_thousands",
    "TFR": "tfr_children_per_woman", "Births": "births_thousands",
    "Deaths": "deaths_thousands", "PopGrowthRate": "pop_growth_rate_pct",
    "NetMigrations": "net_migration_thousands", "MedianAgePop": "median_age_years"})
demo_countries = demo_countries.sort_values(["iso3", "year"])
demo_countries = demo_countries[["iso3", "location", "year",
                                 "population_1july_thousands", "tfr_children_per_woman",
                                 "births_thousands", "deaths_thousands",
                                 "pop_growth_rate_pct", "net_migration_thousands",
                                 "median_age_years"]]
demo_countries.to_csv(os.path.join(PROC, "un_wpp_country_demographic_indicators_1950_2100.csv"),
                      index=False)
print("demographic rows:", len(demo_countries))

print("== country summary ==")
base = countries[countries["year"].isin([2024, 2050, 2100])].pivot_table(
    index="iso3", columns="year", values="population_thousands")
base.columns = ["pop_2024_thousands", "pop_2050_thousands", "pop_2100_thousands"]

peaks = countries.groupby("iso3")["population_thousands"].agg(["idxmax", "max"])
peak_years = countries.loc[peaks["idxmax"], ["iso3", "year"]].set_index("iso3")["year"]

d = demo_countries[demo_countries["year"].isin([2023, 2026, 2050, 2100])].pivot_table(
    index="iso3", columns="year", values="tfr_children_per_woman")
d.columns = ["tfr_2023_observed", "tfr_2026_proj", "tfr_2050_proj", "tfr_2100_proj"]

loc = countries.groupby("iso3")["location"].last()
summary = base.join(loc).join(peak_years.rename("peak_year")).join(
    peaks["max"].rename("peak_pop_thousands")).join(d)
summary["growth_2024_2050_pct"] = (summary["pop_2050_thousands"] / summary["pop_2024_thousands"] - 1) * 100
summary["growth_2050_2100_pct"] = (summary["pop_2100_thousands"] / summary["pop_2050_thousands"] - 1) * 100
summary["income_class"] = ["high_income" if i in HIGH_INCOME else "developing" for i in summary.index]
summary["trend"] = ["shrinking" if p < r else "growing"
                    for r, p in zip(summary["pop_2024_thousands"], summary["pop_2100_thousands"])]
summary = summary.reset_index().rename(columns={"iso3": "iso3_code", "index": "iso3_code"})
order = ["iso3_code", "location", "income_class", "trend", "pop_2024_thousands",
         "pop_2050_thousands", "pop_2100_thousands", "growth_2024_2050_pct",
         "growth_2050_2100_pct", "peak_year", "peak_pop_thousands",
         "tfr_2023_observed", "tfr_2026_proj", "tfr_2050_proj", "tfr_2100_proj"]
summary = summary[order].sort_values("pop_2024_thousands", ascending=False)
summary.to_csv(os.path.join(PROC, "country_summary_medium.csv"), index=False)
print("summary rows:", len(summary))

print("== top 20s ==")
top20_all = summary.head(20)[["iso3_code", "location", "income_class", "pop_2024_thousands"]]
top20_all.insert(0, "rank", range(1, 21))
top20_all.to_csv(os.path.join(PROC, "top20_by_population_2024.csv"), index=False)

for cls, fname in (("high_income", "top20_developed_summary.csv"),
                   ("developing", "top20_developing_summary.csv")):
    sub = summary[summary["income_class"] == cls].head(20).copy()
    sub.insert(0, "rank", range(1, 21))
    sub.to_csv(os.path.join(PROC, fname), index=False)
    print(fname, "rows:", len(sub))

print("== developed vs developing world (1950-2100) ==")
cl = countries.merge(summary[["iso3_code", "income_class"]], left_on="iso3",
                     right_on="iso3_code")
split = cl.groupby(["year", "income_class"])["population_thousands"].sum().unstack()
split.columns = ["developing_thousands", "developed_thousands"]
split = split.reset_index()
split.to_csv(os.path.join(PROC, "developed_vs_developing_world.csv"), index=False)
print(split.head(3).to_string(), "\n", split.tail(3).to_string())
print("DONE")
