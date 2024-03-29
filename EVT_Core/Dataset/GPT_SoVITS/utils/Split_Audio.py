import os
import pandas as pd
from glob import glob
from pathlib import Path
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
    CSV_Path,
    Item,
    Dir_Output
):
    DF = ReadCSV(CSV_Path)

    def SplitAudio(DF):
        Audio = AudioSegment.from_wav(Item)
        Audio_Split = Audio[DF['start_times']:DF['end_times']]
        Audio_Split.export(os.path.join(Dir_Output, (DF['id'] + '.wav')), format = 'wav')

    DF.apply(SplitAudio, axis = 1)


def split_files(
    CSV_Dir_Input,
    WAV_Paths_Input,
    Dir_WAVOutput
):
    '''
    Slice audio files based on start and end times in csv files
    '''
    ParamsList = []
    CSV_Paths_Input = [CSV_Path_Input.as_posix() for CSV_Path_Input in Path(CSV_Dir_Input).glob('*.csv')]
    for WAV_Path_Input in WAV_Paths_Input:
        CSV_Path = Path(CSV_Dir_Input).joinpath(Path(WAV_Path_Input).stem).as_posix() + '.csv'
        if Path(WAV_Path_Input).exists() and CSV_Path in CSV_Paths_Input:
            ParamsList.append((CSV_Path, WAV_Path_Input, Dir_WAVOutput))
        else:
            next

    with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
        Executor.map(
            SplitFile,
            *zip(*ParamsList)
        )