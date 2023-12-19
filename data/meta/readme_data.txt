Please place used datasets as following structures:

openmixup
├── benchmarks
├── configs
├── data
│   ├── meta [used for 'ImageList' dataset]
│   │   ├── Aircrafts
│   │   |   ├── train_labeled.txt (for supervised training)
│   │   |   ├── train_unlabeled.txt (for self-supervised training)
│   │   |   ...
│   │   |   ├── image_list (contains semi-supervised txt files from Self-Tuning)
│   │   ├── Cars
│   │   ├── CUB200
│   │   ├── ImageNet
│   │   ├── iNaturalist2017
│   │   ├── iNaturalist2018
│   │   ├── Places205
│   │   ├── STL10
│   │   ├── TinyImageNet
│   ├── Aircrafts
│   │   |   ├── images (contains all train & val)
│   ├── cifar10
│   ├── cifar100
│   │   ├── cifar-10-batches-py
│   │   ├── cifar-10-python.tar
...
│   ├── ImageNet
│   │   ├── train
│   │   |   ├── n01440764
│   │   |   ├── n01443537
│   │   |   ...
│   │   |   ├── n15075141
│   │   ├── val
...
│   ├── Places205
│   │   ├── images256
│   │   |   ├── a
│   │   |   |   ├── abbey
│   │   |   |   ├── airport_terminal
│   │   |   |   ...
│   │   |   ├── b
│   │   |   ...
│   │   |   ├── y
...
│   ├── TinyImageNet200
│   │   ├── train
│   │   |   ├── n01443537
│   │   |   ├── ...
│   │   |   ├── n12267677
│   │   ├── val
│   │   |   ├── images (contains all train & val)
