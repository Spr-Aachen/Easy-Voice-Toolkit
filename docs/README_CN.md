<div align = "center">

# 简易语音工具箱

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

**简体中文** | [**English**](../README.md)

</div>


## 项目介绍

### 概述

一个基于开源语音项目实现的简易语音工具箱，提供了包括语音模型训练在内的多种自动化音频工具

<br>工具箱目前包含以下功能：

- [音频处理](/docs/CN/Audio-Processor.md)

- [语音识别](/docs/CN/Voice-Recognizer.md)

- [语音转录](/docs/CN/Voice-Transcriber.md)

- [数据集制作](/docs/CN/Dataset-Creator.md)

- [模型训练](/docs/CN/Voice-Trainer.md)

- [语音合成](/docs/CN/Voice-Converter.md)

<br>这些功能依次关联，能够形成一套完整的工作流
<br>用户可以根据自己的需求有选择性地使用，亦或者依次通过这些工具将未经处理的语音文件逐步变为理想的语音模型

### 鸣谢

由衷感谢以下项目的作者，这个工具箱的实现正是得益于他们的优秀成果

- [audio-slicer](https://github.com/openvpi/audio-slicer)
- [VoiceprintRecognition](https://github.com/yeyupiaoling/VoiceprintRecognition-Pytorch/tree/release/1.0)
- [whisper](https://github.com/openai/whisper)
- [SRT-to-CSV-and-audio-split](https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
- [vits](https://github.com/CjangCjengh/vits)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)


## 注意事项

### 系统

目前发布的版本仅支持Windows系统

### 语言

目前各个工具对语言的支持情况如下：

<table cellspacing = "0" cellpadding = "0">
    <style>
        table {
            border-collapse: collapse;
        }
        td {
            background-color: white;
        }
        td#cellSlashedTd {
            background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxsaW5lIHgxPSIwIiB5MT0iMCIgeDI9IjEwMCUiIHkyPSIxMDAlIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjEiLz48L3N2Zz4=);
        }
    </style>
    <tr>
        <td id = "cellSlashedTd">
            <span style = "float:left; margin-top:20px;">工具</span>
            <span style = "float:right; margin-top:-10px;">语言</span>
        </td>
        <th style = "text-align:center;">中文</th>
        <th style = "text-align:center;">英文</th>
        <th style = "text-align:center;">日文</th>
    </tr>
    <tr>
        <th style = "text-align:center;">音频处理</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音识别</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">语音转录</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">数据集制作</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    <tr>
        <th style = "text-align:center;">模型训练</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
    </tr>
    </tr>
        <th style = "text-align:center;">语音合成</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
        <th style = "text-align:center;">&#10004</th>
</table>


## 项目部署

### 本地部署 - 用户

#### 下载

您有两种选择：

- 下载[轻量化的安装程序](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/releases/latest)：包体小且拥有安装引导，但是未配置环境依赖且不带模型

- 下载[解压即用的懒人包](https://huggingface.co/SprAachen/Easy-Voice-Toolkit-Package/resolve/main/EVT_windows_x64.7z?download=true)：配置了所有环境依赖并附带有预设模型，但是包体较大且需要解压

#### 运行

点击Main.exe文件或其快捷方式即可

### 本地部署 - 开发者

#### 搭建环境

- 请确保您已安装了`版本≥3.8`的[Python](https://www.python.org/downloads/)

#### 获取项目

- 克隆项目仓库
    ```shell
    git clone --recurse-submodules https://github.com/Spr-Aachen/Easy-Voice-Toolkit.git
    ```

- 切至项目目录
    ```shell
    %cd Easy-Voice-Toolkit
    ```

#### 安装依赖

- 安装pytorch（可从[官网](https://pytorch.org/get-started/locally/)复制命令）
    ```shell
    # e.g. (注意自己的cuda版本，这里以11.8为例)
    pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
    ```

- 安装项目依赖
    ```shell
    pip install -r requirements.txt
    ```

- 安装[GUI依赖](https://github.com/Spr-Aachen/QEasyWidgets)
    ```shell
    pip install QEasyWidgets
    ```

#### 运行程序

- 启动客户端
    ```shell
    run.py
    ```

### 云端部署

#### Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Spr-Aachen/Easy-Voice-Toolkit/blob/main/run.ipynb)
<br>点击以使用上面的demo，或者在Colab中上传[run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/run.ipynb)


## 迭代计划

### ToDo
- 添加LLM联动功能
- 使用C++重构客户端

### 开发中
- 后端开发
- 语言国际化
- 兼容Linux系统


## 测试平台

### Windows 系统

#### Honor Hunter V700
- **Type**: Laptop
- **GPU**: GTX 1660Ti
- **CPU**: i5-10300H
- **RAM**: 16G
- **OS**: Win10
- **Python**: 3.9
- **Torch**: 2.0.1

#### (待添加)

### Linux 系统

#### (待添加)


## 疑问解答

-   **Q**: 更新客户端/下载依赖/模型时总是提示失败/报错该怎么办？
<br>**A**: 开代理或者直接用懒人包

-   **Q**: 好多参数都不清楚要如何设置该怎么办？
<br>**A**: 不明白的话使用默认值就好

-   **Q**: 你这永久免费开源...它保真吗？
<br>**A**: 嗯哼~♪


## 使用条例

**请自行解决数据集的授权问题。对于使用未经授权的数据集进行训练所导致的任何问题，您将承担全部责任，并且该仓库及其维护者不承担任何后果！相关法律请参照《中华人民共和国治安管理处罚法》和《中华人民共和国民法典》**

0. 本项目仅用于学术交流目的，旨在促进沟通和学习。不适用于生产环境。
1. 基于 Easy Voice Toolkit 发布的任何视频必须在描述中明确指出它们用于变声，并指定声音或音频的输入源，例如使用他人发布的视频或音频，并将分离出的人声作为转换的输入源，必须提供清晰的原始视频链接。如果您使用自己的声音或其他商业语音合成软件生成的声音作为转换的输入源，也必须在描述中说明。
2. 您将对输入源引起的任何侵权问题负全部责任。当使用其他商业语音合成软件作为输入源时，请确保遵守该软件的使用条款。请注意，许多语音合成引擎在其使用条款中明确声明不能用于输入源转换。
3. 继续使用本项目被视为同意本仓库 README 中所述的相关条款。本仓库的 README 有义务进行劝导，但不承担可能出现的任何后续问题的责任。
4. 如果您分发此仓库的代码或将由此项目生成的任何结果公开发布（包括但不限于视频分享平台），请注明原始作者和代码来源（即此仓库）。
5. 如果您将此项目用于任何其他计划，请提前与本仓库的作者联系并告知

Reference: [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)


## 联系方式

[![QQ](https://img.shields.io/badge/QQ-2835946988-brightgreen?style=for-the-badge&logo=tencent-qq&logoColor=white)]()
<br>倘若大伙儿有什么好的建议欢迎随时叨扰哦~


## 收藏趋势

[![Stargazers over time](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit.svg)](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit)