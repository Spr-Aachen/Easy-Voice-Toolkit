import os
import pandas as pd
import re


def Transcript_Writer(CSV_Path, AutoEncoder, IsSpeakerMultiple, Text_Path):
    DF_Text = pd.read_csv(CSV_Path)

    os.makedirs(os.path.dirname(Text_Path), exist_ok = True)

    if AutoEncoder == 'VITS':
        DF_Text[['wav_filename', 'transcript']].to_csv(
            path_or_buf = Text_Path,
            header = None,
            index = None,
            mode = 'w',
            sep = '|'
        )
        if IsSpeakerMultiple:
            with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as File_Old:
                Lines = File_Old.readlines()
            for Sequence, Line in enumerate(Lines):
                Line_Old = Line
                Line_Old_Path = Line_Old.split('|')[0]
                SpeakerId = re.split(r'[\[\]]', re.split(r'[/\\\\]', Line_Old_Path)[-1])[1]
                Line_Old_Text = Line_Old.split("|")[1]
                Line_New = Line_Old_Path + f"|{SpeakerId}|" + Line_Old_Text
                Lines[Sequence] = Line.replace(Line_Old, Line_New)
            with open(file = Text_Path, mode = 'w', encoding = 'utf-8') as File_New:
                File_New.writelines(Lines)

    else:
        raise Exception(f"{AutoEncoder} is not supported!")