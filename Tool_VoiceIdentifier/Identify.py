'''
Edited
'''

import argparse
import functools
import torch
import os
import numpy as np
import shutil
from typing import Optional

from .modules.ECAPA_TDNN import EcapaTdnn, SpeakerIdetification
from .data_utils.Reader import load_audio, CustomDataset
from .utils.Utility import add_arguments, print_arguments
from .utils.Downloader import Execute_Model_Download


class Voice_Identifying:
    '''
    1. Contrast the audio by inference
    2. Classify the audio by similarity
    '''
    def __init__(self,
        Audio_Path_Std: str,
        #Audio_Path_Chk: str,
        Audio_Dir_Input: str,
        Audio_Dir_Output: str = './Recgonized',
        Model_Dir: str = './Models',
        Model_Type: str = 'Ecapa-Tdnn',
        Model_Name: str = 'small',
        Feature_Method: str = 'melspectrogram',
        DecisionThreshold: float = 0.60,
        Duration_of_Audio: float = 4.20,
        Speaker: Optional[str] = None
    ):
        self.Audio_Dir_Input = Audio_Dir_Input
        self.Audio_Dir_Output = Audio_Dir_Output
        self.Audio_Path_Std = Audio_Path_Std
        #self.Audio_Path_Chk = Audio_Path_Chk
        self.Model_Dir = Model_Dir
        self.Model_Type = Model_Type
        self.Model_Name = Model_Name
        self.Feature_Method = Feature_Method
        self.DecisionThreshold = DecisionThreshold
        self.Duration_of_Audio = Duration_of_Audio
        self.Speaker = Speaker

        self.TypeList = ['Ecapa-Tdnn']
        self.NameList = ['small']
        self.MethodList = ['spectrogram', 'melspectrogram']
        self.Model_Path = os.path.join(self.Model_Dir, self.Model_Type, self.Feature_Method, self.Model_Name) + '.pth'

    def GetModel(self):
        Parser = argparse.ArgumentParser(description = __doc__)
        Add_Arg = functools.partial(add_arguments, argparser = Parser)
        Add_Arg('Resume',           str,      self.Model_Dir,            '模型文件夹路径')
        Add_Arg('Model_Type',       str,      self.Model_Type,           '选择模型的类型',             choices = self.TypeList)
        Add_Arg('Model_Name',       str,      self.Model_Name,           '模型文件的名字',             choices = self.NameList)
        Add_Arg('Feature_Method',   str,      self.Feature_Method,       '音频特征提取方法',           choices = self.MethodList)
        Args = Parser.parse_args(args = [])

        # Download Model
        Execute_Model_Download(self.Model_Dir, self.Model_Type, self.Feature_Method, self.Model_Name)

        # 获取模型
        DataSet = CustomDataset(data_list_path = None, feature_method = Args.Feature_Method)
        if Args.Model_Type == 'Ecapa-Tdnn':
            self.Model = SpeakerIdetification(backbone = EcapaTdnn(input_size = DataSet.input_size))
        else:
            raise Exception(f'{Args.Model_Type} 模型不存在！')

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
        Parser = argparse.ArgumentParser(description = __doc__)
        Add_Arg = functools.partial(add_arguments, argparser = Parser)
        Add_Arg('Audio_Path_Std',   str,      self.Audio_Path_Std,       '标准音频的路径')
        #Add_Arg('Audio_Path_Chk',   str,      self.Audio_Path_Chk,       '比对音频的路径')
        Add_Arg('Audio_Dir_Chk',    str,      self.Audio_Dir_Input,      '比对音频的目录')
        Add_Arg('NewDir',           str,      self.Audio_Dir_Output,     '移动音频的目录')
        Add_Arg('Feature_Method',   str,      self.Feature_Method,       '音频特征提取方法',           choices = self.MethodList)
        Add_Arg('Threshold',        float,    self.DecisionThreshold,    '判断是否为同一个人的阈值')
        Add_Arg('Audio_Duration',   float,    self.Duration_of_Audio,    '预测的音频长度，单位秒')
        Add_Arg('Speaker',          str,      self.Speaker,              '说话人物的名字')
        Args = Parser.parse_args(args = [])
        
        #print_arguments(Args)

        os.makedirs(Args.NewDir, exist_ok = True)

        # 预测音频
        def infer(Audio_Path):
            data = load_audio(Audio_Path, mode = 'infer', feature_method = Args.Feature_Method, chunk_duration = Args.Audio_Duration)
            data = data[np.newaxis, :]
            data = torch.tensor(data, dtype = torch.float32, device = self.Device)
            # 执行预测
            Feature = self.Model.backbone(data)
            return Feature.data.cpu().numpy()
        
        # 要预测的两个人的音频文件
        if os.path.exists(Args.Audio_Path_Std):
            Feature1 = infer(Args.Audio_Path_Std)[0]
        for File_Name in os.listdir(Args.Audio_Dir_Chk):
            Audio_Path_Chk = os.path.join(Args.Audio_Dir_Chk, File_Name)
            Feature2 = infer(Audio_Path_Chk)[0]
            # 对角余弦值
            Dist = np.dot(Feature1, Feature2) / (np.linalg.norm(Feature1) * np.linalg.norm(Feature2))
            if Dist > Args.Threshold:
                print(f"{Args.Audio_Path_Std} 和 {Audio_Path_Chk} 为同一个人，相似度为：{Dist}")
                shutil.copy(
                    src = Audio_Path_Chk,
                    dst = os.path.join(Args.NewDir, f"[{Args.Speaker}]{File_Name}") if self.Speaker != None else Args.NewDir
                ) # 复制音频至新目录并实现选择性重命名：“[说话人物的名字]原文件名”
            else:
                print(f"{Args.Audio_Path_Std} 和 {Audio_Path_Chk} 不是同一个人，相似度为：{Dist}")