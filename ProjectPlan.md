Overview: Describe the overall goal of your project.
a. The goal of this project is to analyze the relationship between electric vehicle (EV) adoption and the availability of charging infrastructure across counties in Washington State. As electric vehicles become increasingly popular, charging accessibility plays a crucial role in determining where adoption grows the fastest. By integrating EV registration data from the Washington State Department of Licensing with nationwide charging station data from Kaggle, this project seeks to identify whether areas with more charging stations experience higher levels of EV adoption and to uncover regions that may be underserved in infrastructure.

This analysis aligns with the broader data lifecycle concepts discussed in class — from data acquisition and integration to cleaning, quality assessment, and reproducibility. The findings could inform policymakers and urban planners about how infrastructure influences sustainable transportation growth.

Research Question(s): What is/are the question(s) you intend to address?
a. Primary Question: How does the availability and density of EV charging stations relate to the number of registered electric vehicles across counties in Washington State?
Secondary Questions:Are there counties with high EV adoption but limited charging infrastructure (potential infrastructure gaps)? Do counties with greater urbanization or higher population density show stronger relationships between EV registrations and charging access?

Team: Clearly define team member roles and responsibilities
Affan Leebe
Role: Individual project lead
Responsibilities:
Conducting exploratory data analysis and visualization
Writing documentation and final report
Managing GitHub repository, commits, and versioning


Om Patel:
Role: Team-mate
Responsibilities:
Data collection and cleaning for both datasets
Integration of datasets using Python (Pandas)


Datasets: Identify and describe the datasets that you will use. You need to use at least two different datasets that need to be integrated. If you are looking for ideas for datasets to use, please reach out via Campuswire.
  https://catalog.data.gov/dataset/electric-vehicle-population-data
  https://www.kaggle.com/datasets/salvatoresaia/ev-charging-stations-us?utm_source=chatgpt.com
  
Timeline: Document the plan and timeline for implementing your project including who will complete each task.
Your plan must clearly address each of the requirements described above

Date Range	Task	Responsible
Oct 7 – Oct 10	Collect both datasets and perform basic exploration (check columns, missing values)	Affan
Oct 11 – Oct 17	Clean and preprocess data (remove duplicates, filter for WA, standardize county names)	Affan
Oct 18 – Oct 25	Integrate datasets by county, aggregate EV and charger counts	Affan
Oct 26 – Nov 5	Conduct exploratory analysis and generate visualizations (scatterplots, heatmaps)	Affan
Nov 6 – Nov 11	Write and submit Interim Status Report	Affan
Nov 12 – Dec 1	Conduct additional analysis, refine visuals, document workflow automation	Affan
Dec 2 – Dec 10	Finalize report (README.md), upload final artifacts to GitHub, submit final project release	Affan


Constraints: Describe any known constraints.

Geographic Alignment:
The EV dataset is specific to Washington State, while the Kaggle charging dataset covers all U.S. states. The data must be filtered and matched accurately by county or ZIP code.
Data Completeness:
Some charging stations may lack complete location fields (missing ZIP or county). This could affect aggregation accuracy.
Time Frame:
The EV dataset’s latest update may not align perfectly with the charging dataset’s collection date, potentially introducing small time mismatches.
Technical:
Integration and visualization require Python or SQL tools; computing resources and data cleaning may take time.

Gaps: Identify any known gaps or areas where you need additional input.

Demographic Context:
Future iterations could incorporate income or population data to better explain differences in adoption.
Charger Usage Data:
The Kaggle dataset contains station presence but not utilization rates, which would deepen the analysis if available.
Workflow Automation:
While initial data integration will be manual, a Snakemake or automated Python pipeline will be added later as the course covers workflow automation topics.
Ethical & Legal:
No personally identifiable information is included, but licenses and attributions will be properly cited in the final submission.

Your plan should anticipate later course topics even if you don’t yet know all the details. It is expected that your plan will evolve over time.
