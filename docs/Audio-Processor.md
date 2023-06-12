<div align = "center">

## 音频转换和分割<br>Audio Processor

![Audio Processor](/docs/media/Page1.png)
注意：当前版本的终端集成功能并不完善，缺失的解释器输出信息请见命令行窗口

</div>


### 介绍<br>Intro
将媒体文件批量转换为音频文件并自动切除音频的静音部分

### 用法<br>Usage
0. 检查是否已安装FFmpeg
<br>若未安装，可以通过点击左下方的`安装`按钮进行一键部署，但有概率会提示安装失败

1. 设置参数
> - 媒体输入目录<br>Media Dir Input
<br>需要输出为音频文件的媒体文件的目录
<br>提示：会在该目录的上级目录下创建名为"Backup"的备份文件夹以存放被分割处理的原音频文件
> - 媒体输出格式<br>Media Format Output
<br>需要输出为的音频文件的格式
> - 均方根阈值<br>RMS Threshold
<br>低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值
> - 跳跃大小<br>Hop Size
<br>每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程
> - 最小静音间隔<br>Silent Interval Min
<br>静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值
<br>注意：这个值必须小于 Audio Length Min，大于 Hop Size
> - 最大静音长度<br>Silence Kept Max
<br>被分割的音频周围保持静音的最大长度
<br>提示：这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置
> - 最小音频长度<br>Audio Length Min
<br>每个被分割的音频片段所需的最小长度
> - 媒体输出目录<br>Media Dir Output
<br>用于保存最后生成的音频文件的目录

2. 运行工具
<br>点击底部的`执行`按钮以开始执行，执行过程中点击`终止`按钮以终止进程

### 参考<br>Reference
https://github.com/zackees/static_ffmpeg
https://github.com/openvpi/audio-slicer