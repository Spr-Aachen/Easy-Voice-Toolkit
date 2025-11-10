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
        fileList_path = reqJs.get("fileList_path", ""),
        modelPath_gpt = reqJs.get("modelPath_gpt", ""),
        modelPath_sovitsG = reqJs.get("modelPath_sovitsG", ""),
        modelPath_sovitsD = reqJs.get("modelPath_sovitsD", ""),
        modelPath_sv = reqJs.get("modelPath_sv", ""),
        modelDir_bert = reqJs.get("modelDir_bert", ""),
        modelDir_hubert = reqJs.get("modelDir_hubert", ""),
        modelDir_g2pw = reqJs.get("modelDir_g2pw", ""),
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
        sovits_path = reqJs.get("sovits_path", ""),
        sovits_v3_path = reqJs.get("sovits_v3_path", ""),
        sovits_v4_path = reqJs.get("sovits_v4_path", ""),
        gpt_path = reqJs.get("gpt_path", ""),
        cnhubert_base_path = reqJs.get("cnhubert_base_path", ""),
        bert_path = reqJs.get("bert_path", ""),
        bigvgan_path = reqJs.get("bigvgan_path", ""),
        vocoder_path = reqJs.get("vocoder_path", ""),
        sv_path = reqJs.get("sv_path", ""),
        g2pw_path = reqJs.get("g2pw_path", ""),
        half_precision = reqJs.get("half_precision"),
        batched_infer = reqJs.get("batched_infer"),
    )
    return StreamingResponse(
        content = contentStream,
        media_type = "text/plain"
    )


# @router.get("/gptsovits_infer_init")
# async def infer_init(request: Request, terminate: bool = False):
#     reqJs: dict = await request.json()
#     gptsovits.start()
#     if evalString(terminate):
#         gptsovits.terminate_infer_init()
#         return
#     contentStream = gptsovits.infer_init(
#         sovits_path = reqJs.get("sovits_path", ""),
#         sovits_v3_path = reqJs.get("sovits_v3_path", ""),
#         sovits_v4_path = reqJs.get("sovits_v4_path", ""),
#         gpt_path = reqJs.get("gpt_path", ""),
#         cnhubert_base_path = reqJs.get("cnhubert_base_path", ""),
#         bert_path = reqJs.get("bert_path", ""),
#         bigvgan_path = reqJs.get("bigvgan_path", ""),
#         vocoder_path = reqJs.get("vocoder_path", ""),
#         sv_path = reqJs.get("sv_path", ""),
#         g2pw_path = reqJs.get("g2pw_path", ""),
#         refer_wav_path = reqJs.get("refer_wav_path", ""),
#         prompt_text = reqJs.get("prompt_text"),
#         prompt_language = reqJs.get("prompt_language"),
#         device = reqJs.get("device"),
#         half_precision = reqJs.get("half_precision"),
#         media_type = reqJs.get("media_type"),
#         sub_type = reqJs.get("sub_type"),
#         stream_mode = reqJs.get("stream_mode"),
#     )
#     return StreamingResponse(
#         content = contentStream,
#         media_type = "text/plain"
#     )


# @router.get("/gptsovits_infer_handle")
# async def infer_handle(request: Request, terminate: bool = False):
#     reqJs: dict = await request.json()
#     if evalString(terminate):
#         gptsovits.terminate_infer_handle()
#         return
#     upstreamResponse = await gptsovits.infer_handle(
#         refer_wav_path = reqJs.get("refer_wav_path", ""),
#         prompt_text = reqJs.get("prompt_text"),
#         prompt_language = reqJs.get("prompt_language"),
#         inp_refs = reqJs.get("inp_refs"),
#         text = reqJs.get("text"),
#         text_language = reqJs.get("text_language"),
#         cut_punc = reqJs.get("cut_punc"),
#         top_k = reqJs.get("top_k"),
#         top_p = reqJs.get("top_p"),
#         temperature = reqJs.get("temperature"),
#         speed = reqJs.get("speed"),
#         sample_steps = reqJs.get("sample_steps"),
#         if_sr = reqJs.get("if_sr"),
#     )
#     return StreamingResponse(
#         upstreamResponse.aiter_bytes(),
#         media_type = upstreamResponse.headers.get("content-type", "audio/wav"),
#     )

##############################################################################################################################