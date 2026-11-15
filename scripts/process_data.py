import gzip, os, io
import pandas as pd

RAW = r"data\raw"
OUT = r"data\processed"
os.makedirs(OUT, exist_ok=True)

# ---------- 1. UN WPP total population by variant ----------
print("WPP TotalPopulationBySex ...")
cols = ["LocID", "ISO3_code", "Location", "Variant", "Time", "PopMale", "PopFemale", "PopTotal"]
df = pd.read_csv(os.path.join(RAW, "WPP2024_TotalPopulationBySex.csv.gz"),
                 usecols=cols, dtype={"ISO3_code": "string"})
df = df.rename(columns={"Time": "year", "PopMale": "pop_male_thousands",
                        "PopFemale": "pop_female_thousands",
                        "PopTotal": "population_thousands"})
df.to_csv(os.path.join(OUT, "un_wpp_total_population_by_variant.csv"), index=False)
print(f"  rows={len(df):,}, variants={df['Variant'].unique().tolist()}")

# World total by variant (LocID 900) for chart simplicity
world = df[df["LocID"] == 900]
world = world[["Variant", "year", "population_thousands"]]
world.to_csv(os.path.join(OUT, "un_wpp_world_population_by_variant.csv"), index=False)
print(f"  world rows={len(world):,}")

del df, world

