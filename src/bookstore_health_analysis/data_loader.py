import pandas as pd
from pathlib import Path

def load_all_data(data_dir: Path) -> dict[str, pd.DataFrame]:
    files = list(data_dir.glob("*.csv"))
    dfs: dict[str, pd.DataFrame] = {}
    for f in files:
        if f.stem == "data_dictionary":
            continue
        df = pd.read_csv(f)
        date_columns = [col for col in df.columns if 'date' in col.lower()]
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        key = f.stem.lower().replace(" ", "_")
        dfs[key] = df
    return dfs