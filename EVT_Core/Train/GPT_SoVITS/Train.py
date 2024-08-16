import os,sys
if len(sys.argv)==1:sys.argv.append('v2')
version="v1"if sys.argv[1]=="v1" else"v2"
os.environ["version"]=version
now_dir = os.getcwd()
#sys.path.insert(0, now_dir)
import warnings
warnings.filterwarnings("ignore")
import json,yaml,torch,pdb,re,shutil
import platform
import psutil
import signal
import traceback
from subprocess import Popen
from pathlib import Path

from .config import python_exec#, exp_root
#from .GPT_SoVITS.tools.my_utils import load_audio, check_for_existance, check_details


torch.manual_seed(233333)
tmp = Path(now_dir).joinpath("TEMP").as_posix()
os.makedirs(tmp, exist_ok=True)
if(Path(tmp).exists()):
    for name in os.listdir(tmp):
        if(name=="jieba.cache"):continue
        path="%s/%s"%(tmp,name)
        delete=os.remove if Path(path).is_file() else shutil.rmtree
        try:
            delete(path)
        except Exception as e:
            print(str(e))
            pass
os.environ["TEMP"] = tmp


current_dir = Path(__file__).absolute().parent.as_posix()
os.chdir(current_dir)
sys.path.insert(0, f"{current_dir}/GPT_SoVITS")


def kill_proc_tree(pid, including_parent=True):
    try:
        parent = psutil.Process(pid)
    except psutil.NoSuchProcess:
        # Process already terminated
        return

    children = parent.children(recursive=True)
    for child in children:
        try:
            os.kill(child.pid, signal.SIGTERM)  # or signal.SIGKILL
        except OSError:
            pass
    if including_parent:
        try:
            os.kill(parent.pid, signal.SIGTERM)  # or signal.SIGKILL
        except OSError:
            pass


def kill_process(pid):
    if(platform.system()=="Windows"):
        cmd = "taskkill /t /f /pid %s" % pid
        os.system(cmd)
    else:
        kill_proc_tree(pid)


