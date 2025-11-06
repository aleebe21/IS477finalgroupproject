Project Overview

This project seeks to explore the relationship between electric vehicle (EV) registrations and EV charging stations on a per capita basis across Washington State's counties. As EVs become more common, equity of access suggests that the per capita infrastructure must be available for people in respective areas to also adopt such vehicles. Therefore, understanding how large relative to one's driving radius the number of charging stations is either positively or negatively impacted by county registrations will indicate where infrastructure is not keeping up with need.

Research question: What is the correlation between the number of registered electric vehicles across the counties and the number of charging stations per capita? Not only do we seek to understand this relationship, but also we'll seek to find counties that, relative to others, may have high adoption of electric vehicles but limited charging stations per person, suggesting newer gaps or gaps that may be occurring in the future.

This project is relevant to the data lifecycle covered in class as these data acquisition sources, preliminary scripts and documentation are all part of the data quality lifecycle process: acquisition, data cleaning, integration, quality assessment, exploration/visualization, and reporting/reproducibility. The project folder will contain datasets, scripts/notebooks, and related documentation for each of these components.

Data Sources and Changes After Feedback

Upon initial planning, we were set to use the Kaggle dataset to get EV charging stations. However, following feedback from Milestone 2, I realized I needed to rethink where we got our second data source from. The instructor noted that while Kaggle can be a good source, it's not always reliable in terms of licensing or source credit. After looking through the Kaggle dataset's metadata, we were able to confirm that this particular dataset was from the U.S. Department of Energy Alternative Fuels Data Center (AFDC), which is an official nationwide grid of charging access.

Therefore, for purposes of transparency and reproducibility, we decided to access the AFDC dataset directly instead of keeping it through Kaggle. By doing this, we are able to credit a federal open-data source instead, remove licensing issues from the equation, and ensure that third-party reviewers can independently access the same dataset download without relying on something like Kaggle.

Our other dataset regarding EV adoption remains consistent and comes from the Washington State Department of Licensing (DOL). This dataset comprises all registered electric vehicles across the state since these records are consistently uploaded and reported by the state government.

Work Accomplished Thus Far

The majority of early work revolved around accumulating both datasets and performing exploratory data analysis to understand how the data were structured and what fields were relevant for later integration. These notes exist in the notebook notebooks/01_initial_ where we assessed columns and formats, missing data and geographic relevancy.

The primary data cleaning efforts thus far include preparing both datasets for merging through adjusted county names, numbers of locations in Washington only, station statuses, etc.

Initial Steps Include:

For the AFDC dataset:

Filtering to only include charging stations located in Washington State

Removing stations that are inactive or still under construction

Conforming all counties to uppercase formatting so a merge is easier upon integration

Examining ZIP codes and city names so if counties are missing from some rows in the future merge attempt, we can hopefully fall back on more reliable data associations

Thus far, these changes are detailed in scripts/clean_data.py which was developed by Om. The script works effectively but may need minor tweaks post-integration to enhance geo-referencing with certain datasets.

For the DOL Dataset:

No changes were made; however, it was assessed that one column can remain unnamed since we're approaching this with more than one merge technique. Therefore - after geographical observations - names must be conformed on both sides so integration is easier.

Integration:

The next stage of work involves merging the two datasets by counties. County aggregation works most reliably because both datasets have county fields along with aggregated statistics at the county level that provide an obvious policy level of concern to compare along with population associations via per capita assessments. The final integrated dataset will derive a summary from both files that includes:

Total EV registrations by county

Total public charging stations by county

Total stations per capita (population-normed density)

Total adoption-to-infrastructure ratio (EVs/changing stations per county)

This will exist in scripts/integrate_data.py, which is currently scaffolded with notes but no reliable progress thus far.

Preliminary Discoveries:

Although analysis is not yet performed, Exploratory Discoveries make sense thus far; for example,

King County holds the highest number of charging stations as well as EV registrations throughout the state.

Suburban counties dominate overall success (Snohomish, Kitsap) but slightly lag behind King County in overall access.

Several rural towns show almost zero EV adoption and little marketplace demand with few charging stations available.

A few towns exceed expectations of adoption compared to accessible stations which suggest areas that should - at least - be looked at for future expansion as there is currently a strong population there.

These preliminary thoughts will be validated quantitatively through further assessment.

Current Timeline

Here is an updated timeline compared against current accomplishments:

Date RangeTaskTeam MemberStatusOct 9 - Oct 15Data acquisition and initial explorationAffan & OmCompleteOct 17 - Nov 15Data cleaning and geographic standardizationOmCurrently almost completeNov 12 - Dec 1Integration findings, analysis, and visualizationAffanUpcomingDec 2 - Dec 10Final reporting and release packagingAffan & OmUpcoming

The previous timeline suggested that data cleaning would finish by October 24; however, it took extra time to assess both cities and how to integrate them together took longer than expected because of missing geographic fields needing additional mapping assessments. This has not impacted our ability to finalize the project on time.

Contributions Made (Milestone 3)

Affan Leebe

I took the lead in determining preliminary stages of feedback on the dataset sourcing issue and transitioned us from Kaggle to AFDC without difficulty. I performed exploratory data analysis in Jupyter Notebook, wrote this Status Report, drafted this section of the project proposal with documentary notes for GitHub folder creation for transparency and success.

Om Patel

Om downloaded both datasets and formatted both before creating scripts/clean_data.py, where we documented how we could clean the data for potential implementation. Om visually led efforts for filtering geo-referenced data across the country and prepared for Washington alone while also beginning to structure the integration process between the two datasets.

Next Steps

The next steps involve integrating both datasets together for accessible analysis for later visuals through graphs that can be generated heat maps compared between each metric so we can visualize efficacy with granularity. Once analysis is complete, we'll write our final report then generate a GitHub release for public viewing success.
