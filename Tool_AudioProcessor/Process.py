import os
import shutil
import librosa
import soundfile

from .utils.Convert_Audio import Converter
from .utils.Slice_Audio import Slicer


class Audio_Processing:
    '''
    1. Convert the audio
    2. Slice off the silent parts
    '''
    def __init__(self,
        Media_Dir_Input: str,
        Media_Dir_Output: str,
        Media_Format_Output: str,
        RMS_Threshold: float = -40.,
        Audio_Length_Min: int = 5000,
        Silent_Interval_Min: int = 300,
        Hop_Size: int = 10,
        Silence_Kept_Max: int = 1000
    ):
        self.Media_Dir_Input = Media_Dir_Input
        self.Media_Dir_Output = Media_Dir_Output
        self.Media_Format_Output = Media_Format_Output
        self.RMS_Threshold = RMS_Threshold
        self.Audio_Length_Min = Audio_Length_Min
        self.Silent_Interval_Min = Silent_Interval_Min
        self.Hop_Size = Hop_Size
        self.Silence_Kept_Max = Silence_Kept_Max

    def Convert_Media(self):
        Converter(self.Media_Dir_Input, self.Media_Dir_Output, self.Media_Format_Output)
        #print('Format of audio files changed.')

    def Slice_Audio(self):
        '''
        Once the valid (sound) part reached min length since last slice and a silent part longer than min interval are detected, the audio will be sliced apart from the frame(s) with the lowest RMS value within the silent area.
        Long silence parts may be deleted.
        '''
        Audio_Dir = self.Media_Dir_Output
        for Audio_Name_Input in os.listdir(Audio_Dir):
            Audio_Path_Input = os.path.join(Audio_Dir, Audio_Name_Input)
            audio, sr = librosa.load(Audio_Path_Input, sr = None, mono = False)  # Load an audio file with librosa.
            slicer = Slicer(
                Sampling_Rate = sr,
                RMS_Threshold = self.RMS_Threshold,
                Audio_Length_Min = self.Audio_Length_Min,
                Silent_Interval_Min = self.Silent_Interval_Min,
                Hop_Size = self.Hop_Size,
                Silence_Kept_Max = self.Silence_Kept_Max
            )
            chunks, IsSlicingNeeded = slicer.slice(audio)
            if IsSlicingNeeded == True:
                for i, chunk in enumerate(chunks):
                    if len(chunk.shape) > 1:
                        chunk = chunk.T  # Swap axes if the audio is stereo.
                    Audio_Name_Output = Audio_Name_Input.rsplit('.', 1)[0] + f'_Sliced_{i}' + '.' + self.Media_Format_Output
                    soundfile.write(os.path.join(Audio_Dir, Audio_Name_Output), chunk, sr)  # Save sliced audio files.
                Audio_Dir_Backup = os.path.join(os.path.dirname(Audio_Dir), 'Backup')
                os.makedirs(name = Audio_Dir_Backup, exist_ok = True)
                try:
                    os.remove(path = os.path.join(Audio_Dir_Backup, Audio_Name_Input))
                except OSError:
                    pass
                else:
                    shutil.move(src = Audio_Path_Input, dst = Audio_Dir_Backup)
            else:
                pass