ps1abc=[]
def open1abc(
    inp_text,
    inp_wav_dir,
    exp_root,
    exp_name,
    is_half,
    gpu_numbers1a,
    gpu_numbers1Ba,
    gpu_numbers1c,
    bert_pretrained_dir,
    ssl_pretrained_dir,
    pretrained_s2G_path
):
    global ps1abc
    '''
    inp_text = my_utils.clean_path(inp_text)
    inp_wav_dir = my_utils.clean_path(inp_wav_dir)
    if check_for_existance([inp_text,inp_wav_dir], is_dataset_processing=True):
        check_details([inp_text,inp_wav_dir], is_dataset_processing=True)
    '''
    if (ps1abc == []):
        opt_dir="%s/%s"%(exp_root,exp_name)
        try:
            #############################1a
            path_text="%s/2-name2text.txt" % opt_dir
            if(os.path.exists(path_text)==False or (os.path.exists(path_text)==True and len(open(path_text,"r",encoding="utf8").read().strip("\n").split("\n"))<2)):
                config={
                    "inp_text":inp_text,
                    "inp_wav_dir":inp_wav_dir,
                    "exp_name":exp_name,
                    "opt_dir":opt_dir,
                    "bert_pretrained_dir":bert_pretrained_dir,
                    "is_half": str(is_half)
                }
                gpu_names=gpu_numbers1a.split("-")
                all_parts=len(gpu_names)
                for i_part in range(all_parts):
                    config.update(
                        {
                            "i_part": str(i_part),
                            "all_parts": str(all_parts),
                            "_CUDA_VISIBLE_DEVICES": fix_gpu_number(gpu_names[i_part]),
                        }
                    )
                    os.environ.update(config)
                    cmd = f'"{python_exec}" "GPT_SoVITS/prepare_datasets_1-get-text.py"'
                    print(cmd)
                    p = Popen(cmd, shell=True)
                    ps1abc.append(p)
                print("进度：1a-ing") #yield "进度：1a-ing", {"__type__": "update", "visible": False}, {"__type__": "update", "visible": True}
                for p in ps1abc:p.wait()
                opt = []
                for i_part in range(all_parts):#txt_path="%s/2-name2text-%s.txt"%(opt_dir,i_part)
                    txt_path = "%s/2-name2text-%s.txt" % (opt_dir, i_part)
                    with open(txt_path, "r",encoding="utf8") as f:
                        opt += f.read().strip("\n").split("\n")
                    os.remove(txt_path)
                with open(path_text, "w",encoding="utf8") as f:
                    f.write("\n".join(opt) + "\n")
                assert len("".join(opt)) > 0, "1Aa-文本获取进程失败"
            print("进度：1a-done") #yield "进度：1a-done", {"__type__": "update", "visible": False}, {"__type__": "update", "visible": True}
            ps1abc=[]
            #############################1b
            config={
                "inp_text":inp_text,
                "inp_wav_dir":inp_wav_dir,
                "exp_name":exp_name,
                "opt_dir":opt_dir,
                "cnhubert_base_dir":ssl_pretrained_dir,
            }
            gpu_names=gpu_numbers1Ba.split("-")
            all_parts=len(gpu_names)
            for i_part in range(all_parts):
                config.update(
                    {
                        "i_part": str(i_part),
                        "all_parts": str(all_parts),
                        "_CUDA_VISIBLE_DEVICES": fix_gpu_number(gpu_names[i_part]),
                    }
                )
                os.environ.update(config)
                cmd = f'"{python_exec}" "GPT_SoVITS/prepare_datasets_2-get-hubert-wav32k.py"'
                print(cmd)
                p = Popen(cmd, shell=True)
                ps1abc.append(p)
            print("进度：1a-done, 1b-ing") #yield "进度：1a-done, 1b-ing", {"__type__": "update", "visible": False}, {"__type__": "update", "visible": True}
            for p in ps1abc:p.wait()
            print("进度：1a1b-done") #yield "进度：1a1b-done", {"__type__": "update", "visible": False}, {"__type__": "update", "visible": True}
            ps1abc=[]
            #############################1c
            path_semantic = "%s/6-name2semantic.tsv" % opt_dir
            if(os.path.exists(path_semantic)==False or (os.path.exists(path_semantic)==True and os.path.getsize(path_semantic)<31)):
                config={
                    "inp_text":inp_text,
                    "exp_name":exp_name,
                    "opt_dir":opt_dir,
                    "pretrained_s2G":pretrained_s2G_path,
                    "s2config_path":f"GPT_SoVITS/configs/s2.json",
                }
                gpu_names=gpu_numbers1c.split("-")
                all_parts=len(gpu_names)
                for i_part in range(all_parts):
                    config.update(
                        {
                            "i_part": str(i_part),
                            "all_parts": str(all_parts),
                            "_CUDA_VISIBLE_DEVICES": fix_gpu_number(gpu_names[i_part]),
                        }
                    )
                    os.environ.update(config)
                    cmd = f'"{python_exec}" "GPT_SoVITS/prepare_datasets_3-get-semantic.py"'
                    print(cmd)
                    p = Popen(cmd, shell=True)
                    ps1abc.append(p)
                print("进度：1a1b-done, 1cing") #yield "进度：1a1b-done, 1cing", {"__type__": "update", "visible": False}, {"__type__": "update", "visible": True}
                for p in ps1abc:p.wait()
                opt = ["item_name\tsemantic_audio"]
                for i_part in range(all_parts):
                    semantic_path = "%s/6-name2semantic-%s.tsv" % (opt_dir, i_part)
                    with open(semantic_path, "r",encoding="utf8") as f:
                        opt += f.read().strip("\n").split("\n")
                    os.remove(semantic_path)
                with open(path_semantic, "w",encoding="utf8") as f:
                    f.write("\n".join(opt) + "\n")
                print("进度：all-done") #yield "进度：all-done", {"__type__": "update", "visible": False}, {"__type__": "update", "visible": True}
            ps1abc = []
            print("一键三连进程结束") #yield "一键三连进程结束", {"__type__": "update", "visible": True}, {"__type__": "update", "visible": False}
        except:
            traceback.print_exc()
            print("一键三连中途报错") #yield "一键三连中途报错", {"__type__": "update", "visible": True}, {"__type__": "update", "visible": False}
    else:
        print("已有正在进行的一键三连任务，需先终止才能开启下一次任务") #yield "已有正在进行的一键三连任务，需先终止才能开启下一次任务", {"__type__": "update", "visible": False}, {"__type__": "update", "visible": True}


