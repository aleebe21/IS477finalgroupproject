import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def clean_ev_data():
    ev_path = RAW_DIR / "Electric_Vehicle_Population_Data.csv"
    df = pd.read_csv(ev_path)

    # Filter to WA just in case
    df = df[df["State"] == "WA"].copy()

    # ✅ Correct way to strip + uppercase a Series
    df["City_clean"] = df["City"].astype(str).str.strip().str.upper()

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / "ev_wa_clean.csv", index=False)
    print("Saved cleaned EV data.")


def clean_station_data():
    stations_path = RAW_DIR / "alt_fuel_stations.csv"
    df = pd.read_csv(stations_path)

    df = df[
        (df["State"] == "WA")
        & (df["Fuel Type Code"] == "ELEC")
        & (df["Status Code"] == "E")
    ].copy()

    df["City_clean"] = df["City"].astype(str).str.strip().str.upper()

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / "stations_wa_clean.csv", index=False)
    print("Saved cleaned station data.")


if __name__ == "__main__":
    clean_ev_data()
    clean_station_data()
