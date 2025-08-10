<div align = "center">

![Title](/docs/media/Title.png)

# Easy Voice Toolkit

A toolkit based on open source voice projects，which provides a variety of automated audio tools:
<br>[Audio Processing](/docs/EN/Audio-Processor.md), [Voice Recognition](/docs/EN/Voice-Recognizer.md), [Voice Transcription](/docs/EN/Voice-Transcriber.md), [Dataset Creating (For Voice Conversion)](/docs/EN/Dataset-Creator.md), [Model Training (For Voice Conversion)](/docs/EN/Voice-Trainer.md), and [Voice Conversion](/docs/EN/Voice-Converter.md)
<br>Users can use these tools selectively according to their own needs, or use them in sequence to gradually transform raw audio files into ideal speech models

[![Releases](https://img.shields.io/github/v/release/Spr-Aachen/Easy-Voice-Toolkit?color=green&label=Release&logo=Github&logoColor=white&style=for-the-badge)](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases/latest)&nbsp;
[![Bilibili](https://img.shields.io/badge/Bilibili-v1.0%20Intro-blue?logo=Bilibili&style=for-the-badge)](https://www.bilibili.com/video/BV1uJ4m157P2)&nbsp;
[![YouTube](https://img.shields.io/badge/YouTube-v1.0%20Intro-red?logo=YouTube&style=for-the-badge)](https://www.youtube.com/watch?v=)

</div>


<p align = "center">
    <a href = "https://ko-fi.com/spr_aachen">
        <img src = "https://cdn.ko-fi.com/cdn/kofi3.png?v=2" width = "150">
    </a>
</p>


<div align = "center">

[**简体中文**](./docs/README_CN.md) | **English**

</div>


## Acknowledgement

I'd like to express my sincere gratitude to the authors of the following projects, as their excellent work has contributed to the implementation of this toolkit

- [audio-slicer](https://github.com/openvpi/audio-slicer)
- [VoiceprintRecognition](https://github.com/yeyupiaoling/VoiceprintRecognition-Pytorch/tree/release/1.0)
- [whisper](https://github.com/openai/whisper)
- [SRT-to-CSV-and-audio-split](https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)


## User Guide

### Desktop Application

[![Download Windows Portable Version](https://img.shields.io/badge/Download-Windows%20Portable%20Version-yellow?logo=HuggingFace)](https://huggingface.co/SprAachen/Easy-Voice-Toolkit-Package/resolve/main/EVT_windows_x64.7z?download=true)

You have two options：

- Download the [lightweight installer](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases/latest): small package comes with installation instructions, but without necessary environmental dependencies and models

- Download the [Ready-to-use portable package for Windows](https://huggingface.co/SprAachen/Easy-Voice-Toolkit-Package/resolve/main/EVT_windows_x64.7z?download=true): huge package with all environmental dependencies and several model presets, need to unpack after download

### Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Spr-Aachen/Easy-Voice-Toolkit/blob/main/run.ipynb)
<br>Click to use the demo above, or access to Colab and upload [run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/run.ipynb)


## Developer Guide

### 1. Setup Environment

Please make sure that you've installed [Python](https://www.python.org/downloads/) `version 3.8 or higher`

### 2. Obtain Project

- Clone Repository
    ```shell
    git clone --recurse-submodules https://github.com/Spr-Aachen/Easy-Voice-Toolkit.git
    ```

- Change directory
    ```shell
    %cd Easy-Voice-Toolkit
    ```

### 3. Install Dependencies

- Install pytorch (Command can be get from the [official site](https://pytorch.org/get-started/locally/))
    ```shell
    # e.g. (Mind your cuda version，here we take 11.8 as an example)
    pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
    ```

- Install project requirements
    ```shell
    pip install -r requirements.txt
    ```

- Install [GUI dependency](https://github.com/Spr-Aachen/QEasyWidgets)
    ```shell
    pip install QEasyWidgets
    ```

### 4. Run Programm

- Start the client and server
    ```shell
    run.py
    ```


## Terms of Use

**Please solve the authorization problem of the dataset on your own. You shall be solely responsible for any problems caused by the use of non-authorized datasets for training and all consequences thereof.The repository and its maintainer have nothing to do with the consequences!**

1. This project is established for academic exchange purposes only and is intended for communication and learning purposes. It is not intended for production environments.

2. Any videos based on Easy Voice Toolkit that are published on video platforms must clearly indicate in the description that they are used for voice changing and specify the input source of the voice or audio, for example, using videos or audios published by others and separating the vocals as input source for conversion, which must provide clear original video links. If your own voice or other synthesized voices from other commercial vocal synthesis software are used as the input source for conversion, you must also explain it in the description.

3. You shall be solely responsible for any infringement problems caused by the input source. When using other commercial vocal synthesis software as input source, please ensure that you comply with the terms of use of the software. Note that many vocal synthesis engines clearly state in their terms of use that they cannot be used for input source conversion.

4. Continuing to use this project is deemed as agreeing to the relevant provisions stated in this repository README. This repository README has the obligation to persuade, and is not responsible for any subsequent problems that may arise.

5. If you distribute this repository's code or publish any results produced by this project publicly (including but not limited to video sharing platforms), please indicate the original author and code source (this repository).

6. If you use this project for any other plan, please contact and inform the author of this repository in advance. Thank you very much.

Reference: [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)


## FAQ

-   **Q**: What should I do if the client update / dependency download always fails or gives an error?
<br>**A**: Use a proxy or switch to the Ready-to-use portable package.

-   **Q**: There are many parameter settings that I don't know how to deal with, what should I do?
<br>**A**: Just use the default values.

-   **Q**: Free and open source ?
<br>**A**: Natürlich~♪


## Future Features

### ToDo
- Add chatbot (LLM) integration
- Refactor client with C++ (Qt)

### WIP
- Backend development
- Internationalization
- Add support for Linux OS


## Contact Details

[![QQ](https://img.shields.io/badge/QQ-2835946988-brightgreen?style=for-the-badge&logo=tencent-qq&logoColor=white)]()
<br>Feel free to contact me at any time, any comments and suggestions will be appreciated:)


## Stargazers over time

[![Stargazers over time](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit.svg)](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit)