import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAW = r"data\processed"
OUT = r"charts"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"figure.figsize": (10, 6), "figure.dpi": 150,
                     "axes.grid": True, "grid.alpha": 0.3})

BN = 1e6  # thousands -> billions

# ---------- 1. World population by variant ----------
d = pd.read_csv(os.path.join(RAW, "un_wpp_world_population_by_variant.csv"))
fig, ax = plt.subplots()
for variant, color in [("Medium", "#1f77b4"), ("High", "#2ca02c"), ("Low", "#d62728")]:
    v = d[d["Variant"] == variant]
    ax.plot(v["year"], v["population_thousands"] / BN, label=variant, color=color, lw=2)
ax.set_title("World Population 1950-2100, UN WPP 2024 (billions)")
ax.set_xlabel("Year"); ax.set_ylabel("Population (billions)")
ax.legend()
fig.tight_layout(); fig.savefig(os.path.join(OUT, "01_world_population_variants.png")); plt.close(fig)
print("chart 1 done")

# ---------- 2. Global TFR ----------
d = pd.read_csv(os.path.join(RAW, "owid_fertility_rate_tfr.csv"))
w = d[d["Entity"] == "World"].sort_values("Year")
fig, ax = plt.subplots()
ax.plot(w["Year"], w["tfr_children_per_woman"], color="#1f77b4", lw=2)
ax.axhline(2.1, color="#d62728", ls="--", lw=1, label="Replacement level (2.1)")
ax.set_title("Global Total Fertility Rate, 1950-2100 (UN via OWID)")
ax.set_xlabel("Year"); ax.set_ylabel("Births per woman")
ax.legend()
fig.tight_layout(); fig.savefig(os.path.join(OUT, "02_global_tfr.png")); plt.close(fig)
print("chart 2 done")

# ---------- 3. World crude birth rate: 3 sources ----------
fig, ax = plt.subplots()
wb = pd.read_csv(os.path.join(RAW, "world_bank_crude_birth_rate.csv"))
w = wb[wb["iso3"] == "WLD"].sort_values("year")
ax.plot(w["year"], w["crude_birth_rate_per_1000"], label="World Bank", lw=2)
ow = pd.read_csv(os.path.join(RAW, "owid_crude_birth_rate.csv"))
w = ow[ow["Entity"] == "World"].sort_values("Year")
ax.plot(w["Year"], w["crude_birth_rate_per_1000"], label="UN/OWID (incl. projections)", lw=2, ls="--")
gm = pd.read_csv(os.path.join(RAW, "gapminder_merged.csv"))
w = gm[gm["geo"] == "world"].sort_values("year")
ax.plot(w["year"], w["crude_birth_rate_births_per_1000_population"], label="Gapminder", lw=1.5, alpha=0.8)
ax.set_title("World Crude Birth Rate: Source Comparison")
ax.set_xlabel("Year"); ax.set_ylabel("Births per 1,000 people")
ax.legend()
fig.tight_layout(); fig.savefig(os.path.join(OUT, "03_world_cbr_sources.png")); plt.close(fig)
print("chart 3 done")

# ---------- 4. Age structure evolution ----------
d = pd.read_csv(os.path.join(RAW, "un_wpp_age_groups_medium_1950_2100.csv"),
                usecols=["LocID", "Variant", "year", "age_group_start", "pop_total_thousands"])
w = d[(d["LocID"] == 900) & (d["Variant"] == "Medium")]
labels = ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44",
          "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84",
          "85-89", "90-94", "95-99", "100+"]
fig, ax = plt.subplots()
colors = plt.cm.YlGnBu(np.linspace if False else None) if False else None
bottoms = [0.0] * 3
years = [2024, 2050, 2100]
import numpy as np
cmap = plt.get_cmap("YlGnBu")
for i, (ag, lab) in enumerate(zip(range(0, 101, 5), labels)):
    vals = [w[(w["year"] == y) & (w["age_group_start"] == ag)]["pop_total_thousands"].sum() / BN
            for y in years]
    ax.bar([str(y) for y in years], vals, bottom=bottoms, color=cmap(i / 20), label=lab,
           width=0.6)
    bottoms = [b + v for b, v in zip(bottoms, vals)]
for i, y in enumerate(years):
    ax.text(i, bottoms[i] + 0.05, f"{bottoms[i]:.1f}B", ha="center", fontweight="bold")
ax.set_title("World Population by Age Group (UN WPP Medium)")
ax.set_ylabel("Population (billions)")
ax.legend(title="Age group", ncol=2, fontsize=7, loc="upper left", bbox_to_anchor=(1.01, 1))
fig.tight_layout(); fig.savefig(os.path.join(OUT, "04_age_structure_evolution.png")); plt.close(fig)
print("chart 4 done")

# ---------- 5. Birth rate trends for selected countries ----------
d = pd.read_csv(os.path.join(RAW, "owid_crude_birth_rate.csv"))
countries = ["Niger", "Nigeria", "India", "China", "United States", "Japan", "Germany", "Ethiopia"]
fig, ax = plt.subplots()
for c in countries:
    w = d[(d["Entity"] == c) & (d["Year"] <= 2025)].sort_values("Year")
    if len(w):
        ax.plot(w["Year"], w["crude_birth_rate_per_1000"], label=c, lw=1.8)
ax.set_title("Crude Birth Rate Trends, Selected Countries (UN/OWID)")
ax.set_xlabel("Year"); ax.set_ylabel("Births per 1,000 people")
ax.legend(fontsize=8, ncol=2)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "05_country_birth_rate_trends.png")); plt.close(fig)
print("chart 5 done")

# ---------- 6. CIA 2025 top-15 birth rates ----------
d = pd.read_csv(os.path.join(RAW, "cia_factbook_birth_rates_1990_2025.csv"))
d25 = d[d["year"] == 2025].dropna(subset=["Birth_Rate"]).sort_values("Birth_Rate").tail(15)
fig, ax = plt.subplots(figsize=(10, 6.5))
ax.barh(d25["entity"], d25["Birth_Rate"], color="#2ca02c")
ax.set_title("Top 15 Countries by Birth Rate, 2025 (CIA World Factbook)")
ax.set_xlabel("Births per 1,000 people")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "06_cia_top15_birth_rate_2025.png")); plt.close(fig)
print("chart 6 done")

# ---------- 7. Regional population projections (Medium) ----------
d = pd.read_csv(os.path.join(RAW, "un_wpp_total_population_by_variant.csv"),
                usecols=["LocID", "Location", "Variant", "year", "population_thousands"])
regions = {903: "Africa", 935: "Asia", 904: "Latin America & Caribbean",
           905: "Northern America", 908: "Europe", 909: "Oceania"}
fig, ax = plt.subplots()
for loc, name in regions.items():
    w = d[(d["LocID"] == loc) & (d["Variant"] == "Medium")].sort_values("year")
    if len(w):
        print(f"  region {loc}: {name} rows={len(w)}")
        ax.plot(w["year"], w["population_thousands"] / BN, label=name, lw=2)
ax.set_title("Regional Population, 1950-2100 (UN WPP Medium)")
ax.set_xlabel("Year"); ax.set_ylabel("Population (billions)")
ax.legend(fontsize=9)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "07_regional_population.png")); plt.close(fig)
print("chart 7 done")

print("ALL CHARTS DONE")
for f in sorted(os.listdir(OUT)):
    print(f"  {f}: {os.path.getsize(os.path.join(OUT, f)):,} bytes")
