import json
import os
test_result = "/home/dlsuncheng/Steel_Defect/Submit/FRCN_baseline_test_result.bbox.json"
blank_test = "/home/dlsuncheng/Steel_Defect/Dataset/Annotation/test.json"

result=[]
with open(test_result,'r') as load_f:
    test_json = json.load(load_f)
with open(blank_test,'r') as load_f:
    info_json = json.load(load_f)
    
for image in test_json:
    index = image["image_id"]
    _,image_name = os.path.split(info_json["images"][index]["file_name"])
    test_image_info = {'name':image_name,'category_id':image["category_id"],'bbox':[round(num,2) for num in image["bbox"]],'score':image["score"]}
    result.append(test_image_info)
with open('./Submit/result.json', 'w') as fp:
    json.dump(result, fp, indent=4, separators=(',', ': '))