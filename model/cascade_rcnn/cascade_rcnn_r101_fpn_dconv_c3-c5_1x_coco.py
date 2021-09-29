_base_ = './cascade_rcnn_r101_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        dcn=dict(type='DCN', deform_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True),
        )
        )
work_dir = "/home/dlsuncheng/Work_dir/Steel_Defect/20210928/cascade/dcn"
