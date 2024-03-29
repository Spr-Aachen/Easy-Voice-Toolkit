import os
import pandas as pd
#from unidecode import unidecode


def Read_CSV(CSV_Path):
    try:
        return pd.read_csv(CSV_Path, engine = 'python')
    except Exception as e:
        print(e, type(e))
        if (isinstance(e, pd.errors.EmptyDataError)):
            pass


def clean_unwanted_characters(CSV_Dir_Final, CSV_Name_Final):
    '''
    Remove unwanted characters. After cleaning the transcripts, the text is extracted and saved in a txt file which can be used for training the language model.
    '''
    DF_DS_Final = Read_CSV(os.path.join(CSV_Dir_Final, CSV_Name_Final))

    # some srt files contain font codes which are removed hereby
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('<font color=#91FFFF>', '', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('<font color=#72FD59>', '', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('<font color=#E8E858>', '', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('<font color=#FFFFFF>', '', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('</font>', '', regex=True)

    '''
    # Characters to be removed
    punct = str(['.!"#$%&\'()*+,-/:;<–=>?@[\\]^_°`{}~ ̀ ̆ ̃ ́'])
    transtab = str.maketrans(dict.fromkeys(punct, ' '))
    '''
    DF_DS_Final = DF_DS_Final.dropna()
    '''
    DF_DS_Final['transcript'] = '£'.join(DF_DS_Final['transcript'].tolist()).translate(transtab).split('£')
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].str.lower()
    '''
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('\s+', '', regex = True) # Replace line feeds without spaces
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].str.strip()
    '''
    # Further remove unwanted characters
    remove_char = '鄚氏鐷顤鐰鄣酹輐霵鐼羦鄜酲酺酺礫飉舣δφℳˁｶᛠᛏˁːɣ\ʿʻʾŋ\ʹªьʺъˀˇʼʔˊˈ!"#$%&\()*+,-./:;<=>?@[]^_`{|}~'

    table_2 = str.maketrans('','', remove_char)
    DF_DS_Final['transcript'] = [w.translate(table_2) for w in DF_DS_Final['transcript']]

    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('ä','ae', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('ö','oe', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('ü','ue', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('α','alpha', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('ə','e', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('ё','e', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('γ','gamma', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('µ','mikro', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('π','pi', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('β','beta', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('ζ','zeta', regex=True)
    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].replace('ß','ss', regex=True)

    # to get rid of final unwanted characters transform characters to strictly unicode
    def to_ASCII(text):
        text = unidecode(text)
        return text

    DF_DS_Final['transcript'] = DF_DS_Final['transcript'].apply(to_ASCII)
    '''

    # Save cleaned files
    CSV_Name_Final_Cleaned = CSV_Name_Final[:-4]
    CSV_Path_Final_Cleaned = os.path.join(CSV_Dir_Final, (CSV_Name_Final_Cleaned + '_cleaned.csv'))
    DF_DS_Final.to_csv(CSV_Path_Final_Cleaned, header = True, index = False, encoding = 'utf-8') #DF_DS_Final.to_csv('./merged_csv/' + final_path + '_char_removed.csv', header = True, index = False, encoding = 'utf-8-sig')

    print('Length of ds_final: {}'.format(len(DF_DS_Final)))
    print('Final Files cleaned of unwanted characters')

    return CSV_Path_Final_Cleaned