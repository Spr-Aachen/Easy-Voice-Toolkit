'''
Edited
'''
# Create csv with filepath and -size in preparation for final DS training-csv

import pandas as pd
import os
from glob import glob
import wave
import contextlib


def create_DS_csv(
    WAV_Dir_Extract,
    CSV_Dir
):
    #this function holds the code to extract the filepath and filesize of all audio in the respective directory
    print(f'Extracting filepath and -size for every .wav file in {WAV_Dir_Extract}')
    Data = pd.DataFrame(columns = ['wav_filename', 'wav_filesize', 'duration'])
    DF = pd.DataFrame(columns = ['wav_filename', 'wav_filesize', 'duration'])

    for entry in glob(os.path.join(WAV_Dir_Extract, '*.wav')):
        filepath = os.path.abspath(entry)
        filesize = os.path.getsize(entry)
        with contextlib.closing(wave.open(entry, 'rb')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
        DF['wav_filename'] = [filepath]
        DF['wav_filesize'] = [filesize]
        DF['duration'] = [duration]
        Data = pd.concat([Data, DF], ignore_index = True)

    Data.to_csv(os.path.join(CSV_Dir, 'Filepath_Filesize.csv'), header = True, index = False, encoding = 'utf-8-sig')
