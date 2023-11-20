'''
Added
'''

import os
import hashlib
import urllib
from typing import Tuple, Union
from tqdm import tqdm


# Spect
ModelList_S = {
    #'tiny' : "",
    #'base' : "",
    'small': "https://github.com/Spr-Aachen/EVT-Resources/raw/main/Voiceprint%20Model/Ecapa-Tdnn/spectrogram/small.pth"
}
SHA256List_S = {
    #'tiny' : "",
    #'base' : "",
    'small': "a7c689599e616f03a339bfd11a27ae7cf7a975ac1713c5b85564a70a2e0c469f"
}

# MelSpect
ModelList_M = {
    #'tiny' : "",
    #'base' : "",
    'small': "https://github.com/Spr-Aachen/EVT-Resources/raw/main/Voiceprint%20Model/Ecapa-Tdnn/melspectrogram/small.pth"
}
SHA256List_M = {
    #'tiny' : "",
    #'base' : "",
    'small': "812c2758805dc7e9d7c2a5b0cd87b342a081f4d9a20513e246a3281ccd8f9bb7"
}


def Model_Download(url: str, root: str, name: str, format: str, expected_sha256: str) -> Tuple[Union[bytes, str], str]:
    
    os.makedirs(root, exist_ok = True)

    download_target = os.path.join(root, name) + '.' + format

    def Download():
        with urllib.request.urlopen(url) as source, open(download_target, "wb") as output:
            with tqdm(total = int(source.info().get("Content-Length")), ncols = 80, unit = 'iB', unit_scale = True, unit_divisor = 1024) as loop:
                while True:
                    buffer = source.read(8192)
                    if not buffer:
                        break
                    output.write(buffer)
                    loop.update(len(buffer))
        return open(download_target, "rb").read()

    if os.path.exists(download_target):
        if os.path.isfile(download_target) == False:
            raise RuntimeError(f"{download_target} exists and is not a regular file")
        else:
            with open(download_target, "rb") as f:
                model_bytes = f.read()
            Download() if hashlib.sha256(model_bytes).hexdigest() != expected_sha256 else None
    else:
        model_bytes = Download()

    return model_bytes, download_target


def Execute_Model_Download(
    Model_Dir: str,
    Model_Type: str,
    Feature_Method: str,
    Model_Name: str
):
    URL = ModelList_S[Model_Name] if Feature_Method == 'spectrogram' else ModelList_M[Model_Name]
    DownloadDir = os.path.join(Model_Dir, Model_Type, Feature_Method)
    Format = 'pth'
    SHA = SHA256List_S[Model_Name] if Feature_Method == 'spectrogram' else SHA256List_M[Model_Name]
    Model_Download(
        url = URL,
        root = DownloadDir,
        name = Model_Name,
        format = Format,
        expected_sha256 = SHA
    )[1]