Overview: Describe the overall goal of your project.

a. The goal of this project is to analyze the relationship between electric vehicle (EV) adoption and the availability of charging infrastructure across counties in Washington State. We want to analyze this because as electric vehicles become increasingly popular, it is important to understand and recognize that charging accessibility plays a crucial role in determining where adoption of electric vehicles grows the fastest. By integrating EV registration data from the Washington State Department of Licensing and then combining that data with nationwide charging station data from Kaggle, this project will identify whether areas with more charging stations experience higher levels of EV adoption. Our project aligns with most of the broader data lifecycle concepts discussed in class — from data acquisition and integration to cleaning, quality assessment, and reproducibility. At the conclusion of our project, the findings could inform policymakers and urban planners about how infrastructure influences sustainable transportation growth.

Research Question(s): What is/are the question(s) you intend to address?
a. Our primary question: How does the availability and density of EV charging stations relate to the number of registered electric vehicles across counties in Washington State?
Alternative questions: Are there counties with high EV adoption but limited charging infrastructure (this question can help us analyze any potential infrastructure gaps)? Do counties with greater urbanization or higher population density show stronger relationships between EV registrations and charging access?

Team: Clearly define team member roles and responsibilities
Affan Leebe
Role: Individual project lead
Responsibilities:
Conducting exploratory data analysis and visualization
Writing documentation and final report
Managing GitHub repository and commits


Om Patel:
Role: Teammate
Responsibilities:
Data collection and cleaning for both datasets
Integration of datasets using Python (Pandas)


Datasets: Identify and describe the datasets that you will use. You need to use at least two different datasets that need to be integrated. If you are looking for ideas for datasets to use, please reach out via Campuswire.

https://catalog.data.gov/dataset/electric-vehicle-population-data

This dataset provides detailed information about registered electric vehicles in Washington State with fields such as make, model, model year, electric range, county, city, postal code, and anonymized VIN numbers. It is formatted in CSV, and with approximately 200,000+ records covering all Washington counties

https://www.kaggle.com/datasets/salvatoresaia/ev-charging-stations-us?utm_source

This dataset contains information about public and private EV charging stations across the United States. It includes station name, location (latitude and longitude), city, state, ZIP code, and connector type (Level 1, Level 2, DC Fast). We will filter this subset to limit it to just Washington State which will be used to align with the EV registration data.
It is formatted in CSV.

Timeline: Document the plan and timeline for implementing your project including who will complete each task.
Your plan must clearly address each of the requirements described above

Date Range	Task	Responsible
Oct 9 – Oct 15	Collect both datasets and perform basic exploration (check columns, missing values)	Affan and Om
Oct 17 – Oct 24	Clean and preprocess data (remove duplicates, filter for WA, standardize county names) Om
Oct 27 – Nov 11	Write and submit Interim Status Report	Affan and Om
Nov 12 – Dec 1	Conduct additional analysis, refine visuals, document workflow automation	Affan
Dec 2 – Dec 10	Finalize report (README.md), upload final artifacts to GitHub, submit final project release	Affan and Om


Constraints: 

The EV dataset is specific to Washington State, while the Kaggle charging dataset covers all U.S. states. The data must be filtered and matched accurately by county or ZIP code. Some charging stations do not have complete location fields which could affect aggregation accuracy.

Gaps: Identify any known gaps or areas where you need additional input.

The Kaggle dataset contains station presence but not utilization rates of the EV chargers, which would deepen the analysis if available. It would also help if there was incorporated income or population data to better explain differences in adoption. There is no personally identifiable information.
