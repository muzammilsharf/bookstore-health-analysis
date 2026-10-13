# Bookstore Health Analysis

An end-to-end exploratory and statistical analysis of a synthetic Calgary
bookstore business (three stores, 2019 to 2024). The question: is the business
healthy enough to support a second location?

## Key findings

- Revenue recovered to its pre-COVID level but did not grow past it.
- YYC-DT leads, and every store sells about 20% online.
- The checking account is a partial view of the business and cannot show
  profitability on its own.
- Debt taken on in 2020 was never paid down, but it is small next to the
  account's deficit.

Full write-up: [reports/findings.md](reports/findings.md)

## Data

Kaggle: [Bookstore Financial Dataset 2019-2024 Calgary](https://www.kaggle.com/datasets/gabriellecharlton/bookstore-financial-dataset-2019-2024-calgary)

Files are not committed. Download them with `uv run python scripts/download_data.py`
(Kaggle credentials may be required). [Add here if you copied any file by hand,
for example bookstore_inventory.csv or the dataset README.]

## Notebooks

Run in order from the `notebooks/` folder:

1. `01_data_understanding`: load all files, check types, map how files connect
2. `02_core_view`: build a quarterly ledger from sales, checking and loans
3. `03_covid_recovery_analysis`: Kruskal-Wallis and Dunn's test across periods
4. `04_store_channel_analysis`: store ranking and channel mix
5. `05_cashflow_analysis`: checking balance, sales sweeps and loan principal

## Methods

Time-based aggregation, Kruskal-Wallis, Dunn's post-hoc test with Bonferroni
correction. A non-parametric test was chosen for the small COVID-period samples.

## Setup

    uv sync
    uv run jupyter lab

## Structure

    data/            raw and processed data (gitignored)
    notebooks/       numbered analysis notebooks
    reports/         findings.md
    scripts/         download_data.py
    src/             reusable loading code

## Limitations

Synthetic dataset. The checking account does not reconcile with sales or
payroll. Figures are nominal. Customer and payroll-vs-revenue analyses were
not completed.