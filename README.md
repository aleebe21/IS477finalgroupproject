# EV Adoption and Charging Infrastructure in Washington State

## Contributors
- Affan Leebe
- Om Patel

---

## Summary (500–1000 words)

This project investigates the relationship between electric vehicle (EV) adoption and the availability of EV charging infrastructure across communities in Washington State. As EVs become more common, understanding whether charging access is keeping pace with vehicle adoption is important for both equity and long-term planning. If some areas accumulate EVs faster than they gain charging stations, residents may face range anxiety, congestion at chargers, or barriers to adopting an EV at all.

Our original project plan focused on county-level analysis, but when we moved from a Kaggle copy of the charging dataset to the official U.S. Department of Energy Alternative Fuels Data Center (AFDC) export, we discovered that the AFDC file we used does not include a county field for each station. Instead, the AFDC data provides city, ZIP code, and latitude/longitude. To preserve data integrity and avoid building an additional ZIP-to-county crosswalk, we pivoted from a county-level analysis to a city-level analysis. We still retain the policy motivation (identifying gaps in infrastructure relative to EV adoption), but now frame our results in terms of cities across Washington.

We integrate two main datasets:

1. **Washington State EV Registrations** from the Department of Licensing (DOL), which contains every registered EV in the state with detailed attributes including make, model, model year, EV type (Battery Electric Vehicle [BEV] or Plug-In Hybrid Electric Vehicle [PHEV]), county, city, postal code, and other metadata.

2. **EV Charging Stations** from the **AFDC “Alt Fuel Stations”** dataset, filtered to Washington State, electric fuel type, and “existing” (operational) stations only.

Using these datasets, we:

- Filter both datasets to Washington State.
- Standardize city names to a canonical form.
- Aggregate EV registrations and charging stations by city.
- Construct a merged city-level dataset with:
  - Total EVs per city  
  - Total charging stations per city  
  - A simple EV-per-station ratio for each city
- Calculate a correlation between EV counts and station counts across cities.
- Identify cities with “high adoption but relatively limited charging access” by looking at cities with high EV counts but high EV-per-station ratios.

The final dataset includes **502 Washington cities** that appear in at least one of the two sources. Of these:

- **484 cities** have at least one registered EV.  
- **222 cities** have at least one charging station.  
- **204 cities** have both an EV presence and at least one charging station.  
- **280 cities** have EVs but no stations.
- **18 cities** have stations but no registered EVs (often highway or corridor locations serving through-traffic).

Across the entire state sample:

- The EV registration dataset contains **239,232 EV records**, of which:
  - **189,678** are Battery Electric Vehicles (BEVs).
  - **49,554** are Plug-In Hybrid Electric Vehicles (PHEVs).
- The AFDC data contains **2,907 existing EV charging station locations** in Washington State (after filtering to Status Code = “E” and Fuel Type Code = “ELEC”).

At the city level, EV counts and station counts are strongly related. Restricting to cities that have at least one EV and at least one station, the **Pearson correlation coefficient** between EV count and station count is approximately **0.94**, indicating a very strong positive relationship: places with more EVs almost always have more charging locations.

However, the absolute EV-per-station ratios reveal important local differences. Some large, urban cities with high EV adoption (e.g., Seattle, Bellevue, Redmond) also have dense charging infrastructure, resulting in moderate EV-per-station ratios. In contrast, certain suburban cities such as **Newcastle, Lake Stevens, Mercer Island, Sammamish, and Mukilteo** have relatively high EV counts but very few stations, producing particularly high EV-per-station ratios. These locations appear to be “next-wave” infrastructure priorities: they already have strong adoption but lag behind in public station coverage.

Overall, this project demonstrates how integrating official EV registration data with the federal EV infrastructure dataset can reveal where public charging is roughly keeping pace with adoption and where potential gaps are emerging. The final products include a documented and reproducible workflow, cleaned and integrated datasets, and summary statistics that can inform future work on more detailed spatial analysis and per-capita metrics using population data.

---

## Data Profile (500–1000 words)

### 1. Electric Vehicle Population Data (Washington DOL)

**Source:** Washington State Department of Licensing  
**Format:** CSV (`Electric_Vehicle_Population_Data.csv`)  
**Geographic scope:** Entire state of Washington, United States  
**Unit of observation:** Individual registered electric vehicle

This dataset lists every registered EV in Washington State. Each row represents a single vehicle record. Key fields include:

