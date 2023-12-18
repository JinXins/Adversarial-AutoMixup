# Experiments
**Here are the results of Mixups' classification experiments.**
## CIFAR-100
### CNNs
R18 denotes [ResNet-18](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html) and RX50 denotes [ResNext-50](https://arxiv.org/abs/1611.05431)
| Name             | alpha | Conference | R18 200 | R18 400 | R18 800 | RX50 200 | RX50 400 | RX50 800 |
|------------------|-------|------------|---------|---------|---------|----------|----------|----------|
| Vanilla          | -     |            | 76.42   | 77.73   | 78.04   | 79.37    | 80.24    | 81.09    |
| [MixUp](https://arxiv.org/abs/1710.09412)            | 1.0   | ICLR2018   | 78.52   | 79.34   | 79.12   | 81.18    | 82.54    | 82.10    |
| [CutMix](https://arxiv.org/abs/1905.04899)           | 0.2   | ICCV2019   | 79.45   | 79.58   | 78.17   | 81.52    | 78.52    | 78.32    |
| [ManifoldMix](https://arxiv.org/abs/1806.05236)      | 2.0   | ICML2019   | 79.18   | 80.18   | 80.35   | 81.59    | 82.56    | 82.88    |
| [SmoothMix](https://openaccess.thecvf.com/content_CVPRW_2020/html/w45/Lee_SmoothMix_A_Simple_Yet_Effective_Data_Augmentation_to_Train_Robust_CVPRW_2020_paper.html)        | 0.2   | CVPRW2020  | 77.90   | 78.77   | 78.69   | 80.68    | 79.56    | 78.85    |
| [SaliencyMix](https://arxiv.org/abs/2006.01791)      | 0.2   | ICLR2021   | 79.75   | 79.64   | 79.12   | 80.72    | 78.63    | 78.77    |
| [Attentive-CutMix](https://arxiv.org/abs/2003.13048) | 2.0   | ICASSP2020 | 79.62   | 80.14   | 78.91   | 81.69    | 81.53    | 80.54    |
| [FMix](https://arxiv.org/abs/2002.12047)             | 0.2   | ArXiv      | 78.91   | 79.91   | 79.69   | 79.87    | 78.99    | 79.02    |
| [GridMix](https://www.sciencedirect.com/science/article/abs/pii/S0031320320303976)          | 0.2   | PR2021     | 78.23   | 78.60   | 78.72   | 81.11    | 79.80    | 78.90    |
| [ResizeMix](https://arxiv.org/abs/2012.11101)        | 1.0   | ArXiv      | 79.56   | 79.19   | 80.01   | 79.23    | 79.78    | 80.35    |
| [PuzzleMix](https://arxiv.org/abs/2009.06962)        | 1.0   | ICML2020   | 79.96   | 80.82   | 81.13   | 81.69    | 82.84    | 82.85    |
| [Co-Mixup](https://arxiv.org/abs/2102.03065)         | 2.0   | ICLR2021   | 80.01   | 80.87   | 81.17   | 81.73    | 82.88    | 82.91    |
| [AutoMix](https://arxiv.org/abs/2103.13027)          | 2.0   | ECCV2022   | 80.12   | 81.78   | 82.04   | 82.84    | 83.32    | 83.64    |
| [SAMix](https://arxiv.org/abs/2111.15454)            | 2.0   | ArXiv      | 81.21   | 81.97   | 82.30   | 83.81    | 84.27    | 84.42    |
| AdAutoMix        | 1.0   | ICLR2024   | 81.55   | 81.97   | 82.32   | 84.40    | 84.05    | 84.22    |

### ViTs
DeiT-S denotes [DeiT-Samll](https://arxiv.org/abs/2012.12877) Transformer, Swin-T denotes [Swin-Tiny](https://arxiv.org/abs/2103.14030) Transformer and ConvNeXt-T denotes [ConvNeXt-Tiny](https://arxiv.org/abs/2201.03545) Transformer.
| Name              | alpha     | Conference | DeiT-S 200 | DeiT-S 600 | Swin-T 200 | Swin-T 600 | ConvNeXt-T 200 | ConvNeXt-T 600 |
|-------------------|-----------|------------|----------------|----------------|---------------|---------------|-------------------|-------------------|
| Vanilla         | -         |            | 65.81          | 68.50          | 78.41         | 81.29         | 78.70             | 80.65             |
| [MixUp](https://arxiv.org/abs/1710.09412)             | 0.8       | ICLR2018   | 69.98          | 76.35          | 76.78         | 83.67         | 81.13             | 83.08             |
| [CutMix](https://arxiv.org/abs/1905.04899)            | 2.0       | ICCV2019   | 74.12          | 79.54          | 80.64         | 83.38         | 82.46             | 83.20             |
| DeiT=MixUp+CutMix |           |            | 75.92          | 79.38          | 81.25         | 84.41         | 83.09             | 84.12             |
| [ManifoldMix](https://arxiv.org/abs/1806.05236)       | 2.0       | ICML2019   | -              | -              | -             | -             | 82.06             | 83.94             |
| [SmoothMix](https://openaccess.thecvf.com/content_CVPRW_2020/html/w45/Lee_SmoothMix_A_Simple_Yet_Effective_Data_Augmentation_to_Train_Robust_CVPRW_2020_paper.html)           | 0.2       | CVPRW2020  | 67.54          | 80.25          | 66.69         | 81.18         | 78.87             | 81.31             |
| [SaliencyMix](https://arxiv.org/abs/2006.01791)        | 0.2       | ICLR2021   | 69.78          | 76.60          | 80.40         | 82.58         | 82.82             | 83.03             |
| [Attentive-CutMix](https://arxiv.org/abs/2003.13048)  | 2.0       | ICASSP2020 | 75.89          | 80.33          | 81.13         | 83.69         | 82.59             | 83.04             |
| [FMix](https://arxiv.org/abs/2002.12047)              | 1.0       | ArXiv      | 70.41          | 74.31          | 80.72         | 82.82         | 81.79             | 82.29             |
| [GridMix](https://www.sciencedirect.com/science/article/abs/pii/S0031320320303976)           | 1.0       | PR2021     | 68.86          | 74.96          | 78.54         | 80.79         | 79.53             | 79.66             |
| [ResizeMix](https://arxiv.org/abs/2012.11101)         | 1.0       | ArXiv      | 68.45          | 71.95          | 80.16         | 82.36         | 82.53             | 82.91             |
| [PuzzleMix](https://arxiv.org/abs/2009.06962)         | 2.0       | ICML2020   | 73.60          | 81.01          | 80.33         | 84.74         | 82.29             | 84.17             |
| [Co-Mixup](https://arxiv.org/abs/2102.03065)          | 2.0       | ICLR2021   | -              | -              | -             | -             | -                 | -                 |
| [AlignMix](https://arxiv.org/abs/2103.15375)          | 1.0       | CVPR2022   | -              | -              | 78.91         | 83.34         | 80.88             | 83.03             |
| [AutoMix](https://arxiv.org/abs/2103.13027)           | 2.0       | ECCV2022   | 76.24          | 80.91          | 82.67         | 84.05         | 83.30             | 84.79             |
| [SAMix](https://arxiv.org/abs/2111.15454)             | 2.0       | ArXiv      | 77.94          | 82.49          | 82.70         | 84.74         | 83.56             | 84.98             |
| [TransMix](https://arxiv.org/abs/2111.09833)          | "0.8,1.0" | CVPR2022   | 76.17          | 79.33          | 81.33         | 84.45         | -                 | -                 |
| [SMMix](https://arxiv.org/abs/2212.12977)             | "0.8,1.0" | ICCV2023   | 74.49          | 80.05          | 81.55         | -             | -                 | -                 |
| AdAutoMix         | 1.0       | ICLR2024   | -              | -              | 84.33         | 85.34         | 83.54             |                   |

## Tiny-ImageNet Epochs=400
| Name             | alpha | Conference | ResNet18 | ResNeXt50 |
|------------------|-------|------------|----------|-----------|
| Vanilla          | -     | -          | 61.68    | 65.04     |
| MixUp            | 1.0   | ICLR2018   | 63.86    | 66.36     |
| CutMix           | 0.2   | ICCV2019   | 65.53    | 66.47     |
| ManifoldMix      | 2.0   | ICML2019   | 64.15    | 67.30     |
| SmoothMix        | 0.2   | CVPRW2020  | 66.65    | 69.65     |
| SaliencyMix      | 0.2   | ICLR2021   | 64.40    | 66.55     |
| Attentive-CutMix | 2.0   | ICASSP2020 | 64.85    | 67.42     |
| FMix             | 0.2   | ArXiv      | 63.47    | 65.08     |
| GridMix          | 0.2   | PR2021     | 65.14    | 66.53     |
| ResizeMix        | 1.0   | ArXiv      | 63.17    | 65.87     |
| PuzzleMix        | 1.0   | ICML2020   | 65.81    | 67.83     |
| Co-Mixup         | 2.0   | ICLR2021   | 65.92    | 68.02     |
| AutoMix          | 2.0   | ECCV2022   | 67.33    | 70.72     |
| SAMix            | 2.0   | ArXiv      | 68.89    | 72.18     |
| AdAutoMix        | 1.0   | ICLR2024   | 69.19    | 72.89     |

## ImageNet-1K Epochs=100
| Name             | alpha | Conference | ResNet18 | ResNet34 | ResNet50 | ResNet101 | ResNeXt101 |
|------------------|-------|------------|----------|----------|----------|-----------|------------|
| Vanilla          | -     |            | 70.04    | 73.85    | 76.83    | 78.18     | 78.71      |
| MixUp            | 1.0   | ICLR2018   | 69.98    | 73.97    | 77.12    | 78.97     | 79.98      |
| CutMix           | 0.2   | ICCV2019   | 68.95    | 73.58    | 77.17    | 78.96     | 80.42      |
| ManifoldMix      | 2.0   | ICML2029   | 69.98    | 73.98    | 77.01    | 79.02     | 79.93      |
| SmoothMix        | 0.2   | CVPRW2020  | -        | -        | -        | -         | -          |
| SaliencyMix      | 0.2   | ICLR2021   | 69.16    | 73.56    | 77.14    | 79.32     | 80.27      |
| Attentive-CutMix | 2.0   | ICASSP2020 | -        | -        | -        | -         | -          |
| FMix             | 0.2   | ArXiv      | 69.96    | 74.08    | 77.19    | 79.09     | 80.06      |
| GridMix          | 0.2   | PR2021     | -        | -        | -        | -         | -          |
| ResizeMix        | 1.0   | ArXiv      | 69.50    | 73.88    | 77.42    | 79.27     | 80.55      |
| PuzzleMix        | 1.0   | ICML2020   | 70.12    | 74.26    | 77.54    | 79.43     | 80.53      |
| Co-Mixup         | 2.0   | ICLR2021   | -        | -        | -        | -         | -          |
| AutoMix          | 2.0   | ECCV2022   | 70.50    | 74.52    | 77.91    | 79.87     | 80.89      |
| SAMix            | 2.0   | ArXiv      | 70.83    | 74.95    | 78.06    | 80.05     | 80.98      |
| AdAutoMix        | 1.0   | ICLR2024   | 70.86    | 74.82    | 78.04    | 79.90     | 81.10      |

## Find-Grained
| Name             | alpha | Confrence  | CUB R18 | CUB R50 | CUB RX50 | FGVC R18 | FGVC RX50 | Cars R18 | Cars RX50 |
|------------------|-------|------------|---------|---------|----------|--------------------|---------------------|--------------------|---------------------|
| Vanilla          | -     |            | 77.68   | 82.38   | 83.01    | 80.23              | 85.1                | 86.32              | 90.15               |
| MixUp            | 1.0   | ICLR2018   | 78.39   | 82.98   | 84.58    | 79.52              | 85.18               | 86.27              | 90.81               |
| CutMix           | 0.2   | ICCV2019   | 78.40   | 83.17   | 85.68    | 78.84              | 84.55               | 87.48              | 91.22               |
| ManifoldMixup    | 2.0   | ICML2019   | 79.76   | 83.76   | 86.38    | 80.68              | 86.6                | 85.88              | 90.20               |
| SmoothMix        | 0.2   | CVPRW2020  | 76.42   | 82.78   | 82.84    | 75.01              | 83.26               | 84.28              | 89.23               |
| SaliencyMix      | 0.2   | ICLR2021   | 77.95   | 82.02   | 83.29    | 80.02              | 84.31               | 86.48              | 90.60               |
| AttentiveCutMix  | 2.0   | ICASSP2020 | 78.34   | 83.76   | 83.69    | 74.95              | 83.17               | 86.91              | 90.62               |
| FMix             | 0.2   | ArXiv      | 77.28   | 83.34   | 84.06    | 79.36              | 86.23               | 87.55              | 90.90               |
| GridMix          | 0.2   | PR2021     | 77.15   | 81.98   | 83.19    | 80.08              | 84.82               | 86.77              | 91.50               |
| ResizeMix        | 1.0   | ArXiv      | 78.5    | 83.41   | 84.77    | 78.1               | 84.08               | 88.17              | 91.36               |
| [SnapMix](https://arxiv.org/abs/2012.04846)          | 1.0   | AAAI2020   | 79.27   | 83.15   | 83.53    | 77.86              | 83.41               | 88.45              | 91.37               |
| PuzzleMix        | 1.0   | ICML2020   | 78.63   | 83.83   | 84.51    | 80.76              | 86.23               | 87.78              | 91.29               |
| Co-Mixup         | 2.0   | ICLR2021   | -       | -       | -        | -                  | -                   | -                  | -                   |
| AutoMix          | 2.0   | ECCV2022   | 79.87   | 83.88   | 86.56    | 81.37              | 86.72               | 88.89              | 91.38               |
| SAMix            | 2.0   | ArXiv      | 81.11   | 84.10   | 86.33    | 82.15              | 86.80               | 89.14              | 90.46               |
| AdAutoMix        | 1.0   | ICLR2024   | 80.88   | 84.57   | -        | 81.73              | 87.16               | 89.19              | 91.59               |

**You can visit this link for more Mixup methods：[Awesome-Mixup](https://github.com/Westlake-AI/Awesome-Mixup)**
