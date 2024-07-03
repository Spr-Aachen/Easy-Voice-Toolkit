import os
import re
import argparse
import json
import torchaudio
from typing import Optional
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from utils import (
    load_audiopaths_sid_text,
    add_elements
)
from text import (
    _clean_text
)


parser = argparse.ArgumentParser()
parser.add_argument("--FileList_Path_Training", type = str, default = "train.txt")
parser.add_argument("--FileList_Path_Validation", type = str, default = "val.txt")
parser.add_argument("--Set_Epochs", type = int, default = 10000)
parser.add_argument("--Set_Eval_Interval", type = int, default = 1000)
parser.add_argument("--Set_Batch_Size", type = int, default = 16)
parser.add_argument("--Set_FP16_Run", type = bool, default = True)
parser.add_argument("--Keep_Original_Speakers", type = bool, default = False)
parser.add_argument("--Config_Path_Load", type = Optional[str], default = None)
parser.add_argument("--Output_Root", type = str, default = "./")
parser.add_argument("--Output_Dir_Name", type = str, default = "Output")
parser.add_argument("--Output_Config_Name", type = str, default = "Config.json")
args = parser.parse_args()

FileList_Path_Training = str(os.environ.get('FileList_Path_Training', str(args.FileList_Path_Training)))
FileList_Path_Validation = str(os.environ.get('FileList_Path_Validation', str(args.FileList_Path_Validation)))
Set_Epochs = int(os.environ.get('Set_Epochs', str(args.Set_Epochs)))
Set_Eval_Interval = int(os.environ.get('Set_Eval_Interval', str(args.Set_Eval_Interval)))
Set_Batch_Size = int(os.environ.get('Set_Batch_Size', str(args.Set_Batch_Size)))
Set_FP16_Run = eval(os.environ.get('Set_FP16_Run', str(args.Set_FP16_Run)))
Keep_Original_Speakers = eval(os.environ.get('Keep_Original_Speakers', str(args.Keep_Original_Speakers)))
Config_Path_Load = str(os.environ.get('Config_Path_Load', str(args.Config_Path_Load))) if Keep_Original_Speakers else None
Output_Root = str(os.environ.get('Output_Root', str(args.Output_Root)))
Output_Dir_Name = str(os.environ.get('Output_Dir_Name', str(args.Output_Dir_Name)))
Output_Config_Name = str(os.environ.get('Output_Config_Name', str(args.Output_Config_Name)))

Dir_Output = Path(Output_Root).joinpath(Output_Dir_Name).as_posix()
os.makedirs(Dir_Output, exist_ok = True)
Config_Path_Edited = Path(Dir_Output).joinpath(Output_Config_Name).__str__()
FileList_Path_Training_Updated = Path(Config_Path_Edited).parent.joinpath(Path(FileList_Path_Training).name).__str__()
FileList_Path_Validation_Updated = Path(Config_Path_Edited).parent.joinpath(Path(FileList_Path_Validation).name).__str__()
Out_Extension = "cleaned"


def Configurator():
    '''
    Edit JSON file
    '''
    def Get_Languages(Text_Path_Training, Text_Path_Validation):
        Languages = []
        for Text_Path in [Text_Path_Training, Text_Path_Validation]:
            with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as File:
                Lines = File.readlines()
            for _, Line in enumerate(Lines):
                Line_Text = Line.split('|', maxsplit = 2)[2]
                Language = re.split(r'[\[\]]', Line_Text)[1]
                Languages.append(Language) if Language not in Languages else None
        if set(Languages).issubset({'ZH', 'EN', 'JA'}):
            if set(Languages) == {'ZH'}:
                return "mandarin"
            else:
                return "mandarin_english_japanese"
        else:
            raise Exception('Unsupported language!')

    def Get_NewSpeakers(Text_Path_Training, Text_Path_Validation):
        Speakers = []
        for Text_Path in [Text_Path_Training, Text_Path_Validation]:
            with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as File:
                Lines = File.readlines()
            for _, Line in enumerate(Lines):
                Speaker = Line.split('|', maxsplit = 2)[1]
                Speakers.append(Speaker) if Speaker not in Speakers else None
        return Speakers

    def Get_OldSpeakers(Config_Path_Load):
        if Config_Path_Load is not None and Path(Config_Path_Load).exists():
            with open(file = Config_Path_Load, mode = 'rb') as ConfigFile_Extra:
                OldSpeakers = json.load(ConfigFile_Extra)["speakers"]
        else:
            OldSpeakers = []
        return OldSpeakers

    Language = Get_Languages(FileList_Path_Training, FileList_Path_Validation)
    NewSpeakers = Get_NewSpeakers(FileList_Path_Training, FileList_Path_Validation)
    OldSpeakers = Get_OldSpeakers(Config_Path_Load) if Keep_Original_Speakers else []

    with open(file = Path(__file__).parent.joinpath('./configs', f'{Language}_base.json').__str__(), mode = 'rb') as ConfigFile_Default:
        Params = json.load(ConfigFile_Default)
    try:
        Params_Old = Params
        Params_Old["train"]["eval_interval"]   = Set_Eval_Interval
        Params_Old["train"]["epochs"]          = Set_Epochs
        Params_Old["train"]["batch_size"]      = Set_Batch_Size
        Params_Old["train"]["fp16_run"]        = Set_FP16_Run
        Params_Old["data"]["training_files"]   = f'{FileList_Path_Training_Updated}.{Out_Extension}'
        Params_Old["data"]["validation_files"] = f'{FileList_Path_Validation_Updated}.{Out_Extension}'
        Params_Old["data"]["text_cleaners"]    = [(Language + "_cleaners").lower()]
        Params_Old["data"]["n_speakers"]       = add_elements(OldSpeakers, NewSpeakers).__len__()
        Params_Old["speakers"]                 = add_elements(OldSpeakers, NewSpeakers)
        Params_New = Params_Old
    except:
        raise Exception("Please check if params exist")
    with open(Config_Path_Edited, 'w', encoding = 'utf-8') as File_New:
        json.dump(Params_New, File_New, indent = 4)
    print(f"Config created in {Dir_Output}")


