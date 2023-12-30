import os

from Process.Process import Audio_Processing
from ASR.VPR.Identify import Voice_Identifying
from STT.Whisper.Transcribe import Voice_Transcribing
from Dataset.VITS.Create import Dataset_Creating
from Train.VITS.Train import Voice_Training
from TTS.VITS.Convert import Voice_Converting


class AudioToAudio:
    '''
    '''
    def __init__(self,
        StorageDir,
        Media_Dir_Input,
        StdAudioSpeaker,
        Model_Dir,
        Add_AuxiliaryData,
        AuxiliaryData_Path,
        Epochs,
        Batch_Size,
        Model_Path_Pretrained_G,
        Model_Path_Pretrained_D,
        Text,
        Language,
        Speaker
    ):
        self.StorageDir = StorageDir,
        self.Media_Dir_Input = Media_Dir_Input,
        self.StdAudioSpeaker = StdAudioSpeaker,
        self.Model_Dir = Model_Dir,
        self.AuxiliaryData_Path = AuxiliaryData_Path if Add_AuxiliaryData else None
        self.Epochs = Epochs,
        self.Batch_Size = Batch_Size,
        self.Model_Path_Pretrained_G = Model_Path_Pretrained_G,
        self.Model_Path_Pretrained_D = Model_Path_Pretrained_D,
        self.Text = Text,
        self.Language = Language,
        self.Speaker = Speaker

        os.makedirs(self.StorageDir, exist_ok = True)

    def ProcessAudio(self):
        self.AudioConvertandSlice = Audio_Processing(
            Media_Dir_Input = self.Media_Dir_Input,
            Media_Dir_Output = f"{self.StorageDir}/Temp/1"
        )
        self.AudioConvertandSlice.Process_Audio()

    def IdentifyVoice(self):
        self.AudioContrastInference = Voice_Identifying(
            StdAudioSpeaker = self.StdAudioSpeaker,
            Audio_Dir_Input = f'{self.StorageDir}/Temp/1',
            Audio_Dir_Output = f'{self.StorageDir}/Temp/2',
            Model_Dir = self.Model_Dir,
        )
        self.AudioContrastInference.GetModel()
        self.AudioContrastInference.Inference()

    def TranscribeVoice(self):
        self.WAVtoSRT = Voice_Transcribing(
            Model_Dir = self.Model_Dir,
            WAV_Dir = f'{self.StorageDir}/Temp/2',
            SRT_Dir = f'{self.StorageDir}/Temp/3',
        )
        self.WAVtoSRT.Transcriber()

    def CreateDataset(self):
        self.SRTtoCSVandSplitAudio = Dataset_Creating(
            SRT_Dir = f'{self.StorageDir}/Temp/3',
            WAV_Dir = f'{self.StorageDir}/Temp/2',
            WAV_SampleRate = 22050,
            WAV_SampleWidth = '32 (Float)',
            WAV_ToMono = True,
            WAV_Dir_Split = f'{self.StorageDir}/Temp/4',
            AuxiliaryData_Path = self.AuxiliaryData_Path,
            ModelType = 'VITS',
            FileList_Path_Training = f'{self.StorageDir}/Temp/4/Train_FileList.txt',
            FileList_Path_Validation = f'{self.StorageDir}/Temp/4/Val_FileList.txt'
        )
        self.SRTtoCSVandSplitAudio.CallingFunctions()

    def TrainVoice(self):
        self.PreprocessandTrain = Voice_Training(
            FileList_Path_Training = f'{self.StorageDir}/Temp/4/Train_FileList.txt',
            FileList_Path_Validation = f'{self.StorageDir}/Temp/4/Val_FileList.txt',
            Config_Dir_Save = f'{self.StorageDir}/TrainResult',
            Set_Eval_Interval = 1000,
            Set_Epochs = self.Epochs,
            Set_Batch_Size = self.Batch_Size,
            Keep_Original_Speakers = False,
            Num_Workers = 4,
            Model_Path_Pretrained_G = self.Model_Path_Pretrained_G,
            Model_Path_Pretrained_D = self.Model_Path_Pretrained_D,
            Model_Dir_Save = f'{self.StorageDir}/TrainResult'
        )
        self.PreprocessandTrain.Preprocessing_and_Training()

    def ConvertVoice(self):
        self.TTS = Voice_Converting(
            Config_Path_Load = f'{self.StorageDir}/TrainResult',
            Model_Path_Load = f'{self.StorageDir}/TrainResult',
            Text = self.Text,
            Language = self.Language,
            Speaker = self.Speaker,
            EmotionStrength = 0.667,
            PhonemeDuration = 0.8,
            SpeechRate = 1,
            Audio_Dir_Save = f'{self.StorageDir}/InferResult'
        )
        self.TTS.Converting()

    def Start(self):
        self.ProcessAudio()
        self.IdentifyVoice()
        self.TranscribeVoice()
        self.CreateDataset()
        self.TrainVoice()
        self.ConvertVoice()