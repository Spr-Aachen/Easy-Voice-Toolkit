'''
Edited
'''
# Joins all seperate csv-files

import os
import pandas as pd
from glob import glob


def Read_CSV(CSV_Path):
    try:
        Content = pd.read_csv(CSV_Path, engine = 'python')
    except Exception as e:
        print(e, type(e))
        if (isinstance(e, pd.errors.EmptyDataError)):
            pass
    else:
        return Content


def merge_csv(
    CSV_Dir,
    CSV_Dir_Merged
):
    print('Merging csv-files with transcriptions')
    CSV_Combined = pd.DataFrame()
    for Entry in glob(os.path.join(CSV_Dir, '*.csv')):
        DF = Read_CSV(Entry)
        CSV_Combined = pd.concat([CSV_Combined, DF], ignore_index = True)

    CSV_Combined.to_csv(os.path.join(CSV_Dir_Merged, 'Full_Transcript.csv'), header = True, index = False, encoding = 'utf-8-sig')
    print('All csv-files merged')
