---
title: Part 1 - Proposal
---

For the final project, you will design and complete an original data programming project that demonstrates your mastery of course concepts. You'll identify your own research questions, find and work with a dataset of your choice, and produce a data-driven analysis, visualization, or interactive application. We will also provide [five project strands](https://courses.cs.washington.edu/courses/cse163/26au/strands/). that you may select to work on instead. Your **project proposal** will outline your research questions, motivation, dataset, chosen challenge goals (at least 2 from the provided list), methods, and work plan. This option allows you to explore a topic you're passionate about, apply skills you've developed throughout the quarter to new material, and create something entirely your own from the ground up! You are encouraged to work with up to 2 partners for your project.

For Part 1 of the Final Project, you will propose a data analysis project to the course staff. This can be almost anything that you choose. You might select a project from your field of study, your extracurricular interests, government or public policy, or elsewhere. Another good source of ideas is repeating an analysis that you read about in the popular press or in a scientific paper — usually you will do a simplified version of the analysis. We are just looking for you to show that you have a better understanding of how data works and the kinds of questions you might want to answer!

The goal of the project proposal is for you to describe your idea in enough detail that the course staff can evaluate whether it is an appropriate project. You are able to work in a group of up to 3 people total. The final project is composed of three main parts, a proposal, an exploratory data analysis, and the final report/code. These **cannot be submitted late and cannot be resubmitted through the resubmission process**. Once the deadline for a project part passes, you will no longer be able to make further submissions for that part of the project.

## Requirements

The following sections describe some requirements for your proposal and project more broadly. Your proposal will probably be about 1-2 pages long, but it is acceptable for the proposal to be longer or shorter as long as it sufficiently covers all of the required sections. Do not worry too much about the length, you should just focus on conveying the required information in as much detail as you think is relevant. Submit your proposal as a PDF file. (In Microsoft Word, you can choose "Save As" to save your document as a PDF file. In Google Docs, you can choose "File", then "Download" and save your document as a PDF. **Do not turn in a Word document, ODT, or plain text file.**)

### Proposal Format

 Your project proposal should include the following sections:

* **Title and author(s).** The title should reflect your specific research questions (not just “CSE 163 Project”).
* **Summary of research questions.** Give a numbered list of 3 or more research questions and a brief description of what you will investigate. Each research question should have 1–3 sentences and propose something that can be definitively answered, not just a general topic or area of investigation.
* **Motivation.** Expand on your research questions by providing context about why you care about the problem. How does knowing the answers affect the world or our understanding of it?
* **Dataset.** Describe the real, existing dataset that you will use, **including exact URLs**. You may not use a dataset that has been used in a previous CSE 163 assignment or demo. You may not repeat an analysis that you have performed in another class (though you might do something inspired by another class). The data must be real — neither you nor someone else may make up the data.
* **Challenge goals.** Select at least **2** challenge goals that you are planning to meet. Justify why you think your project will meet each goal. Try to bold the name of your challenge goal to make it obvious which one you are talking about. If you would like to meet more than 2 goals, discuss the 2 goals that you’re most passionate about. It is okay if you're not sure *how* to complete the challenge goal at this stage; we will learn some techniques to address fundamental aspects of all of them during the quarter.
* **Method.** For each research question, outline the steps you will takes to implement your project deliverables. You should provide enough detail that someone else could independently reproduce your experiment. For each computation, indicate how the result would lead you to a conclusion about one or more research questions. Highlight connections to challenge goals. Refer to specific rows, columns, or elements in your dataset. You will not need to provide any code, but your methodology should contain enough details that a TA will be able to understand how you will approach the computation.
* **Work Plan.** Describe your plan to divide the project into at least 3 (but no more than 7) discrete tasks, each with an estimate of the time in hours required for each task. Then, describe your workflow for developing code, testing code, and coordinating work—particularly how team members can support each other in case one task is unexpectedly challenging. You should also discuss with your group the specifics of how you will develop Python and show that you've set up your development environment (see [here](#development-setup) for more information on development environments. All team members must contribute equally to the deliverables.
    * While you don't need to submit any proof you've done so, you should do the local development setup for Python on your computer if possible. A very common challenge students face on the project is realizing too late that they can't use an online solution since their dataset is too large or it might not have the library you want. You **must** install Python on your computer early to help you avoid running into this later.

### Dataset

**You are not allowed to use a dataset that we have used in class as the central dataset of your project.** You can use one of our datasets to add on to a part of your project, but it should not be the central focus.