- `VIN (1-10)`: An anonymized portion of the vehicle’s VIN.
- `County`: County associated with the registration.
- `City`: City associated with the registration.
- `State`: Two-letter state code (in our case always “WA” after filtering).
- `Postal Code`: ZIP code.
- `Model Year`, `Make`, `Model`: Vehicle characteristics.
- `Electric Vehicle Type`: EV type; the two main values are  
  - “Battery Electric Vehicle (BEV)”  
  - “Plug-in Hybrid Electric Vehicle (PHEV)”
- `Clean Alternative Fuel Vehicle (CAFV) Eligibility`: Indicates eligibility for Washington incentives based on range.
- `Electric Range`: Electric-only range in miles (for BEVs and PHEVs).
- Additional fields relating to census tract, legislative district, and utility service area.

From the copy you provided, there are **239,232 EV records** in total. We restrict this dataset to vehicles where `State == "WA"` and then create a standardized city label (`City_clean`) by uppercasing and trimming spaces in the `City` field. This is the field we use to integrate with the AFDC station dataset.

**Ethical, legal, and policy considerations:**  
This dataset is published by a state government as open data. VINs are truncated and anonymized, and no personally identifiable information (PII) such as names or exact addresses are included. Our use is limited to aggregated counts at the city level, which further minimizes any reidentification risk. The dataset’s use falls under Washington’s open data terms; we comply by citing the source and not attempting to reidentify individuals.

---

### 2. Alternative Fuel Stations (AFDC) – EV Stations in Washington

**Source:** U.S. Department of Energy, Alternative Fuels Data Center (AFDC)  
**Original file name you provided:** `alt_fuel_stations (Nov 6 2025).csv`  
**Format:** CSV  
**Geographic scope:** United States; we filter to Washington State only.  
**Unit of observation:** Individual alternative fuel station location

This dataset lists alternative fuel stations for multiple fuel types across the United States. We restrict to EV charging locations in Washington using:

- `State == "WA"`
- `Fuel Type Code == "ELEC"`
- `Status Code == "E"` (existing / operational stations)

Key fields used in this project:

- `Fuel Type Code`: we filter to “ELEC”.
- `Station Name`: name of the station.
- `Street Address`, `City`, `State`, `ZIP`, `Country`: location fields.
- `Status Code`: station status (E = existing).
- `EV Level1 EVSE Num`, `EV Level2 EVSE Num`, `EV DC Fast Count`: counts of different charging equipment types per station.
- `Latitude`, `Longitude`: geographic coordinates for mapping.
- `ID`, `Updated At`, `Open Date`: metadata about each station entry.

After filtering, we obtain **2,907 existing EV charging station locations in Washington**.

We again create a standardized `City_clean` field by uppercasing and trimming the `City` string. Unlike some versions of the AFDC dataset, this particular export does **not** include a dedicated county field, which motivated our decision to work at the city level rather than the county level.

**Ethical, legal, and policy considerations:**  
The AFDC dataset is an official U.S. government resource published for public use. It does not contain personal information about EV owners or drivers; it lists only station locations and operational metadata. We access the dataset directly from AFDC instead of through Kaggle to ensure that licensing, provenance, and reproducibility are clear and that anyone can re-download the same file structure independently.

---

### 3. Integration Perspective

Although our original plan referenced “counties,” in practice our integration uses **cities** as the shared geographic unit because:

- The DOL EV data includes both county and city.
- The AFDC stations file you provided includes city but **not** county.
- Both datasets have complete `City` values for Washington (no missing cities after filtering), making city a robust join key.

We document this change explicitly in the Status Report and again here to maintain transparency between the planned and implemented design.

---

## Data Quality (500–1000 words)

We evaluated data quality along several dimensions: completeness, consistency, validity, and fitness for our intended analysis.

### Completeness

- **EV Registrations (DOL):**  
  After filtering to `State == "WA"`, there are **239,232 EV records**. The fields we rely on most—`City` and `State`—are fully populated in the data you supplied (no missing values in `City` for Washington rows). Other attributes like `Electric Range` or `CAFV Eligibility` contain occasional missing or “Unknown” values, but these are not central to our integration and analysis.

- **AFDC Stations:**  
  After filtering to Washington (`State == "WA"`), EV fuel type (`Fuel Type Code == "ELEC"`), and existing stations (`Status Code == "E"`), we have **2,907 rows**. In this subset, `City` is also fully populated (no missing values), which is critical for city-level integration. Some fields such as `EV Level1 EVSE Num`, `EV Level2 EVSE Num`, or `EV DC Fast Count` are missing for some stations, reflecting incomplete reporting on the equipment counts. Because our primary unit for integration is “station location,” and not the exact count of plugs per site, we treat each row as one station and do not attempt to impute missing EVSE counts.

