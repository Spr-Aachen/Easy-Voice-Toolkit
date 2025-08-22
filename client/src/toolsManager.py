import os
import sys
import shutil
import json
import PyEasyUtils as EasyUtils
from glob import glob
from pathlib import Path
from typing import Union, Optional, Any
from PySide6.QtCore import QObject, Signal

from functions import FunctionSignals

##############################################################################################################################

class CustomSignals_Tools(QObject):
    '''
    Set up signals for functions
    '''
    serverStarted = Signal()
    serverEnded = Signal()

toolSignals = CustomSignals_Tools()


host = None
port = None
subprocessMonitor = None
logPath = None

def startServer(
    filePath: str,
    logOutputPath: str
):
    """
    """
    global host, port, subprocessMonitor, logPath
    host = "localhost"
    port = EasyUtils.findAvailablePorts((8000, 8080), host)[0]
    args = EasyUtils.mkPyFileCommand(
        filePath,
        host = host,
        port = port,
    )
    spm = EasyUtils.subprocessManager(shell = True)
    FunctionSignals.Signal_ForceQuit.connect(
        lambda: (
            EasyUtils.terminateProcess(spm.subprocesses[-1].pid),
            toolSignals.serverEnded.emit()
        )
    )
    spm.create(args, env = os.environ)
    subprocessMonitor = spm.monitor(logPath = logOutputPath)
    isServerStarted = False
    for outputLine, errorLine in subprocessMonitor:
        if f"{host}:{port}" in outputLine.decode(errors = 'ignore'):
            isServerStarted = True
            toolSignals.serverStarted.emit()
        yield isServerStarted
        if isServerStarted:
            break
    logPath = logOutputPath


def sendRequest(
    reqMethod: EasyUtils.requestManager,
    protocol: str,
    host: str,
    port: int,
    pathParams: Union[str, list[str], None] = None,
    queryParams: Union[str, list[str], None] = None,
    stream: bool = False,
    **reqParams,
):
    """
    """
    payload = reqParams
    with reqMethod.request(protocol, host, port, pathParams, queryParams, None, json.dumps(payload), stream) as response:
        if response.status_code == 200:
            for parsed_content, status_code in EasyUtils.responseParser(response, stream, decodeUnicode = True):
                result = parsed_content
                yield result, status_code
        else:
            yield "Request failed", response.status_code
            return

##############################################################################################################################

class Tool_AudioProcessor(QObject):
    '''
    Start audio processing
    '''
    def __init__(self):
        super().__init__()

    def processAudio(self,
        inputDir: str,
        outputFormat: Optional[str] = 'wav',
        sampleRate: Optional[Union[int, str]] = None,
        sampleWidth: Optional[Union[int, str]] = None,
        toMono: bool = False,
        denoiseAudio: bool = True,
        denoiseModelPath: str = "",
        denoiseTarget: str = '',
        sliceAudio: bool = True,
        rmsThreshold: float = -40.,
        audioLength: int = 5000,
        silentInterval: int = 300,
        hopSize: int = 10,
        silenceKept: int = 1000,
        outputRoot: str = "./",
        outputDirName: str = "",
    ):
        output, error = "", ""
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/processAudio", "terminate=False", stream = True,
            inputDir = inputDir,
            outputFormat = outputFormat,
            sampleRate = sampleRate,
            sampleWidth = sampleWidth,
            toMono = toMono,
            denoiseAudio = denoiseAudio,
            denoiseModelPath = denoiseModelPath,
            denoiseTarget = denoiseTarget,
            sliceAudio = sliceAudio,
            rmsThreshold = rmsThreshold,
            audioLength = audioLength,
            silentInterval = silentInterval,
            hopSize = hopSize,
            silenceKept = silenceKept,
            outputRoot = outputRoot,
            outputDirName = outputDirName,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)
            output += outputLine
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate_processAudio(self):
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/processAudio", "terminate=True", stream = True,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)


