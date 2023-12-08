'''
Added
'''

import numpy
import librosa
from pydub import AudioSegment
from typing import Optional


def Converter(
    Path: str,
    SR: Optional[float] = 22050.,
    Mono: bool = True
):
    '''
    Load an media file like using librosa.load()
    '''
    AudioFile = AudioSegment.from_file(Path)

    AudioFile.set_channels(1) if Mono and AudioFile.channels > 1 else None

    SamplesArray = [Channel.get_array_of_samples() for Channel in AudioFile.split_to_mono()]
    SamplesArray_ND = numpy.array(SamplesArray) if AudioFile.channels > 1 else numpy.array(*SamplesArray)

    AudioData = SamplesArray_ND.astype(numpy.float32) / numpy.iinfo(SamplesArray[0].typecode).max # Normalization (Librosa defaults to float32, soundfile defaults to float64)
    SampleRate = float(AudioFile.frame_rate)

    AudioData = librosa.core.resample(AudioData, orig_sr = SampleRate, target_sr = float(SR), res_type = 'soxr_vhq') if SR is not None else AudioData
    SampleRate = float(SR) if SR is not None else SampleRate

    return AudioData, SampleRate