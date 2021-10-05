_base_ = './cascade_rcnn_r101_fpn_1x_coco.py'
work_dir = "/home/hustwen/sun_chen/Work_dir/Steel_Defect/20211005/cascade_x101/context_block/"

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
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch',
        plugins=[
            dict(
                cfg=dict(type='ContextBlock', ratio=1. / 16),
                stages=(False, True, True, True),
                position='after_conv3')
        ],
        init_cfg=dict(
            type='Pretrained', checkpoint='open-mmlab://resnext101_64x4d')),      
    )