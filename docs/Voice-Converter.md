<div align = "center">

## 音频转换和分割<br>Voice Converter

![Voice Converter](/docs/media/Page6.png)
注意：当前版本的终端集成功能并不完善，缺失的解释器输出信息请见命令行窗口

</div>


### 介绍<br>Intro
将文字转为语音并生成音频文件

### 用法<br>Usage
0. 检查是否需要同步设置
<br>若有使用连续流程的需求，即令当前工具中的部分设置衔接前面工具中的设置，可以通过点击左下方的`同步`按钮进行一键同步

1. 设置参数
> - 配置加载路径<br>Config_Path_Load
<br>该路径对应的配置文件会用于推理
> - 输入文字<br>Text
<br>输入的文字会作为说话人的语音内容
> - G_*模型加载路径<br>Model_Path_Load
<br>该路径对应的生成器（Generator）模型会用于推理
> - 所用语言<br>Language
<br>说话人/文字所使用的语言
> - 人物名字<br>Speaker
<br>说话人物的名字
> - 情感强度<br>EmotionStrength
<br>情感的变化程度
> - 音素音长<br>PhonemeDuration
<br>音素的发音长度
> - 整体语速<br>SpeechRate
<br>整体的说话速度
> - 音频保存目录<br>Audio_Dir_Save
<br>推理得到的音频会保存到该目录

2. 运行工具
<br>点击底部的`执行`按钮以开始执行，执行过程中点击`终止`按钮以终止进程

### 参考<br>Reference
https://github.com/zackees/static_ffmpeg
https://github.com/openvpi/audio-slicer