def Cleaner():
    '''
    Convert natural language text to symbols
    '''
    def Update_SID(Config_Path, Text_Path, Save_Path):
        with open(file = Config_Path, mode = 'rb') as ConfigFile:
            NewSpeakers = json.load(ConfigFile)["speakers"]
        with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as TextFile:
            Lines = TextFile.readlines()
        for Index, Line in enumerate(Lines):
            Line_Path = Line.split('|', maxsplit = 1)[0]
            Line_Path = Path(Text_Path).parent.joinpath(Line_Path).as_posix() if not Path(Line_Path).is_absolute() else Line_Path
            Speaker = Line.split('|', maxsplit = 2)[1]
            SpeakerID = NewSpeakers.index(Speaker)
            Line_Text = Line.split('|', maxsplit = 2)[2]
            Line = f"{Line_Path}|{SpeakerID}|{Line_Text}"
            Lines[Index] = Line
        with open(file = Save_Path, mode = 'w', encoding = 'utf-8') as TextFile:
            TextFile.writelines(Lines)

    def Get_Cleaners(Config_Path):
        with open(file = Config_Path, mode = 'rb') as ConfigFile:
            NewCleaners = json.load(ConfigFile)["data"]["text_cleaners"]
        return NewCleaners

    for Index, FileList in enumerate([FileList_Path_Training, FileList_Path_Validation]):
        print("START:", FileList)
        FileList_Updated = [FileList_Path_Training_Updated, FileList_Path_Validation_Updated][Index]
        Update_SID(Config_Path_Edited, FileList, FileList_Updated)
        Path_SID_Text = load_audiopaths_sid_text(FileList_Updated)
        for i in range(len(Path_SID_Text)):
            Path_SID_Text[i][2] = _clean_text(Path_SID_Text[i][2], Get_Cleaners(Config_Path_Edited))
        Filelist_Cleaned = FileList_Updated + "." + Out_Extension
        with open(Filelist_Cleaned, 'w', encoding = 'utf-8') as f:
            f.writelines(["|".join(x) + "\n" for x in Path_SID_Text])


def Resampler():
    '''
    Resample dataset audio to fit the sampling rate setting in config
    '''
    def Get_Resample_List(Config_Path, Text_Path):
        ResampleList = []
        with open(file = Config_Path, mode = 'rb') as ConfigFile:
            SampleRate_New = json.load(ConfigFile)['data']['sampling_rate']
        with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as TextFile:
            Lines = TextFile.readlines()
        for Line in Lines:
            Line_Path = Line.split('|', maxsplit = 1)[0]
            ResampleList.append((Line_Path, SampleRate_New))
        return ResampleList

    def Resample(Audio_Path, SampleRate_New):
        AudioData_Old, SampleRate_Old = torchaudio.load(Audio_Path)
        AudioData_New = torchaudio.transforms.Resample(orig_freq = SampleRate_Old, new_freq = SampleRate_New)(AudioData_Old)
        torchaudio.save(Audio_Path, src = AudioData_New, sample_rate = SampleRate_New)

    for FileList in (FileList_Path_Validation, FileList_Path_Training):
        print("Resampling audio according to", FileList)
        with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
            Executor.map(
                Resample,
                *zip(*Get_Resample_List(Config_Path_Edited, FileList))
            )


if __name__ == "__main__":
    Configurator()
    Cleaner()
    Resampler()