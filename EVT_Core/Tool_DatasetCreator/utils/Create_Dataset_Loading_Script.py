import os
import pandas as pd
import random
import re
from pathlib import Path


def Transcript_Writer(
        CSV_Path,
        AuxiliaryData_Path,
        TrainRatio,
        ModelType,
        Text_Path_Training,
        Text_Path_Validation
    ):
    '''
    CSV to TXT
    '''
    CSV_Path_DataSet = os.path.join(os.path.dirname(CSV_Path), "Dataset.csv")
    pd.read_csv(CSV_Path)[['wav_filename', 'transcript']].to_csv(
        path_or_buf = CSV_Path_DataSet,
        header = None,
        index = None,
        mode = 'w',
        sep = '|'
    )
    #shutil.copy(CSV_Path_DataSet, CSV_Save_Path) if CSV_Save_Path is not None else None
    with open(file = CSV_Path_DataSet, mode = 'r', encoding = 'utf-8') as File_Old:
        Lines = File_Old.readlines()

    Languages = []
    for Line in Lines:
        Line_Text = Line.split('|', maxsplit = 1)[1]
        Language = re.split(r'[\[\]]', Line_Text)[1]
        Languages.append(Language) if Language not in Languages else None

    if AuxiliaryData_Path is not None:
        print("Writing AuxiliaryData paths...")
        with open(file = AuxiliaryData_Path, mode = 'r', encoding = 'utf-8') as AuxiliaryData:
            AuxiliaryDataLines_Old = AuxiliaryData.readlines()
        AuxiliaryDataLines_New = []
        for Line_Old in AuxiliaryDataLines_Old:
            Line_Old_Path = Line_Old.split('|', maxsplit = 1)[0]
            Line_New_Path = Path(AuxiliaryData_Path).parent.joinpath(Line_Old_Path).__str__()
            '''
            if not Path(Line_New_Path).exists():
                raise Exception('Please check if the relative paths inside AuxiliaryData.txt are correct!')
            '''
            Line_Old_Text = Line_Old.split("|", maxsplit = 1)[1]
            Language = re.split(r'[\[\]]', Line_Old_Text)[1]
            if Language not in Languages:
                continue
            Line_New = Line_New_Path + "|" + Line_Old_Text
            AuxiliaryDataLines_New.append(Line_New)
        ReplicateTimes = len(AuxiliaryDataLines_New) // len(Lines) if len(AuxiliaryDataLines_New) > len(Lines) else 1
        Lines = Lines * ReplicateTimes + AuxiliaryDataLines_New

    random.shuffle(Lines)
    TrainSize = int(len(Lines) * TrainRatio)
    Lines_Train = Lines[:TrainSize]
    Lines_Val = Lines[TrainSize:]

    if ModelType == 'VITS':
        print("Writing VITS DataSet paths...")
        def WriteDataLines(Text_Path, Lines):
            Speakers = []
            os.makedirs(os.path.dirname(Text_Path), exist_ok = True)
            for Index, Line in enumerate(Lines):
                Line_Old = Line
                Line_Old_Path = Path(Line_Old.split('|', maxsplit = 1)[0]).as_posix()
                Speaker = re.split(r'[\[\]]', re.split(r'[/\\\\]', Line_Old_Path)[-1])[1]
                Speakers.append(Speaker) if Speaker not in Speakers else None
                SpeakerID = Speakers.index(Speaker)
                Line_Old_Text = Line_Old.split("|", maxsplit = 1)[1]
                Line_New = Line_Old_Path + f"|{SpeakerID}|" + Line_Old_Text
                Lines[Index] = Line.replace(Line_Old, Line_New)
            with open(file = Text_Path, mode = 'w', encoding = 'utf-8') as File_New:
                File_New.writelines(Lines)
        WriteDataLines(Text_Path_Training, Lines_Train)
        WriteDataLines(Text_Path_Validation, Lines_Val)

    else:
        raise Exception(f"{ModelType} is not supported!")