'''
Edited
'''
# Matches the transcripts to the available audio files.

import os
import re
import pandas as pd


def Read_CSV(CSV_Path):
    try:
        Content = pd.read_csv(CSV_Path, engine = 'python')
    except Exception as e:
        print(e, type(e))
        if (isinstance(e, pd.errors.EmptyDataError)):
            pass
    else:
        return Content


def merge_transcripts_and_wav_files(
    CSV_Dir_Merged,
    CSV_Dir_Final,
    CSV_Name_Final,
    #Time_Limitation
):
    DF_Final = pd.DataFrame()

    CSV_Path_Transcript = os.path.join(CSV_Dir_Merged, 'Full_Transcript.csv')
    CSV_Path_Filesize = os.path.join(CSV_Dir_Merged, 'Filepath_Filesize.csv')

    DF_Transcripts = Read_CSV(CSV_Path_Transcript)
    DF_Filesize = Read_CSV(CSV_Path_Filesize)

    # by splitting the path at / and then choosing -1, the filename can be extracted
    def remove_path(path):
        path = re.split(r'[/\\\\]', path)[-1] #path = path.split('/')[-1]
        return path

    DF_Filesize['id'] = DF_Filesize['wav_filename'].apply(remove_path)

    # filter out duration of less than specified time (seconds)
    def convert(duration):
        time = float(duration)
        return time

    DF_Filesize['duration'] = DF_Filesize['duration'].apply(convert)
    #DF_Filesize = DF_Filesize[DF_Filesize['duration'] < Time_Limitation]

    # drop unnecessary columns
    DF_Transcripts.drop(['start_times', 'end_times'], axis = 1, inplace = True)
    #DF_Filesize.drop(['duration'], axis = 1, inplace = True)

    DF_Filesize['id'] = DF_Filesize['id'].replace('.wav', '', regex = True)

    # merge on column id
    DF_Final = pd.merge(DF_Transcripts, DF_Filesize, on = 'id')
    DF_Final.drop(['id'], axis = 1, inplace = True)

    # rearrange columns
    DF_Final = DF_Final[['wav_filename', 'duration', 'transcript']] #DF_Final = DF_Final[['wav_filename', 'wav_filesize', 'transcript']]

    DF_Final.to_csv(os.path.join(CSV_Dir_Final, CSV_Name_Final), header=True, index=False, encoding='utf-8-sig')