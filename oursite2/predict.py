# モデルの読込
# 保存したjsonファイルとhdf5ファイルを読み込む。モデルを学習に使うにはcompileが必要。
from keras.models import model_from_json

# JSON形式のデータを読み込んでモデルとして復元。学習で使うにはまたコンパイルが必要なので注意。
with open('coin_cal.model', 'r') as f:
    json_string = f.read()
model = model_from_json(json_string)

# モデルにパラメータを読み込む。前回の学習状態を引き継げる。
model.load_weights('param.hdf5')
print('Loaded the model.')

import cv2
import matplotlib.pyplot as plt
import math

#画像からコインを抽出する関数を定義
def cut(in_img):
    img = cv2.imread(in_img)
    
    plt.imshow(img)
    plt.show()
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (7,7), 0)
    ret, bw_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)

    imgEdge, contours, hierarchy = cv2.findContours(bw_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ROUNDNESS_THRESH = 0.9
    coin_list = []
    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        longAx = width
        if (width < height):
            longAx = height
        roundness = (4*area)/(math.pi*(longAx**2)) # it seems like a circle closer to 1.0

        if (roundness > ROUNDNESS_THRESH):
            coin_list.append(roundness)
            topleft = x
            
            cut_img = img[y:y+longAx, x:x+longAx]
            
            cut_img2 = cv2.resize(cut_img , (128, 128))
            
            plt.imshow(cut_img2)
            plt.show()
            
            cv2.imwrite('result%d.jpg'%(len(coin_list)), cut_img2)
            cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 200), 2)
            
    plt.imshow(img)
    plt.show()
    cv2.imwrite('sample_result.jpg', img)
    
    return len(coin_list)

  import numpy as np

#計算
def coin_cal(img):
    #画像を入力
    N = cut(img)
    print('%d枚の硬貨があります。'%N)
    
    #X作成
    in_X = np.empty((0, 128, 128, 3))
    for i in range(N):
        img = cv2.imread('result%d.jpg'%(i+1))
        img = np.array([img])
        in_X = np.concatenate((in_X, img), axis=0)
    
    #予測
    y = np.empty((0, 1))
    for index in range(N):
        pred = model.predict(in_X[index].reshape(1, 128, 128,3)).argmax()
        y = np.concatenate((y, [[pred]]), axis=0)
    y = np.where(y == 5, 500, y)
    y = np.where(y == 4, 100, y)
    y = np.where(y == 3, 50, y)
    y = np.where(y == 2, 10, y)
    y = np.where(y == 1, 5, y)
    y = np.where(y == 0, 1, y)
    
    #予測を出力
    sum = 0

    for index in range(N):
        plt.imshow(in_X[index]/256)
        plt.show()
        print('これは%d円です'%y[index])
        sum = sum + y[index]

    print('全部で%d円です'%sum)  