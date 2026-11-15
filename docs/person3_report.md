## Testing

We created two separate Python testing files, test_data_cleaning.py and test_eda_stats.py, to verify the correctness of our data cleaning and exploratory data analysis functions. Both files use assertions with small, controlled datasets to compare actual outputs against expected results.

The data cleaning tests cover eight areas, including census tract GEOID construction, handling missing values, removing unnecessary annotation columns, parsing ACS variable labels, calculating English assistance needs among adults aged 65 and older, computing percentages and coefficients of variation, checking detailed language mappings, and cleaning program-site language information.

We also developed five additional tests for the EDA functions. These verify missing-value summaries, seven-number statistical summaries, categorical frequency counts, comparisons between broad and detailed language groups, and the number of program sites associated with each language.

All 13 tests passed successfully when executed locally. We also ran flake8 on the src directory, and no style violations were reported.

These tests provide evidence that the functions behave correctly on the tested examples. However, they do not guarantee that all real-world data issues have been identified. We will continue validating the results as additional datasets are integrated.


## Challenge Goals Update

### Multiple Datasets

Our project continues to pursue the Multiple Datasets challenge goal. We are using two American Community Survey (ACS) tables, B16004 and C16001, to examine English proficiency and language assistance needs in King County. B16004 provides language information for adults aged 65 and older, while C16001 provides more detailed language categories for residents aged 5 and older.

We have developed functions to clean and compare these datasets, including matching detailed language categories to broader language groups. We have also implemented geographic identifier processing to support joining census tract data with geographic boundaries.

Our remaining work includes completing and validating the integration of Sound Generations program-site information. This will allow us to examine how available language services compare with community needs. We will also ensure that our analysis does not treat C16001 estimates for residents aged 5 and older as estimates specifically for older adults.

### Messy Data

Our project also continues to pursue the Messy Data challenge goal. The raw ACS data contains complex variable names, missing-value codes, annotation columns, and geographic identifiers that require consistent formatting.

We developed reusable Python functions to convert invalid values into missing values, remove unnecessary annotation columns, construct standardized geographic identifiers, and reshape the ACS tables into a format suitable for analysis.

We also implemented functions to standardize language labels in program-site information and remove duplicate site-language combinations. These functions have been tested using controlled examples.

The main remaining challenges are validating the cleaned data against the original sources, checking the reliability of ACS estimates, and ensuring that language categories are consistently matched across datasets.


## Work Plan Evaluation

Our original proposal estimated approximately 35 hours of work, including 4 hours for data collection, 5 hours for data cleaning, 5 hours for language needs analysis, 7 hours for program coverage analysis, 7 hours for data visualization, and 7 hours for testing and final report preparation.

At the exploratory data analysis stage, we have implemented the ACS data cleaning pipeline, developed functions for statistical summaries and language-group comparisons, and created visualization outputs. We have also completed 13 automated tests covering data cleaning and statistical analysis, and all Python files currently pass flake8.

Some tasks remain in progress, particularly validating the geographic analysis, completing the Sound Generations program-site integration, interpreting the visualizations, and assembling the final report.

Our original time estimates will need to be evaluated against the actual hours contributed by each team member. The remaining work will focus on validating our findings, completing the analysis of program coverage, and integrating the results into a consistent final report.


## Collaboration

Our team collaborated through a shared GitHub repository to develop the data cleaning, exploratory analysis, visualization, and testing components of the project.

We used Python libraries, including pandas, NumPy, Matplotlib, and GeoPandas, to process and analyze the datasets.