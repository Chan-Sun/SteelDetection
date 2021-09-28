from inspect import FrameInfo
import random
from PIL import Image, ImageDraw
from pycocotools.coco import COCO
import argparse
import json
import os
from tqdm import tqdm

classes = ["iron_oxide","cracked_skin","rolling_cycle","slag_inclusion","iron_gray"]
# classes = ["or", "crack", "indentation", "slag", "ash"]



def parse_args():
    parser = argparse.ArgumentParser(description='Visualize images')
    parser.add_argument('img_path', help='img_path')
    parser.add_argument('anno_path', help='anno_path')
    parser.add_argument('save_path', help='save_path')

    args = parser.parse_args()
    return args

def draw_bbox(img_path,ann_file,save_path):
    coco = COCO(ann_file)
    for img_id in tqdm(range(1,len(coco.dataset["images"])+1)):
        img_info = coco.loadImgs(img_id)[0]
        img_file = img_path+ img_info['file_name']
        img = Image.open(img_file)
        draw = ImageDraw.Draw(img)
        if coco.getAnnIds(img_id):
            print(img_file)
            for anno_ids in coco.getAnnIds(img_id):
                annos = coco.loadAnns(anno_ids)
                for anno in annos:
                    x, y, w, h = anno['bbox']
                    bbox = (int(x), int(y), int(x+w), int(y+h))
                    draw.rectangle(bbox, fill=None, outline='red', width=5)
                    category = classes[anno['category_id']-1]
                    draw.text((int(x), int(y)), category)
            if not os.path.exists(save_path+'/'+category+'/'):
                os.mkdir(save_path+'/'+category+'/')
            img.save(save_path+'/'+category+'/'+img_info['file_name'])
        else:
            print("negative:{}".format(img_file))
            if not os.path.exists(save_path+'/negative/'):
                os.mkdir(save_path+'/negative/')
            img.save(save_path+'/negative/'+img_info['file_name'])

def main():
    args = parse_args()
    img_path = args.img_path
    anno_path = args.anno_path
    save_path = args.save_path
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    draw_bbox(img_path,anno_path,save_path)

if __name__ == '__main__':
    main()


# def show_img_cat(cat_name, id=None):
#     ann_file = 'data/train_all.json'
#     coco = COCO(ann_file)
#     cat_id = coco.getCatIds(cat_name)[0]
#     if id is None:
#         img_ids = coco.catToImgs[cat_id]
#         img_id = random.choice(img_ids)
#     else:
#         img_id = id
#     img_info = coco.loadImgs(img_id)[0]
#     anno_ids = coco.getAnnIds(img_id)[0]
#     annos = coco.loadAnns(anno_ids)
#     img_path = 'data/train_all/' + img_info['file_name']
#     img = Image.open(img_path)
#     draw = ImageDraw.Draw(img)
#     for anno in annos:
#         if anno['category_id'] == cat_id:
#             x, y, w, h = anno['bbox']
#             bbox = (int(x), int(y), int(x+w), int(y+h))
#             draw.rectangle(bbox, fill=None, outline='red', width=5)

#     img.show()