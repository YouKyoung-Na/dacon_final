import json
import os
import cv2
import matplotlib.pyplot as plt

file_path = "./라벨링데이터"
file_list = os.listdir(file_path)
# print(file_list)


"""이미지 데이터 크롭 및 파일 생성"""
def crop_img():
    i = 1
    for json_f in file_list:
        path = file_path + "/" + json_f
        file = json.load(open(path, encoding='utf-8'))
    
    img = cv2.imread("./원천데이터/" + file["images"][0]["file_name"], cv2.IMREAD_COLOR)
    
    datas = []
    
    for val in file['annotations']:
        
        text = val["text"]
        if (text.find('x') != -1):
            continue

        datas.append(val['bbox'])


    for j in datas:
        x1 = j[0]
        x2 = j[0]+j[2]
        y1 = j[1]
        y2 = j[1]+j[3]

        cut_image = img[y1:y2, x1:x2].copy()

        cv2.imwrite(f'./p_train/train_{i}.png', cut_image)
        i += 1

        break


crop_img()