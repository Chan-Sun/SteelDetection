_base_ = ['./cascade_rcnn_new_baseline.py',
          '../../SteelMMdet/configs/_base_/default_runtime.py',
          "../dataset_setting/detection_setting_ms_small.py",]

classes = ("iron_gray","rolling_cycle")
data = dict(
    train=dict(classes=classes),
    val=dict(classes=classes),
    test=dict(classes=classes))

work_dir = "/home/dlsuncheng/Work_dir/Steel_Defect/20211009/cascade/part_data"

# optimizer
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[17, 19])
runner = dict(type='EpochBasedRunner', max_epochs=24)

model = dict(
    type='CascadeRCNN',
    rpn_head=dict(
        type='RPNHead',
        in_channels=256,
        feat_channels=256,
        anchor_generator=dict(
            type='AnchorGenerator',
            scales=[4,8],
            ratios=[0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0],
            strides=[4, 8, 16, 32, 64])),
    roi_head=dict(
        type='CascadeRoIHead',
        num_stages=3,
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                num_classes=2,),
            dict(
                type='Shared2FCBBoxHead',
                num_classes=2,),
            dict(
                type='Shared2FCBBoxHead',
                num_classes=2,),
                ]),
        )