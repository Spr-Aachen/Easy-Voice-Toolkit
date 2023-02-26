'''
Added
'''

import os
import shutil
import urllib
from typing import Tuple, Union
from tqdm import tqdm


# Spect
ModelList_S = {
    #'tiny' : "",
    #'base' : "",
    'small': "https://github.com/Spr-Aachen/EVT-Resources/raw/main/Voiceprint%20Model/Ecapa-Tdnn/spectrogram/small.zip"
}
# MelSpect
ModelList_M = {
    #'tiny' : "",
    #'base' : "",
    'small': "https://github.com/Spr-Aachen/EVT-Resources/raw/main/Voiceprint%20Model/Ecapa-Tdnn/melspectrogram/small.zip"
}


def Model_Download(url: str, root: str, name: str, format: str) -> Tuple[Union[bytes, str], str]:
    
    os.makedirs(root, exist_ok = True)

    download_target = os.path.join(root, name) + '.' + format

    if os.path.exists(download_target):
        if os.path.isfile(download_target) == False:
            raise RuntimeError(f"{download_target} exists and is not a regular file")
        else:
            with open(download_target, "rb") as f:
                model_bytes = f.read()
    else:
        with urllib.request.urlopen(url) as source, open(download_target, "wb") as output:
            with tqdm(total=int(source.info().get("Content-Length")), ncols=80, unit='iB', unit_scale=True, unit_divisor=1024) as loop:
                while True:
                    buffer = source.read(8192)
                    if not buffer:
                        break

                    output.write(buffer)
                    loop.update(len(buffer))

        model_bytes = open(download_target, "rb").read()

    return model_bytes, download_target


def Execute_Model_Download(
    Model_Dir: str,
    Model_Type: str,
    Feature_Method: str,
    Model_Name: str
):
    URL = ModelList_S[Model_Name] if Feature_Method == 'spectrogram' else ModelList_M[Model_Name]
    DownloadDir = os.path.join(Model_Dir, "Temp")
    ExtractDir = os.path.join(Model_Dir, Model_Type, Feature_Method)
    Format = 'zip'
    try:
        shutil.unpack_archive(Model_Download(URL, DownloadDir, Model_Name, Format)[1], ExtractDir, Format)
    except:
        shutil.unpack_archive(Model_Download('https://ghproxy.com/' + URL, DownloadDir, Model_Name, Format)[1], ExtractDir, Format)