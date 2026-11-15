# -*- coding: utf-8 -*-
"""Phase 1: Build TFR + CBR datasets for top-20 countries and continents.

Outputs (data/processed/):
  country_tfr_cbr_1950_2100.csv   -- tidy long: iso3, location, year, tfr, cbr, is_projected
  continent_tfr_cbr_1950_2100.csv -- tidy long: LocID-keyed, world + 6 continents
  fill_log.csv                    -- every fill applied per country/year
Prints fill statistics.
"""
import os
import pandas as pd
import numpy as np

ROOT = r"C:\Users\rushi\OneDrive\Desktop\random_projects\population_reserch"
RAW = os.path.join(ROOT, "data", "raw", "WPP2024_Demographic_Indicators_Medium.csv.gz")
PROC = os.path.join(ROOT, "data", "processed")

PROJ_YEAR = 2025  # WPP 2024: observed through 2024 (some data to 2023)

# ---------- 1. Load raw WPP ----------
cols = ["LocID", "ISO3_code", "Location", "Time", "TPopulation1July", "Births", "CBR", "TFR"]
df = pd.read_csv(RAW, usecols=cols, low_memory=False)

df = df[df.Time <= 2100]  # drop 2101 placeholder rows (all NaN)

# ---------- 2. Countries ----------
countries = df[df.ISO3_code.notna()].copy()
countries["tfr"] = countries["TFR"].astype(float)
# CBR: prefer native CBR col, else compute
countries["cbr"] = np.where(
    countries["CBR"].notna(),
    countries["CBR"].astype(float),
    countries["Births"] / countries["TPopulation1July"] * 1000.0,
)
countries["is_projected"] = countries["Time"] >= PROJ_YEAR
out_c = countries.rename(columns={
    "ISO3_code": "iso3", "Location": "location", "Time": "year",
})[["iso3", "location", "year", "tfr", "cbr", "is_projected"]].sort_values(["location", "year"])
out_c.to_csv(os.path.join(PROC, "country_tfr_cbr_1950_2100.csv"), index=False)
print("country_tfr_cbr_1950_2100.csv:", out_c.shape,
      "| countries:", out_c.iso3.nunique(), "| NaN tfr:", out_c.tfr.isna().sum(),
      "| NaN cbr:", out_c.cbr.isna().sum())

# ---------- 3. Continents ----------
AGG = {900: "World", 903: "Africa", 935: "Asia", 908: "Europe",
       904: "Latin America and the Caribbean", 905: "Northern America", 909: "Oceania"}
agg = df[df.LocID.isin(AGG.keys())].copy()
agg["region"] = agg.LocID.map(AGG)
agg["tfr"] = agg["TFR"].astype(float)
agg["cbr"] = np.where(
    agg["CBR"].notna(),
    agg["CBR"].astype(float),
    agg["Births"] / agg["TPopulation1July"] * 1000.0,
)
agg["is_projected"] = agg["Time"] >= PROJ_YEAR
out_a = agg.rename(columns={"Time": "year"})[["region", "LocID", "year", "tfr", "cbr", "is_projected"]]\
    .sort_values(["region", "year"])
out_a.to_csv(os.path.join(PROC, "continent_tfr_cbr_1950_2100.csv"), index=False)
print("continent_tfr_cbr_1950_2100.csv:", out_a.shape,
      "| regions:", out_a.region.nunique(), "| NaNs:", out_a.isna().sum().sum())

# ---------- 4. Orchestration / fill for top-20 countries ----------
top20 = pd.read_csv(os.path.join(PROC, "top20_by_population_2024.csv"))
top20_iso = set(top20.iso3_code)

backbone = out_c[out_c.iso3.isin(top20_iso)].copy()  # tidy: iso3, location, year, tfr, cbr, is_projected

# observed sources
owid = pd.read_csv(os.path.join(PROC, "owid_fertility_rate_tfr.csv"))
owid = owid[owid.Code.notna() & owid.Code.isin(top20_iso)].rename(
    columns={"Code": "iso3", "Year": "year", "tfr_children_per_woman": "obs_tfr"}
)[["iso3", "year", "obs_tfr"]]

wbcbr = pd.read_csv(os.path.join(PROC, "world_bank_crude_birth_rate.csv"))
wbcbr = wbcbr[wbcbr.iso3.notna() & wbcbr.iso3.isin(top20_iso)].rename(
    columns={"iso3": "iso3", "year": "year", "crude_birth_rate_per_1000": "obs_cbr"}
)[["iso3", "year", "obs_cbr"]]