# ---------- 2. UN WPP single-age -> 5-year age groups ----------
def aggregate_age_file(fname, location_filter=None):
    """Read single-age-sex file in chunks, aggregate to 5-year age groups."""
    usecols = ["LocID", "ISO3_code", "Location", "Variant", "Time",
               "AgeGrpStart", "PopMale", "PopFemale", "PopTotal"]
    out_frames = []
    it = pd.read_csv(gzip.open(os.path.join(RAW, fname), "rt", encoding="utf-8-sig"),
                     usecols=usecols, chunksize=2_000_000,
                     dtype={"ISO3_code": "string", "Location": "string"})
    for chunk in it:
        if location_filter is not None:
            chunk = chunk[chunk["LocID"].isin(location_filter)]
        chunk["age_group_start"] = (chunk["AgeGrpStart"] // 5 * 5).clip(upper=100)
        g = (chunk.groupby(["LocID", "ISO3_code", "Location", "Variant", "Time", "age_group_start"],
                           as_index=False, observed=True, dropna=False)
             [["PopMale", "PopFemale", "PopTotal"]].sum())
        out_frames.append(g)
    res = pd.concat(out_frames, ignore_index=True)
    res = res.groupby(["LocID", "ISO3_code", "Location", "Variant", "Time", "age_group_start"],
                      as_index=False, observed=True, dropna=False)[["PopMale", "PopFemale", "PopTotal"]].sum()
    return res

print("WPP Medium 1950-2023 age groups ...")
med_hist = aggregate_age_file("WPP2024_PopulationBySingleAgeSex_Medium_1950-2023.csv.gz")
print("WPP Medium 2024-2100 age groups ...")
med_proj = aggregate_age_file("WPP2024_PopulationBySingleAgeSex_Medium_2024-2100.csv.gz")
medium = pd.concat([med_hist, med_proj], ignore_index=True)
medium = medium.rename(columns={"Time": "year", "age_group_start": "age_group_start",
                                "PopMale": "pop_male_thousands", "PopFemale": "pop_female_thousands",
                                "PopTotal": "pop_total_thousands"})
medium.to_csv(os.path.join(OUT, "un_wpp_age_groups_medium_1950_2100.csv"), index=False)
print(f"  medium age-group rows={len(medium):,}")
del med_hist, med_proj, medium

print("WPP High/Low 2024-2100 (World only) ...")
world_ids = [900]
high = aggregate_age_file("WPP2024_PopulationBySingleAgeSex_High_2024-2100.csv.gz", world_ids)
low = aggregate_age_file("WPP2024_PopulationBySingleAgeSex_Low_2024-2100.csv.gz", world_ids)
hl = pd.concat([high, low], ignore_index=True)
hl = hl.rename(columns={"Time": "year", "PopMale": "pop_male_thousands",
                        "PopFemale": "pop_female_thousands", "PopTotal": "pop_total_thousands"})
hl.to_csv(os.path.join(OUT, "un_wpp_age_groups_world_high_low_2024_2100.csv"), index=False)
print(f"  high/low rows={len(hl):,}")
del high, low, hl

# ---------- 3. OWID ----------
print("OWID ...")
for src, outname, rename in [
    ("owid_children-per-woman-un.csv", "owid_fertility_rate_tfr.csv", {"Fertility rate": "tfr_children_per_woman"}),
    ("owid_crude-birth-rate.csv", "owid_crude_birth_rate.csv", {"Birth rate": "crude_birth_rate_per_1000"}),
    ("owid_population-with-un-projections.csv", "owid_population_with_un_projections.csv", None),
]:
    d = pd.read_csv(os.path.join(RAW, src))
    print(f"  {src}: cols={d.columns.tolist()}, rows={len(d):,}")
    if rename:
        d = d.rename(columns=rename)
    d.to_csv(os.path.join(OUT, outname), index=False)

# ---------- 4. World Bank CBR ----------
print("World Bank CBR ...")
wb = pd.read_csv(os.path.join(RAW, "wb_cbr", "API_SP.DYN.CBRT.IN_DS2_en_csv_v2_74855.csv"),
                 skiprows=4)
year_cols = [c for c in wb.columns if c.isdigit()]
wbm = wb.melt(id_vars=["Country Name", "Country Code"], value_vars=year_cols,
              var_name="year", value_name="crude_birth_rate_per_1000")
wbm = wbm.dropna(subset=["crude_birth_rate_per_1000"])
wbm = wbm.rename(columns={"Country Name": "entity", "Country Code": "iso3"})
wbm["year"] = wbm["year"].astype(int)
wbm.to_csv(os.path.join(OUT, "world_bank_crude_birth_rate.csv"), index=False)
print(f"  rows={len(wbm):,}")

# ---------- 5. Gapminder ----------
print("Gapminder ...")
gm_frames = {}
gm_files = {
    "population_total": "gapminder_ddf--datapoints--total_population_with_projections--by--geo--time.csv",
    "crude_birth_rate_per_1000": "gapminder_ddf--datapoints--crude_birth_rate_births_per_1000_population--by--geo--time.csv",
    "births_total_estimated": "gapminder_ddf--datapoints--new_births_total_number_estimated--by--geo--time.csv",
    "teen_fertility_rate_per_1000": "gapminder_ddf--datapoints--teen_fertility_rate_births_per_1000_women_ages_15_19--by--geo--time.csv",
}
for name, f in gm_files.items():
    d = pd.read_csv(os.path.join(RAW, f))
    d = d.rename(columns={"time": "year"})
    gm_frames[name] = d
    print(f"  {name}: rows={len(d):,}, years {d['year'].min()}-{d['year'].max()}")

gm = gm_frames["population_total"][["geo", "year"]]
for name, d in gm_frames.items():
    gm = gm.merge(d[["geo", "year", d.columns[-1]]], on=["geo", "year"], how="outer")
gm = gm.sort_values(["geo", "year"])
gm.to_csv(os.path.join(OUT, "gapminder_merged.csv"), index=False)
print(f"  merged rows={len(gm):,}")

# ---------- 6. CIA ----------
print("CIA ...")
cia = pd.read_csv(os.path.join(RAW, "cia_dataset_all.csv"))
keep = ["Country", "ISO3", "Year", "Region", "Population", "Pop_Growth_Rate",
        "Birth_Rate", "Death_Rate", "Infant_Mortality"]
ciak = cia[keep].rename(columns={"Country": "entity", "ISO3": "iso3", "Year": "year",
                                 "Region": "region"})
ciak.to_csv(os.path.join(OUT, "cia_factbook_birth_rates_1990_2025.csv"), index=False)
print(f"  rows={len(ciak):,}, countries={ciak['entity'].nunique()}")

print("\nDONE. Processed files:")
for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    print(f"  {f}: {os.path.getsize(p):,} bytes")
