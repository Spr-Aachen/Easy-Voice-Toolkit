import os
import pandas as pd


def Transcript_Writer(CSV_Path, Encoder, IsSpeakerMultiple, Text_Path):
    DF_Text = pd.read_csv(CSV_Path)

    os.makedirs(os.path.dirname(Text_Path), exist_ok = True)

    if Encoder == 'VITS':
        DF_Text[['wav_filename', 'transcript']].to_csv(Text_Path, header = None, index = None, mode = 'w', sep = '|')
        if IsSpeakerMultiple:
            #Text_Path_New = Text_Path[:(len(Text_Path) - len('.txt'))] + '_re.txt'
            Text_Path_New = Text_Path.rsplit('.', 1)[0] + '_re.txt'
            File_Old = open(Text_Path, encoding = 'utf-8')
            File_New = open(Text_Path_New, mode = 'w', encoding = 'utf-8')
            while True:
                line = File_Old.readline()
                if line != None:
                    Path = line.split('|')[0]
                    text = line.split("|")[1]
                    line = line.split('/')[-1]
                    speakerId = line.split('_')[0]
                    Path.split('/')[1]
                    line = Path + "|" + speakerId + "|" + text
                    File_New.write(line)
                else:
                    break
            File_Old.close()
            File_New.close()
            os.remove(Text_Path)
            os.rename(Text_Path_New, Text_Path)
    
    else:
        raise Exception(f"{Encoder} is not supported!")