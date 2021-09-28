### train
python /home/dlsuncheng/Steel_Defect/SteelMMdet/tools/train.py \
        /home/dlsuncheng/Steel_Defect/model/FRCN_baseline/FRCN_Baseline_ratio.py \
       --gpu-ids 1

### test
# python ./SteelMMdet/tools/test.py \
#     /home/dlsuncheng/Steel_Defect/model/FRCN_Baseline.py \
#     /home/dlsuncheng/Work_dir/Steel_Defect/20210927/Baseline_FRCN50/epoch_24.pth \
#     --format-only \
#     --options "jsonfile_prefix=./Submit/FRCN_baseline_test_result"
    
#     # --eval mAP\
#     # --show xxx\
#     # --show_dir xxx\
#     # --out results.pkl\
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