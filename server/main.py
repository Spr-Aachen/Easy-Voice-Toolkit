import os, sys
import argparse
import random
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from PyEasyUtils import isPortAvailable, findAvailablePorts, terminateProcess
from typing import Union, Optional, List
from pathlib import Path

from tools import AudioProcessor, VPR, Whisper, GPT_SoVITS

##############################################################################################################################

currentDir = Path(sys.argv[0]).parent.as_posix()

toolDir = currentDir

##############################################################################################################################

parser = argparse.ArgumentParser()
parser.add_argument("--host", help = "主机地址", type = str, default = "localhost")
parser.add_argument("--port", help = "端口",     type = int, default = 8080)
args = parser.parse_known_args()[0]

host = args.host
port = args.port if isPortAvailable(args.port) else random.choice(findAvailablePorts((8000, 8080)))

##############################################################################################################################

audioProcessor = AudioProcessor(toolDir)
voiceIdentifier = VPR(toolDir)
whisper = Whisper(toolDir)
gptsovits = GPT_SoVITS(toolDir)

##############################################################################################################################

app = FastAPI()

app.add_middleware(
    middleware_class = CORSMiddleware,
    allow_origins = ["*"],
    allow_origin_regex = None,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
    expose_headers = ["*"],
    max_age = 600,
)


server = uvicorn.Server(uvicorn.Config(app))


@app.get("/")
async def default():
    return "Welcome!"


@app.post("/shutdown")
async def shutdown():
    server.should_exit = True
    terminateProcess(os.getpid())


@app.get("/processAudio")
async def processAudio(request: Request):
    reqJs: dict = await request.json()
    audioProcessor.processAudio(
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
    audioProcessor.terminate()


@app.get("/vpr_infer")
async def vpr_infer(request: Request):
    reqJs: dict = await request.json()
    voiceIdentifier.infer(
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
    voiceIdentifier.terminate()


@app.get("/asr_infer")
async def asr_infer(request: Request):
    reqJs: dict = await request.json()
    whisper.infer(
        modelPath = reqJs.get("modelPath"),
        audioDir = reqJs.get("audioDir"),
        verbose = reqJs.get("verbose"),
        addLanguageInfo = reqJs.get("reqaddLanguageInfo"),
        conditionOnPreviousText = reqJs.get("conditionOnPreviousText"),
        fp16 = reqJs.get("fp16"),
        outputRoot = reqJs.get("outputRoot"),
        outputDirName = reqJs.get("outputDirName"),
    )
    whisper.terminate()


@app.get("/gptsovits_preprocess")
async def preprocess(request: Request):
    reqJs: dict = await request.json()
    gptsovits.preprocess(
        srtDir = reqJs.get("srtDir"),
        audioSpeakersDataPath = reqJs.get("audioSpeakersDataPath"),
        dataFormat = reqJs.get("dataFormat"),
        outputRoot = reqJs.get("outputRoot"),
        outputDirName = reqJs.get("outputDirName"),
        fileListName = reqJs.get("fileListName"),
    )
    gptsovits.terminate()


@app.get("/gptsovits_train")
async def train(request: Request):
    reqJs: dict = await request.json()
    gptsovits.train(
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
    gptsovits.terminate()


@app.get("/gptsovits_infer_webui")
async def infer_webui(request: Request):
    reqJs: dict = await request.json()
    gptsovits.infer_webui(
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
    gptsovits.terminate()

##############################################################################################################################

if __name__ == "__main__":
    uvicorn.run(app = app, host = host, port = port)

##############################################################################################################################