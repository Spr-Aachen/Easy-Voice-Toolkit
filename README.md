<div align="center">

# 简易语音工具箱<br>Easy Voice Toolkit

![Title](/docs/media/Title.png "Home Page")

[![Releases](https://img.shields.io/github/v/release/Spr-Aachen/Easy-Voice-Toolkit?color=green&label=Release&logo=Github&logoColor=white&style=flat-square)](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases)
[![Bilibili](https://img.shields.io/badge/Bilibili-v1.0%20Intro-blue?logo=Bilibili&style=flat-square)](https://www.bilibili.com/video/BV)
[![YouTube](https://img.shields.io/badge/YouTube-v1.0%20Intro-red?logo=YouTube&style=flat-square)](https://www.youtube.com/watch?v=)

</div>


## 【项目介绍 Description】

**概述 Overview**
<br>一个基于VoiceprintRecognition、Whisper、VITS等项目的简易语音工具箱，目前尚在施工中~

<br>工具将包含且不限于以下功能：

- [音频转换和分割](/docs/Audio-Processor.md)
- [语音识别和筛选](/docs/Voice-Identifier.md)
- [语音转文字字幕](/docs/Voice-Transcriber.md)
- [语音数据集制作](/docs/Dataset-Creator.md)
- [语音模型训练](/docs/Voice-Trainer.md)

<br>项目完全为爱发电，欢迎感兴趣的小伙伴们参与进来哦！

**鸣谢 Acknowledgement**
<br>非常感谢以下项目的作者们，是你们的无私奉献给予了我灵感并大幅提升了项目的开发效率，也让更多的开发者从中受益

- [static_ffmpeg](https://github.com/zackees/static_ffmpeg)
- [audio-slicer](https://github.com/openvpi/audio-slicer)
- [VoiceprintRecognition](https://github.com/yeyupiaoling/VoiceprintRecognition-Pytorch/tree/release/1.0)
- [whisper](https://github.com/openai/whisper)
- [SRT-to-CSV-and-audio-split](https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
- [vits](https://github.com/CjangCjengh/vits)


## 【注意事项 Consideration】

**语言 Language**
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
        <th style = "text-align:center;">&#10006</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音模型训练<br>Voice Trainer</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#160</th>
        <th style = "text-align:center;">&#10006</th>
    </tr>
</table>

**提示 Tooltip**
<br>将鼠标停留在部分控件上方一段时间后会出现提示语，设置参数时请多留意
<br>


## 【项目部署 Deployment】

### 本地部署<br>Local Deployment

**搭建环境 Setup Environment**
- 请确保您已安装了`版本≥3.8`的[Python](https://www.python.org/downloads/)
<br>Please make sure that you've installed [Python](https://www.python.org/downloads/) `version 3.8 or higher`

- 请确保您已安装了[FFmpeg](https://ffmpeg.org/download.html)，您也可以尝试使用工具箱内置的安装功能（有概率失败）
<br>Please make sure that you've installed [FFmpeg](https://ffmpeg.org/download.html), or you can try using the toolkit's built-in install function (possibly failed)

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

即无界面版本
<br>见[Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)中的`Setup Environment`
<br>See `Setup Environment` in [Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)


## 【测试平台 Tested Devices】

**1.Honor Hunter V700**
- Type：NoteBook
- GPU：GTX 1660Ti
- CPU：i5-10300H
- RAM：16G
- OS：Win10
- Python：3.9
- Torch: 2.0.1

**2. (Waiting to add other devices)**


## 【疑问解答 FAQ】

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


## 【收藏趋势 Stargazers over time】

[![Stargazers over time](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit.svg)](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit)


## 【联系方式 Contact Details】

[![QQ](https://img.shields.io/badge/QQ-2835946988-brightgreen?style=flat-square&logo=tencent-qq&logoColor=white)]()

倘若大伙儿有什么好的建议欢迎随时叨扰哦~
<br>Please feel free to contact me at any time, any comments and suggestions will be appreciated:)