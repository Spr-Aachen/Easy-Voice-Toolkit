<div align = "center">

## 语音模型训练<br>Voice Trainer

![Voice Trainer](/docs/media/Page5.png)
注意：当前版本的终端集成功能并不完善，缺失的解释器输出信息请见命令行窗口

</div>


### 介绍<br>Intro
训练出适用于语音合成的模型文件

### 用法<br>Usage
0. 检查是否需要同步设置
<br>若有使用连续流程的需求，即令当前工具中的部分设置衔接前面工具中的设置，可以通过点击左下方的`同步`按钮进行一键同步

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
<br>最好设置为2的幂次，若设置为1会导致网络很难收敛
> - 进程数量<br>Num Workers
<br>进行数据加载时可并行的进程数量，若用户CPU性能较弱可减小该值
<br>提示：如果配置属于低U高显的话不妨试试把数值降到2
> - 半精度训练<br>FP16 Run
<br>通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量
> - 配置保存目录<br>Config Dir Save
<br>用于保存根据以上设置更新参数后的配置文件的目录
> - 模型保存目录<br>Model Dir Save
<br>用于存放生成的模型的目录，若目录中已存在模型则会将其视为检查点
<br>提示：当目录中存在多个模型时，编号最大的那个会被选为检查点
> - [可选] 配置加载路径<br>[Optional] Config Path Load
<br>用于替代默认配置文件的用户配置文件的路径
> - [可选] 预训练G_*模型路径<br>[Optional] Model Path Pretrained G_*
<br>预训练生成器（Generator）模型的所在路径，载入优先级高于检查点
> - [可选] 预训练D_*模型路径<br>[Optional] Model Path Pretrained D_*
<br>预训练判别器（Discriminator）模型的所在路径，载入优先级高于检查点
> - [可选] 人物名字<br>[Optional] Speakers
<br>若数据集非本工具箱生成且未包含人名信息，则应按序号填写并用逗号隔开
<br>注意：不同人物名之间要用逗号隔开；逗号后面不需要加空格

2. 运行工具
<br>点击底部的`执行`按钮以开始执行，执行过程中点击`终止`按钮以终止进程

### 参考<br>Reference
https://github.com/CjangCjengh/vits