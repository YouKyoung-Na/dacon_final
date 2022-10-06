import json
import os
import cv2
import matplotlib.pyplot as plt
import csv

i = 1
path = "./라벨링데이터"
file_lists = os.listdir(path)
# print(file_lists)

f = open('sub_train.csv', 'w', newline='\n')
wr = csv.writer(f)

for json_f in file_lists:

    path_ = path + "/" + json_f
    files = json.load(open(path_, encoding='utf-8'))
    print(files)

    for file in files['annotations']:
        # print(file)
        text = file["text"]
        if (text.find('x') != -1):
            continue
        wr.writerow([f"./train/train_{i}.png", text])
        i += 1