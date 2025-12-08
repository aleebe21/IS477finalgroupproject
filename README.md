# EV Adoption and Charging Infrastructure in Washington State

## Contributors
- Affan Leebe
- Om Patel
The project was a joint collaboration where everyone had their role with unique and integral contributions to the deliverable. Affan Leebe was responsible for the overall vision and documentation of the project including the project overview, narrative of the profiling, quality check and analysis interpretation. In addition, Affan implemented the analysis pipeline from start to finish by generating visuals and making the whole project reproducible from the final product. Om Patel was responsible for the technical preparations of the datasets including gathering all of the data sources in their raw form, implementing the data cleaning script that served as a preprocessing utility for both EV and AFDC datasets, as well as outlining the ideas behind merging both in the cities format. The two then came together to assess the end results to confirm that the repository, output and documentation structure met the requirements for Milestone 4 by validating that the merged dataset was accurate. This allocation of tasks made it easy to create this project with high efficiency and low margin of error with regard to clarity, accuracy, and reproducibility.
---

## Summary (500–1000 words)
This project seeks to understand patterns of electric vehicle (EV) purchases compared to charging station availability as related to neighborhoods across Washington state. As the state moves towards EV adoption, this research is important for equity and future patterns since if certain areas have greater populations of EVs than charging stations, it will result in range anxiety, overpopulated charging stations, or even the inability to purchase an EV in the first place due to no charging stations in proximity.
The original project intention was to compare data at the county level; however, once transitioning from a Kaggle copy of the Department of Energy's fueling stations to the official Alternative Fuels Data Center (AFDC) export, it was discovered that the AFDC file does not possess a county level associated with each fueling station. Instead, the AFDC data includes city, zip code and lat/long. Thus, to ensure data quality without creating an additional crosswalk from zip to county levels (unnecessarily complicated), we switched our analysis from a county to a city level. Thus, we maintain the policy intention (to find deficiencies in charging availability per EV access) but report results on a city level across Washington instead.

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

At the city level, city totals of EVs and city totals of stations are highly correlated. Excluding the cities without at least one EV or one station, the Pearson correlation coefficient of city count EV and city count station comes out to ~0.94, meaning there's a very strong positive correlation: cities with more EVs have more charging locations and vice versa.
Nevertheless, the actual ratios of EVs to stations relative to population reveal nuanced local differences. For example, cities that are larger (Seattle, Bellevue, Redmond) and more urban in nature have high adoption rates but also many stations, showing reasonable ratios of EVs to stations. Yet certain suburban cities like Newcastle, Lake Stevens, Mercer Island, Sammamish, Mukilteo have a high number of EVs with very few stations, creating some very high ratios of EVs to stations. These cities seem to be on the radar for the "next wave" of infrastructure buildout - they have strong adoption so far, but without public stations yet, they lag behind.
Therefore, this project overall provides an example of how access to official datasets for registered EVs can be merged with the federal dataset for EV stations for infrastructure considerations to see where public charging is approximately in line with adoption or where discrepancies are starting to grow. The major takeaways from this project are a reproducible process, a cleaned and merged dataset and final metrics that would assist with future work involving spatial analysis and population-based per-capita measures.


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

Data Quality (500-1000 words)

We assessed the quality of data based on various dimensions: completeness, consistency, validity and fitness for our purposes.

Completeness

EV Registrations (DOL):
The filtered data contains 239,232 EV records post-scrub (only State == "WA" stays). The fields we use most - City and State - are populated for all rows in the data you provided (no missing values in City for Washington rows); fields like Electric Range or CAFV Eligibility may be missing or "Unknown" but are not fields we're integrating an analyzing at this time.

AFDC Stations:
Post-scrub, we have 2,907 rows (only State == "WA", Fuel Type Code == "ELEC" and Status Code == "E" are kept). In this filtered version, City is also populated for all stations (no missing values), which is critical for joining on the city level. However, fields like EV Level1 EVSE Num, EV Level2 EVSE Num or EV DC Fast Count are null for some stations; this represents partial reporting about how many EVSEs are available. Therefore, since the integrative unit of analysis is "station location" and not what's physically present at each site, these count misses will be treated as null, but no imputation will happen to create the same values for ease of data integration.

