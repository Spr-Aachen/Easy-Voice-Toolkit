<div align = "center">

# 简易语音工具箱<br>Easy Voice Toolkit

![Title](/docs/media/Title.png "Home Page")

[![Releases](https://img.shields.io/github/v/release/Spr-Aachen/Easy-Voice-Toolkit?color=green&label=Release&logo=Github&logoColor=white&style=for-the-badge)](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases/latest)&nbsp;
[![Bilibili](https://img.shields.io/badge/Bilibili-v1.0%20Intro-blue?logo=Bilibili&style=for-the-badge)](https://www.bilibili.com/video/BV)&nbsp;
[![YouTube](https://img.shields.io/badge/YouTube-v1.0%20Intro-red?logo=YouTube&style=for-the-badge)](https://www.youtube.com/watch?v=)

</div>

<p align = "center">
    <a href = "https://ko-fi.com/spr_aachen">
        <img src = "https://cdn.ko-fi.com/cdn/kofi3.png?v=2" width = "150">
    </a>
</p>


## 项目介绍<br>Description

### 概述<br>Overview

一个基于开源语音项目实现的简易语音工具箱，提供了包括语音模型训练在内的多种自动化音频工具
<br>A toolkit based on open source voice projects，which provides a variety of automated audio tools including speech model training

<br>工具箱目前包含以下功能：
<br>Functions that are currently included in the toolkit are as follows:

- [音频处理](/docs/Audio-Processor.md)
<br>Audio Processing

- [语音识别](/docs/Voice-Recognizer.md)
<br>Voice Recognition

- [语音转录](/docs/Voice-Transcriber.md)
<br>Voice Transcribing

- [数据集制作](/docs/Dataset-Creator.md)
<br>Dataset Creating (SRT Converting & WAV Splitting)

- [模型训练](/docs/Voice-Trainer.md)
<br>Model Training

- [语音合成](/docs/Voice-Converter.md)
<br>Voice Convertion

<br>这些功能依次关联，能够形成一套完整的工作流
<br>These functions are independent of each other but seamlessly integrated to form a complete workflow
<br>用户可以根据自己的需求有选择性地使用，亦或者依次通过这些工具将未经处理的语音文件逐步变为理想的语音模型
<br>Users can use these tools selectively according to their own needs, or use them in sequence to gradually transform raw audio files into ideal speech models.

### 鸣谢<br>Acknowledgement

由衷感谢以下项目的作者，这个工具箱的实现正是得益于他们的优秀成果
<br>I'd like to express my sincere gratitude to the authors of the following projects, as their excellent work has contributed to the implementation of this toolkit

- [audio-slicer](https://github.com/openvpi/audio-slicer)
- [VoiceprintRecognition](https://github.com/yeyupiaoling/VoiceprintRecognition-Pytorch/tree/release/1.0)
- [whisper](https://github.com/openai/whisper)
- [SRT-to-CSV-and-audio-split](https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
- [vits](https://github.com/CjangCjengh/vits)


## 注意事项<br>Consideration

### 语言<br>Language

目前各个工具对语言的支持情况如下：
<br>Languages that are currently supported/unsupported by the tools are shown as follows:

<table border = "1">
    <tr>
        <th style = "text-align:center;">工具<br>Tool</th>
        <th style = "text-align:center;">中文<br>Chinese</th>
        <th style = "text-align:center;">英文<br>English</th>
        <th style = "text-align:center;">日文<br>Japnese</th>
    </tr>
    <tr>
        <th style = "text-align:center;">音频处理<br>Audio Processor</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音识别<br>Voice Recognizer</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音转录<br>Voice Transcriber</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">数据集制作<br>DataSet Creator</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">模型训练<br>Voice Trainer</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    </tr>
        <th style = "text-align:center;">语音合成<br>Voice Converter</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
</table>


## 项目部署<br>Deployment

### 本地部署 - 用户<br>Local Deployment - User

#### 下载<br>Download

您有两种选择：
<br>
- 下载[轻量化的安装程序](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases/latest)：包体小且拥有安装引导，但是未配置环境依赖且不带模型
<br>Download the [lightweight installer](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases/latest): small package comes with installation instructions, but without necessary environmental dependencies and models

- 下载[解压即用的懒人包]()：配置了所有环境依赖并附带有预设模型，但是包体较大且需要解压
<br>Download the [Ready-to-use portable package](): huge package with all environmental dependencies and several model presets, need to unpack after download

#### 运行<br>Run

点击.exe文件或其快捷方式即可
<br>Just click on the .exe file or its shortcut

### 本地部署 - 开发者<br>Local Deployment - Developer

#### 搭建环境<br>Setup Environment

- 请确保您已安装了`版本≥3.8`的[Python](https://www.python.org/downloads/)
<br>Please make sure that you've installed [Python](https://www.python.org/downloads/) `version 3.8 or higher`

#### 获取项目<br>Obtain Project

- 克隆项目仓库
<br>Clone Repository
    ```shell
    git clone https://github.com/Spr-Aachen/Easy-Voice-Toolkit.git
    ```

- 切至项目目录
<br>Change directory
    ```shell
    %cd Easy-Voice-Toolkit
    ```

#### 安装依赖<br>Install Dependencies

- 安装pytorch（需从[官网](https://pytorch.org/get-started/locally/)复制命令）
<br>Install pytorch (Command can be get from the [official site](https://pytorch.org/get-started/locally/))
    ```shell
    # e.g. (注意自己的cuda版本，这里以11.8为例)
    pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
    ```

- 安装项目依赖
<br>Install project requirements
    ```shell
    pip install -r requirements.txt
    ```

- 安装GUI依赖
<br>Install GUI dependency
    ```shell
    pip install pyside6 pywin32==300 psutil pynvml darkdetect PyGithub
    ```

#### 运行程序<br>Run Programm

- 启动图形界面
<br>Activate GUI
    ```shell
    Run.py
    ```

### 云端部署<br>Cloud Deployment

#### Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Spr-Aachen/EVT-Resources/blob/main/Easy_Voice_Toolkit_for_Colab.ipynb)
<br>点击以使用上面的demo，或者在Colab中上传[Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)
<br>Click to use the demo above, or access to Colab and upload [Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)


## 测试平台<br>Tested Devices

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


## 疑问解答<br>FAQ

-   **Q**: 更新客户端/下载依赖/模型时总是提示失败/报错该怎么办？
<br>**A**: 开代理或者直接用懒人包

-   **Q**: 好多参数都不清楚要如何设置该怎么办？
<br>**A**: 不明白的话使用默认值就好，至于有些参数（如语音识别工具中的“判断阈值”）可能要视实际效果多调试几次

-   **Q**: 你这永久免费开源...它保真吗？
<br>**A**: 嗯哼~♪


## 使用条例<br>Terms of Use

**Please solve the authorization problem of the dataset on your own. You shall be solely responsible for any problems caused by the use of non-authorized datasets for training and all consequences thereof.The repository and its maintainer have nothing to do with the consequences!**

1. This project is established for academic exchange purposes only and is intended for communication and learning purposes. It is not intended for production environments.

2. Any videos based on Easy Voice Toolkit that are published on video platforms must clearly indicate in the description that they are used for voice changing and specify the input source of the voice or audio, for example, using videos or audios published by others and separating the vocals as input source for conversion, which must provide clear original video links. If your own voice or other synthesized voices from other commercial vocal synthesis software are used as the input source for conversion, you must also explain it in the description.

3. You shall be solely responsible for any infringement problems caused by the input source. When using other commercial vocal synthesis software as input source, please ensure that you comply with the terms of use of the software. Note that many vocal synthesis engines clearly state in their terms of use that they cannot be used for input source conversion.

4. Continuing to use this project is deemed as agreeing to the relevant provisions stated in this repository README. This repository README has the obligation to persuade, and is not responsible for any subsequent problems that may arise.

5. If you distribute this repository's code or publish any results produced by this project publicly (including but not limited to video sharing platforms), please indicate the original author and code source (this repository).

6. If you use this project for any other plan, please contact and inform the author of this repository in advance. Thank you very much.

Reference: [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)

**相关法律请参照《中华人民共和国治安管理处罚法》和《中华人民共和国民法典》。**


## 联系方式<br>Contact Details

[![QQ](https://img.shields.io/badge/QQ-2835946988-brightgreen?style=for-the-badge&logo=tencent-qq&logoColor=white)]()
<br>倘若大伙儿有什么好的建议欢迎随时叨扰哦~
<br>Please feel free to contact me at any time, any comments and suggestions will be appreciated:)


## 收藏趋势<br>Stargazers over time

[![Stargazers over time](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit.svg)](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit)