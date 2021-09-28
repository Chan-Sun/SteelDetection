_base_ = ["../../SteelMMdet/configs/_base_/models/cascade_rcnn_r50_fpn.py",
          '../../SteelMMdet/configs/_base_/default_runtime.py',
          "../dataset_setting.py"]

model = dict(
    type='CascadeRCNN',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        dcn=dict(type='DCN', deform_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True),
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch',
        init_cfg=dict(
            type='Pretrained', checkpoint='open-mmlab://resnext101_64x4d')))

# learning policy
optimizer = dict(type='SGD', lr=0.00125, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

log_config = dict(
    interval=5,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[16, 19])
runner = dict(type='EpochBasedRunner', max_epochs=24)
work_dir = "/home/dlsuncheng/Work_dir/Steel_Defect/20210927/Cascade_RCNN/X101_DCN"