import json
import shutil
import tqdm
import os
datapath="/home/lyp/Data/coco2017"
whitelist=["bottle","wine glass","cup","fork","knife","spoon","bowl","banana","apple",
           "sandwich","orange","broccoli","carrot","hotdog","mouse","cell phone",
           "scissors","teddy bear","toothbrush"]
# whitelist=["person"]



if not os.path.exists("data/coco2017"):
    os.makedirs("data/coco2017/images/train")
    os.makedirs("data/coco2017/images/val")
    os.makedirs("data/coco2017/labels/train")
    os.makedirs("data/coco2017/labels/val")

train_label=json.load(open(os.path.join(datapath,"annotations/instances_train2017.json"),"rb"))
id2cat={}
for item in train_label["categories"]:
    id2cat[item["id"]]=item["name"]
id2img={}
for item in tqdm.tqdm(train_label["images"]):
    id2img[item["id"]]=[item["file_name"],item["width"],item["height"]]
for anno in tqdm.tqdm(train_label["annotations"]):
    if id2cat[anno["category_id"]] not in whitelist:
        continue
    image_id=anno["image_id"]
    img=id2img[image_id][0]
    name=img.split(".jpg")[0]
    W=id2img[image_id][1]
    H=id2img[image_id][2]
    bbox=anno["bbox"]
    category=0
    x1,y1,w,h=bbox
    cx=(x1+w/2)/W
    cy=(y1+h/2)/H
    w=w/W
    h=h/H
    with open("data/coco2017/labels/train/%s.txt"%name,"a") as f:
        f.write("%d %.4f %.4f %.4f %.4f\n"%(category,cx,cy,w,h))

val_label=json.load(open(os.path.join(datapath,"annotations/instances_val2017.json"),"rb"))
id2img={}
for item in tqdm.tqdm(val_label["images"]):
    id2img[item["id"]]=[item["file_name"],item["width"],item["height"]]
for anno in tqdm.tqdm(val_label["annotations"]):
    if id2cat[anno["category_id"]] not in whitelist:
        continue
    image_id=anno["image_id"]
    img=id2img[image_id][0]
    name=img.split(".jpg")[0]
    W=id2img[image_id][1]
    H=id2img[image_id][2]
    bbox=anno["bbox"]
    category=0
    x1,y1,w,h=bbox
    cx=(x1+w/2)/W
    cy=(y1+h/2)/H
    w=w/W
    h=h/H
    with open("data/coco2017/labels/val/%s.txt"%name,"a") as f:
        f.write("%d %.4f %.4f %.4f %.4f\n"%(category,cx,cy,w,h))