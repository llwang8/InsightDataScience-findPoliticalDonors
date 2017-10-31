#!/bin/python

"""
Insight DataScience Challenge:
Find Political Donors

Summary:

Given an input file that lists campaign contributions by individual donors and
distill it into two output files based on certain conditions:

medianvals_by_zip.txt: contains a calculated running median, total dollar amount
                       and total number of contributions by recipient and zip code
medianvals_by_date.txt: has the calculated median, total dollar amount and total
                        number of contributions by recipient and date.

"""

import re
import statistics
import datetime

# Return True if the date is in the correct format and valid date
def validate(datestr):
    if not datestr:
        return False
    if not re.match('[0-1][0-9][0-3][0-9][1-2][0-9]{3}', datestr):
        return False
    try:
        return datetime.datetime.strptime(datestr, '%m%d%Y')
    except ValueError:
        return False


def process_batch(lineList, by_zip, by_date, f_zip):
    for line in lineList:
        arr = line.strip().split('|')
        cmte_id = arr[0]
        zipcode = arr[10]
        tran_date = arr[13]
        tran_amt = int(arr[14])
        other_id = arr[15]

        if other_id or not cmte_id or not tran_amt: continue

        # get first five digits of zipcode
        if len(zipcode) >= 5:
            zipcode = zipcode[:5]

            # try to add more elements to respective dict.
            # If there is KeyError, initiate new key
            try:
                by_zip[cmte_id][zipcode].append(tran_amt)
            except KeyError:
                if cmte_id not in by_zip:
                    by_zip[cmte_id] = {}
                by_zip[cmte_id][zipcode] = [tran_amt]


            amt_list = by_zip[cmte_id][zipcode]
            L = '|'.join(map(str, [cmte_id, zipcode, round(statistics.median(amt_list)), len(amt_list), sum(amt_list)]))
            f_zip.writelines(L)
            f_zip.writelines('\n')

        # change to datetime format, check if successful
        tran_date = validate(tran_date)
        if not tran_date:
            continue
        else:
            # check if key exist before adding new info to dict
            try:
                by_date[cmte_id][tran_date].append(tran_amt)
            except KeyError:
                if cmte_id not in by_date:
                    by_date[cmte_id] = {}
                by_date[cmte_id][tran_date] = [tran_amt]

    return (by_zip, by_date)


def main():
    # open file object to read file from input folder
    f_read = open('./input/itcont.txt', 'r')
    # open file object to append for info by zip
    f_zip = open('./output/medianvals_by_zip.txt', 'a')

    # batch size
    # ===========
    n = 50
    batch = []
    by_zip = {}
    by_date = {}

    # save line in batch to be processed
    for line in f_read:
        batch.append(line)
        if len(batch) == n:
            by_zip, by_date = process_batch(batch, by_zip, by_date, f_zip)
            batch = []

    # last batch
    by_zip, by_date = process_batch(batch, by_zip, by_date, f_zip)

    # close file object for read
    f_read.close()
    # close file object for writing by zip info
    f_zip.close()

    # open file object to write sorted by date info
    f_date = open('./output/medianvals_by_date.txt', 'w')
    # sorted() return (key, value) tuple
    sorted_by_id_date = sorted(by_date.items(), key=lambda x: (x[0], x[1].keys()))
    for item in sorted_by_id_date:
        cid = item[0]
        for dt in item[1]:
            str_dt = '{:0>2}{:0>2}{}'.format(dt.month, dt.day, dt.year)
            amt_list = item[1][dt]
            L = '|'.join(map(str, [cid, str_dt, statistics.median(amt_list), len(amt_list), sum(amt_list)]))
            # write to file
            f_date.writelines(L)
            # add a new line
            f_date.writelines('\n')
    #file object to write by date info is closed
    f_date.close()


if __name__ == "__main__": main()


