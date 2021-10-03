import json
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Convert to cubmit version')
    parser.add_argument('test_path', help='test_path')
    parser.add_argument('save_path', help='save_path')

    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    test_result = args.test_path
    save_path = args.save_path
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
    with open(save_path, 'w') as fp:
        json.dump(result, fp, indent=4, separators=(',', ': '))
    print("convert sucess!")


if __name__ == '__main__':
    main()




