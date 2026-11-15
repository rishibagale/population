import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAW = r"data\processed"
OUT = r"charts"
plt.rcParams.update({"figure.dpi": 150, "axes.grid": True, "grid.alpha": 0.3})

BN = 1e6  # thousands -> billions

# ---------- panel 1: UN Medium vs Worldometers 2020-2100 ----------
un = pd.read_csv(os.path.join(RAW, "un_wpp_world_population_by_variant.csv"))
m = un[un["Variant"] == "Medium"].sort_values("year")
wm = pd.read_csv(os.path.join(RAW, "kaggle_worldometers_projection_2020_2100.csv")).sort_values("year")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(m["year"], m["population_thousands"] / BN, label="UN WPP 2024 Medium", color="#1f77b4", lw=2)
ax.plot(wm["year"], wm["population"] / 1e9, label="Worldometers (Kaggle)", color="#ff7f0e", lw=2)
u2100 = m[m["year"] == 2100]["population_thousands"].iloc[0] / BN
w2100 = wm[wm["year"] == 2100]["population"].iloc[0] / 1e9
ax.annotate(f"{u2100:.2f}B", (2100, u2100), textcoords="offset points", xytext=(-8, -14), color="#1f77b4")
ax.annotate(f"{w2100:.2f}B", (2100, w2100), textcoords="offset points", xytext=(-8, 6), color="#ff7f0e")
ax.axvline(2024, color="grey", ls=":", lw=1)
ax.set_title("World Population Projections 2020-2100: UN Medium vs Worldometers")
ax.set_xlabel("Year"); ax.set_ylabel("Population (billions)")
ax.legend()
fig.tight_layout(); fig.savefig(os.path.join(OUT, "08a_un_vs_worldometers_projection.png")); plt.close(fig)
print("08a done", f"UN2100={u2100:.3f} WM2100={w2100:.3f}")

# ---------- panel 2: World TFR, OWID/UN vs Worldometers ----------
ow = pd.read_csv(os.path.join(RAW, "owid_fertility_rate_tfr.csv"))
w = ow[ow["Entity"] == "World"].sort_values("Year")
w = w[w["Year"] <= 2023]
kg = pd.read_csv(os.path.join(RAW, "kaggle_worldometers_world_population_1955_2023.csv")).sort_values("year")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(w["Year"], w["tfr_children_per_woman"], label="UN/OWID TFR", color="#1f77b4", lw=2)
ax.plot(kg["year"], kg["fertility_rate_children_per_woman"], label="Worldometers (Kaggle)", color="#ff7f0e", lw=2, ls="--")
ax.axhline(2.1, color="#d62728", ls=":", lw=1, label="Replacement level (2.1)")
ax.set_title("World Total Fertility Rate: UN/OWID vs Worldometers, 1950-2023")
ax.set_xlabel("Year"); ax.set_ylabel("Births per woman")
ax.legend()
fig.tight_layout(); fig.savefig(os.path.join(OUT, "08b_world_tfr_sources.png")); plt.close(fig)
print("08b done")

# ---------- panel 3: US population 1900-2019 ----------
us = pd.read_csv(os.path.join(RAW, "us_census_us_population_1900_2019.csv")).sort_values("year")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(us["year"], us["population_thousands"] / 1e3, color="#2ca02c", lw=2)
ax.set_title("US Population 1900-2019 (US Census Bureau POP/POPH via Kaggle)")
ax.set_xlabel("Year"); ax.set_ylabel("Population (millions)")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "08c_us_population_census.png")); plt.close(fig)
print("08c done")
