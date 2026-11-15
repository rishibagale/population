import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

BASE = r"C:\Users\rushi\OneDrive\Desktop\random_projects\population_reserch"
PROC = os.path.join(BASE, "data", "processed")
CH = os.path.join(BASE, "charts")
os.makedirs(CH, exist_ok=True)

plt.rcParams["figure.dpi"] = 150
plt.rcParams["grid.alpha"] = 0.3

REGIONS = ["Africa", "Asia", "Europe", "Latin America and the Caribbean",
           "Northern America", "Oceania", "World"]
C_HI = "#8da0cb"
C_DEV = "#66c2a5"

top20 = pd.read_csv(os.path.join(PROC, "top20_by_population_2024.csv"))
tc = pd.read_csv(os.path.join(PROC, "top20_tfr_cbr_filled_1950_2100.csv"))
ta = pd.read_csv(os.path.join(PROC, "continent_tfr_cbr_1950_2100.csv"))

INC = dict(zip(top20["iso3_code"], top20["income_class"]))
ISO2LOC = dict(zip(top20["iso3_code"], top20["location"]))
LOCS = [ISO2LOC[r["iso3_code"]] for _, r in top20.iterrows()]

def split_series(d, col):
    """observed solid + projected dashed as two masked series"""
    obs = d[d["is_projected"] == False]
    proj = d[d["is_projected"] == True]
    return obs, proj

def plot_split(ax, d, col, color, lw=1.4, label=None):
    obs, proj = split_series(d, col)
    if len(obs):
        ax.plot(obs["year"], obs[col], lw=lw, color=color, label=label)
    if len(proj):
        ax.plot(proj["year"], proj[col], lw=lw, color=color, ls="--")

def grid_chart(col, fname, title, ylabel):
    ncols, nrows = 5, 4
    fig, axes = plt.subplots(nrows, ncols, figsize=(16, 10), dpi=150, sharex=True)
    for ax, loc in zip(axes.flat, LOCS):
        d = tc[tc["location"] == loc].sort_values("year")
        iso = top20.loc[top20["location"] == loc, "iso3_code"].iloc[0]
        color = C_HI if INC[iso] == "high_income" else C_DEV
        plot_split(ax, d, col, color)
        ax.axhline(2.1, color="gray", ls=":", lw=0.8) if col == "tfr" else None
        ax.axvline(2024, color="gray", ls="--", lw=0.6, alpha=0.6)
        ax.set_title(loc, fontsize=9)
        ax.grid(alpha=0.3)
        ax.tick_params(labelsize=6)
        ax.set_xlim(1950, 2100)
    handles = [
        Line2D([0], [0], color=C_DEV, lw=1.6, label="developing (solid=obs, dashed=proj)"),
        Line2D([0], [0], color=C_HI, lw=1.6, label="high income (solid=obs, dashed=proj)"),
    ]
    if col == "tfr":
        handles.append(Line2D([0], [0], color="gray", ls=":", lw=1.2, label="replacement level (2.1)"))
    fig.legend(handles=handles, loc="lower center", ncol=3, fontsize=9)
    fig.suptitle(title, fontsize=12)
    fig.text(0.5, 0.06, "Year", ha="center")
    fig.text(0.04, 0.5, ylabel, va="center", rotation=90)
    fig.tight_layout(rect=[0.05, 0.09, 1, 0.95])
    fig.savefig(os.path.join(CH, fname))
    plt.close(fig)

# ---------- 14: top-20 TFR grid ----------
grid_chart("tfr", "14_top20_tfr_grid.png",
           "Total fertility rate, top 20 most populous countries, UN WPP 2024 Medium (1950-2100)",
           "TFR (children per woman)")

# ---------- 15: top-20 CBR grid ----------
grid_chart("cbr", "15_top20_cbr_grid.png",
           "Crude birth rate, top 20 most populous countries, UN WPP 2024 Medium (1950-2100)",
           "CBR (births per 1,000 people)")

# ---------- 16 + 17: continents TFR and CBR ----------
for col, fname, title, ylabel in [
    ("tfr", "16_continents_tfr.png",
     "Total fertility rate by continent, UN WPP 2024 Medium (1950-2100)",
     "TFR (children per woman)"),
    ("cbr", "17_continents_cbr.png",
     "Crude birth rate by continent, UN WPP 2024 Medium (1950-2100)",
     "CBR (births per 1,000 people)"),
]:
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    cmap = plt.get_cmap("tab10")
    for i, r in enumerate(REGIONS):
        d = ta[ta["region"] == r].sort_values("year")
        if r == "World":
            plot_split(ax, d, col, "black", lw=2.5, label="World")
        else:
            plot_split(ax, d, col, cmap(i % 10), lw=1.8, label=r)
    if col == "tfr":
        ax.axhline(2.1, color="gray", ls=":", lw=1.5)
        ax.text(1952, 2.15, "Replacement level (2.1)", fontsize=9, color="gray")
    ax.axvline(2024, color="gray", ls="--", lw=1, alpha=0.6)
    ax.text(2026, ax.get_ylim()[1] * 0.97, "projections ->", fontsize=9, color="gray")
    ax.set_title(title)
    ax.set_xlabel("Year"); ax.set_ylabel(ylabel)
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3)
    ax.set_xlim(1950, 2100)
    fig.tight_layout()
    fig.savefig(os.path.join(CH, fname))
    plt.close(fig)

print("charts done:", [f for f in os.listdir(CH) if f.startswith(("14", "15", "16", "17"))])
