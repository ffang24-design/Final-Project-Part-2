# CSE 163 Final Project — Exploratory Data Analysis

This project explores language assistance needs among older adults in King County and compares those needs with documented language offerings at Sound Generations.

## Data

- ACS B16004: age, language, and English proficiency.
- ACS C16001: detailed language groups for residents aged 5 and older.
- Census tract boundaries.
- Sound Generations program and language information.

## Responsibilities

### Person 1 — Data Cleaning & Statistical Analysis

Load and clean data using pandas, document dataset structure and missingness, calculate descriptive statistics and categorical counts, and write the Dataset section and statistical findings.

### Person 2 — Visualizations & Findings

Create at least two visualizations per dataset or required dataset combination. Include titles, legends where applicable, captions, and explanations of patterns, relationships, and anomalies.

### Person 3 — Testing & Report Integration

Update research questions, motivation, methods, and challenge goals. Write tests using assertions, check flake8 compliance, evaluate the work plan, document collaboration, and combine contributions into `eda.pdf`.

## Repository layout

```
docs/
  proposal.pdf            Part 1 proposal (submitted)
  assignment/             course specs: proposal.md, eda.md, strands.md
src/
  data_cleaning.py        download (Census API) + clean ACS tables, site list
  eda_stats.py            dataset size, missingness, summaries, joins
  test_data_cleaning.py   tests for data_cleaning.py (small hand-made data)
data/
  raw/                    raw API responses + variable metadata (committed)
  clean/                  tidy tables written by data_cleaning.py
results/
  eda_summary.md          generated summary used for eda.pdf
  tables/                 generated CSV tables
  figures/                plots
```

## How to run

Run every command from the repository root (Python 3 with pandas,
requests, matplotlib, geopandas, flake8):

```
python src/data_cleaning.py      # writes data/clean/
python src/eda_stats.py          # writes results/eda_summary.md and results/tables/
python src/test_data_cleaning.py
flake8 src
```

## Getting the data

- **ACS 2024 5-year, tables B16004 and C16001** (King County, WA:
  state 53, county 033; county and every census tract). The raw responses
  are already in `data/raw/`, so no key is needed to rerun. To download
  again, delete those CSVs, get a free key at
  https://api.census.gov/data/key_signup.html, and set
  `export CENSUS_API_KEY=<your key>` (or save it in `~/.census_api_key`).
  **Never commit the key.** Example query:
  `https://api.census.gov/data/2024/acs/acs5?get=group(B16004)&for=tract:*&in=state:53%20county:033&key=<key>`
- **2020 TIGER/Line census tracts, Washington** (not the HW mapping
  shapefile, which uses older tracts):
  https://www2.census.gov/geo/tiger/TIGER2020/TRACT/tl_2020_53_tract.zip —
  unzip into `data/raw/tl_2020_53_tract/` (ignored by git).
- **Sound Generations site list** (provided by the partner through the
  instructor for Strand B): save as `data/raw/sound_generations_sites.csv`
  with columns `site` and `languages`.

## Deliverables

Runnable Python analysis and visualization scripts, testing files, summary tables, plots, and the final EDA report.