class Tool_VPR(QObject):
    '''
    Start VPR inferencing
    '''
    def __init__(self):
        super().__init__()

    def infer(self,
        stdAudioSpeaker: dict,
        audioDirInput: str,
        modelPath: str = './Models/.pth',
        modelType: str = 'Ecapa-Tdnn',
        featureMethod: str = 'melspectrogram',
        decisionThreshold: float = 0.6,
        audioDuration: float = 4.2,
        outputRoot: str = "./",
        outputDirName: str = "",
        audioSpeakersDataName: str = "AudioSpeakerData",
    ):
        output, error = "", ""
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/vpr_infer", "terminate=False", stream = True,
            stdAudioSpeaker = stdAudioSpeaker,
            audioDirInput = audioDirInput,
            modelPath = modelPath,
            modelType = modelType,
            featureMethod = featureMethod,
            decisionThreshold = decisionThreshold,
            audioDuration = audioDuration,
            outputRoot = outputRoot,
            outputDirName = outputDirName,
            audioSpeakersDataName = audioSpeakersDataName,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)
            output += outputLine
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate_infer(self):
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/vpr_infer", "terminate=True", stream = True,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)


class Tool_Whisper(QObject):
    '''
    Start Whisper transcribing
    '''
    def __init__(self):
        super().__init__()

    def infer(self,
        modelPath: str = './Models/.pt',
        audioDir: str = './WAV_Files',
        verbose: Any = True,
        addLanguageInfo: bool = True,
        conditionOnPreviousText: Any = False,
        fp16: Any = True,
        outputRoot: str = './',
        outputDirName: str = 'SRT_Files'
    ):
        output, error = "", ""
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/asr_infer", "terminate=False", stream = True,
            modelPath = modelPath,
            audioDir = audioDir,
            verbose = verbose,
            addLanguageInfo = addLanguageInfo,
            conditionOnPreviousText = conditionOnPreviousText,
            fp16 = fp16,
            outputRoot = outputRoot,
            outputDirName = outputDirName,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)
            output += outputLine
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate_infer(self):
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/asr_infer", "terminate=True", stream = True,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)


class Tool_GPTSoVITS(QObject):
    '''
    Start GPTSoVITS preprocessing
    '''
    def __init__(self):
        super().__init__()

    def preprocess(self,
        srtDir: str,
        audioSpeakersDataPath: str,
        dataFormat: str = 'PATH|NAME|LANG|TEXT',
        outputRoot: str = "./",
        outputDirName: str = "",
        fileListName: str = 'FileList'
    ):
        output, error = "", ""
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/gptsovits_preprocess", "terminate=False", stream = True,
            srtDir = srtDir,
            audioSpeakersDataPath = audioSpeakersDataPath,
            dataFormat = dataFormat,
            outputRoot = outputRoot,
            outputDirName = outputDirName,
            fileListName = fileListName,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)
            output += outputLine
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate_preprocess(self):
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/gptsovits_preprocess", "terminate=True", stream = True,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)

    def train(self,
        version: str = "v3",
        fileList_path: str = "GPT-SoVITS/raw/xxx.list",
        modelDir_bert: str = "GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large",
        modelDir_hubert: str = "GPT_SoVITS/pretrained_models/chinese-hubert-base",
        modelPath_gpt: str = "GPT_SoVITS/pretrained_models/s1bert25hz-5kh-longer-epoch=12-step=369668.ckpt",
        modelPath_sovitsG: str = "GPT_SoVITS/pretrained_models/s2G2333k.pth",
        modelPath_sovitsD: str = "GPT_SoVITS/pretrained_models/s2D2333k.pth",
        half_precision: bool = False, # 16系卡没有半精度
        if_grad_ckpt: bool = False, # v3是否开启梯度检查点节省显存占用
        lora_rank: int = 32, # Lora秩 choices=[16, 32, 64, 128]
        output_root: str = "SoVITS_weights&GPT_weights",
        output_dirName: str = "模型名",
        output_logDir: str = "logs",
    ):
        output, error = "", ""
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/gptsovits_train", "terminate=False", stream = True,
            version = version,
            fileList_path = fileList_path,
            modelDir_bert = modelDir_bert,
            modelDir_hubert = modelDir_hubert,
            modelPath_gpt = modelPath_gpt,
            modelPath_sovitsG = modelPath_sovitsG,
            modelPath_sovitsD = modelPath_sovitsD,
            half_precision = half_precision,
            if_grad_ckpt = if_grad_ckpt,
            lora_rank = lora_rank,
            output_root = output_root,
            output_dirName = output_dirName,
            output_logDir = output_logDir,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)
            output += outputLine
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate_train(self):
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/gptsovits_train", "terminate=True", stream = True,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)

    def infer_webui(self,
        version: str = "v3",
        sovits_path: str = ...,
        sovits_v3_path: str = ...,
        gpt_path: str = ...,
        cnhubert_base_path: str = ...,
        bert_path: str = ...,
        bigvgan_path: str = ...,
        half_precision: bool = True,
        batched_infer: bool = False,
    ):
        output, error = "", ""
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/gptsovits_infer_webui", "terminate=False", stream = True,
            version = version,
            sovits_path = sovits_path,
            sovits_v3_path = sovits_v3_path,
            gpt_path = gpt_path,
            cnhubert_base_path = cnhubert_base_path,
            bert_path = bert_path,
            bigvgan_path = bigvgan_path,
            half_precision = half_precision,
            batched_infer = batched_infer,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)
            output += outputLine
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate_infer_webui(self):
        for outputLine, status_code in sendRequest(
            EasyUtils.requestManager.Get, "http", host, port, "/gptsovits_infer_webui", "terminate=True", stream = True,
        ):
            with open(logPath, mode = 'a', encoding = 'utf-8') as log:
                log.write(outputLine)

