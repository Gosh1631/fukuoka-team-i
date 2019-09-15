from django.db import models

#推定に使うモジュールのインポート
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from PIL import Image
import io, base64
import cv2
import math

# Create your models here.
graph = tf.get_default_graph()
class Photo(models.Model):
    image = models.ImageField(upload_to='photos')

    IMAGE_SIZE = 224 # 画像サイズ
    MODEL_FILE_PATH ='./coin_cal/ml_models/param.hdf5' #モデルファイル

    # モデルの読込
    # 保存したjsonファイルとhdf5ファイルを読み込む。モデルを学習に使うにはcompileが必要。
    from keras.models import model_from_json

    # JSON形式のデータを読み込んでモデルとして復元。学習で使うにはまたコンパイルが必要なので注意。
    #with open('coin_cal.model', 'r') as f:
    #    json_string = f.read()
    #model = model_from_json(json_string)

    # モデルにパラメータを読み込む。前回の学習状態を引き継げる。
    


    def predict(self):
        model = None
        global graph
        with graph.as_default():
            model = load_model(self.MODEL_FILE_PATH)

            img_data = self.image.read()
            img_bin = io.BytesIO(img_data)

            def cut(in_img):
                img = Image.open(img_bin)
                gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                gray_img = cv2.GaussianBlur(gray_img, (7,7), 0)
                ret, bw_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)

                contours, hierarchy = cv2.findContours(bw_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
                        cv2.imwrite('result%d.jpg'%(len(coin_list)), cut_img2)
                        cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 200), 2)

                cv2.imwrite('sample_result.jpg', img)
                return len(coin_list)

                N = cut(img)
                
                in_X = np.empty((0,128,128,3))
                for i in range(N):
                    img = cv2.imread('result%d.jpg'%(i+1))
                    img = np.array([img])
                    in_X = np.concatenate((in_X, img), axis=0)
                
                #よそく
                y = np.empty((0,1))
                for index in range(N):
                    pred = model.predict(in_X[index].reshape(1,128,128,3)).argmax()
                    y = np.concatenate((y,[[pred]]), axis=0)
                y = np.where(y == 5,500,y)
                y = np.where(y == 4, 100, y)
                y = np.where(y == 3, 50, y)
                y = np.where(y == 2, 10, y)
                y = np.where(y == 1, 5, y)
                y = np.where(y == 0, 1, y)

                sum = 0

                for index in range(N):
                    plt.imshow(in_X[index]/256)
                    sum = sum + y[index]
                
                #print(sum)
    
    def image_src(self):
        with self.image.open() as img:
            based64_img = base64.base64encoding(img.read()).decode()

            return 'data:' + img.file.content_type + ';based64,' + based64_img