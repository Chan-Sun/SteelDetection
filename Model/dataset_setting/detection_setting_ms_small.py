# dataset settings
dataset_type = 'CocoDataset'
data_root = '/home/dlsuncheng/Dataset/Steel_Defect/'

albu_train_transforms = [
    dict(
    type = "CopyPaste",
    blend=True, sigma=1, pct_objects_paste=0.5, p=1)
]

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='InstaBoost',
        action_candidate=('normal', 'horizontal', 'skip'),
        action_prob=(1, 0, 0),
        scale=(0.8, 1.2),
        dx=15,
        dy=15,
        theta=(-1, 1),
        color_prob=0.5,
        hflag=False,
        aug_ratio=0.5),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),

    dict(type='Resize', img_scale=[(2666, 1600),(1333, 800)], keep_ratio=True),
    dict(
        type='RandomFlip',
        flip_ratio=[0.25, 0.25, 0.25],
        direction=['horizontal', 'vertical', 'diagonal']),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', 
        keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=[(1333, 800),(2000, 1200),(2666, 1600)],
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file=data_root + '/Annotation/train.json',
        img_prefix=data_root + '/Train_Val/',
        pipeline=train_pipeline,
        filter_empty_gt=True),
    val=dict(
        type=dataset_type,
        ann_file=data_root + '/Annotation/val.json',
        img_prefix=data_root + '/Train_Val/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + '/Annotation/final.json',
        img_prefix=data_root + '/Final/',
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='bbox')
