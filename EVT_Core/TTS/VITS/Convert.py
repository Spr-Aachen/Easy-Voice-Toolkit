import os
import sys
from typing import Optional
from subprocess import Popen
from pathlib import Path


current_dir = Path(__file__).absolute().parent.as_posix()
os.chdir(current_dir)
sys.path.insert(0, f"{current_dir}/VITS2_finetuning")


python_exec = sys.executable or "python"

p_infer = None


def Convert(
    Config_Path_Load: str = ...,
    Model_Path_Load: str = ...,
    Text: str = '请输入语句',
    Language: Optional[str] = None,
    Speaker: str = ...,
    EmotionStrength: float = .667,
    PhonemeDuration: float = 0.8,
    SpeechRate: float = 1.,
    Audio_Path_Save: str = "audio.wav"
):
    '''
    Convert text to speech and save as audio files
    '''
    global p_infer
    if p_infer is None:
        os.environ['Config_Path_Load'] = str(Config_Path_Load)
        os.environ['Model_Path_Load'] = str(Model_Path_Load)
        os.environ['Text'] = str(Text)
        os.environ['Language'] = str(Language)
        os.environ['Speaker'] = str(Speaker)
        os.environ['EmotionStrength'] = str(EmotionStrength)
        os.environ['PhonemeDuration'] = str(PhonemeDuration)
        os.environ['SpeechRate'] = str(SpeechRate)
        os.environ['Audio_Path_Save'] = str(Audio_Path_Save)
        print("Start converting...")
        p_infer = Popen(f'"{python_exec}" "VITS2_finetuning/inference.py"', shell = True)
        p_infer.wait()
        p_infer = None
    else:
        print("已有正在进行的推理任务，需先终止才能开启下一次任务")