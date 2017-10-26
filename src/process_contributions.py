#!/bin/python

import re
import statistics
import datetime

# Return True if the date is in the correct format and valid date
def validate(datestr):
    if !datestr:
        return False
    if !re.match('[0-1][0-9][0-3][0-9][1-2][0-9]{3}', datestr):
        return False
    try:
        return datetime.datetime.strptime(datestr, '%m%d%Y')
    except ValueError:
        return False

def process_batch(lineList):
    for line in lineList:
        arr = line.strip().split('|')
        cmte_id = arr[0]
        zipcode = arr[10]
        tran_date = arr[13]
        tran_amt = int(arr[14])
        other_id = arr[15]

        continue if other_id or not cmte_id or not tran_amt

        if len(zipcode) >= 5:
            zipcode = zipcode[:5]
            if zipcode in by_zip[cmte_id]:
                by_zip[cmte_id][zipcode].append(tran_amt)
            else:
                by_zip[cmte_id][zipcode] = []
            temp = by_zip[cmte_id][zipcode]
            f_zip.writelines('|'.join([cmte_id, zipcode, round(statistics.median(amt_list)), len(amt_list), sum(amt_list)]))

        # change to datetime format, check if successful

        tran_date = validate(tran_date)
        if !tran_date:
            continue
        else:
            if tran_date in by_date[cmte_id]:
                by_date[cmte_id][tran_date].append(tran_amt)
            else:
                by_date[cmte_id][tran_date] = []

        sorted_by_id_date = sorted(by_date.items() key=lambda x: x[0], x[1].keys()) # need to sort by id, date
        for cid in sorted_by_id_date:
            for dt in sorted_by_id_date[cid]:
                str_dt = '{:0>2}{:0>2}{}'.format(dt.month, dt.day, dt.year)
                amt_list = sorted_by_id_date[cid][dt]
                L = '|'.join([id, str_dt, statistics.median(amt_list), len(amt_list), sum(amt_list)])
                f_zip.writelines(L)


with open(r'./input/itcont.txt', 'r') as f_read:
    f_zip = open('./output/medianvals_by_zip.txt', 'a')
    f_date = open('./output/medianvals_by_date.txt', 'w+')

    n = 10
    batch = []
    by_zip = {}
    by_date = {}

    for line in f_read:
        batch.append(line)
        if len(batch) == n:
            process_batch(batch)
            batch = []

    f_zip.close()
    f_date.close()


