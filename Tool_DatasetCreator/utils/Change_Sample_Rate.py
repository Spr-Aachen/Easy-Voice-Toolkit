'''
Edited
'''

import os
import time
import librosa
import soundfile


def pre_process_audio(
    Audio_Dir_Input,
    Sample_Rate,
    Subtype,
    Audio_Dir_Output
):
    Start_Sub = time.time()

    print('Downsampling wav files and changing bit pro sample...')

    s = 0

    for File_Name in os.listdir(Audio_Dir_Input):
        if File_Name.endswith('.wav'):
            try:
                nameSolo_1 = File_Name.rsplit('.', 1)[0]
                '''
                y, s = librosa.load(Audio_Dir_Input + File_Name, sr=16000) # Downsample 44.1kHz to 8kHz
                librosa.output.write_wav(path_audio_processed + nameSolo_1 + '.wav', y, s)
                '''
                data, samplerate = librosa.load(os.path.join(Audio_Dir_Input, File_Name), sr = Sample_Rate) # Downsample 44.1kHz to 22050HZ (default). Or use none to preserve the native sampling rate of the file
                soundfile.write(os.path.join(Audio_Dir_Output, (nameSolo_1 + '.wav')), data, samplerate, subtype = Subtype)
                s = s + 1
                print('File ', s , ' completed:', nameSolo_1)

            except EOFError as error:
                next

    print('Downsampling and bit pro sample changing complete')
    print('---------------------------------------------------------------------')

    #shutil.rmtree('./audio', ignore_errors=True)

    End_Sub = time.time()

    print('The script took ', End_Sub - Start_Sub, ' seconds to run')


#Source:
#https://stackoverflow.com/questions/30619740/python-downsampling-wav-audio-file
#https://stackoverflow.com/questions/44812553/how-to-convert-a-24-bit-wav-file-to-16-or-32-bit-files-in-python3