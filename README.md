# Adversarial AutoMixup

## ⏰ Official PyTorch implementation of Adversarial AutoMixup (ICLR`2024 spotlight)
### 📬 You can contact me by email： 158398730@qq.com or WeChat： xinxinxinxin_j if you like.
### 👨‍🏫 And you can also contact my advisor[(*Huafeng Qin*)](https://scholar.google.com/citations?user=5jvXcJ0AAAAJ&hl=zh-CN)  by email: qinhuafengfeng@163.
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

**Chongqing Intelligence Perception and Block Chain Technology Key Lab(CQIPBCT Key Lab)**  
*If you are interested in vein research (palm veins, finger veins, etc.), why not contact us and we will be happy to discuss the research or questions with you.  
Of course, we're also trying to research how we can use AI to predict and detect diseases, potentially Alzheimer's, Parkinson's, etc., but of course, this is new research for us, so we're still figuring it out.*