gpu_infos = []
mem = []
if_gpu_ok = False

# 判断是否有能用来训练和加速推理的N卡
ngpu = torch.cuda.device_count()
ok_gpu_keywords={"10","16","20","30","40","A2","A3","A4","P4","A50","500","A60","70","80","90","M4","T4","TITAN","L4","4060","H"}
set_gpu_numbers=set()
if torch.cuda.is_available() or ngpu != 0:
    for i in range(ngpu):
        gpu_name = torch.cuda.get_device_name(i)
        if any(value in gpu_name.upper()for value in ok_gpu_keywords):
            # A10#A100#V100#A40#P40#M40#K80#A4500
            if_gpu_ok = True  # 至少有一张能用的N卡
            gpu_infos.append("%s\t%s" % (i, gpu_name))
            set_gpu_numbers.add(i)
            mem.append(int(torch.cuda.get_device_properties(i).total_memory/ 1024/ 1024/ 1024+ 0.4))
'''
# 判断是否支持mps加速
if torch.backends.mps.is_available():
    if_gpu_ok = True
    gpu_infos.append("%s\t%s" % ("0", "Apple GPU"))
    mem.append(psutil.virtual_memory().total/ 1024 / 1024 / 1024) # 实测使用系统内存作为显存不会爆显存
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1' # 当遇到mps不支持的步骤时使用cpu
'''

if if_gpu_ok and len(gpu_infos) > 0:
    gpu_info = "\n".join(gpu_infos)
    default_batch_size = min(mem) // 2
else:
    gpu_info = ("%s\t%s" % ("0", "CPU"))
    gpu_infos.append("%s\t%s" % ("0", "CPU"))
    set_gpu_numbers.add(0)
    default_batch_size = int(psutil.virtual_memory().total/ 1024 / 1024 / 1024 / 2)
gpus = "-".join([i[0] for i in gpu_infos])
default_gpu_numbers=str(sorted(list(set_gpu_numbers))[0])
def fix_gpu_number(input):#将越界的number强制改到界内
    try:
        if(int(input)not in set_gpu_numbers):return default_gpu_numbers
    except:return input
    return input
def fix_gpu_numbers(inputs):
    output=[]
    try:
        for input in inputs.split(","):output.append(str(fix_gpu_number(input)))
        return ",".join(output)
    except:
        return inputs


