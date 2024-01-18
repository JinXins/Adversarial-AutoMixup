<div align="center">
<!-- <h1>Adversarial AutoMixup</h1> -->
<h2><a href="https://arxiv.org/abs/2312.11954">Adversarial AutoMixup (ICLR 2024 spotlight)</a></h2>

[Huafeng Qin](https://scholar.google.com/citations?user=5jvXcJ0AAAAJ&hl=zh-CN)<sup>1,\*</sup>, [Xin Jin](https://scholar.google.com/citations?user=v3OwxWIAAAAJ&hl=zh-CN)<sup>1,\*</sup>, Yun Jiang<sup>1</sup>, [Mounim A. El-Yacoubi](https://scholar.google.com/citations?user=ObFYefYAAAAJ&hl=zh-CN)<sup>2</sup>, [Xinbo Gao](https://scholar.google.com/citations?user=VZVTOOIAAAAJ&hl=zh-CN&oi=sra)<sup>†,3</sup>

<sup>1</sup>[Chongqing Technology and Business University](https://www.ctbu.edu.cn/)

<sup>2</sup>[Telecom SudParis, Institut Polytechnique de Paris](https://www.ip-paris.fr/telecom-sudparis)

<sup>3</sup>[Chongqing University of Posts and Telecommunications](https://www.cqupt.edu.cn/)
</div>

<p align="center">
<a href="https://arxiv.org/abs/2312.11954" alt="arXiv">
    <img src="https://img.shields.io/badge/arXiv-2211.03295-b31b1b.svg?style=flat" /></a>
<a href="https://github.com/JinXins/Adversarial-AutoMixup/blob/main/LICENSE" alt="license">
    <img src="https://img.shields.io/badge/license-Apache--2.0-%23B7A800" /></a>
</p>

<p align="center">
<img src="https://github.com/JinXins/Adversarial-AutoMixup/assets/124172716/c8b2f194-41b1-4117-8965-68c9c20d3c83" width=75% height=75% 
class="center">
</p>

We propose **AdAutoMix**, an adversarial automatic mixup augmentation approach that generates challenging samples to train a robust classifier for image classification, by alternatively optimizing the classifier and the mixup sample generator. AdAutoMix comprises two modules, a mixed example generator, and a target classifier. The mixed sample generator aims to produce hard mixed examples to challenge the target classifier while the target classifier’s aim is to learn robust features from hard mixed examples to improve generalization. To prevent the collapse of the inherent meanings of images, we further introduce an exponential moving average (EMA) teacher and cosine similarity to train AdAutoMix in an end-to-end way. 

### Mixed Images of Various Mixup-based Approaches.
<p align="center">
<img src="https://github.com/JinXins/Adversarial-AutoMixup/assets/124172716/ab30bb40-cc57-455e-98f1-436d9e16aafe" width=75% height=75% 
class="center">
</p>

### 📬 You can contact me by email: 158398730@qq.com or WeChat: *xinxinxinxin_j*.
**If you are interested in *palm or finger vein research*, please contact us!**
___
## 🛠 Installation
**💥News! ! !💥**  
*you can clone Openmixup training AdAutoMix!*  
We update some analysis tools code such as: Calibration, FGSM `calibration_fgsm.py` and Occlusion Robustness `occlusion_robustness.py` experiments, also we support a mix augmentation method **SnapMix[[AAAI 2020]](https://arxiv.org/abs/2012.04846)**.  
Big thanks to **Siyuan Li[(@Lupin1998)](https://github.com/Lupin1998)**.  

In fact, you can add our python file in **OpenMixup**.  
There, you can see how to use it and the environment required. What you need to do is add or replace our files by folder inside OpenMixup, and then add the function names of the files in the `__init__.py` file.   
You also can download or find other Mixup methods in **OpenMixup("https://github.com/Westlake-AI/openmixup")**  
Thanks contributors: **Siyuan Li[(@Lupin1998)](https://github.com/Lupin1998), Zichen Liu[(@pon7)](https://github.com/pone7) and Zedong Wang[(@Jacky1128)](https://github.com/Jacky1128)**.  
___
**Here are the commands to install OpenMixup**
```markdown
conda create -n openmixup python=3.8 pytorch=1.12 cudatoolkit=11.3 torchvision -c pytorch -y
conda activate openmixup
pip install openmim
mim install mmcv-full
git clone https://github.com/Westlake-AI/openmixup.git
cd openmixup
python setup.py develop
```
**Here are the commands to git clone AdAutoMixup**
```markdown
git clone https://github.com/JinXins/Adversarial-AutoMixup.git
```
___

## 📊 Experiments

### CIFAR-100
| Name             | alpha | Conference | ResNet18 | ResNeXt50 | Swin-Tiny | ConvNeXt-T |
|------------------|-------|------------|----------|-----------|-----------|------------|
| Vanilla                                              | -     |            | 78.04   | 81.09    | 78.41 | 78.70 |
| [MixUp](https://arxiv.org/abs/1710.09412)            | 1.0   | ICLR2018   | 79.12   | 82.10    | 76.78 | 81.13 |
| [CutMix](https://arxiv.org/abs/1905.04899)           | 0.2   | ICCV2019   | 78.17   | 78.32    | 80.64 | 82.46 |
| [SaliencyMix](https://arxiv.org/abs/2006.01791)      | 0.2   | ICLR2021   | 79.12   | 78.77    | 80.40 | 82.82 |
| [FMix](https://arxiv.org/abs/2002.12047)             | 0.2   | ArXiv      | 79.69   | 79.02    | 80.72 | 81.79 |
| [ResizeMix](https://arxiv.org/abs/2012.11101)        | 1.0   | CVMJ2023   | 80.01   | 80.35    | 80.16 | 82.53 |
| [PuzzleMix](https://arxiv.org/abs/2009.06962)        | 1.0   | ICML2020   | 81.13   | 82.85    | 80.33 | 82.29 |
| [AutoMix](https://arxiv.org/abs/2103.13027)          | 2.0   | ECCV2022   | 82.04   | 83.64    | 82.67 | 83.30 |
| [AdAutoMix](https://arxiv.org/abs/2312.11954)        | 1.0   | ICLR2024   |**82.32**|**84.22** |**84.33**|**83.54**|
___
### Tiny-ImageNet & ImageNet-1K
| Name             | alpha | Conference | ResNet18 | ResNeXt50 |ImageNet-1K| ResNet18 | ResNet34 | ResNet50 |
|------------------|-------|------------|----------|-----------|-|----------|----------|----------|
| Vanilla          | -     |            | 61.68    | 65.04     | | 70.04    | 73.85    | 76.83    |
| MixUp            | 1.0   | ICLR2018   | 63.86    | 66.36     | | 69.98    | 73.97    | 77.12    |
| CutMix           | 0.2   | ICCV2019   | 65.53    | 66.47     | | 68.95    | 73.58    | 77.17    |
| SaliencyMix      | 0.2   | ICLR2021   | 64.40    | 66.55     | | 69.16    | 73.56    | 77.14    |
| FMix             | 0.2   | ArXiv      | 63.47    | 65.08     | | 69.96    | 74.08    | 77.19    |
| ResizeMix        | 1.0   | CVMJ2023   | 63.17    | 65.87     | | 69.50    | 73.88    | 77.42    |
| PuzzleMix        | 1.0   | ICML2020   | 65.81    | 67.83     | | 70.12    | 74.26    | 77.54    |
| AutoMix          | 2.0   | ECCV2022   | 67.33    | 70.72     | | 70.50    | 74.52    | 77.91    |
| AdAutoMix        | 1.0   | ICLR2024   | **69.19**| **72.89** | | **70.86**| **74.82**| **78.04**|
___
### Find-Grained
| Name             | alpha | Confrence  | CUB R18 | CUB R50 | FGVC R18 | FGVC RX50 | Cars R18 | Cars RX50 |
|------------------|-------|------------|---------|---------|--------------------|---------------------|--------------------|---------------------|
| Vanilla          | -     |            | 77.68   | 82.38   | 80.23              | 85.1                | 86.32              | 90.15               |
| MixUp            | 1.0   | ICLR2018   | 78.39   | 82.98   | 79.52              | 85.18               | 86.27              | 90.81               |
| CutMix           | 0.2   | ICCV2019   | 78.40   | 83.17   | 78.84              | 84.55               | 87.48              | 91.22               |
| ManifoldMixup    | 2.0   | ICML2019   | 79.76   | 83.76   | 80.68              | 86.6                | 85.88              | 90.20               |
| SaliencyMix      | 0.2   | ICLR2021   | 77.95   | 82.02   | 80.02              | 84.31               | 86.48              | 90.60               |
| FMix             | 0.2   | ArXiv      | 77.28   | 83.34   | 79.36              | 86.23               | 87.55              | 90.90               |
| ResizeMix        | 1.0   | CVMJ2023   | 78.5    | 83.41   | 78.1               | 84.08               | 88.17              | 91.36               |
| PuzzleMix        | 1.0   | ICML2020   | 78.63   | 83.83   | 80.76              | 86.23               | 87.78              | 91.29               |
| AutoMix          | 2.0   | ECCV2022   | 79.87   | 83.88   | 81.37              | 86.72               | 88.89              | 91.38               |
| AdAutoMix        | 1.0   | ICLR2024   |**80.88**|**84.57**| **81.73**          | **87.16**           | **89.19**          | **91.59**           |
___

**If you want see more results, please check this [Experiments.md](Experiments.md).**  
___

## 😉 Citation
**If you like this paper of ours, please remember citing it 🥰, and please don`t forget citing OpenMixup if you use this project ! ! !** 🤗:  
```markdown
@article{Qin2023AdversarialA,
  title={Adversarial AutoMixup},
  author={Huafeng Qin and Xin Jin and Yun Jiang and Mounim A. El-Yacoubi and Xinbo Gao},
  journal = {ArXiv},
  year={2023},
  volume = {abs/2312.11954}
}

@article{li2022openmixup,
  title = {OpenMixup: A Comprehensive Mixup Benchmark for Visual Classification},
  author = {Siyuan Li and Zedong Wang and Zicheng Liu and Di Wu and Cheng Tan and Stan Z. Li},
  journal = {ArXiv},
  year = {2022},
  volume = {abs/2209.04851}
}
```

___
## 💬 Other info
**Chongqing Intelligence Perception and Block Chain Technology Key Lab (CQIPBCT Key Lab)**  
*If you are interested in vein research (palm veins, finger veins, etc.), why not contact us and we will be happy to discuss the research or questions with you.  
Of course, we're also trying to research how we can use AI to predict and detect diseases, potentially Alzheimer's, Parkinson's, etc., but of course, this is new research for us, so we're still figuring it out.*


