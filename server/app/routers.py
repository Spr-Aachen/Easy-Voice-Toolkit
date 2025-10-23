from fastapi import APIRouter, Request
from fastapi.responses import Response, JSONResponse, StreamingResponse
from PyEasyUtils import getBaseDir, getCurrentPath, evalString

from tools import AudioProcessor, VPR, Whisper, GPT_SoVITS

##############################################################################################################################

currentDir = getBaseDir(getCurrentPath())


audioProcessor = AudioProcessor()
voiceIdentifier = VPR()
whisper = Whisper()
gptsovits = GPT_SoVITS()

##############################################################################################################################

router = APIRouter(
    prefix = "",
)


@router.get("/processAudio")
async def processAudio(request: Request, terminate: bool = False):
    reqJs: dict = await request.json()
    if evalString(terminate):
        audioProcessor.terminate_processAudio()
        return
    contentStream = audioProcessor.processAudio(
        inputDir = reqJs.get("inputDir"),
        outputFormat = reqJs.get("outputFormat"),
        sampleRate = reqJs.get("sampleRate"),
        sampleWidth = reqJs.get("sampleWidth"),
        toMono = reqJs.get("toMono"),
        denoiseAudio = reqJs.get("denoiseAudio"),
        denoiseModelPath = reqJs.get("denoiseModelPath"),
        denoiseTarget = reqJs.get("denoiseTarget"),
        sliceAudio = reqJs.get("sliceAudio"),
        rmsThreshold = reqJs.get("rmsThreshold"),
        audioLength = reqJs.get("audioLength"),
        silentInterval = reqJs.get("silentInterval"),
        hopSize = reqJs.get("hopSize"),
        silenceKept = reqJs.get("silenceKept"),
        outputRoot = reqJs.get("outputRoot"),
        outputDirName = reqJs.get("outputDirName"),
    )
    return StreamingResponse(
        content = contentStream,
        media_type = "text/plain"
    )


@router.get("/vpr_infer")
async def vpr_infer(request: Request, terminate: bool = False):
    reqJs: dict = await request.json()
    if evalString(terminate):
        voiceIdentifier.terminate_infer()
        return
    contentStream = voiceIdentifier.infer(
        stdAudioSpeaker = reqJs.get("stdAudioSpeaker"),
        audioDirInput = reqJs.get("audioDirInput"),
        modelPath = reqJs.get("modelPath"),
        modelType = reqJs.get("modelType"),
        featureMethod = reqJs.get("featureMethod"),
        decisionThreshold = reqJs.get("decisionThreshold"),
        audioDuration = reqJs.get("audioDuration"),
        outputRoot = reqJs.get("outputRoot"),
        outputDirName = reqJs.get("outputDirName"),
        audioSpeakersDataName = reqJs.get("audioSpeakersDataName"),
    )
    return StreamingResponse(
        content = contentStream,
        media_type = "text/plain"
    )


@router.get("/asr_infer")
async def asr_infer(request: Request, terminate: bool = False):
    reqJs: dict = await request.json()
    if evalString(terminate):
        whisper.terminate_infer()
        return
    contentStream = whisper.infer(
        modelPath = reqJs.get("modelPath"),
        audioDir = reqJs.get("audioDir"),
        verbose = reqJs.get("verbose"),
        addLanguageInfo = reqJs.get("addLanguageInfo"),
        conditionOnPreviousText = reqJs.get("conditionOnPreviousText"),
        fp16 = reqJs.get("fp16"),
        outputRoot = reqJs.get("outputRoot"),
        outputDirName = reqJs.get("outputDirName"),
    )
    return StreamingResponse(
        content = contentStream,
        media_type = "text/plain"
    )


@router.get("/gptsovits_preprocess")
async def preprocess(request: Request, terminate: bool = False):
    reqJs: dict = await request.json()
    if evalString(terminate):
        gptsovits.terminate_preprocess()
        return
    contentStream = gptsovits.preprocess(
        srtDir = reqJs.get("srtDir"),
        audioSpeakersDataPath = reqJs.get("audioSpeakersDataPath"),
        dataFormat = reqJs.get("dataFormat"),
        outputRoot = reqJs.get("outputRoot"),
        outputDirName = reqJs.get("outputDirName"),
        fileListName = reqJs.get("fileListName"),
    )
    return StreamingResponse(
        content = contentStream,
        media_type = "text/plain"
    )


@router.get("/gptsovits_train")
async def train(request: Request, terminate: bool = False):
    reqJs: dict = await request.json()
    if evalString(terminate):
        gptsovits.terminate_train()
        return
    contentStream = gptsovits.train(
        version = reqJs.get("version"),
        fileList_path = reqJs.get("fileList_path"),
        modelDir_bert = reqJs.get("modelDir_bert"),
        modelDir_hubert = reqJs.get("modelDir_hubert"),
        modelPath_gpt = reqJs.get("modelPath_gpt"),
        modelPath_sovitsG = reqJs.get("modelPath_sovitsG"),
        modelPath_sovitsD = reqJs.get("modelPath_sovitsD"),
        half_precision = reqJs.get("half_precision"),
        if_grad_ckpt = reqJs.get("if_grad_ckpt"),
        lora_rank = reqJs.get("lora_rank"),
        output_root = reqJs.get("output_root"),
        output_dirName = reqJs.get("output_dirName"),
        output_logDir = reqJs.get("output_logDir"),
    )
    return StreamingResponse(
        content = contentStream,
        media_type = "text/plain"
    )


@router.get("/gptsovits_infer_webui")
async def infer_webui(request: Request, terminate: bool = False):
    reqJs: dict = await request.json()
    if evalString(terminate):
        gptsovits.terminate_infer_webui()
        return
    contentStream = gptsovits.infer_webui(
        version = reqJs.get("version"),
        sovits_path = reqJs.get("sovits_path"),
        sovits_v3_path = reqJs.get("sovits_v3_path"),
        gpt_path = reqJs.get("gpt_path"),
        cnhubert_base_path = reqJs.get("cnhubert_base_path"),
        bert_path = reqJs.get("bert_path"),
        bigvgan_path = reqJs.get("bigvgan_path"),
        half_precision = reqJs.get("half_precision"),
        batched_infer = reqJs.get("batched_infer"),
    )
    return StreamingResponse(
        content = contentStream,
        media_type = "text/plain"
    )

##############################################################################################################################