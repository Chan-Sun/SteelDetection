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


# dict(
#     type='AutoAugment',
#     policies=[[
#         dict(
#             type='Resize',
#             img_scale=[(480, 1333), (512, 1333), (544, 1333), (576, 1333),
#                         (608, 1333), (640, 1333), (672, 1333), (704, 1333),
#                         (736, 1333), (768, 1333), (800, 1333)],
#             multiscale_mode='value',
#             keep_ratio=True)
#     ],
#                 [
#                     dict(
#                         type='Resize',
#                         img_scale=[(400, 1333), (500, 1333), (600, 1333)],
#                         multiscale_mode='value',
#                         keep_ratio=True),
#                     dict(
#                         type='RandomCrop',
#                         crop_type='absolute_range',
#                         crop_size=(384, 600),
#                         allow_negative_crop=True),
#                     dict(
#                         type='Resize',
#                         img_scale=[(480, 1333), (512, 1333), (544, 1333),
#                                     (576, 1333), (608, 1333), (640, 1333),
#                                     (672, 1333), (704, 1333), (736, 1333),
#                                     (768, 1333), (800, 1333)],
#                         multiscale_mode='value',
#                         override=True,
#                         keep_ratio=True)
#                 ]]),