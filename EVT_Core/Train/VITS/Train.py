import os
import sys
from typing import Optional
from subprocess import Popen
from pathlib import Path


current_dir = Path(__file__).absolute().parent.as_posix()
os.chdir(current_dir)
sys.path.insert(0, f"{current_dir}/VITS2_finetuning")


python_exec = sys.executable or "python"

p_preprocess = None
p_train = None


def Train(
    FileList_Path_Training: str = 'train.txt',
    FileList_Path_Validation: str = 'val.txt',
    Set_Epochs: int = 10000,
    Set_Eval_Interval: int = 1000,
    Set_Batch_Size: int = 16,
    Set_FP16_Run: bool = True,
    Keep_Original_Speakers: bool = False,
    Config_Path_Load: Optional[str] = None,
    Num_Workers: int = 4,
    Use_PretrainedModels: bool = False,
    Model_Path_Pretrained_G: str = 'pretrained_G.pth',
    Model_Path_Pretrained_D: str = 'pretrained_D.pth',
    Output_Root: str = './',
    Output_Dir_Name: str = 'Output',
    Output_Config_Name: str = 'Config.json',
    Output_LogDir: str = './'
):
    '''
    Train speech models
    '''
    global p_preprocess
    if p_preprocess is None:
        os.environ['FileList_Path_Training'] = str(FileList_Path_Training)
        os.environ['FileList_Path_Validation'] = str(FileList_Path_Validation)
        os.environ['Set_Epochs'] = str(Set_Epochs)
        os.environ['Set_Eval_Interval'] = str(Set_Eval_Interval)
        os.environ['Set_Batch_Size'] = str(Set_Batch_Size)
        os.environ['Set_FP16_Run'] = str(Set_FP16_Run)
        os.environ['Keep_Original_Speakers'] = str(Keep_Original_Speakers)
        os.environ['Config_Path_Load'] = str(Config_Path_Load)
        os.environ['Output_Root'] = str(Output_Root)
        os.environ['Output_Dir_Name'] = str(Output_Dir_Name)
        os.environ['Output_Config_Name'] = str(Output_Config_Name)
        print("Start preprocessing...")
        p_preprocess = Popen(f'"{python_exec}" "VITS2_finetuning/preprocess.py"', shell = True)
        p_preprocess.wait()
        p_preprocess = None
    else:
        print("已有正在进行的预处理任务，需先终止才能开启下一次任务")

    global p_train
    if p_train is None:
        os.environ['Num_Workers'] = str(Num_Workers)
        os.environ['Use_PretrainedModels'] = str(Use_PretrainedModels)
        os.environ['Model_Path_Pretrained_G'] = str(Model_Path_Pretrained_G)
        os.environ['Model_Path_Pretrained_D'] = str(Model_Path_Pretrained_D)
        os.environ['Output_LogDir'] = str(Output_LogDir)
        print("Start training...")
        p_train = Popen(f'"{python_exec}" "VITS2_finetuning/train.py"', shell = True)
        p_train.wait()
        p_train = None
    else:
        print("已有正在进行的训练任务，需先终止才能开启下一次任务")