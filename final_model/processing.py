import json
import os
import cv2
import matplotlib.pyplot as plt

i = 0
file_path = "./라벨링데이터"
file_list = os.listdir(file_path)

# print(file_list)

for json_f in file_list:
    path = file_path + "/" + json_f
    file = json.load(open(path', encoding='utf-8))
    
    print("./원천데이터/" + file["images"][0]["file_name"])
    img = cv2.imread("./원천데이터/" + file["images"][0]["file_name"], cv2.IMREAD_COLOR)

    # print(type(img))
    
    
    
    break
    