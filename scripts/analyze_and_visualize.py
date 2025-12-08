import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROCESSED_DIR = Path("data/processed")
ANALYSIS_DIR = Path("analysis")
VIS_DIR = Path("visualizations")

def analyze_city_level():
    df = pd.read_csv(PROCESSED_DIR / "city_ev_stations_merged.csv")

    ANALYSIS_DIR.mkdir(exist_ok=True)
    VIS_DIR.mkdir(exist_ok=True)

    subset = df[(df["ev_count"] > 0) & (df["station_count"] > 0)]
    corr = subset["ev_count"].corr(subset["station_count"])

    with open(ANALYSIS_DIR / "city_level_summary.md", "w") as f:
        f.write("# Summary\n")
        f.write(f"- Total EVs: {df.ev_count.sum()}\n")
        f.write(f"- Total Stations: {df.station_count.sum()}\n")
        f.write(f"- Correlation: {corr:.3f}\n")

    plt.scatter(subset["station_count"], subset["ev_count"])
    plt.xlabel("Stations")
    plt.ylabel("EV Count")
    plt.title("EV vs Stations by City")
    plt.savefig(VIS_DIR / "ev_vs_stations_scatter.png")

if __name__ == "__main__":
    analyze_city_level()
