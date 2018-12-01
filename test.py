import cv2 as cv
import os
import numpy as np
from ClassifierModel import TrainingModel
from FeatureCompute import FeatureCompute

if __name__ == '__main__':
    classifier = TrainingModel()
    generator = FeatureCompute(300,70)
    dir = os.getcwd() + '/bbs'
    data = np.float32([]).reshape(0,generator.wordCnt)
    for count in range(len(os.listdir(dir)) - 1):
        filename = dir + '/' + str(count) + '.jpg'
        print(filename)
        img = cv.imread(filename)
        phi = generator.generatePhi(img, 'Lakers')
        data = np.append(data, phi, axis=0)
    data = np.mat(data)
    print(data.shape)
    print(type(data))
    response = classifier.Predict(data, 'LakerSVM.sav')
    print(response)
    print(type(response))
    i = np.argmax(response)
    print(i)
    # print(data.shape)
    # print(type(data))
    # a = np.save('tes.npy', data)