p_train_SoVITS=None
def open1Ba(
    batch_size,
    total_epoch,
    exp_root,
    exp_name,
    exp_dir_weight,
    is_half,
    text_low_lr_rate,
    if_save_latest,
    if_save_every_weights,
    save_every_epoch,
    gpu_numbers1Ba,
    pretrained_s2G,
    pretrained_s2D
):
    global p_train_SoVITS
    if(p_train_SoVITS==None):
        with open(f"GPT_SoVITS/configs/s2.json")as f:
            data=f.read()
            data=json.loads(data)
        s2_dir="%s/%s"%(exp_root,exp_name)
        os.makedirs("%s/logs_s2"%(s2_dir),exist_ok=True)
        if(is_half==False):
            data["train"]["fp16_run"]=False
            batch_size=max(1,batch_size//2)
        data["train"]["batch_size"]=batch_size
        data["train"]["epochs"]=total_epoch
        data["train"]["text_low_lr_rate"]=text_low_lr_rate
        data["train"]["pretrained_s2G"]=pretrained_s2G
        data["train"]["pretrained_s2D"]=pretrained_s2D
        data["train"]["if_save_latest"]=if_save_latest
        data["train"]["if_save_every_weights"]=if_save_every_weights
        data["train"]["save_every_epoch"]=save_every_epoch
        data["train"]["gpu_numbers"]=gpu_numbers1Ba
        data["data"]["exp_dir"]=data["s2_ckpt_dir"]=s2_dir
        data["save_weight_dir"]=exp_dir_weight
        data["name"]=exp_name
        tmp_config_path="%s/tmp_s2.json"%tmp
        with open(tmp_config_path,"w")as f:f.write(json.dumps(data))

        cmd = f'"{python_exec}" "GPT_SoVITS/s2_train.py" --config "{tmp_config_path}"'
        print("SoVITS训练开始：%s"%cmd) #yield "SoVITS训练开始：%s"%cmd,{"__type__":"update","visible":False},{"__type__":"update","visible":True}
        print(cmd)
        p_train_SoVITS = Popen(cmd, shell=True)
        p_train_SoVITS.wait()
        p_train_SoVITS=None
        print("SoVITS训练完成") #yield "SoVITS训练完成",{"__type__":"update","visible":True},{"__type__":"update","visible":False}
    else:
        print("已有正在进行的SoVITS训练任务，需先终止才能开启下一次任务") #yield "已有正在进行的SoVITS训练任务，需先终止才能开启下一次任务",{"__type__":"update","visible":False},{"__type__":"update","visible":True}


p_train_GPT=None
def open1Bb(
    batch_size,
    total_epoch,
    exp_root,
    exp_name,
    exp_dir_weight,
    is_half,
    if_dpo,
    if_save_latest,
    if_save_every_weights,
    save_every_epoch,
    gpu_numbers,
    pretrained_s1
):
    global p_train_GPT
    if(p_train_GPT==None):
        with open(f"GPT_SoVITS/configs/s1longer.yaml")as f:
            data=f.read()
            data=yaml.load(data, Loader=yaml.FullLoader)
        s1_dir="%s/%s"%(exp_root,exp_name)
        os.makedirs("%s/logs_s1"%(s1_dir),exist_ok=True)
        if(is_half==False):
            data["train"]["precision"]="32"
            batch_size = max(1, batch_size // 2)
        data["train"]["batch_size"]=batch_size
        data["train"]["epochs"]=total_epoch
        data["pretrained_s1"]=pretrained_s1
        data["train"]["save_every_n_epoch"]=save_every_epoch
        data["train"]["if_save_every_weights"]=if_save_every_weights
        data["train"]["if_save_latest"]=if_save_latest
        data["train"]["if_dpo"]=if_dpo
        data["train"]["half_weights_save_dir"]=exp_dir_weight
        data["train"]["exp_name"]=exp_name
        data["train_semantic_path"]="%s/6-name2semantic.tsv"%s1_dir
        data["train_phoneme_path"]="%s/2-name2text.txt"%s1_dir
        data["output_dir"]="%s/logs_s1"%s1_dir

        os.environ["_CUDA_VISIBLE_DEVICES"]=fix_gpu_numbers(gpu_numbers.replace("-",","))
        os.environ["hz"]="25hz"
        tmp_config_path="%s/tmp_s1.yaml"%tmp
        with open(tmp_config_path, "w") as f:f.write(yaml.dump(data, default_flow_style=False))

        # cmd = '"%s" GPT_SoVITS/s1_train.py --config_file "%s" --train_semantic_path "%s/6-name2semantic.tsv" --train_phoneme_path "%s/2-name2text.txt" --output_dir "%s/logs_s1"'%(python_exec,tmp_config_path,s1_dir,s1_dir,s1_dir)
        cmd = f'"{python_exec}" "GPT_SoVITS/s1_train.py" --config_file "{tmp_config_path}"'
        print("GPT训练开始：%s"%cmd) #yield "GPT训练开始：%s"%cmd,{"__type__":"update","visible":False},{"__type__":"update","visible":True}
        print(cmd)
        p_train_GPT = Popen(cmd, shell=True)
        p_train_GPT.wait()
        p_train_GPT=None
        print("GPT训练完成") #yield "GPT训练完成",{"__type__":"update","visible":True},{"__type__":"update","visible":False}
    else:
        print("已有正在进行的GPT训练任务，需先终止才能开启下一次任务") #yield "已有正在进行的GPT训练任务，需先终止才能开启下一次任务",{"__type__":"update","visible":False},{"__type__":"update","visible":True}


def Train(
    FileList_Path: str = "GPT-SoVITS/raw/xxx.list",
    #Set_s1_Epochs: int = 8,
    #Set_s1_Save_Interval: int = 4,
    #Set_s2_Epochs: int = 15,
    #Set_s2_Save_Interval: int = 5,
    #Set_Batch_Size: Optional[int] = None,
    Set_FP16_Run: bool = False, # 16系卡没有半精度
    Model_Dir_Pretrained_bert: str = "GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large",
    Model_Dir_Pretrained_ssl: str = "GPT_SoVITS/pretrained_models/chinese-hubert-base",
    Model_Path_Pretrained_s1: str = "GPT_SoVITS/pretrained_models/s1bert25hz-2kh-longer-epoch=68e-step=50232.ckpt",
    Model_Path_Pretrained_s2G: str = "GPT_SoVITS/pretrained_models/s2G488k.pth",
    Model_Path_Pretrained_s2D: str = "GPT_SoVITS/pretrained_models/s2D488k.pth",
    Output_Root: str = "SoVITS_weights&GPT_weights",
    Output_DirName: str = "模型名",
    Output_LogDir: str = "logs"
):
    os.makedirs(Output_Root, exist_ok = True)
    # To absolut audio path & get audio dir
    with open(file = FileList_Path, mode = 'r', encoding = 'utf-8') as TextFile:
        Lines = TextFile.readlines()
    for Index, Line in enumerate(Lines):
        Line_Path, Line_SpeakerText = Line.split('|', maxsplit = 1)
        Line_Path = Path(FileList_Path).parent.joinpath(Line_Path).as_posix()# if not Path(Line_Path).is_absolute() else Line_Path
        Line = f"{Line_Path}|{Line_SpeakerText}"
        Lines[Index] = Line
    FileList_Path = Path(Output_Root).joinpath(Path(FileList_Path).name).as_posix()
    with open(file = FileList_Path, mode = 'w', encoding = 'utf-8') as TextFile:
        TextFile.writelines(Lines)
    Line_Path = Lines[0].split('|', maxsplit = 1)[0]
    assert Path(Line_Path).exists(), "请检查数据集是否为相对路径格式且音频在同一目录下"
    AudioDir = Path(Line_Path).parent.as_posix()
    # 1A-训练集格式化
    open1abc(
        inp_text = FileList_Path,
        inp_wav_dir = AudioDir,
        exp_root = Output_LogDir,
        exp_name = Output_DirName,
        is_half = Set_FP16_Run,
        gpu_numbers1a = "%s-%s"%(gpus, gpus),
        gpu_numbers1Ba = "%s-%s"%(gpus, gpus),
        gpu_numbers1c = "%s-%s"%(gpus, gpus),
        bert_pretrained_dir = Model_Dir_Pretrained_bert,
        ssl_pretrained_dir = Model_Dir_Pretrained_ssl,
        pretrained_s2G_path = Model_Path_Pretrained_s2G
    )
    # 1B-SoVITS训练
    open1Ba(
        batch_size = default_batch_size, #batch_size = default_batch_size if Set_Batch_Size is None else Set_Batch_Size,
        total_epoch = 8,
        exp_root = Output_LogDir,
        exp_name = Output_DirName,
        exp_dir_weight = Output_Root,
        is_half = Set_FP16_Run,
        text_low_lr_rate = 0.4,
        if_save_latest = True,
        if_save_every_weights = True,
        save_every_epoch = 4,
        gpu_numbers1Ba = "%s" % (gpus),
        pretrained_s2G = Model_Path_Pretrained_s2G,
        pretrained_s2D = Model_Path_Pretrained_s2D
    )
    # 1B-GPT训练
    open1Bb(
        batch_size = default_batch_size, #batch_size = default_batch_size if Set_Batch_Size is None else Set_Batch_Size,
        total_epoch = 15,
        exp_root = Output_LogDir,
        exp_name = Output_DirName,
        exp_dir_weight = Output_Root,
        is_half = Set_FP16_Run,
        if_dpo = False,
        if_save_latest = True,
        if_save_every_weights = True,
        save_every_epoch = 5,
        gpu_numbers = "%s" % (gpus),
        pretrained_s1 = Model_Path_Pretrained_s1
    )