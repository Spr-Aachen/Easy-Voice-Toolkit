import os
import pandas as pd
import random
import re


def Transcript_Writer(
        CSV_Path,
        AutoEncoder,
        TrainRatio,
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
    with open(file = CSV_Path_DataSet, mode = 'r', encoding = 'utf-8') as File_Old:
        Lines = File_Old.readlines()
    random.shuffle(Lines)
    TrainSize = int(len(Lines) * TrainRatio)
    Lines_Train = Lines[:TrainSize]
    Lines_Val = Lines[TrainSize:]

    if AutoEncoder == 'VITS':
        def WriteDataLines(Text_Path, Lines):
            Speakers = []
            os.makedirs(os.path.dirname(Text_Path), exist_ok = True)
            for Sequence, Line in enumerate(Lines):
                Line_Old = Line
                Line_Old_Path = Line_Old.split('|')[0]
                Speaker = re.split(r'[\[\]]', re.split(r'[/\\\\]', Line_Old_Path)[-1])[1]
                Speakers.append(Speaker) if Speaker not in Speakers else None
                SpeakerID = Speakers.index(Speaker)
                Line_Old_Text = Line_Old.split("|")[1]
                Line_New = Line_Old_Path + f"|{SpeakerID}|" + Line_Old_Text
                Lines[Sequence] = Line.replace(Line_Old, Line_New)
            with open(file = Text_Path, mode = 'w', encoding = 'utf-8') as File_New:
                File_New.writelines(Lines)
        WriteDataLines(Text_Path_Training, Lines_Train)
        WriteDataLines(Text_Path_Validation, Lines_Val)

    else:
        raise Exception(f"{AutoEncoder} is not supported!")