<div align = "center">

# 简易语音工具箱

一个基于开源语音项目实现的简易语音工具箱，提供了包括语音模型训练在内的多种自动化音频工具

[![下载 Windows 懒人包](https://img.shields.io/badge/下载%20-Windows%20懒人包-yellow?logo=HuggingFace)](https://huggingface.co/SprAachen/Easy-Voice-Toolkit-Package/resolve/main/EVT_windows_x64.7z?download=true)&nbsp;
[![打开 Google Colab](https://img.shields.io/badge/打开%20-Google%20Colab-orange?logo=GoogleColab)](https://colab.research.google.com/github/Spr-Aachen/Easy-Voice-Toolkit/blob/main/run.ipynb)

[![Bilibili](https://img.shields.io/badge/Bilibili-Intro-blue?logo=Bilibili)](https://space.bilibili.com/359461611/lists/2668347)&nbsp;
[![YouTube](https://img.shields.io/badge/YouTube-Intro-red?logo=YouTube)](https://www.youtube.com/playlist?list=PLzjq8Hx1SRV7zJ9cQvzwOU_4yOE65UfVW)

![Title](/docs/media/Cover.jpg)

</div>

---

<div align = "center">

**中文** | [**English**](../README.md)

</div>


## 功能特性

- 音频处理
- 语音识别
- 语音转录
- 数据集制作
- 模型训练
- 语音合成

用户可以根据自己的需求有选择性地使用，亦或者依次通过这些工具将未经处理的语音文件逐步变为理想的语音模型


## 用户指南

### 桌面程序

[![下载 Windows 懒人包](https://img.shields.io/badge/下载%20-Windows%20懒人包-yellow?logo=HuggingFace)](https://huggingface.co/SprAachen/Easy-Voice-Toolkit-Package/resolve/main/EVT_windows_x64.7z?download=true)
<br>点击上面的 badge 以下载解压即用的 Windows 懒人包

### 谷歌 Colab

[![打开 Google Colab](https://img.shields.io/badge/打开%20-Google%20Colab-orange?logo=GoogleColab)](https://colab.research.google.com/github/Spr-Aachen/Easy-Voice-Toolkit/blob/main/run.ipynb)
<br>点击上面的 badge 以使用 demo，或者在 Colab 中上传 [run.ipynb](https://github.com/Spr-Aachen/Easy-Voice-Toolkit/blob/main/run.ipynb)


## 开发指南

### 1. 搭建环境

- 请确保您已安装了`版本≥3.8`的[Python](https://www.python.org/downloads/)

### 2. 获取项目

- 克隆项目仓库
    ```shell
    git clone --recurse-submodules https://github.com/Spr-Aachen/Easy-Voice-Toolkit.git
    ```

- 切至项目目录
    ```shell
    %cd Easy-Voice-Toolkit
    ```

### 3. 安装依赖

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

### 4. 运行程序

- 启动客户端与服务器
    ```shell
    run.py
    ```


## 使用条例

0. 本项目仅用于学术交流目的，旨在促进沟通和学习。不适用于生产环境。

1. 基于 Easy Voice Toolkit 发布的任何视频必须在描述中明确指出它们用于变声，并指定声音或音频的输入源，例如使用他人发布的视频或音频，并将分离出的人声作为转换的输入源，必须提供清晰的原始视频链接。如果您使用自己的声音或其他商业语音合成软件生成的声音作为转换的输入源，也必须在描述中说明。

2. 您将对输入源引起的任何侵权问题负全部责任。当使用其他商业语音合成软件作为输入源时，请确保遵守该软件的使用条款。请注意，许多语音合成引擎在其使用条款中明确声明不能用于输入源转换。

3. 继续使用本项目被视为同意本仓库 README 中所述的相关条款。本仓库的 README 有义务进行劝导，但不承担可能出现的任何后续问题的责任。

4. 如果您分发此仓库的代码或将由此项目生成的任何结果公开发布（包括但不限于视频分享平台），请注明原始作者和代码来源（即此仓库）。

5. 如果您将此项目用于任何其他计划，请提前与本仓库的作者联系并告知


## 疑问解答

-   **Q**: 更新客户端/下载依赖/模型时总是提示失败/报错该怎么办？
<br>**A**: 开代理或者直接用懒人包

-   **Q**: 好多参数都不清楚要如何设置该怎么办？
<br>**A**: 不明白的话使用默认值就好

-   **Q**: 你这永久免费开源...它保真吗？
<br>**A**: 嗯哼~♪


## 迭代计划

### ToDo

- 添加LLM联动功能
- 使用C++重构客户端

### 开发中

- 后端开发
- 兼容Linux系统


## 项目支持

由衷感谢以下项目的作者，这个工具箱的实现正是得益于他们的优秀成果

- [audio-slicer](https://github.com/openvpi/audio-slicer)
- [VoiceprintRecognition](https://github.com/yeyupiaoling/VoiceprintRecognition-Pytorch/tree/release/1.0)
- [whisper](https://github.com/openai/whisper)
- [SRT-to-CSV-and-audio-split](https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)


## 收藏趋势

[![Stargazers over time](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit.svg)](https://starchart.cc/Spr-Aachen/Easy-Voice-Toolkit)