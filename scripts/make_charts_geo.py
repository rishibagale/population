import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = r"C:\Users\rushi\OneDrive\Desktop\random_projects\population_reserch"
PROC = os.path.join(BASE, "data", "processed")
RAW = os.path.join(BASE, "data", "raw")
CH = os.path.join(BASE, "charts")
os.makedirs(CH, exist_ok=True)

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["grid.alpha"] = 0.3

def pop_m(x):
    return x / 1e6

# ---------- 09: continents 1950-2100 (Medium) ----------
reg = pd.read_csv(os.path.join(PROC, "region_population_medium_1950_2100.csv"))
regions = ["Africa", "Asia", "Europe", "Latin America and the Caribbean",
           "Northern America", "Oceania", "World"]
fig, ax = plt.subplots()
for r in regions:
    d = reg[reg["region"] == r].sort_values("year")
    if r == "World":
        ax.plot(d["year"], pop_m(d["population_thousands"]), color="black", lw=2.5, ls="--", label="World")
    else:
        ax.plot(d["year"], pop_m(d["population_thousands"]), lw=1.8, label=r)
ax.set_title("Continental population, UN WPP 2024 Medium variant (1950-2100)")
ax.set_xlabel("Year"); ax.set_ylabel("Population (millions)")
ax.legend(fontsize=8, loc="lower right"); ax.grid(alpha=0.3)
ax.set_xlim(1950, 2100)
fig.tight_layout(); fig.savefig(os.path.join(CH, "09_continents_1950_2100_medium.png")); plt.close(fig)

# ---------- 10: top 10 countries 1950-2100 (Medium) ----------
top10 = pd.read_csv(os.path.join(PROC, "top20_by_population_2024.csv")).head(10)
cp = pd.read_csv(os.path.join(PROC, "country_population_medium_1950_2100.csv"))
fig, ax = plt.subplots()
for _, row in top10.iterrows():
    d = cp[cp["iso3"] == row["iso3_code"]].sort_values("year")
    ax.plot(d["year"], pop_m(d["population_thousands"]), lw=1.8, label=row["location"])
ax.set_title("Top 10 most populous countries, UN WPP 2024 Medium variant (1950-2100)")
ax.set_xlabel("Year"); ax.set_ylabel("Population (millions)")
ax.legend(fontsize=8, loc="lower right"); ax.grid(alpha=0.3)
ax.set_xlim(1950, 2100)
fig.tight_layout(); fig.savefig(os.path.join(CH, "10_top10_countries_medium.png")); plt.close(fig)

# ---------- 11: developed vs developing world ----------
dvd = pd.read_csv(os.path.join(PROC, "developed_vs_developing_world.csv"))
fig, ax = plt.subplots()
ax.stackplot(dvd["year"],
             pop_m(dvd["developing_thousands"]),
             pop_m(dvd["developed_thousands"]),
             labels=["Developing", "Developed"],
             colors=["#66c2a5", "#8da0cb"], alpha=0.85)
ax.set_title("Developed vs developing world population, UN WPP 2024 Medium (1950-2100)")
ax.set_xlabel("Year"); ax.set_ylabel("Population (millions)")
ax.legend(loc="upper left"); ax.grid(alpha=0.3)
ax.set_xlim(1950, 2100); ax.set_ylim(0, None)
fig.tight_layout(); fig.savefig(os.path.join(CH, "11_developed_vs_developing.png")); plt.close(fig)

# ---------- 12: world TFR projection ----------
gz = os.path.join(RAW, "WPP2024_Demographic_Indicators_Medium.csv.gz")
demo = pd.read_csv(gz, low_memory=False, usecols=["LocID", "Location", "Time", "TFR"])
w = demo[demo["LocID"] == 900].sort_values("Time")
fig, ax = plt.subplots()
ax.plot(w["Time"], w["TFR"], lw=2, color="#d95f02")
ax.axhline(2.1, color="gray", ls=":", lw=1.5)
ax.text(1952, 2.13, "Replacement level (2.1)", fontsize=9, color="gray")
for yr, val, lab in [(2023, 2.2505, "2023 obs: 2.25"),
                     (2026, 2.2304, "2026 proj: 2.23"),
                     (2050, 2.0966, "2050 proj: 2.10"),
                     (2100, 1.838, "2100 proj: 1.84")]:
    ax.scatter([yr], [val], color="#d95f02", zorder=5, s=30)
    ax.annotate(lab, xy=(yr, val), xytext=(yr - 32, val + 0.12), fontsize=9)
ax.axvline(2023, color="gray", ls="--", lw=1, alpha=0.6)
ax.text(2024.5, 4.6, "projections ->", fontsize=9, color="gray")
ax.set_title("World total fertility rate, UN WPP 2024 Medium variant (1950-2100)")
ax.set_xlabel("Year"); ax.set_ylabel("TFR (children per woman)")
ax.grid(alpha=0.3); ax.set_xlim(1950, 2100)
fig.tight_layout(); fig.savefig(os.path.join(CH, "12_world_tfr_medium.png")); plt.close(fig)

# ---------- 13: country grid focus (~40 countries) ----------
summ = pd.read_csv(os.path.join(PROC, "country_summary_medium.csv"))
top40 = summ.sort_values("pop_2024_thousands", ascending=False).head(40)
n = len(top40)
ncols, nrows = 8, 5
fig, axes = plt.subplots(nrows, ncols, figsize=(16, 10), dpi=150, sharex=True)
for ax, (_, row) in zip(axes.flat, top40.iterrows()):
    d = cp[cp["iso3"] == row["iso3_code"]].sort_values("year")
    color = "#8da0cb" if row["income_class"] == "high_income" else "#66c2a5"
    ax.plot(d["year"], pop_m(d["population_thousands"]), lw=1.4, color=color)
    ax.fill_between(d["year"], 0, pop_m(d["population_thousands"]), color=color, alpha=0.25)
    peak = row["peak_year"]
    if peak < 2100:
        ax.axvline(peak, color="#d95f02", lw=0.8, alpha=0.8)
    ax.set_title(f"{row['iso3_code']}", fontsize=8)
    ax.grid(alpha=0.3)
    ax.tick_params(labelsize=6)
    ax.set_xlim(1950, 2100)
fig.suptitle("Population trajectories, top 40 countries (UN WPP 2024 Medium) - "
             "green=developing, blue=high income, orange line=peak year", fontsize=11)
fig.text(0.5, 0.04, "Year", ha="center"); fig.text(0.04, 0.5, "Population (millions)", va="center", rotation=90)
fig.tight_layout(rect=[0.05, 0.05, 1, 0.94])
fig.savefig(os.path.join(CH, "13_country_grid_focus.png")); plt.close(fig)

print("charts done:", [f for f in os.listdir(CH) if f.startswith(("09", "10", "11", "12", "13"))])