Your report must include simple, clear, unambiguous instructions that anyone can follow to download the data themselves. You should not rely on the staff to be able to "figure out" how to access the data, you must provide instructions for us. If the data is not publicly available or requires an account to log in, then you should make it available to course staff or include it with your assignment submission. One way to do this is to host your dataset on Dropbox or Google Drive and provide a link to this in your report. If the full dataset is too large to download, then provide a subset of it for the course staff to experiment with.

**Do not** use a dataset that cannot be shared with the course staff, such as one that contains confidential medical information or intellectual property. **Do not** manually perform any data cleaning steps — all data cleaning should be done programmatically, by Python code that you write.

### Challenge Goals

Challenge goals help us to define expectations while still offering flexibility for you to design your own project. Meeting 2 or more challenge goals will likely require writing at least 120 lines of Python code. In order to qualify for a challenge goal, you must experiment with something not explicitly discussed in the course. Here are the challenge goals you can choose from. We provide some examples for some of the bullets that are not meant to be exhaustive lists.

* **Multiple Datasets**: Use multiple datasets together to come up with a richer analysis. This requirement is not just about using more than one dataset across your research questions, but is more about combining the datasets to make a more in-depth analysis. This will likely requires you to join or combine tables together to solve a research question. Our take-home assessment 5 that combines Census data with food access data is a good example of this.
* **Messy Data**: Using a dataset that is not cleanly presented to you in a CSV already (or any other format that could be easily converted into a CSV). Some possible examples: writing code to scrape data from the web, using an API to gather data, or using some dataset that requires a lot of pre-processing to be usable.
* **Result Validity**: Do some extra work on top of your results to verify the validity of the results. For example, using some test of statistical significance to verify your results aren't likely to happen by chance.
* **Machine Learning**: Dive deep into applying machine learning to your dataset to gain insights about the data or use it to make predictions about the future. Be explicit with what your goal is and how you will assess if you meet that goal. One example could be looking at various model types (and different settings of their hyperparameters) to identify which model is "best" (by how you define best). Another could be looking at how to use an "interpretable model" to understand which features are the most informative for how a decision is made. **This challenge goal requires going above and beyond the fundamental steps of a Machine Learning pipeline we introduce in class. To achieve this challenge goal, you need to demonstrate exploration of more ideas in machine learning.**
* **New Library**: Learn a new Python library and use it in your project in a significant way to help with your analysis. Part of this class is being able to learn libraries in Python. Show that you are able to take what you've learned in the context of learning a library we have not discussed in-depth in this course. In the [Libraries](#libraries) below, we list some recommended libraries (and a complete list of the libraries will cover in this class that do not count as new).
* **Other**: If you are thinking of doing a project that you think is challenging enough but does not fit into any of these challenge goals, you can propose a new one to explain why you think your project will be challenging. Do remember that this should be a last resort since it can be challenging to assess the difficulty of your new goal. We reserve the right to deny your proposed challenge goal and you will need to go back and figure out how to make your project challenging enough before submitting.

### Challenge Goal Requirements

Additional requirements for each of the challenge goals listed above are as follows. Your challenge goals must meet these minimum requirements in order to be counted.

* **Multiple Datasets**
    * Must have at least 3 datasets that are used together in some way
    * At least two of the research questions should involve at least two datasets
    * Must have at least one join/merge operation between the datasets
* **Messy Data**
    * Data cannot be in a file format that we have worked with in class (`.csv`, `.shp`, `.json`, `.txt`) or be easily converted to one of these forms (i.e., cannot be converted in 5 or fewer lines of code)
    * Data from web-scraping, API, or which require lots of preprocessing all count as messy data
        * Example: using imputation for large amounts of missing data
* **Result Validity**
    * Validity must be verified through statistical testing or some other proven testing method using domain expertise
    * Any test that is used must be justified and explained in the context of the data and research questions
    * Results of the validity tests must be clearly interpreted alongside preliminary results from the analysis
    * Validity tests do not count towards required testing modules in the final report and code as they should be validating results, not testing the robustness of your code
* **Machine Learning**
    * One or both of the following:
        * Using a new model that was not previously discussed in class (no `DecisionTree`s)
        * Training several models with different hyperparameters 
* **New Library**
    * Must use at least one library that was not introduced in class (see [below](#libraries)) to answer at least two research questions
    * Multiple libraries do not count as separate challenge goals
        * e.g., using `Scipy` and `plotly` counts as one challenge goal
    * The new library may be used in tandem with one of the other challenge goals
        * e.g., using `Pytorch` to create advanced machine learning models

## Advice

The following sections have some advice on dataset sources and libraries that you might want to look into. We also provide some more context for what we will be covering for the rest of the quarter.

### Sources of Data

The best approach is to start with a problem that interests you, and then look for data. Google will be your friend for finding a dataset. Alternately an equally valid approach involves, starting with a dataset that looks interesting and designing questions that interest you around that data. Here are some possible data sources, but many more exist:

* A variety of datasets are available from [UW Libraries](https://db.lib.washington.edu/)
* [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets) - large variety of maintained data sets
* [Baron Schwartz's list of datasets](http://www.mysqlperformanceblog.com/2011/02/01/sample-datasets-for-benchmarking-and-testing/). Some of these are themselves rich lists of datasets, such as the [Amazon AWS public data sets](http://aws.amazon.com/datasets).
* [Data.gov](http://www.data.gov/) for U.S. open government data, [data.wa.gov](https://data.wa.gov/) for Washington state open government data, and [data.seattle.gov](https://data.seattle.gov/) for Seattle open government data
* [Data.cencus.gov](https://data.census.gov/) for U.S. Census data
* [Reddit Data Sets](https://www.reddit.com/r/datasets/)
* [Civic Data Sets for the Pacific Northwest](http://nwdata.org/)
* [An archive of datasets distributed with the R statistical language](https://vincentarelbundock.github.io/Rdatasets/)
* [Office for National Statistics (UK)](http://www.statistics.gov.uk/default.asp) a repository of detailed statistics about Great Britain and Northern Ireland
* [World Bank Data Catalog](http://data.worldbank.org/data-catalog)
* [CDC NCHS Data](https://data.cdc.gov/browse) - CDC's National Center for Health Statistics Data Access
* [Machine Learning Repository](http://archive.ics.uci.edu/ml/) - large variety of maintained data sets
* [For datasets used in CSE 163 Lessons](https://courses.cs.washington.edu/courses/cse163/21su/files/data/lecture-readings) (remember, these can't be the central part of your project)

Later in the course (if you are reading this close to the time Project Part 1 releases), we will explore geospatial data to create maps. If mapping sounds interesting to you, feel free to use any of the class datasets below! (Again, it's OK if you're not completely sure how to use the data yet; none of these datasets will be the focus of your project anyway!)

* [USA, from Lesson 6.2](https://gitlab.cs.washington.edu/cse163/23sp/course/-/blob/master/lessons/gz_2010_us_040_00_5m.json)
* [World Countries, from Section 6](https://gitlab.cs.washington.edu/cse163/23sp/course/-/blob/master/lessons/geo_data/ne_110m_admin_0_countries.shp)
* [Washington State, from HW5](https://gitlab.cs.washington.edu/cse163/23sp/course/-/blob/master/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp)

(libraries)=
### Libraries

You are free to use most any Python library you find that will be useful to you, especially the ones we have learned in class this quarter. If you know of a library you will use at this time (not required for the proposal) please mention it in your proposal. Below, we list some libraries you might want to look into for your project since students have found them useful in the past:

* Download from Web: [requests](https://requests.readthedocs.io/en/latest/)
* Scientific Computing: [SciPy](https://www.scipy.org/), [statsmodels](https://www.statsmodels.org/stable/index.html)
* Web Scraping: [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), [selenium](https://selenium-python.readthedocs.io/)
* Natural Language Processing: [spaCy](https://spacy.io/), [nltk](https://www.nltk.org/)
* Advanced/Interactive Visualizations: [altair](https://altair-viz.github.io/) or [plotly](https://plot.ly/python/)
* Domain-Specific Applications: [astropy](https://www.astropy.org/), [chempy](https://pypi.org/project/chempy/), [Bioconductor](https://www.bioconductor.org/), [cantera](https://cantera.org/)

You are also encouraged to take advantage of the libraries we learned this quarter to help you on this project (but they won't count as a new library for that challenge goal). In the list below, we include a list of all libraries we have (or will) discuss in depth in CSE 163.

* `pandas`
* `seaborn`
* `matplotlib`
* `scikit-learn`
* `geopandas` (geo-spatial data, covered in Week 6)
* `numpy` (image data, covered in Week 6)

(development-setup)=
### Development Setup

One of the challenges with developing your own project is that you need to make sure you have the computing resources you need. There are some excellent online options that let you experiment with your code in a notebook, but they usually have limits on what dataset sizes or libraries you can use.

You do not need to write code for the Project Proposal, but you and your group should explore your development setup earlier than later to make sure it is appropriate for your project. Make sure that you are able to run and edit Python scripts, not just Jupyter Notebooks.

For a local alternative to JupyterHub, we recommend using VSCode. You can follow along with our [software setup guide](/software-setup.md) for instructions on how to install and setup VSCode, along with Python and other dependencies on your local machine.

### Working Collaboratively

If you are working in a group, you will likely want to work collaboratively on your code, whether that be at the same time, or asynchronously at different times. Regardless, we recommend setting up a [Github](https://github.com/) repository for your project's code. Using Git allows you to seamlessly collaborate with others, while maintaining a reliable version history of your entire project, file by file! Other online alternatives are listed below. Information on how to set up a repository is also provided in the [software setup guide](/software-setup.md). We'll cover Git and repositories in class on October 16.

### Online Prototyping Tools

Note that the following tools are great for prototyping parts of your project, but you should be using your local Python installation to write runnable Python scripts that can handle data of any size.

* [Google Colaboratory](https://colab.research.google.com/) is an online Jupyter Notebook provided by Google. Think Google Docs but for Jupyter Notebooks. Great resource and easy to setup.
* [Jetbrains Datalore](https://datalore.jetbrains.com/) is a commercial service offering a powerful online collaboration environment for Jupyter Notebooks. The free tier should be enough for most data analysis and machine learning projects. Note that it is unable to write Python scripts so it may not be suitable for your final submission but can be useful for developing prototypes.

### Example: Too Easy Project

To give some context for why we have these challenge goals, we provide an example project proposal that is way too simple.

Consider a project proposal that wants to use the following CSV dataset about salaries.

| id  | age | salary | gender | location |
|-----|-----|--------|--------|----------|
| 1   | 42  | 110000 | F      | Seattle  |
| 2   | 23  | 56000  | M      | Kenmore  |
| 3   | 18  | 20000  | M      | SF       |
| ... | ... | ...    | ...    | ...      |

Suppose the project asked the following research questions:

1. What is the average age in the data?
2. How does salary relate to age?
3. What is the average salary by gender?

Is this a good project? In general, it can be a bit hard to say since you can't base it just on the number of research questions. Instead, you need to think about their depth and how much work would be necessary to answer them. This project ends up being very straight-forward to do in about 4 lines of code! One way to tell this project is too easy is it doesn't meet any of the challenge goals! As we mentioned before, to adequately meet the challenge goals you will probably be writing at least 120 lines of Python code! That might sound a lot, but that's already fewer lines than most of your homework assignments!

```python
df = pd.read_csv('data.csv')

# Question 1: What is the average age?
df['age'].mean()

# Question 2: How does salary relate to age?
sns.relplot(x='age', y='salary', data=df, kind='scatter')

# Question 3: What is the average salary by gender?
df.groupby('gender')['salary'].mean()
```

It's definitely okay to have some easier questions to build up a narrative in your report, but we are looking for you to challenge yourself on this project!

### Past Project Gallery

For some example reports and slides, please refer to our past [project gallery](https://courses.cs.washington.edu/courses/cse163/26au/archive/). Note: Some of these projects were before we added challenge goals and changed the spec so there might be some inconsistencies between their reports and what we are asking you to do.

## Grading

The project proposal will be graded for satisfactory completion of the written requirements and demonstrated effort. You will receive full credit for this part of the project as long as you have completed all the requirements and have demonstrated genuine effort in completing them.

## Submission

Your project proposal is due on Tuesday October 27 at 11:59pm, Seattle time. Submit your proposal as a **PDF file** on Gradescope. Remember that you **cannot submit any part of the project late** and you can not use the resubmission process for take-home assessments to make submissions after the due date.

Submit your Part 1 as a PDF file. Do not turn in a Word document or plain text. Only one group member needs to submit your proposal on [Gradescope](https://www.gradescope.com/courses/1401707) and should use Group Members functionality to add the appropriate partner if you have one. If you want to learn about how to add Group Members on Gradescope, please see instructions [here](https://www.gradescope.com/help#help-center-item-student-group-members). Group members that are not listed in Gradescope by the due date will be marked as not submitted.

<a class="btn btn-373" role="button" type="button" href="https://www.gradescope.com/courses/1401707">Submit Proposal</a>