from scripts.clean_data import clean_ev_data, clean_station_data
from scripts.integrate_data import integrate_city_level
from scripts.analyze_and_visualize import analyze_city_level

def main():
    print("Cleaning data...")
    clean_ev_data()
    clean_station_data()

    print("Integrating...")
    integrate_city_level()

    print("Analyzing...")
    analyze_city_level()
    print("Done.")

if __name__ == "__main__":
    main()