Consistency and Standardization

There will always be variation in spelling of words between datasets. For example, cities may not be spelled in uppercase or there might be a blank space afterwards (“Seattle”, “SEATTLE” with a trailing space). To circumvent any issues, we:

Create City_clean in both datasets where:

The entries are converted to uppercase.

The leading and trailing spaces are stripped.

Therefore, all city level group by and join actions will occur off of City_clean so that there is no inconsistency in what should be the same keys across datasets. This will be done in scripts/clean_data.py.

We also create a consistent definition of a "station"; similar to the AFDC schema, if there are many plugs or connectors at one location, it will still only count as one station.

### Validity and Filtering Criteria

To ensure that our analysis reflects the current operational infrastructure:

- We **exclude** AFDC stations that are:
  - Under construction.
  - Planned but not yet operational.
  - Temporarily unavailable (if indicated by other statuses).

Practically, this is done by requiring `Status Code == "E"`. Similarly, we limit to `Fuel Type Code == "ELEC"` to avoid including other fuel types.

On the EV side, we include both BEVs and PHEVs because both require access to EV charging infrastructure, even though their charging patterns can differ. We do not restrict by model year; older EVs remain part of the adoption landscape as long as they are currently registered.

Integration Completeness and Anticipated Constraints

The only challenge in integration came from what we originally planned for and what fields were available in the AFDC stations data, specifically:

The DOL dataset has a field for County.

The AFDC export you sent does not have a field for County, but rather City, ZIP, and coordinates.

Therefore, to avoid creating a custom ZIP-to-county crosswalk or geocoding additional data that extends beyond the scope of the course project, we chose to integrate on the city level. We acknowledge this in the Status Report as well as in this final README, so you are aware of our intentions. As a result:

484 cities have at least one registered EV.

222 cities have at least one EV station.

204 cities have at least one EV and one station (the intersecting set used for regression analysis).

This means that this integration on the city level is internally consistent and replicable based exclusively on the two provided .csvs.
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

Statewide Summary

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

This project presents a repeatable process from matching EV registration data to EV charging station data to geographically finding appropriate patterns on a city basis. At the same time, it suggests some tangible avenues for next steps:

Bringing back the County Comparison

Our original research question focused on counties as the level of assessment, but we changed our scope to cities due to the lack of a county field in the AFDC export. Given more time or additional fields from other sources, it would be possible to:

Incorporate a ZIP-to-county crosswalk to determine each AFDC station's ZIP code and what county it belongs to

Incorporate latitude/longitude in combination with publicly available counties' boundary shapefiles to determine which county a station belongs to through spatial join.

Thus, we could compare county registration EVs to county availability of stations, much like the original assessment question intended.

Adding Population and Demographics into the Mix

At present, we have only looked at:

Count of EVs (adoption)

Count of stations (infrastructure)

However, both would make more sense if normalized by population or households. Thus, future work could:

Bring in population data from the U.S. Census or American Community Survey (ACS)

Normalize EVs per 1,000 residents and stations per 10,000 residents in each city or county

Further stratify by urban vs. rural status or socioeconomic parameters (e.g., median household income).

This would give a clearer picture of equity of access to charging station infrastructure: are lower-income or rural populations receiving their fair share of resources?

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

Temporal Trends

Both datasets contain the possibility of measuring change over time:

The DOL data has model years and could, at best, be associated with the year of registration.

The AFDC data has fields for stations open and updated at.

A future study could build a time series to determine:

Are stations being opened at a pace that meets the new EVs being registered?

Which cities are "catching up" and which cities are "falling behind"?

Utilization and Behavioral Data

We're missing use data since our analysis only concerns capacity. Ideally, we'd have:

Charger session data (harkening to utilities or networks).

Charging network pricing data.

Trip data/transportation surveys.

This would go a long way in determining whether gaps in information suggest a lack of charging capabilities or user frustration (wait times, queuing) that can better prioritize investments in the most effective areas.

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
git clone <https://github.com/aleebe21/IS477finalgroupproject/tree/main>.git
cd <IS477finalgroupproject>


