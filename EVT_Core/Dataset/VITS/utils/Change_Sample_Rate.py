import os
import time
import librosa
import soundfile
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def PreprocessAudio(
    Audio_Path_Input,
    Audio_Path_Output,
    SampleRate,
    SampleWidth,
    ToMono
):
    SubtypeDict = {
        '8':          'PCM_8',
        '16':         'PCM_16',
        '24':         'PCM_24',
        '32':         'PCM_32',
        '32 (Float)': 'FLOAT'
    }
    try:
        AudioData, SampleRate = librosa.load(Audio_Path_Input, sr = SampleRate, mono = True if ToMono else False)
        soundfile.write(
            file = Audio_Path_Output,
            data = AudioData.T if len(AudioData.shape) > 1 else AudioData,
            samplerate = int(SampleRate),
            subtype = str(SubtypeDict.get(SampleWidth)) if SampleWidth is not None else None
        )

    except Exception as e:
        print(e)
        next


def preprocess_audio(
    Audio_Paths_Input,
    SampleRate,
    SampleWidth,
    ToMono,
    Audio_Dir_Output
):
    Start_Sub = time.time()

    print('Downsampling wav files and changing bit pro sample...')

    ParamsList = []
    for Audio_Path_Input in Audio_Paths_Input:
        if Audio_Path_Input.endswith('.wav'):
            Audio_Name = Path(Audio_Path_Input).name
            Audio_Path_Output = os.path.join(Audio_Dir_Output, Audio_Name)
            ParamsList.append((Audio_Path_Input, Audio_Path_Output, SampleRate, SampleWidth, ToMono))

    with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
        Executor.map(
            PreprocessAudio,
            *zip(*ParamsList)
        )

    print('Downsampling and bit pro sample changing complete')
    print('---------------------------------------------------------------------')

    #shutil.rmtree('./audio', ignore_errors=True)

    End_Sub = time.time()

    print('The script took ', End_Sub - Start_Sub, ' seconds to run')