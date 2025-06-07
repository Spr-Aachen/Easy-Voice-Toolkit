import os
import shutil
import json
import hashlib
import PyEasyUtils as EasyUtils
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

##############################################################################################################################

def getModelsInfo(manifestPath: str, modelsDir: str, modelsFormats: list):
    """
    view model
    """
    modelsInfo = {}
    os.makedirs(modelsDir, exist_ok = True)

    modelDicts_cloud = []
    tags = [Path(modelsDir).parts[-2], Path(modelsDir).parts[-1]]
    if not Path(manifestPath).exists():
        return []
    with open(EasyUtils.normPath(manifestPath), 'r', encoding = 'utf-8') as File:
        param = json.load(File)
    for modelDict in param["models"]:
        if modelDict["tags"] == tags:
            modelDicts_cloud.append(modelDict)
    def _getModelInfo_cloud(modelDict):
        if isinstance(modelDict["SHA"], dict):
            name = modelDict["name"]
            for Model, modelSHA in modelDict["SHA"].items():
                modelName = Model
                modelName, modelType = modelName.rsplit('.', 1)
                modelSize = modelDict["size"][Model]
                modelDate = modelDict["date"][Model]
                modelSHA = modelSHA
                modelURL = modelDict["downloadurl"][Model]
                modelDir = Path(modelsDir).joinpath("Downloaded", name)
                downloadParam = (modelURL, modelDir, modelName, Path(modelURL).suffix, modelSHA)
                modelsInfo[modelSHA] = [str(f"[{name}]{modelName}"), str(modelType), str(modelSize), str(modelDate), tuple(downloadParam)]
        else:
            modelName = modelDict["name"]
            modelName, modelType = modelName.rsplit('.', 1)
            modelSize = modelDict["size"]
            modelDate = modelDict["date"]
            modelSHA = modelDict["SHA"]
            modelURL = modelDict["downloadurl"]
            modelDir = Path(modelsDir).joinpath("Downloaded")
            downloadParam = (modelURL, modelDir, modelName, Path(modelURL).suffix, modelSHA)
            modelsInfo[modelSHA] = [str(modelName), str(modelType), str(modelSize), str(modelDate), tuple(downloadParam)]
    with ThreadPoolExecutor(max_workers = os.cpu_count()) as executor:
        executor.map(
            _getModelInfo_cloud,
            modelDicts_cloud
        ) if modelDicts_cloud is not None else None

    modelPaths_local = []
    for modelsFormat in modelsFormats:
        modelPaths_local_sep = EasyUtils.toIterable(EasyUtils.getPaths(modelsDir, modelsFormat))
        modelPaths_local_sep = [modelPath_local_sep for modelPath_local_sep in modelPaths_local_sep if modelPath_local_sep is not None and modelPath_local_sep.endswith(modelsFormat)]
        modelPaths_local.extend(modelPaths_local_sep) if modelPaths_local_sep is not None else None
    modelPaths_local = list(set(modelPaths_local))
    def _getModelInfo_local(modelPath):
        name = Path(modelPath).parts[-2] if Path(modelPath).parent.__str__() not in Path(modelsDir).joinpath("Downloaded").__str__() else None
        modelName = Path(modelPath).name
        modelName, modelType = modelName.rsplit('.', 1)
        modelSize = round(Path(modelPath).stat().st_size / (1024 ** 2), 1)
        modelDate = datetime.fromtimestamp(Path(modelPath).stat().st_mtime)
        with open(modelPath, "rb") as m:
            ModelBytes = m.read()
        modelSHA = hashlib.sha256(ModelBytes).hexdigest()
        modelDir = Path(modelPath).parent
        modelsInfo[modelSHA] = [str(f"[{name}]{modelName}" if name is not None else modelName), str(modelType), str(modelSize)+'MB', str(modelDate), str(modelDir)]
    with ThreadPoolExecutor(max_workers = os.cpu_count()) as executor:
        executor.map(
            _getModelInfo_local,
            modelPaths_local
        ) if modelPaths_local is not None else None

    return list(modelsInfo.values())


def downloadModel(downloadParams: tuple):
    """
    ClientFunc: download model
    """
    filePath = EasyUtils.downloadFile(*downloadParams, createNewConsole = True)[1]
    fileSuffix = Path(filePath).suffix
    shutil.unpack_archive(filePath, downloadParams[1], fileSuffix) if fileSuffix in ('zip', 'tar', 'gztar', 'bztar') else None


def addLocalModel(modelDir: str, modelPath: str, sector: list[str] = ['Tool', 'type']):
    """
    ClientFunc: add local model
    """
    moveToDst = EasyUtils.normPath(Path(modelDir).joinpath(*sector))
    shutil.move(modelPath, moveToDst)

##############################################################################################################################