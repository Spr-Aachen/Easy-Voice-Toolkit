<div align = "center">

## 语音模型训练<br>Voice Trainer

![Voice Trainer](/docs/media/Page5.png)
注意：当前版本已移除终端集成功能，解释器输出信息请见命令行窗口

</div>


### 介绍<br>Intro
训练出适用于语音合成的模型文件

### 用法<br>Usage
0. 检查是否需要同步设置
<br>若有使用连续流程的需求，即令当前工具中的部分设置衔接前面工具中的设置，可以通过点击左下方的`Sync`按钮进行一键同步

1. 设置参数
> - 训练集文本路径<br>FileList Path Training
<br>用于提供训练集音频路径及其语音内容的训练集txt文件的路径
> - 验证集文本路径<br>FileList Path Validation
<br>用于提供验证集音频路径及其语音内容的验证集txt文件的路径
> - 所用语言<br>Language
<br>音频中说话人所使用的语言
> - 评估间隔<br>Eval Interval
<br>每次评估并保存模型所间隔的step数
> - 迭代轮数<br>Epochs
<br>将全部样本完整迭代一轮的次数
> - 批处理量<br>Batch Size
<br>每轮迭代中单位批次的样本数量，若用户GPU性能较弱可减小该值
<br>注意：最好设置为2的幂次。设置为1会导致网络很难收敛
> - 进程数量<br>Num Workers
<br>进行数据加载时可使用的子进程数量，若用户CPU性能较弱可减小该值
> - 半精度训练<br>FP16 Run
<br>通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量
> - 是否多人<br>Is Speaker Multiple
<br>启用以支持多人模型训练
> - 人物名字<br>Speakers
<br>单人模型可不填写，多人模型需填写对应名字
<br>注意：不同人物名之间要用逗号隔开
> - 配置保存目录<br>Config Dir Save
<br>用于保存根据以上设置更新参数后的配置文件的目录
> - 模型保存目录<br>Model Dir Save
<br>用于存放生成的模型的目录
<br>注意：请不要在目录中存放由不同数据集训练得到的模型
> - [可选] 配置加载路径<br>[Optional] Config Path Load
<br>用于替代默认配置文件的用户配置文件的路径
> - [可选] 预训练G模型路径<br>[Optional] Model Path Pretrained G
<br>用作检查点的预训练生成器（Generator）模型的路径
<br>提示：该模型文件会被复制到模型保存目录下的"checkpoints"文件夹中
> - [可选] 预训练D模型路径<br>[Optional] Model Path Pretrained D
<br>用作检查点的预训练判别器（Discriminator）模型的路径
<br>提示：该模型文件会被复制到模型保存目录下的"checkpoints"文件夹中

2. 运行工具
<br>点击左下方的`Execute`按钮以开始执行，执行过程中点击`Terminate`按钮以终止进程

### 参考<br>Reference
https://github.com/CjangCjengh/vits