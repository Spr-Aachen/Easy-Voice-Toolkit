<div align = "center">

## 语音数据集制作<br>Dataset Creator

![Dataset Creator](/docs/media/Page4.png)
注意：当前版本已移除终端集成功能，解释器输出信息请见命令行窗口

</div>


### 介绍<br>Intro
生成适用于语音模型训练的数据集

### 用法<br>Usage
0. 检查是否需要同步设置
<br>若有使用连续流程的需求，即令当前工具中的部分设置衔接前面工具中的设置，可以通过点击左下方的`Sync`按钮进行一键同步

1. 设置参数
> - 音频输入目录<br>WAV Dir
<br>需要重采样和按字幕时间戳进行分割的wav文件的目录
> - 采样率<br>Sample Rate
<br>要使用的新采样率
> - 采样格式<br>Subtype
<br>要使用的新采样格式
> - 音频输出目录<br>WAV Dir Split
<br>用于保存最后处理完成的音频的目录
> - 字幕输入目录<br>SRT Dir
<br>需要转为适用于模型训练的csv文件的srt文件的目录
> - 自编码器<br>AutoEncoder
<br>模型训练所使用的自动编码器
> - 训练集文本路径<br>FileList Path Training
<br>用于保存最后生成的训练集txt文件的路径
> - 验证集文本路径<br>FileList Path Validation
<br>用于保存最后生成的验证集txt文件的路径

2. 运行工具
<br>点击左下方的`Execute`按钮以开始执行，执行过程中点击`Terminate`按钮以终止进程

### 参考<br>Reference
https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split