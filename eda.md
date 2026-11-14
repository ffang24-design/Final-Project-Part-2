---
title: Part 2 - Exploratory Data Analysis
---

## Overview

Now that you have a more solid idea of what you'd like to do for your final project, let's explore your data in more depth. For this part of the final project, you will conduct an open-ended Exploratory Data Analysis (EDA) on your chosen dataset(s) to explore the structure, patterns, and relationships within the data. This includes cleaning and summarizing the data, creating visualizations, and highlighting any trends, anomalies, or interesting observations. Your task is to think critically, ask questions of the data, and communicate your findings clearly. Your EDA should lay the groundwork for more advanced analysis or modeling in later parts of the project.

## Requirements

The following sections describe the requirements for the EDA. Some sections will be the same or updated from your proposal. Your EDA report will probably be about 3-5 pages long, but it is acceptable for the report to be longer or shorter as long as it sufficiently covers all of the required sections. We will recommend a soft upper limit of 8 pages. Submit your EDA as a PDF file. (In Microsoft Word, you can choose "Save As" to save your document as a PDF file. In Google Docs, you can choose "File", then "Download" and save your document as a PDF. **Do not turn in a Word document, ODT, or plain text file.**)

### Report

**Include a link to your Github repository in the Title and Author(s) section. Make sure your repository's visibility setting is set to 'Public'!**

**Submit a roughly 3-5 page report documenting your findings.** You should update any of the previous sections based on feedback from the proposal.

Outline your report with at least the following sections (**make sure to label your sections in your report**):

1. **Title and Author(s):** Include a link to your Github repository containing all relevant source code files for your project so far, including but not limited to code for your EDA.
2. **Summary of Research Questions:** Same as Proposal, updated according to feedback.
3. **Motivation:** Same as Proposal, updated according to feedback.
4. **Dataset:** Same as Proposal, updated according to feedback.
5. **Method:** Same as Proposal, updated with any changes made during implementation of the EDA components. You should describe, at a high level, the steps you took to conduct your EDA.
6. **EDA Results:** Answer the following questions about your data about each dataset you are working with. If you are specifically pursuing the **Multiple Datasets** or **Result Validity** challenge goals, you will have some slightly different requirements. See the end of this list for details.
    * **How large is your dataset?** Give the number of rows and columns. What do the rows represent? What about the columns?
    * **Does your dataset have any missing data?** 
        * If your dataset does not have missing data, explain how you know this. You should use Pythonic functions or implementation to justify your answer!
        * If your dataset has missing data, describe the missing data (e.g., number of rows or columns; % missingness; etc.) and your plan for working with it. 
    * **What are the variables of interest for your research questions?** Give the names of columns or data attributes, and what they represent. Connect them back to your research question(s). Why are you using these specific columns or attributes?
    * **Give a summary of each variable of interest.**
        * For quantitative variables, this will be a seven-number summary (mean, standard deviation, minimum, first quartile, median, third quartile, maximum). You are welcome to reuse your code from [**HW 1: Processing**](https://courses.cs.washington.edu/courses/cse163/26au/processing/) or use [`pandas`' `DataFrame.describe` method.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html).
        * For categorical variables, this will be a list of all the unique values that the variable can take, along with a count for each value.
    * **Create at least 2 visualizations** *per dataset*, for the variables of interest that you identified in the previous question. You can use scatter, line, and bar plots as we've done in class, or another type of plot of your choosing. Include, at minimum, the following information for each plot:
        * Legend (if applicable)
        * Caption for the plot that gives a one-sentence summary of what your reader should interpret from the plot
        * A brief paragraph explaining the variable(s) represented in the plot, why you chose this particular plot, and the information your readers should take away from seeing the plot.
    * **(Multiple Datasets only):** Give a brief summary of how the datasets are related to one another.
    * **(Multiple Datasets only):** Perform the EDA above for every *combination* of datasets you intend to use, instead of on single datasets. For example, if you have the datasets `movies.csv`, `actors.csv`, and `reviews.csv`; and you intend to join `movies.csv` and `actors.csv`, and `movies.csv` and `reviews.csv`, you will need to conduct EDA for the joined `movies.csv`-`actors.csv` and for the joined `movies.csv`-`reviews.csv`.
    * **(Result Validity only):** State your null hypothesis for each research question you intend to do result validation on. Give the type of statistical test you will be using and the assumptions for that test. As part of your EDA, you must verify the assumptions for your test.
7. **Challenge Goals Update** Same as Proposal, updated with any changes made during implementation. If you find that your challenge goals have been scaled back, expanded, or changed since your proposal, explain those changes here, along with your updated plan for meeting the challenge goals.
8. **Work Plan Evaluation** Evaluate your proposed work plan. How accurate were your proposed work plan estimates? Why were your estimates close to reality or far from reality? What tasks still need to be completed, and how much time do you estimate you'll need for them?
9. **Testing** Describe how you tested your EDA code and why you tested in that way to ensure your results were correct. Did you use assert statements? Smaller data files? Visualizations? You should submit your tests and any testing files along with your code. Make sure you tell us why we should trust your results!
10. **Collaboration** State the other people and resources that you have consulted so far during the project aside from the course staff and team members.

Some additional formatting guidelines are as follows:

* **All visualizations must be captioned and titled AND be described or referenced in the body of the report.** Make sure to explain how your visualizations were produced and contribute to your EDA.
* **All pages must be numbered.** If you choose to include a title page, it must also have the page number. All other headers and footers are optional.
* The report must have the title **`eda.pdf`** (exactly as such!) in order to be counted on Gradescope. 
* **Do not single-space your report. Font size must be 11 or above.** Beyond this, you are free to use whatever font, spacing, and margins you'd like.
* You may choose to include additional information, questions, or references in an appendix that follows the report. There is no limit to how long your appendix may be, but its contents will neither be assessed for quality nor read in detail.

### Code

Your code should meet the following requirements.

* Your project must be written in at least one Python script (`.py` files). You are more than welcome to experiment and/or develop in a Jupyter Notebook, but your end result must be a runnable Python script to output all your results. Your project should use the main method pattern for modules that can be run. **For the final project deliverables, you will be required to write at least two substantial non-testing Python modules, but there is no requirement for the number of modules you submit for the EDA.**
* Your code must pass `flake8` and should follow the [CSE 163 Code Quality Guide](/resources/code_quality.md). Your source code documentation can assume that the reader has already read your report — you do not need to repeat any of those details, but it doesn't hurt to restate the highlights.
* You should write a testing Python program to test the code that you wrote for the project. Remember that testing is a way for you to ensure your results are valid by checking that the code you wrote is correct. Your testing programs do not count as one of the two required modules for the final project deliverables.

## Submissions and Grading

You will be graded on the quality and thoughtfulness of your responses, so make sure you are giving adequate time to each question.

[Submit your work on Gradescope by November 15th at 11:59pm PST.](https://www.gradescope.com/courses/1401707) Make sure to include your EDA as a **PDF** titled `eda.pdf`, and at least two Python modules (your code, and your testing file)!