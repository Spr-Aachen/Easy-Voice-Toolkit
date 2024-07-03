import os
import re
import argparse
import langdetect
#import IPython.display as ipd
import torch
from typing import Optional
from pathlib import Path
from scipy.io.wavfile import write
from datetime import datetime

from commons import intersperse
from utils import get_hparams, load_checkpoint, Get_Config_Path, Get_Model_Path
from models import SynthesizerTrn
from text import text_to_sequence
from text.symbols import symbols


if torch.cuda.is_available() is True:
    device = 'cuda:0'
else:
    device = 'cpu'


parser = argparse.ArgumentParser()
parser.add_argument("--Config_Path_Load", type = str, default = "...")
parser.add_argument("--Model_Path_Load", type = str, default = "...")
parser.add_argument("--Text", type = str, default = "请输入语句")
parser.add_argument("--Language", type = Optional[str], default = None)
parser.add_argument("--Speaker", type = str, default = "...")
parser.add_argument("--EmotionStrength", type = float, default = .667)
parser.add_argument("--PhonemeDuration", type = float, default = 0.8)
parser.add_argument("--SpeechRate", type = float, default = 1.)
parser.add_argument("--Audio_Path_Save", type = str, default = "audio.wav")
args = parser.parse_args()
#logging.info(str(args))

Config_Path_Load = Get_Config_Path(os.environ.get('FileList_Path_Training', args.Config_Path_Load))
Model_Path_Load = Get_Model_Path(os.environ.get('Model_Path_Load', args.Model_Path_Load))
Text = str(os.environ.get('Text', args.Text))
Language = str(os.environ.get('Language', args.Language))
Speaker = str(os.environ.get('Speaker', args.Speaker))
EmotionStrength = float(os.environ.get('EmotionStrength', args.EmotionStrength))
PhonemeDuration = float(os.environ.get('PhonemeDuration', args.PhonemeDuration))
SpeechRate = float(os.environ.get('SpeechRate', args.SpeechRate))
Audio_Path_Save = str(os.environ.get('Audio_Path_Save', args.Audio_Path_Save))

os.remove(Audio_Path_Save) if Path(Audio_Path_Save).exists() else os.makedirs(Path(Audio_Path_Save).parent.__str__(), exist_ok = True)


def Convert():
    hps = get_hparams(Config_Path_Load)

    net_g = SynthesizerTrn(
        len(symbols),
        80 if 'use_mel_posterior_encoder' in hps.model.keys() and hps.model.use_mel_posterior_encoder == True else hps.data.filter_length // 2 + 1,
        hps.train.segment_size // hps.data.hop_length,
        n_speakers=hps.data.n_speakers,
        **hps.model).to(device)
    _ = net_g.eval()

    _ = load_checkpoint(Model_Path_Load, net_g, None)

    def get_text(text, hps):
        text_norm = text_to_sequence(text, hps.data.text_cleaners)
        if hps.data.add_blank:
            text_norm = intersperse(text_norm, 0)
        text_norm = torch.LongTensor(text_norm)
        return text_norm

    def langdetector(text):  # from PolyLangVITS
        try:
            LangDict = {
                'zh-cn': 'ZH',
                'en':    'EN',
                'ja':    'JA'
            }
            Lang = LangDict.get(langdetect.detect(text).lower())
            return f'[{Lang}]{text}[{Lang}]'
        except Exception as e:
            raise Exception("Failed to detect language!")

    stn_tst = get_text(
        langdetector(re.sub(r"[\[\]\(\)\{\}]", "", Text)) if Language is not None else f"[{Language}]{Text}[{Language}]",
        hps
    )

    with torch.no_grad():
        x_tst = stn_tst.to(device).unsqueeze(0)
        x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).to(device)
        speakers = list(hps.speakers.keys()) if hasattr(hps.speakers, 'keys') else hps.speakers
        sid = torch.LongTensor([speakers.index(Speaker)]).to(device) if Speaker is not None else 0
        audio = net_g.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=EmotionStrength, noise_scale_w=PhonemeDuration, length_scale=SpeechRate)[0][0,0].data.cpu().float().numpy()
        write(os.path.normpath(Audio_Path_Save), hps.data.sampling_rate, audio) #ipd.display(ipd.Audio(audio, rate=hps.data.sampling_rate, normalize=False))


if __name__ == "__main__":
    Convert()