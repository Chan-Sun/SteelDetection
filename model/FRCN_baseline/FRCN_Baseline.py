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
