import os
import glob
import soundfile
from typing import Union, Optional
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from .utils.Load_Media import Loader
from .utils.Denoise_Audio import Denoiser
from .utils.Slice_Audio import Slicer


class Audio_Processing:
    '''
    0. Load the audio
    1. Denoise the audio
    2. Slice off the silent parts
    '''
    MediaExtensions = ['*.flac', '*.wav', '*.mp3', '*.aac', '*.m4a', '*.wma', '*.aiff', '*.au', '*.ogg', '*.mp4', '*.flv', '*.mkv', '*.avi']
    AudioExtensions = ['*.flac', '*.wav', '*.mp3', '*.aac', '*.m4a', '*.wma', '*.aiff', '*.au', '*.ogg']

    SubtypeDict = {
        '8':          'PCM_8',
        '16':         'PCM_16',
        '24':         'PCM_24',
        '32':         'PCM_32',
        '32 (Float)': 'FLOAT'
    }

    def __init__(self,
        Media_Dir_Input: str,
        Media_Format_Output: Optional[str] = 'wav',
        SampleRate: Optional[Union[int, str]] = None,
        SampleWidth: Optional[Union[int, str]] = None,
        ToMono: bool = False,
        Denoise_Audio: bool = True,
        Denoise_Model_Path: str = "",
        Denoise_Target: str = '',
        Slice_Audio: bool = True,
        RMS_Threshold: float = -40.,
        Audio_Length_Min: int = 5000,
        Silent_Interval_Min: int = 300,
        Hop_Size: int = 10,
        Silence_Kept_Max: int = 1000,
        Media_Root_Output: str = "./",
        Media_DirName_Output: str = "",
    ):
        self.Media_Dir_Input = Media_Dir_Input
        self.Media_Format_Output = Media_Format_Output.lower() if Media_Format_Output is not None else None
        self.Denoise_Audio = Denoise_Audio
        self.DenoiseModel_Path = Denoise_Model_Path
        self.DenoiseTarget = Denoise_Target.replace('人声', 'vocals').replace('背景声', 'instrument')
        self.Slice_Audio = Slice_Audio
        self.RMS_Threshold = RMS_Threshold
        self.Audio_Length_Min = Audio_Length_Min
        self.Silent_Interval_Min = Silent_Interval_Min
        self.Hop_Size = Hop_Size
        self.Silence_Kept_Max = Silence_Kept_Max
        self.SampleRate = eval(SampleRate) if SampleRate is not None else None
        self.SampleWidth = str(SampleWidth) if SampleWidth is not None else None
        self.ToMono = ToMono
        self.Media_Dir_Output = Path(Media_Root_Output).joinpath(Media_DirName_Output).as_posix()

        os.makedirs(self.Media_Dir_Output, exist_ok = True)

    def GetPatterns(self,
        Directory: str,
        Extensions: list
    ):
        PatternList = []

        for Extension in Extensions:
            PatternList.extend(glob.glob(Path(Directory).joinpath(Extension).as_posix()))

        return PatternList

    def ProcessMedia(self,
        Media_Name_Input: str
    ):
        '''
        Loader: Load audio from media files which supported by ffmpeg.
        Denoiser: WIP
        Slicer: Once the valid (sound) part reached min length since last slice and a silent part longer than min interval are detected, the audio will be sliced apart from the frame(s) with the lowest RMS value within the silent area.
        Long silence parts may be deleted.
        '''
        if self.Media_Format_Output is not None:
            if f'*.{self.Media_Format_Output}'.lower() not in self.AudioExtensions:
                raise Exception(f"Format '{self.Media_Format_Output}' is currently not supported!")
        else:
            self.Media_Format_Output = Path(Media_Name_Input).suffix.strip('.')

        Media_Name_Output = os.path.splitext(os.path.basename(Media_Name_Input))[0] + '.' + self.Media_Format_Output
        Media_Path_Output = os.path.join(self.Media_Dir_Output, Media_Name_Output)
        Audio_Name_Input, Audio_Path_Input = Media_Name_Output, Media_Path_Output
        AudioData, SampleRate = Loader(Path = Media_Name_Input, SR = self.SampleRate, Mono = self.ToMono)

        WriteParamsList = [(Audio_Path_Input, AudioData.T if len(AudioData.shape) > 1 else AudioData, int(SampleRate))] # .T: Swap axes if the audio is stereo

        if self.Denoise_Audio:
            WriteParamsList.clear()
            AudioData, SampleRate = Denoiser(
                AudioData,
                SampleRate,
                ModelPath = self.DenoiseModel_Path,
                Target = self.DenoiseTarget
            )
            Audio_Name_Output = Audio_Name_Input.rsplit('.', 1)[0] + '_Denoised_' + '.' + self.Media_Format_Output
            Audio_Path_Output = os.path.normpath(os.path.join(self.Media_Dir_Output, Audio_Name_Output))
            WriteParamsList.append((Audio_Path_Output, AudioData.T if len(AudioData.shape) > 1 else AudioData, int(SampleRate)))

        if self.Slice_Audio:
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
                WriteParamsList.clear()
                for i, chunk in enumerate(chunks):
                    Audio_Name_Output = Audio_Name_Input.rsplit('.', 1)[0] + f'_Sliced_{i}' + '.' + self.Media_Format_Output
                    Audio_Path_Output = os.path.normpath(os.path.join(self.Media_Dir_Output, Audio_Name_Output))
                    WriteParamsList.append((Audio_Path_Output, chunk.T if len(chunk.shape) > 1 else chunk, int(SampleRate)))
                try:
                    os.remove(Audio_Path_Input)
                except OSError:
                    pass
            else:
                pass

        for WriteParams in WriteParamsList:
            soundfile.write(
                *WriteParams,
                subtype = str(self.SubtypeDict.get(self.SampleWidth)) if self.SampleWidth is not None else None
            )

    def Process_Audio(self):
        print('Processing media...')

        with ThreadPoolExecutor(max_workers = os.cpu_count() if not self.Denoise_Audio else 1) as Executor:
            Executor.map(
                self.ProcessMedia,
                self.GetPatterns(self.Media_Dir_Input, self.MediaExtensions)
            )

        print('Finished processing.')