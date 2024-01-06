import torch
import os
import numpy as np
import shutil
from pathlib import Path

from .modules.ECAPA_TDNN import EcapaTdnn, SpeakerIdetification
from .data_utils.Reader import load_audio, CustomDataset
from .utils.Downloader import Execute_Model_Download


class Voice_Identifying:
    '''
    1. Contrast the audio by inference
    2. Classify the audio by similarity
    '''
    def __init__(self,
        StdAudioSpeaker: dict,
        Audio_Dir_Input: str,
        Audio_Dir_Output: str = './Recgonized',
        Model_Path: str = './Models/.pth',
        Model_Type: str = 'Ecapa-Tdnn',
        Feature_Method: str = 'melspectrogram',
        DecisionThreshold: float = 0.60,
        Duration_of_Audio: float = 4.20
    ):
        self.StdAudioSpeaker = StdAudioSpeaker
        self.Audio_Dir_Input = Audio_Dir_Input
        self.Audio_Dir_Output = Audio_Dir_Output
        self.Model_Path = Model_Path
        self.Model_Dir = Path(Model_Path).parent.__str__()
        self.Model_Name = Path(Model_Path).stem.__str__()
        self.Model_Type = Model_Type
        self.Feature_Method = Feature_Method
        self.DecisionThreshold = DecisionThreshold
        self.Duration_of_Audio = Duration_of_Audio

    def GetModel(self):
        '''
        Function to load model
        '''
        # Download Model
        if self.Model_Name in ['Ecapa-Tdnn_spectrogram', 'Ecapa-Tdnn_melspectrogram']:
            Execute_Model_Download(self.Model_Dir, self.Model_Name)

        # 获取模型
        DataSet = CustomDataset(data_list_path = None, feature_method = self.Feature_Method)
        if self.Model_Type == 'Ecapa-Tdnn':
            self.Model = SpeakerIdetification(backbone = EcapaTdnn(input_size = DataSet.input_size))
        else:
            raise Exception(f'{self.Model_Type} 模型不存在！')

        # 指定使用设备
        self.Device = torch.device("cuda")

        # 加载模型
        self.Model.to(self.Device)
        Model_Dict = self.Model.state_dict()
        Param_State_Dir = torch.load(self.Model_Path)
        for name, weight in Model_Dict.items():
            if name in Param_State_Dir.keys():
                if list(weight.shape) != list(Param_State_Dir[name].shape):
                    Param_State_Dir.pop(name, None)
        self.Model.load_state_dict(Param_State_Dir, strict = False)
        print(f"成功加载模型参数和优化方法参数：{self.Model_Path}")
        self.Model.eval()

        #return self.Device, self.Model

    def Inference(self):
        '''
        Function to infer 
        '''
        # Create Dir
        os.makedirs(self.Audio_Dir_Output, exist_ok = True)

        # 预测音频
        def infer(Audio_Path):
            data = load_audio(Audio_Path, mode = 'infer', feature_method = self.Feature_Method, chunk_duration = self.Duration_of_Audio)
            data = data[np.newaxis, :]
            data = torch.tensor(data, dtype = torch.float32, device = self.Device)
            # 执行预测
            Feature = self.Model.backbone(data)
            return Feature.data.cpu().numpy()

        # 两两比对
        for Speaker, Audio_Path_Std in self.StdAudioSpeaker.items():
            if os.path.exists(Audio_Path_Std):
                Feature1 = infer(Audio_Path_Std)[0]
            for File_Name in os.listdir(self.Audio_Dir_Input):
                Audio_Path_Chk = os.path.join(self.Audio_Dir_Input, File_Name)
                Feature2 = infer(Audio_Path_Chk)[0]
                # 对角余弦值
                Dist = np.dot(Feature1, Feature2) / (np.linalg.norm(Feature1) * np.linalg.norm(Feature2))
                if Dist > self.DecisionThreshold:
                    print(f"{Audio_Path_Std} 和 {Audio_Path_Chk} 为同一个人，相似度为：{Dist}")
                    shutil.copy(
                        src = Audio_Path_Chk,
                        dst = os.path.join(self.Audio_Dir_Output, f"[{Speaker}]{File_Name}") if Speaker != None else self.Audio_Dir_Output
                    ) # 复制音频至新目录并实现选择性重命名：“[说话人物的名字]原文件名”
                else:
                    print(f"{Audio_Path_Std} 和 {Audio_Path_Chk} 不是同一个人，相似度为：{Dist}")