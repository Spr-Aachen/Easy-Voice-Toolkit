<div align = "center">

# 简易语音工具箱<br>Easy Voice Toolkit

![Title](/docs/media/Title.png "Home Page")

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


## Description

### Overview

A toolkit based on open source voice projects，which provides a variety of automated audio tools including speech model training

Functions that are currently included in the toolkit are as follows:

- [Audio Processing](/docs/Audio-Processor.md)

- [Voice Recognition](/docs/Voice-Recognizer.md)

- [Voice Transcribing](/docs/Voice-Transcriber.md)

- [Dataset Creating (SRT Converting & WAV Splitting)](/docs/Dataset-Creator.md)

- [Model Training](/docs/Voice-Trainer.md)

- [Voice Convertion](/docs/Voice-Converter.md)

<br>These functions can be seamlessly integrated to form a complete workflow
<br>Users can use these tools selectively according to their own needs, or use them in sequence to gradually transform raw audio files into ideal speech models

### Acknowledgement

I'd like to express my sincere gratitude to the authors of the following projects, as their excellent work has contributed to the implementation of this toolkit

- [audio-slicer](https://github.com/openvpi/audio-slicer)
- [VoiceprintRecognition](https://github.com/yeyupiaoling/VoiceprintRecognition-Pytorch/tree/release/1.0)
- [whisper](https://github.com/openai/whisper)
- [SRT-to-CSV-and-audio-split](https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
- [vits](https://github.com/CjangCjengh/vits)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)


## Consideration

### System

Currently the UI interface only supports Windows system

### Language

Languages that are currently supported/unsupported by the tools are shown as follows:

<table border = "1">
    <tr>
        <th style = "text-align:center;">Tool</th>
        <th style = "text-align:center;">Chinese</th>
        <th style = "text-align:center;">English</th>
        <th style = "text-align:center;">Japnese</th>
    </tr>
    <tr>
        <th style = "text-align:center;">Audio Processor</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">Voice Recognizer</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">Voice Transcriber</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">DataSet Creator</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">Voice Trainer</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    </tr>
        <th style = "text-align:center;">Voice Converter</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
</table>


## Deployment

### Local Deployment - User

#### Download

You have two options：

- Download the [lightweight installer](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases/latest): small package comes with installation instructions, but without necessary environmental dependencies and models

- Download the [Ready-to-use portable package](https://pixeldrain.com/api/file/JLUJwfNA?download): huge package with all environmental dependencies and several model presets, need to unpack after download

#### Run

Just click on the .exe file or its shortcut

### Local Deployment - Developer

#### Setup Environment

Please make sure that you've installed [Python](https://www.python.org/downloads/) `version 3.8 or higher`

#### Obtain Project

- Clone Repository
    ```shell
    git clone https://github.com/Spr-Aachen/Easy-Voice-Toolkit.git
    ```

- Change directory
    ```shell
    %cd Easy-Voice-Toolkit
    ```

#### Install Dependencies

- Install pytorch (Command can be get from the [official site](https://pytorch.org/get-started/locally/))
    ```shell
    # e.g. (注意自己的cuda版本，这里以11.8为例)
    pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
    ```

- Install project requirements
    ```shell
    pip install -r requirements.txt
    ```

- Install GUI dependency
    ```shell
    pip install pyside6 QEasyWidgets pywin32==300 psutil pynvml darkdetect PyGithub
    ```

#### Run Programm

- Activate GUI
    ```shell
    Run.py
    ```

### Cloud Deployment

#### Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Spr-Aachen/EVT-Resources/blob/main/Easy_Voice_Toolkit_for_Colab.ipynb)
<br>Click to use the demo above, or access to Colab and upload [Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)


## Tested Devices

### Windows OS

#### Honor Hunter V700
- **Type**: Laptop
- **GPU**: GTX 1660Ti
- **CPU**: i5-10300H
- **RAM**: 16G
- **OS**: Win10
- **Python**: 3.9
- **Torch**: 2.0.1

#### (Waiting to add other devices)

### Linux OS

#### (Waiting to add other devices)


## FAQ

-   **Q**: What should I do if the client update / dependency download always fails or gives an error?
<br>**A**: Use a proxy or switch to the Ready-to-use portable package.

-   **Q**: There are many parameter settings that I don't know how to deal with, what should I do?
<br>**A**: Just use the default values.

-   **Q**: Free and open source ?
<br>**A**: Natürlich~♪


## Terms of Use

**Please solve the authorization problem of the dataset on your own. You shall be solely responsible for any problems caused by the use of non-authorized datasets for training and all consequences thereof.The repository and its maintainer have nothing to do with the consequences!**

1. This project is established for academic exchange purposes only and is intended for communication and learning purposes. It is not intended for production environments.

2. Any videos based on Easy Voice Toolkit that are published on video platforms must clearly indicate in the description that they are used for voice changing and specify the input source of the voice or audio, for example, using videos or audios published by others and separating the vocals as input source for conversion, which must provide clear original video links. If your own voice or other synthesized voices from other commercial vocal synthesis software are used as the input source for conversion, you must also explain it in the description.

3. You shall be solely responsible for any infringement problems caused by the input source. When using other commercial vocal synthesis software as input source, please ensure that you comply with the terms of use of the software. Note that many vocal synthesis engines clearly state in their terms of use that they cannot be used for input source conversion.

4. Continuing to use this project is deemed as agreeing to the relevant provisions stated in this repository README. This repository README has the obligation to persuade, and is not responsible for any subsequent problems that may arise.

5. If you distribute this repository's code or publish any results produced by this project publicly (including but not limited to video sharing platforms), please indicate the original author and code source (this repository).

6. If you use this project for any other plan, please contact and inform the author of this repository in advance. Thank you very much.

Reference: [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)


## Contact Details

[![QQ](https://img.shields.io/badge/QQ-2835946988-brightgreen?style=for-the-badge&logo=tencent-qq&logoColor=white)]()
<br>Please feel free to contact me at any time, any comments and suggestions will be appreciated:)


## Stargazers over time

[![Stargazers over time](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit.svg)](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit)