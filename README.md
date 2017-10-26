## Insight DataScience - Data Engineering Challenge

# Find Political Donors


## Challenge Summary


For this challenge, we're asking you to take an input file that lists campaign contributions by individual donors and distill it into two output files:

medianvals_by_zip.txt: contains a calculated running median, total dollar amount and total number of contributions by recipient and zip code

medianvals_by_date.txt: has the calculated median, total dollar amount and total number of contributions by recipient and date.

As part of the team working on the project, another developer has been placed in charge of building the graphical user interface, which consists of two dashboards. The first would show the zip codes that are particularly generous to a recipient over time while the second would display the days that were lucrative for each recipient.

Your role on the project is to work on the data pipeline that will hand off the information to the front-end. As the backend data engineer, you do not need to display the data or work on the dashboard but you do need to provide the information.


## Approach

CMTE_ID: identifies the flier, which for our purposes is the recipient of this contribution
ZIP_CODE: zip code of the contributor (we only want the first five digits/characters)
TRANSACTION_DT: date of the transaction
TRANSACTION_AMT: amount of the transaction
OTHER_ID: a field that denotes whether contribution came from a person or an entity

## Dependencies


## Run Instruction


### Built with:

Implemented with Python and libraries Time and Statistics.


### Resources

Original inspirations from Udacity Course
- [Intro to Python](https://www.udacity.com/course/introduction-to-python--ud1110)