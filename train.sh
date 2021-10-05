### train
# ####mask rcnn dcn
# python /home/hustwen/sun_chen/SteelDetection/SteelMMdet/tools/train.py \
#        /home/hustwen/sun_chen/SteelDetection/model/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco_OHEM.py --gpu-ids 1


python /home/hustwen/sun_chen/SteelDetection/SteelMMdet/tools/train.py \
       /home/hustwen/sun_chen/SteelDetection/model/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco_context_block.py --gpu-ids 1
       # /home/hustwen/sun_chen/SteelDetection/model/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco_mixup.py --gpu-ids 1


# python /home/hustwen/sun_chen/SteelDetection/SteelMMdet/tools/train.py \
#        /home/hustwen/sun_chen/SteelDetection/model/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco_global_context.py --gpu-ids 1

# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/test.py \
#     /home/dlsuncheng/Steel_Defect/model/Mask-RCNN/mask_rcnn_r101_fpn_dconv_c3-c5_1x_coco.py \
#     /home/dlsuncheng/Work_dir/Steel_Defect/20210929/mask/dcn/epoch_24.pth \
#     --format-only \
#     --options "jsonfile_prefix=./Submit/mask_dcn_test_result"

# python /home/dlsuncheng/Steel_Defect/Submit/submit_convert.py \
#         ./Submit/mask_dcn_test_result.bbox.json \
#         ./Submit/mask_dcn_test_result.json

# ####casacde r101
# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/train.py \
#       /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_r101_fpn_1x_coco.py --gpu-ids 1

# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/test.py \
#     /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_r101_fpn_1x_coco.py \
#     /home/dlsuncheng/Work_dir/Steel_Defect/20210928/cascade/baseline/epoch_24.pth \
#     --format-only \
#     --options "jsonfile_prefix=./Submit/cascade_baseline_test_result"

# python /home/dlsuncheng/Steel_Defect/Submit/submit_convert.py \
#         ./Submit/cascade_baseline_test_result.bbox.json \
#         ./Submit/cascade_baseline_test_result.json

# ####casacde r101 dcn
# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/train.py \
#     /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco.py --gpu-ids 1

# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/test.py \
#     /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_r101_fpn_dconv_c3-c5_1x_coco.py \
#     /home/dlsuncheng/Work_dir/Steel_Defect/20210928/cascade/dcn/epoch_24.pth \
#     --format-only \
#     --options "jsonfile_prefix=./Submit/cascade_dcn_test_result"

#####casacde r101 s101
# CUDA_VISIBLE_DEVICES=1,2 bash /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/dist_train.sh \
#     /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_s101_fpn_syncbn-backbone+head_mstrain-range_1x_coco.py 2

####casacde x101
# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/train.py \
#     /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco.py --gpu-ids 2

# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/test.py \
#     /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco.py \
#     /home/dlsuncheng/Work_dir/Steel_Defect/20210928/cascade/x101/epoch_24.pth \
#     --format-only \
#     --options "jsonfile_prefix=./Submit/cascade_x101_test_result"

# python /home/dlsuncheng/Steel_Defect/Submit/submit_convert.py \
#         ./Submit/cascade_x101_test_result.bbox.json \
#         ./Submit/cascade_x101_test_result.json

####casacde x101 dcn
# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/train.py \
#     /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_dconv_c3-c5_1x_coco.py --gpu-ids 2

# python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/test.py \
#     /home/dlsuncheng/Steel_Defect/model/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_dconv_c3-c5_1x_coco.py \
#     /home/dlsuncheng/Work_dir/Steel_Defect/20210928/cascade/x101_dcn/epoch_24.pth \
#     --format-only \
#     --options "jsonfile_prefix=./Submit/cascade_x101_test_result"