### Consistency and Standardization

There are natural variations in city spelling and formatting (e.g., “Seattle”, “SEATTLE”, trailing spaces). To address this, we:

- Create `City_clean` in both datasets by:
  - Converting to uppercase.
  - Stripping leading and trailing whitespace.

All city-level grouping and merging are then performed on `City_clean`, ensuring consistent keys. This step is implemented in `scripts/clean_data.py`.

We also standardize the conceptual definition of a “station” to match the AFDC schema: one row in the AFDC file corresponds to one station location, regardless of how many plugs or connectors it has.

### Validity and Filtering Criteria

To ensure that our analysis reflects the current operational infrastructure:

- We **exclude** AFDC stations that are:
  - Under construction.
  - Planned but not yet operational.
  - Temporarily unavailable (if indicated by other statuses).

Practically, this is done by requiring `Status Code == "E"`. Similarly, we limit to `Fuel Type Code == "ELEC"` to avoid including other fuel types.

On the EV side, we include both BEVs and PHEVs because both require access to EV charging infrastructure, even though their charging patterns can differ. We do not restrict by model year; older EVs remain part of the adoption landscape as long as they are currently registered.

### Integration Quality and Known Limitations

The main integration challenge was the mismatch between our original county-based plan and the available fields in the AFDC stations data:

- The DOL dataset includes a `County` field.
- The AFDC export you provided does **not** include a `County` field; it offers only `City`, `ZIP`, and coordinates.

To avoid constructing a custom ZIP-to-county crosswalk or performing additional geocoding beyond the scope of this course project, we decided to integrate at the **city** level. We explicitly document this change in both the Status Report and this final README. The result is:

- **484 cities** with at least one registered EV.
- **222 cities** with at least one EV station.
- **204 cities** with at least one EV and at least one station (the overlapping set used for correlation analysis).

This city-based integration is internally consistent and reproducible based solely on the two provided CSVs.

### Suitability for Purpose

For our research question—broadly, how EV adoption and charging infrastructure relate geographically—the data are fit for purpose:

- They are official, government-maintained sources.
- They are comprehensive for Washington State.
- They allow us to identify cities with potential infrastructure gaps (high EV counts but high EV-per-station ratios).

At the same time, we note two limitations:

1. **No utilization data:**  
   The AFDC dataset lists station presence but not usage (e.g., kWh delivered, session counts, or time-of-use). We cannot directly measure congestion or real-world strain on infrastructure.

2. **No population data in our current workflow:**  
   We initially planned to analyze per-capita station availability by incorporating census population data. However, we ended up focusing on EV counts and station counts rather than integrating a third dataset. Population-normalized metrics remain an explicit target for future work.

---

## Findings (~500 words)

Our findings are derived from the integrated city-level dataset constructed from your two CSVs.

### Statewide Summary

- **239,232 registered EVs** in Washington (189,678 BEVs and 49,554 PHEVs).
- **2,907 existing EV charging station locations** in Washington.
- **484 cities** with at least one EV.
- **222 cities** with at least one station.
- **204 cities** with both EVs and stations.
- **280 cities** have EVs but no public EV station in the AFDC dataset.
- **18 cities** have stations but no EVs (likely corridor or special-use sites).

### Relationship Between EV Adoption and Stations

Using the 204 cities that have both at least one EV and at least one station, we compute the correlation between:

- `ev_count` = total registered EVs per city  
- `station_count` = total EV charging stations per city  

The **Pearson correlation coefficient is approximately 0.94**, indicating a very strong positive relationship. In other words, cities with more EVs almost always have more stations as well.

This pattern is intuitive: larger and more urbanized cities have both higher EV adoption and more public and semi-public charging locations.

### Top EV and Station Cities

The top cities by EV registrations include:

- **Seattle** – ~38,046 EVs and 709 stations  
- **Bellevue** – ~11,684 EVs and 295 stations  
- **Vancouver** – ~8,740 EVs and 75 stations  
- **Redmond** – ~8,320 EVs and 109 stations  
- **Bothell** – ~7,872 EVs and 28 stations  

Seattle and Bellevue, in particular, combine high EV counts with very large numbers of stations, yielding moderate EV-per-station ratios (around 40–55 EVs per station). This suggests relatively strong infrastructure coverage in those urban cores.

### Cities with Potential Infrastructure Gaps

To identify potential infrastructure gaps, we:

1. Focus on cities in the top quartile of EV counts (i.e., high adoption).
2. Rank them by **EV-per-station ratio** (higher ratio = more EVs per station = higher potential pressure on infrastructure).

