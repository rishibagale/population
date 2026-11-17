"""Build the GitHub Pages site in docs/ from reports/*.md + charts/.

Usage:
    python build_site.py

Outputs:
    docs/index.html                       landing page
    docs/report.html                      full analysis
    docs/consequences_and_solutions.html  consequences & policy report
    docs/ai_robotics_and_demography.html  AI/robotics & demography report
    docs/charts/                          copies of charts/*.png
"""

import shutil
import re
import time
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
CHARTS = ROOT / "charts"

REPORTS = [
    ("reports/report.md", "report.html", "World Population, Birth Rates & Long-Term Projections"),
    ("reports/consequences_and_solutions.md", "consequences_and_solutions.html",
     "Consequences of Fertility Decline & What Works"),
    ("reports/ai_robotics_and_demography.md", "ai_robotics_and_demography.html",
     "AI, Physical AI & Robotics in an Aging World"),
]

CSS = """
:root {
  --bg: #ffffff;
  --fg: #1a1a1a;
  --muted: #595959;
  --accent: #0b5394;
  --border: #e0e0e0;
  --code-bg: #f5f5f5;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, 'Times New Roman', serif;
  color: var(--fg);
  background: var(--bg);
  line-height: 1.7;
  font-size: 17px;
}
header.site {
  border-bottom: 1px solid var(--border);
  padding: 0.75rem 0;
  font-family: 'Segoe UI', Arial, sans-serif;
  font-size: 0.85rem;
}
header.site a { color: var(--accent); text-decoration: none; }
header.site a:hover { text-decoration: underline; }
header.site nav a { margin-right: 1.25rem; }
main {
  max-width: 860px;
  margin: 0 auto;
  padding: 2rem 1.25rem 4rem;
}
h1, h2, h3, h4, h5, h6 {
  font-family: 'Segoe UI', Arial, sans-serif;
  line-height: 1.25;
  margin-top: 2rem;
}
h1 { font-size: 2rem; }
h2 { font-size: 1.4rem; border-bottom: 1px solid var(--border); padding-bottom: 0.3rem; }
h3 { font-size: 1.15rem; }
a { color: var(--accent); }
p, li { max-width: 70ch; }
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1.5rem auto;
  border: 1px solid var(--border);
}
table {
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.9rem;
  font-family: 'Segoe UI', Arial, sans-serif;
}
th, td {
  border: 1px solid var(--border);
  padding: 0.45rem 0.7rem;
  text-align: left;
  vertical-align: top;
}
th { background: var(--code-bg); }
code {
  font-family: Consolas, 'Courier New', monospace;
  background: var(--code-bg);
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  font-size: 0.88em;
}
pre { background: var(--code-bg); padding: 1rem; overflow-x: auto; }
pre code { padding: 0; background: none; }
blockquote {
  border-left: 4px solid var(--border);
  margin: 1.5rem 0;
  padding: 0.5rem 1.25rem;
  color: var(--muted);
}
hr { border: none; border-top: 1px solid var(--border); margin: 2.5rem 0; }
footer.site {
  border-top: 1px solid var(--border);
  padding: 1rem 0 2rem;
  font-family: 'Segoe UI', Arial, sans-serif;
  font-size: 0.8rem;
  color: var(--muted);
  max-width: 860px;
  margin: 0 auto;
}
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; margin: 2rem 0; }
@media (max-width: 700px) { .cards { grid-template-columns: 1fr; } }
@media print {
  header.site, footer.site { display: none; }
  main { max-width: none; padding: 0; }
  img { border: none; max-height: 8.5in; }
  a { color: inherit; text-decoration: none; }
  h2 { break-after: avoid; }
  img, table, pre { break-inside: avoid; }
}
.card {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.25rem;
  font-family: 'Segoe UI', Arial, sans-serif;
}
.card h2 { border: none; margin-top: 0; font-size: 1.15rem; }
.card a { text-decoration: none; }
.card p { color: var(--muted); font-size: 0.95rem; margin-bottom: 0; }
"""


def md_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        extension_configs={"toc": {"permalink": False}},
    )


