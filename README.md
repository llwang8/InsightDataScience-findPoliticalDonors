## Insight DataScience - Data Engineering Challenge

# Find Political Donors


## Challenge Summary

For this challenge, engineer is asked to take an input file that lists campaign contributions by individual donors and distill it into two output files:

medianvals_by_zip.txt: contains a calculated running median, total dollar amount and total number of contributions by recipient and zip code

medianvals_by_date.txt: has the calculated median, total dollar amount and total number of contributions by recipient and date.

Engineer's role on the project is to work on the data pipeline that will hand off the information to the front-end. As the backend data engineer, no need to display the data or work on the dashboard but to provide the information.


## Approach

The following fields are relevant to this project:

CMTE_ID: identifies the flier, which  is the recipient of this contribution

ZIP_CODE: zip code of the contributor (only first five digits/characters needed)

TRANSACTION_DT: date of the transaction

TRANSACTION_AMT: amount of the transaction

OTHER_ID: a field that denotes whether contribution came from a person or an entity

Initiate 2 dictionaries by_date, by_zip to hold data.  Open file object to read from input/itcont.txt.  Save each line to a batch list until batch size is n.

With each batch (size n) and the last batch, first split each line by "|" to generate
an list.  Extract relevant data from the list with the right indexes.

If any field of other_id, cmte_id, tran_amt is/are empty, ignore this line.  First get the first 5 digits of zipcode as the new zip value.  Then append tran_amt to value list of the 2 tier keys of cmte_id and zip.  If keys don't exist, creat keys then add current trans_amt as the first element to this value list.

Write to _by_zip file with streamed so far statistics meadian for each cmte_id, zipcode, count and summary of tran_amt list for the specific cmte_id and zip keys.  Add a new line after writing each line so as current line not to concatenate with the next line.

Update by_date dict similarly. First validate tran_date first.  Make sure it is not empty. Second, month, day and year all have allowable digits. Last it can be transformed to valid datetime object.

Use cmte_id and valid date as 2-tier dict keys to store relevent tran_amt to its value list.  If keys don't exist, create keys first before adding the first elements.

After all batches are processed, sort by_date dict alphabetical by recipient and then chronologically by date.  Then print to _by_date file statistics meadian, count and summary of list containing all tran_amt for that specific cmte_id and date keys.  Add a new line after writing each line so as current line not to concatenate with next line.

Close file object for writing _by_date file.


## Run Instruction

The default batch size is set as 50.  Change it if needed before running the program.

At command line at the directory of root type:
./run.sh



### Built with:

Implemented with Python and libraries Time and Statistics.


### Resources

Original challenge from Insight DataScience
- [Find Political Donors](https://github.com/InsightDataScience/find-political-donors)



