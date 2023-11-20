'''
Added
'''

import os
from typing import Optional
from pydub import AudioSegment


def Converter(
    Media_Name_Input: str,
    Media_Dir_Output: str,
    Media_Format_New: str = 'wav',
    Channels: Optional[int] = None, # choices = [1, 2, None]
    SampleRate: Optional[int] = None, # choices = [44100, 48000, 96000, 192000, None]
    SampleWidth: Optional[int] = None # choices = [8, 16, 24, 32, None]
):
    try:
        Media_Name_Output = os.path.splitext(os.path.basename(Media_Name_Input))[0] + '.' + Media_Format_New
        Media_Path_Output = os.path.join(Media_Dir_Output, Media_Name_Output)
        AudioFile = AudioSegment.from_file(Media_Name_Input)
        AudioFile.set_channels(Channels) if Channels else None
        AudioFile.set_frame_rate(SampleRate) if SampleRate else None
        AudioFile.set_sample_width(SampleWidth) if SampleWidth else None
        AudioFile.export(
            out_f = Media_Path_Output,
            format = Media_Format_New
        )
    except:
        print(f"Convertion of file {Media_Name_Input} failed!")
    else:
        return Media_Name_Output, Media_Path_Output