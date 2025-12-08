# Data Dictionary

## Electric_Vehicle_Population_Data.csv (raw)

- VIN (1-10): Truncated vehicle identifier (anonymized).
- County: County of registration.
- City: City of registration.
- State: 2-letter state code.
- Postal Code: ZIP code.
- Model Year: Vehicle model year.
- Make: Manufacturer.
- Model: Vehicle model.
- Electric Vehicle Type: "Battery Electric Vehicle (BEV)" or "Plug-in Hybrid Electric Vehicle (PHEV)".
- Electric Range: Electric-only range (miles).
- CAFV Eligibility: Clean Alternative Fuel Vehicle incentive eligibility.
- ... (you can add 2–3 more key fields if you want).

## alt_fuel_stations.csv (raw, AFDC)

- Station Name: Name of the charging location.
- Street Address, City, State, ZIP: Location fields.
- Fuel Type Code: "ELEC" for electric.
- Status Code: "E" = existing/operational station.
- EV Level1 EVSE Num: Number of Level 1 chargers (if reported).
- EV Level2 EVSE Num: Number of Level 2 chargers (if reported).
- EV DC Fast Count: Number of DC fast chargers (if reported).
- Latitude, Longitude: Geographic coordinates.

## city_ev_stations_merged.csv (processed)

- City_clean: Standardized city name (uppercase, trimmed).
- ev_count: Number of registered EVs in that city.
- station_count: Number of EV charging station locations in that city.
- evs_per_station: ev_count / station_count (NaN if no stations).
