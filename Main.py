from SelectiveSearch import regionGenerate
#from ClassifierModel import TrainingModel
from FeatureCompute import FeatureCompute
import matplotlib.pyplot as plt

import numpy as np
import cv2 as cv
import datetime
import os
import operator as op

if __name__ == '__main__':
    while (1):
        object = input("detect object:")
        if (op.eq(object, 'Lakers') == 1):
            para = 'Lakers'
        elif (op.eq(object, 'Toy') == 1):
            para = 'Toy'
        elif (op.eq(object, 'Exit') == 1):
            print("Exit")
            break;
        else:
            print("Illegal input")
            continue;
        generator = FeatureCompute(300,70)
        dir = os.getcwd()
        for count in range(len(os.listdir())):
            filename = dir + '/' + str(count) + '.jpg'
            img = cv.imread(filename)
            print(filename)
            plt.imshow(img),plt.show()
            regions = regionGenerate(img)
            data = np.float32([]).reshape(0,Generator.wordCnt)
            for rect in regions:
                phi = generator.generatePhi(rect(1), para)
                data = np.append(data, phi, axis=0)
            '''
            get response from predictor

            i = max()....

            '''
            locaiton = regions[i][0]
            cv2.rectangle(img, (location[0],location[1]),
                         (location[2],location[3]),
                         (0,255,0), 4)
            plt.imshow(img),plt.show()
