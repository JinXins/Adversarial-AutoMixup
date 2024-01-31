import glob
import PIL.Image
import torchvision.transforms.functional
from PIL.Image import Resampling
from torchvision.utils import save_image
from openmixup.models.augments import *
from openmixup.models.classifiers.mixup_classification import *
from openmixup.models.backbones.resnet_mmcls import *
from openmixup.models.classifiers.automix_V1plus import *
from openmixup.models.heads.pmix_block import *
from torch.autograd import Variable
import torch


def mix_samples(paths):

    size = (224, 224)
    i1, i2 = paths[:2]
    print(paths[:2])
    i1 = PIL.Image.open(i1).resize(size)
    i1 = i1.convert('RGB')
    i1 = torchvision.transforms.functional.to_tensor(i1).view(1,3,224,224)
    i2 = PIL.Image.open(i2).resize(size)
    i2 = i2.convert('RGB')
    i2 = torchvision.transforms.functional.to_tensor(i2).view(1,3,224,224)

    imgs = torch.cat([i1, i2], dim=0).cuda()
    lables = torch.randint(high=2, size=[2]).cuda()

    modes = ['cutmix', 'resizemix', 'mixup', 'fmix', 'smoothmix', 'saliencymix',]


    mode = 'cutmix'

    if mode == 'cutmix':
        img, info = cutmix(imgs, gt_label=lables, lam=0.75)
    elif mode == 'resizemix':
        img, info = resizemix(imgs, gt_label=lables, lam=0.5, scope=(0.5, 0.5))
    elif mode == 'mixup':
        img, info = mixup(imgs, gt_label=lables, lam=0.5)
    elif mode == 'fmix':
        img, info = fmix(imgs, gt_label=lables, lam=0.5, size=(224, 224))
    elif mode == 'smoothmix':
        img, info = smoothmix(imgs, gt_label=lables, lam=0.5)
    elif mode == 'gridmix':
        img, info = gridmix(imgs, gt_label=lables, lam=0.5, n_holes=(3, 6), hole_aspect_ratio=1.,
                            cut_area_ratio=(0.5, 1), cut_aspect_ratio=(0.5, 2))
    elif mode == 'saliencymix':
        img, info = saliencymix(imgs, gt_label=lables, lam=0.5)

    name = mode + '.jpg'
    save_image(img[:1, :, :, :], name)
    print('finish!')

    return 0

def resize_sample(paths):

    size = (500, 500)
    print(paths)
    for path in paths:
        path_name = path + '.jpg'
        img = PIL.Image.open(path).resize(size, resample=Resampling.BILINEAR)
        img.save(path)
    print("finish!")


def main():
    image_root = 'path/*'

    paths = ['img1_path/n01484850_3529.jpeg',
             'img2_path/n02510455_205.jpeg']
    mixed_image = mix_samples(paths)
    mix_root = 'img_path/*'
    # paths = glob.glob(mix_root)
    # resize_sample(paths)


if __name__ == '__main__':
    main()
