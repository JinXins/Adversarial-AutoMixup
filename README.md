<div align="center">
<!-- <h1>Adversarial AutoMixup</h1> -->
<h2><a href="https://arxiv.org/abs/2312.11954">Adversarial AutoMixup (ICLR 2024 spotlight)</a></h2>

Huafeng Qin<sup>1,\*</sup>, Xin Jin<sup>1,\*</sup>, Yun Jiang<sup>1</sup>, Mounim A. El-Yacoubi<sup>2</sup>, Xinbo Gao<sup>†,3</sup>

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

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="## 🛠 Installation">Installation</a></li>
    <li><a href="## Experiments">Experiments</a></li>
    <li><a href="## 😉 Citation">Citation</a></li>
    <li><a href="## 💬 Other">Other</a></li>
  </ol>
</details>

### 📬 You can contact me by email: 158398730@qq.com or WeChat: *xinxinxinxin_j* if you like.
### 👨‍🏫 And you can also contact my advisor[(*Huafeng Qin*)](https://scholar.google.com/citations?user=5jvXcJ0AAAAJ&hl=zh-CN)  by email: qinhuafengfeng@163.com
**If you are interested in *palm or finger vein research*, please contact us!**
___
## 🛠 Installation
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

## Experiments
Experiments  
___

## 😉 Citation
**If you like this paper of ours, please remember citing it 🥰, and please don`t forget citing OpenMixup if you use this project ! ! !** 🤗:  
```markdown
We'll update the paper with BibTeX citations when ICLR2024 is over!
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
## 💬 Other

**Chongqing Intelligence Perception and Block Chain Technology Key Lab (CQIPBCT Key Lab)**  
*If you are interested in vein research (palm veins, finger veins, etc.), why not contact us and we will be happy to discuss the research or questions with you.  
Of course, we're also trying to research how we can use AI to predict and detect diseases, potentially Alzheimer's, Parkinson's, etc., but of course, this is new research for us, so we're still figuring it out.*


