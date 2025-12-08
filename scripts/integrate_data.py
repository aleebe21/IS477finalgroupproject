import pandas as pd
from pathlib import Path
import math

PROCESSED_DIR = Path("data/processed")

def integrate_city_level():
    ev_df = pd.read_csv(PROCESSED_DIR / "ev_wa_clean.csv")
    stations_df = pd.read_csv(PROCESSED_DIR / "stations_wa_clean.csv")

    ev_by_city = ev_df.groupby("City_clean").size().reset_index(name="ev_count")
    stations_by_city = stations_df.groupby("City_clean").size().reset_index(name="station_count")

    merged = ev_by_city.merge(stations_by_city, on="City_clean", how="outer")
    merged["ev_count"] = merged["ev_count"].fillna(0).astype(int)
    merged["station_count"] = merged["station_count"].fillna(0).astype(int)

    merged["evs_per_station"] = merged.apply(
        lambda row: row["ev_count"] / row["station_count"] if row["station_count"] > 0 else math.nan,
        axis=1,
    )

    merged.to_csv(PROCESSED_DIR / "city_ev_stations_merged.csv", index=False)

if __name__ == "__main__":
    integrate_city_level()

