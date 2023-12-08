'''
Edited
'''
# Slice audio files based on start and end times in csv files

import os
import pandas as pd
from glob import glob
from pydub import AudioSegment
from concurrent.futures import ThreadPoolExecutor


def ReadCSV(CSV_Path):
    try:
        Content = pd.read_csv(CSV_Path, engine = 'python')
    except Exception as e:
        print(e, type(e))
        if (isinstance(e, pd.errors.EmptyDataError)):
            pass
    else:
        return Content


def SplitFile(
    Item,
    Dir_Output
):
    DF = ReadCSV(Item)

    def SplitAudio(DF):
        Audio = AudioSegment.from_wav(Item.replace('.csv', '.wav'))
        Audio_Split = Audio[DF['start_times']:DF['end_times']]
        Audio_Split.export(os.path.join(Dir_Output, (DF['id'] + '.wav')), format = 'wav')

    DF.apply(SplitAudio, axis = 1)


def split_files(
    Dir_Input,
    Dir_Output
):
    ParamsList = []
    for Item in glob(os.path.join(Dir_Input, '*.csv')):
        if os.path.exists(Item.replace('.csv', '.wav')):
            ParamsList.append((Item, Dir_Output))
        else:
            next

    with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
        Executor.map(
            SplitFile,
            *zip(*ParamsList)
        )