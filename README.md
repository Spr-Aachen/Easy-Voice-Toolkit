<div align = "center">

# 简易语音工具箱<br>Easy Voice Toolkit

![Title](/docs/media/Title.png "Home Page")

[![Releases](https://img.shields.io/github/v/release/Spr-Aachen/Easy-Voice-Toolkit?color=green&label=Release&logo=Github&logoColor=white&style=flat-square)](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases)
[![Bilibili](https://img.shields.io/badge/Bilibili-v1.0%20Intro-blue?logo=Bilibili&style=flat-square)](https://www.bilibili.com/video/BV)
[![YouTube](https://img.shields.io/badge/YouTube-v1.0%20Intro-red?logo=YouTube&style=flat-square)](https://www.youtube.com/watch?v=)

</div>


## 项目介绍<br>Description

### 概述<br>Overview

<br>一个基于Whisper、VITS等项目实现的简易语音工具箱，意在为用户提供自动化的语音模型训练流程
<br>A toolkit based on Whisper, VITS and other projects，which is aimed at providing users with an automatic speech model training process

<br>工具箱目前包含以下功能：
<br>Functions that are currently included in the toolkit are as follows:

- [音频转换和分割](/docs/Audio-Processor.md)
- [语音识别和筛选](/docs/Voice-Identifier.md)
- [语音转文字字幕](/docs/Voice-Transcriber.md)
- [语音数据集制作](/docs/Dataset-Creator.md)
- [语音模型训练](/docs/Voice-Trainer.md)

<br>这些功能彼此之间相互独立，但又能无缝衔接地形成一套完整的工作流
<br>These functions are independent of each other but seamlessly integrated to form a complete workflow
<br>用户可以根据自己的需求有选择性地使用，亦或者依次通过这些工具将未经处理的语音文件逐步变为理想的语音模型
<br>Users can use these tools selectively according to their own needs, or use them in sequence to gradually transform raw audio files into ideal speech models.

### 鸣谢<br>Acknowledgement

<br>非常感谢以下项目的作者，这个工具箱的实现正是得益于他们的优秀成果
<br>I'd like to express my sincere gratitude to the authors of the following projects, as their excellent work has contributed to the implementation of this toolkit

- [static_ffmpeg](https://github.com/zackees/static_ffmpeg)
- [audio-slicer](https://github.com/openvpi/audio-slicer)
- [VoiceprintRecognition](https://github.com/yeyupiaoling/VoiceprintRecognition-Pytorch/tree/release/1.0)
- [whisper](https://github.com/openai/whisper)
- [SRT-to-CSV-and-audio-split](https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
- [vits](https://github.com/CjangCjengh/vits)


## 注意事项<br>Consideration

### 语言<br>Language

<br>各个工具所支持的与不支持的语言如下：（ 空缺 表示未经测试）
<br>Languages that are supported&unsupported by the tools are shown as follows: ( Empty means untested)

<table border = "1">
    <tr>
        <th style = "text-align:center;">工具<br>Tool</th>
        <th style = "text-align:center;">中文<br>Chinese</th>
        <th style = "text-align:center;">英文<br>English</th>
        <th style = "text-align:center;">日文<br>Japnese</th>
    </tr>
    <tr>
        <th style = "text-align:center;">音频转换和分割<br>Audio Processor</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音识别和筛选<br>Voice Identifier</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#160</th>
        <th style = "text-align:center;">&#160</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音转文字字幕<br>Voice Transcriber</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音数据集制作<br>DataSet Creator</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音模型训练<br>Voice Trainer</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#160</th>
        <th style = "text-align:center;">&#10006</th>
    </tr>
</table>

### 提示<br>Tooltip

<br>将鼠标停留在部分控件上方一段时间后会出现提示语，设置参数时请多留意
<br>Certain widgets would display tooltips while getting cursor hovered above for a period of time, this should be noticed especially when setting params

### 系统<br>System

<br>Windows系统用户请将系统默认编码更改为UTF-8，具体操作：在 控制面板 ——> 时钟和区域 ——> 区域 ——> 管理 ——> 更改系统区域设置 打开的界面当中勾选“Beta版：使用 Unicode UTF-8 提供全球语言支持”选项然后重启即可
<br>Windows users should set the default encoding to UTF-8 by enabling Unicode UTF-8 WorldWide Support, method: Control Panel > Clock and Region > Region > Administrative tab > Change system locale button > enable Beta:Use Unicode UTF-8 for worldwide language support > reboot system


## 项目部署<br>Deployment

### 本地部署<br>Local Deployment

**搭建环境 Setup Environment**
- 请确保您已安装了`版本≥3.8`的[Python](https://www.python.org/downloads/)
<br>Please make sure that you've installed [Python](https://www.python.org/downloads/) `version 3.8 or higher`

- 请确保您已安装了[FFmpeg](https://ffmpeg.org/download.html)，您也可以尝试使用工具箱内置的安装功能（有概率失败）
<br>Please make sure that you've installed [FFmpeg](https://ffmpeg.org/download.html), or you can try using the toolkit's built-in install function (possibly failed)

**获取项目 Obtain Project**
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

**安装依赖 Install Dependencies**
- 安装pytorch（需从[官网](https://pytorch.org/get-started/locally/)复制命令）
<br>Install pytorch (Command can be get from the [official site](https://pytorch.org/get-started/locally/))
    ```shell
    # e.g. (注意自己的cuda版本，这里以11.7为例)
    pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
    ```
- 安装项目依赖
<br>Install project requirements
    ```shell
    pip install -r requirements.txt
    ```
- 安装GUI依赖
<br>Install GUI dependency
    ```shell
    pip install pyside6
    ```

**运行程序 Run Programm**
- 启动图形界面
<br>Activate GUI
    ```shell
    Run.py
    ```

### 云端部署<br>Cloud Deployment

#### Google Colab
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/.ipynb)
<br>点击以使用上面的demo，或者在你个人的Colab中上传[Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)
<br>Click to use the demo above, or open your own Colab and upload [Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)


## 测试平台<br>Tested Devices

### Windows OS

**1.Honor Hunter V700**
- Type：Laptop
- GPU：GTX 1660Ti
- CPU：i5-10300H
- RAM：16G
- OS：Win10
- Python：3.9
- Torch: 2.0.1

**2. (Waiting to add other devices)**

### Linux OS

**1. (Waiting to add other devices)**


## 疑问解答<br>FAQ

-   Q: 为什么不将项目打包成exe文件并发布？
<br>A: 考虑到用户cuda版本不一致以及torch本身包体过大的问题，故目前不提供打包版本

-   Q: 为什么不在最后面加一个TTS推理功能？
<br>A: 因为已经存在了不少如MoeGoe这样优秀的推理项目且基本都带有UI界面，故暂时没有制作

-   Q: 为什么内置的FFmpeg安装总是提示失败？
<br>A: 因为Static-FFmpeg项目还在维护中并且不支持win64，所以抱歉啦（去官网下一个其实挺快的）

-   Q: 好多参数都不清楚要如何设置该怎么办？
<br>A: 不明白的话使用默认值就好，但像语音识别工具里的“判断阈值”这种参数则可能要视实际效果多调试几次

-   Q: 工具箱右上角的Console是干嘛用的？
<br>A: 那个原本是用来显示Pyhton解释器的输出信息的（即终端工具），但由于技术问题导致效果不如预期而暂时禁用了

-   Q: 你这永久免费开源...它保真吗？
<br>A: 嗯哼~♪

-   Q: 你这做的什么破玩意儿也好意思拿出来？！
<br>A: 嘤嘤嘤QAQ


## 收藏趋势<br>Stargazers over time

[![Stargazers over time](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit.svg)](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit)


## 联系方式<br>Contact Details

[![QQ](https://img.shields.io/badge/QQ-2835946988-brightgreen?style=flat-square&logo=tencent-qq&logoColor=white)]()

倘若大伙儿有什么好的建议欢迎随时叨扰哦~
<br>Please feel free to contact me at any time, any comments and suggestions will be appreciated:)