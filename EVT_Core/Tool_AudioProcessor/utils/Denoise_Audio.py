import numpy
import librosa
from scipy.signal import medfilt


def Denoiser(
    AudioData,
    Mode: int = 1
):
    if Mode == 1: # 中值法
        # 将数据转换为浮点数类型
        AudioData = AudioData.astype(float)

        # 对每个声道的数据进行降噪处理
        for i in range(AudioData.shape[1]):
            AudioData[:, i] = medfilt(AudioData[:, i], 3)

        # 将数据转换回整型类型
        AudioData = AudioData.astype(numpy.int16)

    if Mode == 2: # FFT
        # 通过FFT转换到频域
        AudioData = librosa.stft(AudioData)

        # 在频域进行降噪处理
        Mean_RealPart = numpy.mean(AudioData.real) # 对实部求平均
        Mean_ImagPart = numpy.mean(AudioData.imag) # 对虚部求平均
        AudioData = AudioData - Mean_RealPart - 1j * Mean_ImagPart # 重构复数 去除直流分量

        # 通过逆FFT转换回时域
        AudioData = librosa.istft(AudioData)

    return AudioData