def page(title: str, body: str, active: str = "") -> str:
    bold = ' style="font-weight:bold"'
    nav = (
        '<nav><a href="index.html">Home</a>'
        f'<a href="report.html"{bold if active == "report" else ""}>Full analysis</a>'
        f'<a href="consequences_and_solutions.html"{bold if active == "conseq" else ""}>Consequences &amp; solutions</a>'
        f'<a href="ai_robotics_and_demography.html"{bold if active == "ai" else ""}>AI &amp; demography</a></nav>'
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<header class="site"><main>{nav}</main></header>
<main>{body}</main>
<footer class="site"><main>Built from <code>reports/*.md</code> via <code>build_site.py</code> &middot; UN WPP 2024 / OWID / World Bank / Gapminder / CIA Factbook data.</main></footer>
</body>
</html>
"""


def build_report(md_path: str, out_name: str, title: str, active: str) -> None:
    text = (ROOT / md_path).read_text(encoding="utf-8")
    # Reports reference charts as ../charts/NN.png; the site serves them at charts/NN.png.
    text = text.replace("../charts/", "charts/")
    body = md_to_html(text)
    (DOCS / out_name).write_text(page(title, body, active), encoding="utf-8")
    print(f"wrote docs/{out_name}")


def build_index() -> None:
    body = """<h1>World Population, Birth Rates &amp; Long-Term Projections</h1>
<p>A multi-source demographic research project built on the <strong>UN World Population
Prospects 2024</strong>, <strong>Our World in Data</strong>, the <strong>World Bank</strong>,
<strong>Gapminder</strong>, the <strong>CIA World Factbook</strong>, and three Kaggle datasets.
It cleans and harmonizes ~40 datasets into tidy CSVs and produces 19 publication-style charts
covering world, continental, and country-level population and fertility trajectories through 2100.</p>
<div class="cards">
<div class="card"><h2><a href="report.html">The full analysis &rarr;</a></h2>
<p>Headline findings, projection uncertainty, the fertility transition, continental and country
futures, source cross-checks, and reproducibility notes — every finding, table, and chart.</p></div>
<div class="card"><h2><a href="consequences_and_solutions.html">Consequences of fertility decline &amp; what works &rarr;</a></h2>
<p>A deep-research report on what below-replacement fertility does to growth, pensions, and
societies — and an honest review of the policy evidence on pro-natalist intervention.</p></div>
<div class="card"><h2><a href="ai_robotics_and_demography.html">AI, robots &amp; demographic decline &rarr;</a></h2>
<p>Can AI and physical AI offset an aging workforce — and do they change fertility itself? A
An 188-source synthesis of economist forecasts, robotics data, care evidence, and prediction markets.</p></div>
</div>
<h2>Headline findings</h2>
<ul>
<li>The world reached <strong>8.16 billion in 2024</strong>; under the UN Medium scenario it peaks at
<strong>~10.3 billion in the mid-2080s</strong>, then declines.</li>
<li>Global fertility collapsed from <strong>4.85 children per woman (1950)</strong> to <strong>~2.25 today</strong>.</li>
<li>The <strong>65+ population triples</strong> from 0.83B to 2.44B by 2100; the under-15 cohort never grows again.</li>
<li>China shrinks <strong>1.42B &rarr; 0.63B (−55%)</strong> by 2100; India peaks at ~1.70B around 2061.</li>
<li>Birth rates are already below replacement in <strong>77 of 179</strong> developing countries and
<strong>36 of 58</strong> high-income countries.</li>
</ul>
<p>Raw data and processed CSVs live in the
<a href="https://github.com/rishibagale/population">GitHub repository</a>, alongside the
original Markdown sources in <code>reports/</code> and PDF exports.</p>"""
    (DOCS / "index.html").write_text(page("Population Research", body, "home"), encoding="utf-8")
    print("wrote docs/index.html")


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    if CHARTS.exists():
        dest = DOCS / "charts"
        dest.mkdir(exist_ok=True)  # avoid rmtree: OneDrive briefly locks recreated dirs
        pngs = sorted(CHARTS.glob("*.png"))
        for png in pngs:
            shutil.copy2(png, dest / png.name)
        stale = set(p.name for p in dest.glob("*.png")) - set(p.name for p in pngs)
        for name in stale:
            (dest / name).unlink()
        print(f"mirrored {len(pngs)} charts to docs/charts/")
    active_pages = {"report.html": "report", "consequences_and_solutions.html": "conseq",
                    "ai_robotics_and_demography.html": "ai"}
    for md_path, out_name, title in REPORTS:
        build_report(md_path, out_name, title, active_pages[out_name])
    build_index()


if __name__ == "__main__":
    main()
