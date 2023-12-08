'''
Edited
'''

import os
import time
import librosa
import soundfile
from concurrent.futures import ThreadPoolExecutor


SubtypeDict = {
    '8':          'PCM_8',
    '16':         'PCM_16',
    '24':         'PCM_24',
    '32':         'PCM_32',
    '32 (Float)': 'FLOAT'
}


def PreprocessAudio(
    Audio_Path_Input,
    Audio_Path_Output,
    SampleRate,
    SampleWidth,
    ToMono
):
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
    Audio_Dir_Input,
    SampleRate,
    SampleWidth,
    ToMono,
    Audio_Dir_Output
):
    Start_Sub = time.time()

    print('Downsampling wav files and changing bit pro sample...')

    ParamsList = []
    for File_Name in os.listdir(Audio_Dir_Input):
        if File_Name.endswith('.wav'):
            Audio_Path_Input = os.path.join(Audio_Dir_Input, File_Name)
            Audio_Path_Output = os.path.join(Audio_Dir_Output, (File_Name.rsplit('.', 1)[0] + '.wav'))
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


#Source:
#https://stackoverflow.com/questions/30619740/python-downsampling-wav-audio-file
#https://stackoverflow.com/questions/44812553/how-to-convert-a-24-bit-wav-file-to-16-or-32-bit-files-in-python3