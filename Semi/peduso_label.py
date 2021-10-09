import json
import os
import argparse
import numpy as np

### Dataset info
# Train_dataset pic 3889 box 2312
# Val_dataset   pic 796
# Test_dataset  pic 1501

### coco format annotation
# {"segmentation": [[597.0, 59.0, 666.0, 59.0, 666.0, 97.0, 597.0, 97.0]], 
# "area": 2622.0, 
# "bbox": [597.0, 59.0, 69.0, 38.0], 
# "category_id": 3, 
# "id": 941, 
# "image_id": 794, 
# "iscrowd": 0, 
# "score": 0.5}, 

### test result format
# {'image_id': 0, 
# 'bbox': [484.6229248046875, 5.781468391418457, 39.712158203125, 92.45390605926514], 
# 'score': 0.9962002635002136, 
# 'category_id': 3}

def parse_args():
    parser = argparse.ArgumentParser(description='generate pesudo label')
    parser.add_argument('test_path', help='test_path')
    parser.add_argument('save_path', help='save_path')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    test_result = args.test_path
    save_path = args.save_path+"/pesudo_label.json"
    supervised_label = "/home/dlsuncheng/Steel_Defect/Dataset/Annotation/Annotation.json"
    blank_test = "/home/dlsuncheng/Dataset/Steel_Defect/Annotation/test.json"
    result=[]
    with open(test_result,'r') as load_f:
        test_json = json.load(load_f)
    with open(blank_test,'r') as load_f:
        blank_json = json.load(load_f)
    with open(supervised_label,"r") as load_f:
        label_json = json.load(load_f)   
    label_json["images"].extend(blank_json["images"])
    for info in test_json:
        bbox = [round(box,2) for box in info["bbox"]]
        segmentation = [[bbox[0],bbox[1],
                        bbox[0]+bbox[2],bbox[1],
                        bbox[0]+bbox[2],bbox[1]+bbox[3],
                        bbox[0],bbox[1]+bbox[3]]]
        area = bbox[2]*bbox[3]
        category_id = info["category_id"]
        id = len(label_json["annotations"])+1
        image_id = info["image_id"]
        score = round(info["score"],2)
        image_dict = {"segmentation":segmentation, "area":area,"bbox":bbox,"category_id":category_id,
                      "id":id,"image_id": image_id,"iscrowd": 0,"score":score},
        label_json["annotations"].append(image_dict)
    with open(save_path, 'w') as fp:
        json.dump(label_json, fp)
    print("convert sucess!")

if __name__ == '__main__':
    main()




