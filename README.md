<div align="center">

# 简易语音工具箱<br>Easy Voice Toolkit

[![Releases](https://img.shields.io/github/v/release/Spr-Aachen/Easy-Voice-Toolkit?color=green&label=Release&logo=Github&logoColor=white&style=flat-square)](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases)
[![Bilibili](https://img.shields.io/badge/Bilibili-v1.0%20Intro-blue?logo=Bilibili&style=flat-square)](https://www.bilibili.com/video/BV)
[![YouTube](https://img.shields.io/badge/YouTube-v1.0%20Intro-red?logo=YouTube&style=flat-square)](https://www.youtube.com/watch?v=)

</div>


## 前言
一个基于VoiceprintRecognition、Whisper、VITS等项目的简易语音工具箱，目前尚在施工中~
<br>工具将包含且不限于以下功能：音频转换和分割、语音识别和筛选、语音转文字字幕、语音数据集制作、语音模型训练
<br>项目完全为爱发电，欢迎感兴趣的小伙伴们参与进来哦！


## 【注意 Caution】

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


## 【用法 Usage】

### 本地部署<br>Local Deployment

**搭建环境 Setup Environment**
- 请确保您已安装了`版本≥3.8`的[Python](https://www.python.org/downloads/)
<br>Please make sure that you've installed [Python](https://www.python.org/downloads/) `version 3.8 or higher`.

**安装依赖 Install Dependencies**
- 安装pytorch（需从[官网](https://pytorch.org/get-started/locally/)复制命令）
<br>Install pytorch (Command can be get from the [official site](https://pytorch.org/get-started/locally/))
```shell
# e.g.
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
- ~~安装FFmpeg（实验性）~~
<br>~~Setup FFmpeg (Experimental)~~
```shell
#static_ffmpeg -i file.mp4 ...
```

### 云端部署<br>Cloud Deployment

见[Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)中的`Setup Environment`
<br>See `Setup Environment` in [Run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/Run.ipynb)


## 【测试平台 Tested Devices】

**1.Honor Hunter V700**
- Type：NoteBook
- GPU：GTX 1660Ti
- CPU：i5-10300H
- RAM：16G
- OS：Win10
- Python：3.9

**2. (Waiting to add other devices)**


## 【收藏趋势 Stargazers over time】

[![Stargazers over time](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit.svg)](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit)


## 【联系方式 Contact Details】

[![QQ](https://img.shields.io/badge/QQ-2835946988-brightgreen?style=flat-square&logo=tencent-qq&logoColor=white)]()

倘若大伙儿有什么好的建议欢迎随时叨扰哦~
<br>Please feel free to contact me at any time, any comments and suggestions will be appreciated:)