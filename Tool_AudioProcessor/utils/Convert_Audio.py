'''
Added
'''

import os
import glob
from pydub import AudioSegment


def Converter(
    Media_Dir_Input: str,
    Meida_Dir_Output: str,
    Media_Format_New: str = 'wav'
):
    Media_Format_New = Media_Format_New.lower()

    os.makedirs(Meida_Dir_Output, exist_ok = True)

    '''
    for Media_Name_Input in os.listdir(Media_Dir_Input):
        try:
            Media_Path = os.path.join(Media_Dir_Input, Media_Name_Input)

            if Media_Name_Input.endswith('.mp3') and Media_Format_New != 'mp3':
                Media = AudioSegment.from_mp3(Media_Path)

            if Media_Name_Input.endswith('.wav') and Media_Format_New != 'wav':
                Media = AudioSegment.from_wav(Media_Path)

            if Media_Name_Input.endswith('.ogg') and Media_Format_New != 'ogg':
                Media = AudioSegment.from_ogg(Media_Path)

            if Media_Name_Input.endswith('.mp4') and Media_Format_New != 'mp4':
                Media = AudioSegment.from_mp4(Media_Path)

            if Media_Name_Input.endswith('.flv') and Media_Format_New != 'flv':
                Media = AudioSegment.from_flv(Media_Path)

            Media_Name_Output = Media_Name_Input.rsplit('.', 1)[0] + '.' + Media_Format_New
            Media.export(os.path.join(Meida_Dir_Output, Media_Name_Output), format = Media_Format_New)
        
        except:
            print(f"Convertion of file {Media_Name_Input} failed!")
    '''
    
    ExtensionList = ('*.mp3', '*.wav', '*.ogg', '*.mp4', '*.flv')
    
    os.chdir(Media_Dir_Input)
    
    for Extension in ExtensionList:
        if Extension.rsplit('.', 1)[-1] == Media_Format_New:
            pass
        
        else:
            for Media_Name_Input in glob.glob(Extension):
                try:
                    Media_Name_Output = os.path.splitext(os.path.basename(Media_Name_Input))[0] + '.' + Media_Format_New
                    AudioSegment.from_file(Media_Name_Input).export(os.path.join(Meida_Dir_Output, Media_Name_Output), format = Media_Format_New)

                except:
                    print(f"Convertion of file {Media_Name_Input} failed!")
    
    #print("Conversion done!")