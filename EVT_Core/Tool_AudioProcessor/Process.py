import os
import glob
import shutil
import librosa
import soundfile
from typing import Optional
from pathlib import Path
from tqdm import tqdm

from .utils.Convert_Media import Converter
from .utils.Denoise_Audio import Denoiser
from .utils.Slice_Audio import Slicer


class Audio_Processing:
    '''
    0. Convert the audio
    1. Denoise the audio
    2. Slice off the silent parts
    '''
    MediaExtensions = ['*.flac', '*.wav', '*.mp3', '*.aac', '*.m4a', '*.wma', '*.aiff', '*.au', '*.ogg', '*.mp4', '*.flv', '*.mkv', '*.avi']
    AudioExtensions = ['*.flac', '*.wav', '*.mp3', '*.aac', '*.m4a', '*.wma', '*.aiff', '*.au', '*.ogg']

    def __init__(self,
        Media_Dir_Input: str,
        Media_Dir_Output: str,
        Media_Format_Output: Optional[str] = 'wav',
        Channels: Optional[int] = None,
        SampleRate: Optional[int] = None,
        SampleWidth: Optional[int] = None,
        #Denoise_Audio: bool = True,
        Slice_Audio: bool = True,
        RMS_Threshold: float = -40.,
        Audio_Length_Min: int = 5000,
        Silent_Interval_Min: int = 300,
        Hop_Size: int = 10,
        Silence_Kept_Max: int = 1000
    ):
        self.Media_Dir_Input = Media_Dir_Input
        self.Media_Dir_Output = Media_Dir_Output
        self.Media_Format_Output = Media_Format_Output.lower() if Media_Format_Output is not None else None
        self.Denoise_Audio = False #self.Denoise_Audio = Denoise_Audio
        self.Slice_Audio = Slice_Audio
        self.RMS_Threshold = RMS_Threshold
        self.Audio_Length_Min = Audio_Length_Min
        self.Silent_Interval_Min = Silent_Interval_Min
        self.Hop_Size = Hop_Size
        self.Silence_Kept_Max = Silence_Kept_Max
        self.Channels = Channels
        self.SampleRate = SampleRate
        self.SampleWidth = SampleWidth

        os.makedirs(Media_Dir_Output, exist_ok = True)

    def GetPatterns(self,
        Directory: str,
        Extensions: list
    ):
        os.chdir(Directory)
        for Extension in Extensions:
            PatternList = glob.glob(Extension)
            if PatternList == []:
                pass
            else:
                break
        return PatternList

    def Process_Audio(self):
        '''
        Converter: Convert all the media format supported by ffmpeg to the referred audio format
        Denoiser: WIP
        Slicer: Once the valid (sound) part reached min length since last slice and a silent part longer than min interval are detected, the audio will be sliced apart from the frame(s) with the lowest RMS value within the silent area.
        Long silence parts may be deleted.
        '''
        print('Processing media...')
        for Media_Name_Input in tqdm(self.GetPatterns(self.Media_Dir_Input, self.MediaExtensions)):
            if self.Media_Format_Output is not None:
                if f'*.{self.Media_Format_Output}'.lower() not in self.AudioExtensions:
                    raise Exception(f"Format '{self.Media_Format_Output}' is currently not supported!")
            else:
                self.Media_Format_Output = Path(Media_Name_Input).suffix.strip('.')
            Audio_Name_Input, Audio_Path_Input = Converter(
                Media_Name_Input,
                self.Media_Dir_Output,
                self.Media_Format_Output,
                self.Channels,
                self.SampleRate,
                self.SampleWidth
            )
            AudioData, SampleRate = librosa.load(Audio_Path_Input, sr = None, mono = False)  # Load an audio file with librosa.
            WriteParamsList = [()]
            if self.Denoise_Audio:
                WriteParamsList.clear()
                AudioData = Denoiser(AudioData)
                Audio_Name_Output = Audio_Name_Input.rsplit('.', 1)[0] + '_Denoised_' + '.' + self.Media_Format_Output
                Audio_Path_Output = os.path.normpath(os.path.join(self.Media_Dir_Output, Audio_Name_Output))
                WriteParamsList.append((Audio_Path_Output, AudioData, SampleRate))
            if self.Slice_Audio:
                WriteParamsList.clear()
                slicer = Slicer(
                    Sampling_Rate = SampleRate,
                    RMS_Threshold = self.RMS_Threshold,
                    Audio_Length_Min = self.Audio_Length_Min,
                    Silent_Interval_Min = self.Silent_Interval_Min,
                    Hop_Size = self.Hop_Size,
                    Silence_Kept_Max = self.Silence_Kept_Max
                )
                chunks, IsSlicingNeeded = slicer.slice(AudioData)
                if IsSlicingNeeded == True:
                    for i, chunk in enumerate(chunks):
                        if len(chunk.shape) > 1:
                            chunk = chunk.T  # Swap axes if the audio is stereo.
                        Audio_Name_Output = Audio_Name_Input.rsplit('.', 1)[0] + f'_Sliced_{i}' + '.' + self.Media_Format_Output
                        Audio_Path_Output = os.path.normpath(os.path.join(self.Media_Dir_Output, Audio_Name_Output))
                        WriteParamsList.append((Audio_Path_Output, chunk, SampleRate))
                    try:
                        os.remove(Audio_Path_Input)
                    except OSError:
                        pass
                    '''
                    Audio_Dir_Backup = os.path.normpath(os.path.join(os.path.dirname(self.Media_Dir_Output), 'Backup'))
                    os.makedirs(name = Audio_Dir_Backup, exist_ok = True)
                    try:
                        os.remove(path = os.path.normpath(os.path.join(Audio_Dir_Backup, Audio_Name_Input)))
                    except OSError:
                        pass
                    finally:
                        Audio_Path_Output = os.path.normpath(os.path.join(Audio_Dir_Backup, Audio_Name_Output))
                    '''
                else:
                    pass
            for WriteParams in WriteParamsList:
                soundfile.write(*WriteParams)
        print('Finished processing.')