Among high-EV cities, the following stand out with particularly high EV-per-station ratios:

- **Newcastle** – ~1,205 EVs; 1 station (≈ 1,205 EVs per station)  
- **Lake Stevens** – ~2,018 EVs; 2 stations (≈ 1,009 EVs per station)  
- **Mercer Island** – ~2,890 EVs; 3 stations (≈ 963 EVs per station)  
- **Kenmore** – ~1,363 EVs; 2 stations (≈ 681 EVs per station)  
- **Sammamish** – ~6,754 EVs; 11 stations (≈ 614 EVs per station)  
- **Mukilteo** – ~1,035 EVs; 2 stations (≈ 518 EVs per station)  
- **Mill Creek** – ~954 EVs; 2 stations (≈ 477 EVs per station)  

By contrast, some smaller communities have more stations than you would expect given their EV count—for example:

- **Tulalip** – 4 EVs; 6 stations (≈ 0.67 EVs per station)  
- Several small towns with 1–5 EVs but at least one station, often reflecting corridor charging on highways or near tourist areas.

These patterns suggest that while the overall state infrastructure scales with adoption, certain suburban or higher-income residential communities have strong EV adoption but fewer public stations per EV. These might be high-priority areas for future infrastructure expansion, especially if policymakers want to support equitable, public access beyond private home charging.

---

## Future Work (500–1000 words)

This project demonstrates a reproducible workflow for integrating EV registration data with EV charging station data and analyzing geographic alignment at the city level. At the same time, it points toward several concrete directions for future work:

### 1. Re-introducing County-Level Analysis

Our original research question emphasized **counties**, but we pivoted to cities because the AFDC export did not include a county field. With more time or additional data sources, we could:

- Use a ZIP-to-county crosswalk to map each AFDC station’s ZIP code to a county.
- Use latitude/longitude with a publicly available county boundary shapefile to assign each station to a county via spatial join.

This would allow direct comparison of county-level EV registrations and county-level station availability, closely matching the original project plan.

### 2. Incorporating Population and Demographics

The current analysis considers:

- EV counts (adoption).
- Station counts (infrastructure).

However, both should ideally be normalized by population or number of households. Future work could:

- Integrate population data from the U.S. Census or American Community Survey (ACS).
- Compute EVs per 1,000 residents and stations per 10,000 residents for each city or county.
- Stratify results by urban vs. rural status or socioeconomic indicators such as median household income.

This would allow a more precise view of equity in EV infrastructure: are lower-income or rural communities getting proportionate access to charging?

### 3. Analyzing Equipment Types and Charging Speed

The AFDC dataset includes:

- `EV Level1 EVSE Num`
- `EV Level2 EVSE Num`
- `EV DC Fast Count`

In this project, we treat each row as one “station location” regardless of equipment type or plug count. A deeper investigation could distinguish between:

- Level 2 versus DC fast charging coverage.
- Total number of plugs per city, not just number of sites.
- Coverage along highway corridors versus residential or workplace charging.

This would help identify not just where charging is present, but where **fast, high-throughput** charging is available to support long-distance travel and dense urban usage.

### 4. Temporal Trends

Both datasets include the potential to analyze change over time:

- The DOL dataset contains model years and could potentially be linked to registration dates.
- The AFDC dataset includes `Open Date` and `Updated At` fields for stations.

Future work could build time series to answer questions such as:

- Are stations being added at a rate that keeps up with new EV registrations?
- Which cities are “closing the gap” and which are falling behind?

### 5. Utilization and Behavioral Data

Our analysis is limited to **capacity**, not **usage**. Ideally, we would combine:

- Charger session data (e.g., from utilities or networks).
- Charging network pricing data.
- Trip data or travel surveys.

This could reveal whether apparent gaps in infrastructure actually translate into user hardship (e.g., long wait times, frequent queuing) and help prioritize investments where they would have the greatest impact.

### 6. Reproducible Packaging and Containerization

We currently provide:

- Python scripts for cleaning, integration, and analysis.
- A simple “Run All” script to re-execute the workflow.
- A `requirements.txt` listing Python dependencies.

Future improvements could include:

- A Snakemake or similar workflow describing the pipeline explicitly as rules.
- A Dockerfile so that others can reproduce the environment exactly.
- Hosting the final cleaned and integrated datasets and outputs in a persistent repository such as Zenodo, with a DOI.

---

## Reproducing

This section describes how someone else can reproduce our results from scratch.

### 1. Clone the Repository

```bash
git clone <YOUR_REPO_URL>.git
cd <YOUR_REPO_NAME>


