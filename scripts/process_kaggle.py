import pandas as pd
from pathlib import Path

RAW = Path(r"C:\Users\rushi\OneDrive\Desktop\random_projects\population_reserch\data\raw\kaggle")
OUT = Path(r"C:\Users\rushi\OneDrive\Desktop\random_projects\population_reserch\data\processed")
OUT.mkdir(parents=True, exist_ok=True)

def num(s):
    if pd.isna(s):
        return pd.NA
    return int(str(s).replace(",", "").strip())

def pct(s):
    if pd.isna(s):
        return pd.NA
    return float(str(s).replace("%", "").strip())

# ---- 1. Worldometers historical world population (1955-2023) ----
p = RAW / "wp_1951_2023" / "World_population(1955-2023).csv"
df = pd.read_csv(p)
tidy = pd.DataFrame({
    "year": df["Year (July 1)"].astype(int),
    "population": df["Population"].map(num),
    "yearly_change_pct": df["Yearly % Change"].map(pct),
    "yearly_change": df["Yearly Change"].map(num),
    "median_age": df["Median Age"],
    "fertility_rate_children_per_woman": df["Fertility Rate"],
    "density_per_km2": df["Density (P/Km²)"].map(num),
})
tidy = tidy.sort_values("year")
tidy.to_csv(OUT / "kaggle_worldometers_world_population_1955_2023.csv", index=False)
print("worldometers historical:", tidy.shape, tidy.iloc[[0, -1]].to_dict("records"))

# ---- 2. Worldometers projections (2020-2100) ----
p = RAW / "wp_1951_2023" / "World Population Projections(2020-2100).csv"
df = pd.read_csv(p)
df.columns = [c.strip() for c in df.columns]
tidy2 = pd.DataFrame({
    "year": df["Year"].astype(int),
    "population": df["World Population"].map(num),
    "yearly_change_frac": df["Yearly Change"],
    "yearly_change": df["Net Change"].map(num),
    "density_per_km2": df["Density (P/Km²)"].map(num),
})
tidy2 = tidy2.sort_values("year")
tidy2.to_csv(OUT / "kaggle_worldometers_projection_2020_2100.csv", index=False)
print("worldometers projection:", tidy2.shape, tidy2.iloc[[0, 1, -1]].to_dict("records"))

# ---- 3. US Census national population (annual) ----
pop = pd.read_csv(RAW / "census_time_series" / "POP.csv")   # monthly, thousands, 1952+
poph = pd.read_csv(RAW / "census_time_series" / "POPH.csv")  # annual, persons, 1900+
pop["date"] = pd.to_datetime(pop["date"])
pop["year"] = pop["date"].dt.year
july = pop[pop["date"].dt.month == 7].copy()  # July 1 mid-year estimate
july = july.assign(population_thousands=july["value"]).loc[:, ["year", "population_thousands"]]
poph["date"] = pd.to_datetime(poph["date"])
poph["year"] = poph["date"].dt.year
poph = poph.assign(population_persons=poph["value"]).loc[:, ["year", "population_persons"]]
poph["population_thousands"] = (poph["population_persons"] / 1000).round(1)
poph = poph.loc[:, ["year", "population_thousands"]]
census = pd.concat([poph[poph["year"] < 1952], july], ignore_index=True).sort_values("year")
census.to_csv(OUT / "us_census_us_population_1900_2019.csv", index=False)
print("us census:", census.shape, census.iloc[[0, 20, -1]].to_dict("records"))

# ---- 4. UN 2019 World Fertility Dataset: survey-based TFR ----
tfr = pd.read_csv(RAW / "un_fertility" / "TFR.csv")
tfr = tfr[tfr["Indicator"] == "TFR"].copy()
tfr["year"] = tfr["Date - Year"].apply(lambda x: int(x // 1) if pd.notna(x) else pd.NA)
tidy4 = tfr.loc[:, ["Country or Area", "Country or Area Code", "year",
                    "Value - Total fertility (TFR)", "Data Source Name (short)", "Reference Year"]].copy()
tidy4.columns = ["country", "m49_code", "year", "tfr_children_per_woman", "data_source", "reference_year"]
tidy4["tfr_children_per_woman"] = pd.to_numeric(tidy4["tfr_children_per_woman"], errors="coerce")
tidy4 = tidy4.dropna(subset=["tfr_children_per_woman"]).sort_values(["country", "year"])
tidy4.to_csv(OUT / "un_fertility_tfr_survey_1960_2019.csv", index=False)
print("un fertility TFR:", tidy4.shape, tidy4["country"].nunique(), "countries",
      int(tidy4["year"].min()), "-", int(tidy4["year"].max()))

# quick cross-check vs OWID TFR for a few countries around 2019
owid = pd.read_csv(OUT / "owid_fertility_rate_tfr.csv")
owid = owid.rename(columns={"Entity": "country", "Year": "year"})
ycol = "year"
ccol = "country"
for country in ["India", "Nigeria", "Brazil", "Japan", "United States", "Germany"]:
    survey = tidy4[(tidy4["country"] == country) & (tidy4["year"].between(2015, 2019))]
    s = survey["tfr_children_per_woman"].mean() if len(survey) else None
    o = owid[(owid[[c for c in owid.columns if "country" in c or "name" in c][0]] == country) & (owid[ycol] == 2019)]
    print(country, "survey~", round(float(s), 2) if s is not None else None,
          "| owid2019:", o["tfr_children_per_woman"].iloc[0] if len(o) else "n/a")
