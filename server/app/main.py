import os, sys
import argparse
import random
import time
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from PyEasyUtils import isPortAvailable, findAvailablePorts, getFileInfo, terminateProcess
from typing import Union, Optional, List

from utils import infoLogger, errorLogger
from routers import router

##############################################################################################################################

# Ref: https://github.com/pallets/click/issues/2415
_, isFileCompiled = getFileInfo()
sys.stdin = open(os.devnull, 'w') if isFileCompiled else sys.stdin
sys.stdout = open(os.devnull, 'w') if isFileCompiled else sys.stdin

##############################################################################################################################

parser = argparse.ArgumentParser()
parser.add_argument("--host", help = "主机地址", type = str, default = "localhost")
parser.add_argument("--port", help = "端口",     type = int, default = 8080)
args = parser.parse_known_args()[0]

host = args.host
port = args.port if isPortAvailable(args.port) else random.choice(findAvailablePorts((8000, 8080)))

##############################################################################################################################

app = FastAPI()

app.include_router(router)

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


@app.middleware("http")
async def log(request: Request, call_next):
    startTime = time.perf_counter()
    infoLogger.info(f"INFO: {request.method} {request.url}")

    try:
        response = await call_next(request)
        infoLogger.info(f"INFO: {request.method} {request.url} {response.status_code} - ProcessTime: {(time.perf_counter() - startTime):.3f}sec")
        return response

    except Exception as e:
        errorLogger.error(f"INFO: {request.method} {request.url} {response.status_code} - ProcessTime: {(time.perf_counter() - startTime):.3f}sec")
        errorLogger.error(f"ERROR: {str(e)}")
        raise e

##############################################################################################################################

if __name__ == "__main__":
    uvicorn.run(app = app, host = host, port = port)

##############################################################################################################################