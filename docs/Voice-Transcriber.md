## 语音转文字字幕<br>Voice Transcriber

![Voice Transcriber](/docs/media/Page3.png)
注意：当前版本已移除终端集成功能，解释器输出信息请见命令行窗口


### 介绍<br>Intro
将语音文件的内容批量转换为带时间戳的文本并保存为字幕文件

### 用法<br>Usage
0. 检查是否需要同步设置
<br>若有使用连续流程的需求，即令当前工具中的部分设置衔接前面工具中的设置，可以通过点击左下方的`Sync`按钮进行一键同步

1. 设置参数
> - 音频目录<br>WAV Dir
<br>需要将语音内容转为文字的wav文件的目录
> - 模型存放目录<br>Model Dir
<br>用于存放下载的语音识别模型的目录，若模型已存在会直接使用
> - 模型名字<br>Model Name
<br>语音识别 (whisper) 模型的名字，默认对应了模型的大小
> - 启用输出日志<br>Verbose
<br>是否输出debug日志
> - 前后文一致<br>Condition on Previous Text
<br>将模型之前的输出作为下个窗口的提示，若模型陷入了失败循环则禁用此项
> - 半精度<br>FP16
<br>主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项
> - 字幕输出目录<br>SRT Dir
<br>最后生成的字幕文件将会保存到该目录中
> - [可选] 所用语言<br>[Optional] Language
<br>音频中说话人所使用的语言，若存在多种语言则保持'None'即可

2. 运行工具
<br>点击左下方的`Execute`按钮以开始执行，执行过程中点击`Terminate`按钮以终止进程

### 参考<br>Reference
https://github.com/openai/whisper