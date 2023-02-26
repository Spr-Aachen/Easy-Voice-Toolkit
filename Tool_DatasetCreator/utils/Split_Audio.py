'''
Edited
'''
# Slice audio files based on start and end times in csv files

import os
import pandas as pd
from glob import glob
from pydub import AudioSegment


def Read_CSV(CSV_Path):
    try:
        Content = pd.read_csv(CSV_Path, engine = 'python')
    except Exception as e:
        print(e, type(e))
        if (isinstance(e, pd.errors.EmptyDataError)):
            pass
    else:
        return Content


def split_files(
    Dir_Input,
    Dir_Output
):
    for Item in glob(os.path.join(Dir_Input, '*.csv')):
        
        WAV_Item = Item.replace('.csv', '.wav')
        
        if os.path.exists(WAV_Item):
            Audio = AudioSegment.from_wav(WAV_Item)
            DF = Read_CSV(Item)

            def SplitAudio(DF):
                Audio_Split = Audio[DF['start_times']:DF['end_times']]
                Audio_Split.export(os.path.join(Dir_Output, (DF['id'] + '.wav')), format = 'wav')

            DF.apply(SplitAudio, axis = 1)
        
        else:
            next
