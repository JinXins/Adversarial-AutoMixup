# dataset settings
data_source_cfg = dict(type='CIFAR_C', root='data/CIFAR100C/')

dataset_type = 'ClassificationDataset'
img_norm_cfg = dict(mean=[0.4914, 0.4822, 0.4465], std=[0.2023, 0.1994, 0.201])
train_pipeline = [
    dict(type='RandomResizedCrop', size=224, scale=[0.8, 1], interpolation=3),  # bicubic
    dict(type='RandomHorizontalFlip'),
]
test_pipeline = [
    dict(type='Resize', size=224, interpolation=3),
]
# prefetch
prefetch = False
if not prefetch:
    train_pipeline.extend([dict(type='ToTensor'), dict(type='Normalize', **img_norm_cfg)])
test_pipeline.extend([dict(type='ToTensor'), dict(type='Normalize', **img_norm_cfg)])

data = dict(
    imgs_per_gpu=100,  # 100 x 1gpu = 100
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        data_source=dict(split='train', **data_source_cfg),
        pipeline=train_pipeline,
        prefetch=prefetch,
    ),
    val=dict(
        type=dataset_type,
        data_source=dict(split='test', **data_source_cfg),
        pipeline=test_pipeline,
        prefetch=False),
)

# validation hook
evaluation = dict(
    initial=False,
    interval=1,
    imgs_per_gpu=100,
    workers_per_gpu=4,
    eval_param=dict(topk=(1, 5)),
    save_best='auto')

# checkpoint
checkpoint_config = dict(interval=10, max_keep_ckpts=1)
