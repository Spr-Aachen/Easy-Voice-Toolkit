<div align = "center">

## 语音识别和筛选<br>Voice Identifier

![Voice Identifier](/docs/media/Page2.png)
注意：当前版本已移除终端集成功能，解释器输出信息请见命令行窗口

</div>


### 介绍<br>Intro
从不同说话人的音频中批量筛选出属于同一说话人的音频

### 用法<br>Usage
0. 检查是否需要同步设置
<br>若有使用连续流程的需求，即令当前工具中的部分设置衔接前面工具中的设置，可以通过点击左下方的`Sync`按钮进行一键同步

1. 设置参数
> - 音频输入目录<br>Audio Dir Input
<br>需要进行语音识别筛选的音频文件的目录
> - 标准音频路径<br>Audio Path Std
<br>用于作为识别的比对标准（期望值）的音频的路径
> - 模型存放目录<br>Model Dir
<br>用于存放下载的声纹识别模型的目录，若模型已存在会直接使用
> - 模型类型<br>Model Type
<br>声纹识别模型的类型
> - 模型名字<br>Model Name
<br>声纹识别模型的名字，默认代表模型的大小
> - 特征提取方法<br>Feature Method
<br>音频特征的提取方法
> - 判断阈值<br>Decision Threshold
<br>判断是否为同一人的阈值，若参与比对的说话人声音相识度较高可以增加该值
> - 音频长度<br>Duration of Audio
<br>用于预测的音频长度
> - 音频输出目录<br>Audio Dir Output
<br>用于存放筛选出的音频文件的目录
> - [可选] 人物名字<br>[Optional] Speaker
<br>说话人物的名字，若有进行语音模型训练的需求则推荐填写
<br>注意：名字中尽量不要出现特殊符号

2. 运行工具
<br>点击左下方的`Execute`按钮以开始执行，执行过程中点击`Terminate`按钮以终止进程

### 参考<br>Reference
https://github.com/yeyupiaoling/VoiceprintRecognition-Pytorch/tree/release/1.0