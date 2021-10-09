_base_ = ["../../SteelMMdet/configs/_base_/models/faster_rcnn_r50_fpn.py",
          '../../SteelMMdet/configs/_base_/default_runtime.py',
          "../dataset_setting.py"]

# model settings
model = dict(roi_head=dict(bbox_head=dict(num_classes=5)),
            rpn_head=dict(
                anchor_generator=dict(
                    type='AnchorGenerator',
                    scales=[8],
                    ratios=[0.1,0.2,0.5, 1.0, 2.0,5.0,10],
                    strides=[4, 8, 16, 32, 64]),))

# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[17, 19])
runner = dict(type='EpochBasedRunner', max_epochs=24)
work_dir = "/home/dlsuncheng/Work_dir/Steel_Defect/20210928/Baseline_FRCN50/Ratio/"