##############################################################################################################################

def VPRResult_Get(audioSpeakersData_path: str):
    """
    GetVPRResult
    """
    AudioSpeakerSimList = []
    with open(audioSpeakersData_path, mode = 'r', encoding = 'utf-8') as AudioSpeakersData:
        AudioSpeakerSimLines = AudioSpeakersData.readlines()
    for AudioSpeakerSimLine in AudioSpeakerSimLines:
        AudioSpeakerSim = AudioSpeakerSimLine.strip().split('|')
        if len(AudioSpeakerSim) == 2:
            AudioSpeakerSim.append('')
        AudioSpeakerSimList.append(AudioSpeakerSim)
    return AudioSpeakerSimList


def VPRResult_Save(audioSpeakers: dict, audioSpeakersData_path: str, moveAudio: bool, moveToDst: Optional[str] = None):
    """
    SaveVPRResult
    """
    with open(audioSpeakersData_path, mode = 'w', encoding = 'utf-8') as AudioSpeakersData:
        Lines = []
        for Audio, Speaker in audioSpeakers.items():
            Speaker = Speaker.strip()
            if Speaker == '':
                continue
            if moveAudio:
                if moveToDst is None:
                    raise Exception("Destination shouldn't be 'None'")
                MoveToDst_Sub = EasyUtils.normPath(Path(moveToDst).joinpath(Speaker))
                os.makedirs(MoveToDst_Sub, exist_ok = True) if Path(MoveToDst_Sub).exists() == False else None
                Audio_Dst = EasyUtils.normPath(Path(MoveToDst_Sub).joinpath(Path(Audio).name).as_posix())
                shutil.copy(Audio, MoveToDst_Sub) if not Path(Audio_Dst).exists() else None
                Lines.append(f"{Audio_Dst}|{Speaker}\n")
            else:
                Lines.append(f"{Audio}|{Speaker}\n")
        AudioSpeakersData.writelines(Lines)


def ASRResult_Get(srtDir: str, audioDir: str):
    """
    GetASRResult
    """
    asrResult = {}
    for SRTFile in glob(EasyUtils.normPath(Path(srtDir).joinpath('*.srt'))):
        AudioFiles = glob(EasyUtils.normPath(Path(audioDir).joinpath('**', f'{Path(SRTFile).stem}.*')), recursive = True)
        if len(AudioFiles) == 0:
            continue
        with open(SRTFile, mode = 'r', encoding = 'utf-8') as SRT:
            SRTContent = SRT.read()
        asrResult[AudioFiles[0]] = SRTContent
    return asrResult


def ASRResult_Save(asrResult: dict, srtDir: str):
    """
    SaveASRResult
    """
    for AudioFile in asrResult.keys():
        SRTFiles = glob(EasyUtils.normPath(Path(srtDir).joinpath(f'{Path(AudioFile).stem}.*')))
        if len(SRTFiles) == 0:
            continue
        with open(SRTFiles[0], mode = 'w', encoding = 'utf-8') as SRT:
            SRT.write(asrResult[AudioFile])


def DATResult_Get(datPath: str):
    """
    GetDATResult
    """
    datResult = {}
    with open(datPath, mode = 'r', encoding = 'utf-8') as DAT:
        DATLines = DAT.readlines()
    for DATLine in DATLines:
        Audio = EasyUtils.normPath(Path(datPath).parent.joinpath(DATLine.split('|')[0]))
        datResult[Audio] = DATLine.strip()
    return datResult


def DATResult_Save(datResult: list, datPath: str):
    """
    SaveDATResult
    """
    with open(datPath, mode = 'w', encoding = 'utf-8') as DAT:
        DATLines = '\n'.join(datResult)
        DAT.write(DATLines)

##############################################################################################################################