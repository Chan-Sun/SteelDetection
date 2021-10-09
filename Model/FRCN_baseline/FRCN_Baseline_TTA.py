_base_ = ["../../SteelMMdet/configs/_base_/models/faster_rcnn_r50_fpn.py",
          '../../SteelMMdet/configs/_base_/default_runtime.py',
          "../dataset_setting.py"]

# model settings
model = dict(roi_head=dict(bbox_head=dict(num_classes=5)))

# optimizer
optimizer = dict(type='SGD', lr=0.00125, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[17, 19])
runner = dict(type='EpochBasedRunner', max_epochs=24)
work_dir = "/home/dlsuncheng/Work_dir/Steel_Defect/20210927/Baseline_FRCN50/"

# uncomment below code to enable test time augmentations
# img_norm_cfg = dict(
#     mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
# test_pipeline = [
#     dict(type='LoadImageFromFile'),
#     dict(
#         type='MultiScaleFlipAug',
#         img_scale=[(600, 900), (800, 1200), (1000, 1500), (1200, 1800),
#                    (1400, 2100)],
#         flip=True,
#         transforms=[
#             dict(type='Resize', keep_ratio=True),
#             dict(type='RandomFlip', flip_ratio=0.5),
#             dict(type='Normalize', **img_norm_cfg),
#             dict(type='Pad', size_divisor=32),
#             dict(type='ImageToTensor', keys=['img']),
#             dict(type='Collect', keys=['img']),
#         ])
# ]
# data = dict(
#     val=dict(pipeline=test_pipeline),
#     test=dict(pipeline=test_pipeline))