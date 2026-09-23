import os
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
cache_dir = project_root / "data" / "raw"
os.environ["KAGGLEHUB_CACHE"] = str(cache_dir)

# import kagglehub
import kagglehub # type: ignore

def main():
    print(f"Using cache directory: {os.environ['KAGGLEHUB_CACHE']}")
    path = kagglehub.dataset_download("gabriellecharlton/bookstore-financial-dataset-2019-2024-calgary")
    print(f"Successfully downloaded to: {path}")

if __name__ == "__main__":
    main()