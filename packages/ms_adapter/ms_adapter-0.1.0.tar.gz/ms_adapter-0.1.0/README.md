# MSAdapter

简体中文 | [English](README_en.md)

## 简介

MSAdapter是MindSpore适配PyTorch接口的工具,其目的是在不改变原有PyTorch用户的使用习惯情况下,使得PyTorch代码能在昇腾上获得高效性能.
<p align="center"><img src="https://openi.pcl.ac.cn/laich/pose_data/raw/branch/master/MSA_F.png" width="580"\></p>


- PyTorch接口支持： MSAdapter的目的是支持PyTorch语法的原生态表达，用户只需要将PyTorch源代码中```import torch```替换为```import ms_adapter.pytorch```即可实现模型能支持昇腾上训练。模型中所使用的高阶APIs支持状态可以从这里找到 [Supported List](SupportedList.md)
- PyTroch接口支持范围： MSAdapter目前主要适配PyTorch的数据处理和模型结构部分代码，目前完全支持MindSpore的PYNATIVE模式下训练，部分网络结构支持GRAPH模式训练。训练过程部分代码需要用户自定义编写具体使用可以参考[使用指南](USER_GUIDE.md)

## 安装
### 安装MindSpore
请根据MindSpore官网[安装指南](https://www.mindspore.cn/install) ,安装2.0.0Nightly版本的MindSpore。


### 安装MSAdapter
#### 通过pip安装
```bash
pip install ms_adapter
```
 
#### 通过源码安装
```bash
 git clone https://git.openi.org.cn/OpenI/MSAdapter.git
 cd MSAdapter
 python setup.py install
```
如果出现权限不足的提示，请按照如下方式安装：
```bash
 python setup.py install --user || exit 1
```
## 使用
在数据处理和模型构建上,MSAdapter可以和PyTorch一样使用,模型训练部分代码需要自定义,示例如下：

### 1.数据处理(仅修改导入包)
```python
from ms_adapter.pytorch.utils.data import DataLoader
from ms_adapter.torchvision import datasets, transforms

transform = transforms.Compose([transforms.Resize((224, 224), interpolation=InterpolationMode.BICUBIC),
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.4914, 0.4822, 0.4465], std=[0.247, 0.2435, 0.2616])
                               ])
train_images = datasets.CIFAR10('./', train=True, download=True, transform=transform)
train_data = DataLoader(train_images, batch_size=128, shuffle=True, num_workers=2, drop_last=True)

```
### 2.模型构建(仅修改导入包)
```python
from ms_adapter.pytorch.nn import Module, Linear, Flatten

class MLP(Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.flatten = Flatten()
        self.line1 = Linear(in_features=1024, out_features=64)
        self.line2 = Linear(in_features=64, out_features=128, bias=False)
        self.line3 = Linear(in_features=128, out_features=10)

    def forward(self, inputs):
        x = self.flatten(inputs)
        x = self.line1(x)
        x = self.line2(x)
        x = self.line3(x)
        return x
```
### 3.模型训练(自定义训练)
```python
import ms_adapter.pytorch as torch
import ms_adapter.pytorch.nn as nn
import mindspore as ms

net = MLP()
net.train()
epochs = 500
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.01, momentum=0.9, weight_decay=0.0005)

# 定义训练过程
loss_net = ms.nn.WithLossCell(net, criterion)
train_net = ms.nn.TrainOneStepCell(loss_net, optimizer)

for i in range(epochs):
    for X, y in train_data:
        res = train_net(X, y)
        print("epoch:{}, loss:{:.6f}".format(i, res.asnumpy()))
# 模型保存
ms.save_checkpoint(net, "save_path.ckpt")
```

## 资源
- 模型库：MSAdapter支持丰富的深度学习应用，这里给出了从PyTorch官方代码迁移到MSAdapter模型。[已验证模型资源](https://git.openi.org.cn/OpenI/MSAdapterModelZoo)

## 贡献
欢迎开发者参与贡献。更多详情，请参阅我们的[贡献指南](https://openi.pcl.ac.cn/OpenI/MSAdapter/src/branch/master/CONTRIBUTING_CN.md).

## 许可证
[Apache License 2.0](https://openi.pcl.ac.cn/OpenI/MSAdapter/src/branch/master/LICENSE)

