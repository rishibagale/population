import sys
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\rushi\OneDrive\Desktop\random_projects\population_reserch"
PROC = ROOT + r"\data\processed"

s = pd.read_csv(PROC + r"\country_summary_medium.csv")
print("== top 12 by 2024 pop ==")
print(s.head(12)[["iso3_code", "location", "pop_2024_thousands", "pop_2050_thousands",
                  "pop_2100_thousands", "trend", "tfr_2023_observed", "tfr_2026_proj"]].to_string())

print("\n== top 20 developed (first 8) ==")
dev = pd.read_csv(PROC + r"\top20_developed_summary.csv")
print(dev.head(8)[["rank", "iso3_code", "location", "pop_2024_thousands", "growth_2024_2050_pct"]].to_string())

print("\n== top 20 developing (all, abbreviated) ==")
dvl = pd.read_csv(PROC + r"\top20_developing_summary.csv")
print(dvl[["rank", "iso3_code", "pop_2024_thousands", "growth_2024_2050_pct", "peak_year", "trend"]].to_string())

print("\n== world TFR from demo gz ==")
demo = pd.read_csv(ROOT + r"\data\raw\WPP2024_Demographic_Indicators_Medium.csv.gz",
                   usecols=["Location", "Time", "TFR"])
w = demo[demo["Location"] == "World"]
for y in (2023, 2026, 2050, 2100):
    row = w[w["Time"] == y]
    print(y, row["TFR"].values)

print("\n== sanity: world pop 2024 & 2100 (region file) ==")
r = pd.read_csv(PROC + r"\region_population_medium_1950_2100.csv")
wr = r[r["region"] == "World"]
print(wr[wr["year"].isin([2024, 2050, 2085, 2100])].to_string())
print("\n== shrinking trend count ==")
print(s["trend"].value_counts().to_string())
