import pandas as pd
import os
import io
import re
import numpy as np


def change_encoding(SRT_Path):
    '''
    Change encoding from utf-8 to utf-8-sig to keep Umlaute (e.g. ä, ö, ü)
    '''
    with io.open(SRT_Path, 'r', encoding = 'utf-8') as f:
        text = f.read()
    # process Unicode text
    with io.open(SRT_Path, 'w', encoding = 'utf-8-sig') as f:
        f.write(text)


def convert_srt_to_csv(
    SRT_Path,
    CSV_Dir
):
    '''
    Extract start time, end-time and subtitle from the SRT_Path-files and store in a csv. In preparation for audio-splitting, a column id is generated from the filename with the addition of a unique number.
    '''
    #with open(SRT_Path, 'r', encoding  = 'locale') as h: # Use the current locale encoding
    with open(SRT_Path, 'r', encoding = 'utf-8-sig') as h:
        Sub = h.readlines()   #returns list of all lines

    Re_Pattern = r'[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}'
    Regex = re.compile(Re_Pattern)
    # Get start times
    Times = list(filter(Regex.search, Sub))
    Start_Times = [time.split(' ')[0] for time in Times]  #returns a list
    End_Times = [time.split('--> ')[1] for time in Times] #returns a list

    # Get lines
    Lines = [[]]
    for Sentence in Sub:
        if re.match(Re_Pattern, Sentence):
            Lines[-1].pop()
            Lines.append([])
        else:
            Lines[-1].append(Sentence)

    Lines = Lines[1:] # all text in lists

    Column_Names = ['id', 'start_times', 'end_times', 'transcript']
    DF_Text = pd.DataFrame(columns = Column_Names)

    DF_Text['start_times'] = Start_Times
    DF_Text['end_times'] = End_Times
    DF_Text['transcript'] = [" ".join(i).replace('\n', '') for i in Lines]
    DF_Text['end_times'] = DF_Text['end_times'].replace(r'\n', '', regex = True)

    DF_Text['id'] = np.arange(len(DF_Text))
    ID_Extension = os.path.basename(SRT_Path).replace('.srt', '_')
    '''
    ID_Extension = ID_Extension.replace(' ', '_')
    ID_Extension = ID_Extension.replace('-', '_')
    ID_Extension = ID_Extension.replace('.', '_')
    ID_Extension = ID_Extension.replace('__', '_')
    ID_Extension = ID_Extension.replace('___', '_')
    '''
    DF_Text['id'] = ID_Extension + DF_Text['id'].map(str)

    file_extension = ID_Extension[:-1]

    # converting the times to milliseconds
    def convert_to_ms(time):
        h_ms = int(time[:2])*3600000
        m_ms = int(time[3:5])*60000
        s_ms = int(time[6:8])*1000
        ms = int(time[9:12])
        ms_total = h_ms + m_ms + s_ms + ms
        return(ms_total)

    def conv_int(start):
        new_start = int(start)
        return(new_start)

    DF_Text['start_times'] = DF_Text['start_times'].apply(convert_to_ms)
    DF_Text['start_times'] = DF_Text['start_times'].apply(conv_int)

    DF_Text['end_times'] = DF_Text['end_times'].apply(convert_to_ms)

    DF_Text.to_csv(os.path.join(CSV_Dir, (file_extension + '.csv')), index = False, header = True, encoding = 'utf-8-sig')