merged = backbone.merge(owid, on=["iso3", "year"], how="left").merge(wbcbr, on=["iso3", "year"], how="left")

fill_log_rows = []
fills = {"tfr": 0, "cbr": 0}

for iso in sorted(top20_iso):
    g = merged[merged.iso3 == iso].sort_values("year").copy()
    loc = g.location.iloc[0]
    hist = g.year < PROJ_YEAR

    for col, obs_col in (("tfr", "obs_tfr"), ("cbr", "obs_cbr")):
        # (a) keep observed value where present (projected years stay WPP)
        has_obs = g[obs_col].notna()
        vals = g[col].copy()
        vals[has_obs] = g.loc[has_obs, obs_col]
        # (b) interpolate remaining historical NaNs (linear on year index)
        isna = vals.isna() & hist.values
        if isna.any():
            interp = vals.interpolate(method="linear", limit_area="inside")
            fixed = isna & interp.notna()
            vals[fixed] = interp[fixed]
            for yr in g.loc[fixed, "year"]:
                fill_log_rows.append({"iso3": iso, "location": loc, "year": int(yr),
                                      "column": col, "source": "linear_interpolation"})
            fills[col] += int(fixed.sum())
        # (c) remaining historical NaNs -> nearest WPP value (ffill/bfill)
        isna2 = vals.isna() & hist.values
        if isna2.any():
            nearest = vals.ffill().bfill()
            fixed2 = isna2 & nearest.notna()
            vals[fixed2] = nearest[fixed2]
            for yr in g.loc[fixed2, "year"]:
                fill_log_rows.append({"iso3": iso, "location": loc, "year": int(yr),
                                      "column": col, "source": "nearest_wpp_value"})
            fills[col] += int(fixed2.sum())
        g[col] = vals

    # merge back
    merged.loc[merged.iso3 == iso, ["tfr", "cbr"]] = g[["tfr", "cbr"]].values

coverage = merged.groupby("iso3").agg(
    obs_tfr_years=("obs_tfr", lambda s: int(s.notna().sum())),
    obs_cbr_years=("obs_cbr", lambda s: int(s.notna().sum())),
)
merged = merged[["iso3", "location", "year", "tfr", "cbr", "is_projected"]]\
    .sort_values(["location", "year"])
merged.to_csv(os.path.join(PROC, "top20_tfr_cbr_filled_1950_2100.csv"), index=False)

if fill_log_rows:
    fill_log = pd.DataFrame(fill_log_rows).sort_values(["location", "year", "column"])
    by_country = fill_log.groupby(["location", "column"]).size().unstack(fill_value=0)
    print(by_country.to_string())
else:
    fill_log = pd.DataFrame(columns=["iso3", "location", "year", "column", "source"])
    print("no fills were needed: WPP backbone complete for all top-20 countries 1950-2100")
    # observed-source coverage report (documentation for the report)
    iso2loc = merged.drop_duplicates("iso3").set_index("iso3")["location"]
    cov = coverage.rename(index=iso2loc.to_dict())
    print(cov.sort_index().to_string())
fill_log.to_csv(os.path.join(PROC, "fill_log.csv"), index=False)
print("fill_log.csv rows:", len(fill_log))

print("top20_tfr_cbr_filled_1950_2100.csv:", merged.shape,
      "| NaN tfr:", merged.tfr.isna().sum(), "| NaN cbr:", merged.cbr.isna().sum())
print("fill counts (interpolation + nearest):", fills)

# ---------- 5. Sanity checks ----------
checks = {
    ("IND", 2023): ("tfr", 1.98), ("CHN", 2023): ("tfr", 1.00), ("NGA", 2024): ("tfr", 4.48),
    ("World", 2024): ("cbr", 16.2), ("Africa", 2024): ("tfr", 4.015),
}
c22 = merged[(merged.iso3 == "IND") & (merged.year == 2023)]
print("sanity IND tfr 2023 =", round(c22.tfr.iloc[0], 3), "(expect ~1.98)")
c2 = out_c[(out_c.iso3 == "CHN") & (out_c.year == 2023)]
print("sanity CHN tfr 2023 =", round(c2.tfr.iloc[0], 3), "(expect ~1.00)")
w = out_a[(out_a.region == "World") & (out_a.year == 2024)]
print("sanity World cbr 2024 =", round(w.cbr.iloc[0], 2), "(expect ~16.2)")
af = out_a[(out_a.region == "Africa") & (out_a.year == 2024)]
print("sanity Africa tfr 2024 =", round(af.tfr.iloc[0], 3), "(expect ~4.015)")
