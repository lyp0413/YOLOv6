import json
import shutil
import tqdm
import os
datapath="/home/lyp/Data/RPC"

if not os.path.exists("data/RPC"):
    os.makedirs("data/RPC/images/train")
    os.makedirs("data/RPC/images/val")
    os.makedirs("data/RPC/labels/train")
    os.makedirs("data/RPC/labels/val")

# # train2019 -> train
# train_label=json.load(open(os.path.join(datapath,"instances_train2019.json"),"rb"))
# id2img={}
# for item in tqdm.tqdm(train_label["images"]):
#     id2img[item["id"]]=[item["file_name"],item["width"],item["height"]]
#     shutil.copy(os.path.join(datapath,"train2019",item["file_name"]),"data/RPC/images/train")
# for anno in tqdm.tqdm(train_label["annotations"]):
#     image_id=anno["image_id"]
#     img=id2img[image_id][0]
#     name=img.split(".jpg")[0]
#     W=id2img[image_id][1]
#     H=id2img[image_id][2]
#     bbox=anno["bbox"]
#     category=0
#     x1,y1,w,h=bbox
#     cx=(x1+w/2)/W
#     cy=(y1+h/2)/H
#     w=w/W
#     h=h/H
#     with open("data/RPC/labels/train/%s.txt"%name,"a") as f:
#         f.write("%d %.4f %.4f %.4f %.4f\n"%(category,cx,cy,w,h))
#
# # test2019 -> train
# train_label=json.load(open(os.path.join(datapath,"instances_test2019.json"),"rb"))
# id2img={}
# for item in tqdm.tqdm(train_label["images"]):
#     id2img[item["id"]]=[item["file_name"],item["width"],item["height"]]
#     shutil.copy(os.path.join(datapath,"test2019",item["file_name"]),"data/RPC/images/train")
# for anno in tqdm.tqdm(train_label["annotations"]):
#     image_id=anno["image_id"]
#     img=id2img[image_id][0]
#     name=img.split(".jpg")[0]
#     W=id2img[image_id][1]
#     H=id2img[image_id][2]
#     bbox=anno["bbox"]
#     category=0
#     x1,y1,w,h=bbox
#     cx=(x1+w/2)/W
#     cy=(y1+h/2)/H
#     w=w/W
#     h=h/H
#     with open("data/RPC/labels/train/%s.txt"%name,"a") as f:
#         f.write("%d %.4f %.4f %.4f %.4f\n"%(category,cx,cy,w,h))

# val2019 -> val
val_label=json.load(open(os.path.join(datapath,"instances_val2019.json"),"rb"))
id2img={}
for item in tqdm.tqdm(val_label["images"]):
    id2img[item["id"]]=[item["file_name"],item["width"],item["height"]]
    shutil.copy(os.path.join(datapath,"val2019",item["file_name"]),"data/RPC/images/val")
for anno in tqdm.tqdm(val_label["annotations"]):
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
    with open("data/RPC/labels/val/%s.txt"%name,"a") as f:
        f.write("%d %.4f %.4f %.4f %.4f\n"%(category,cx,cy,w,h))
