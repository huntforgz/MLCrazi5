'''
Created on 2018-11-12

@author: Zhaoyu Sun
'''
import cv2 as cv
import numpy as np


class FeatureCompute(object):

	'''
	A class generate feature vector for image or subimage by SIFT and BOW.

	Var:
		dir: current direcotry
		num_phi: # of SIFT feature points
		num_img: # of images
		wordCnt: dimension of final output
		iterTime: parameter for cv.Kmeans,iteration times
		explosion: parameter for cv.Kmeans,tolerance

	Func:
		calcSiftFeature
		calcFeatVec
		initFeatureSet
		learnVocabulary
	'''

	def __init__(self, dir, num_img, num_phi = 200,
				 wordCnt=50, iterTime=20, explosion=0.1):
		self.dir = dir
		self.num_phi = num_phi
		self.num_img = num_img
		self.wordCnt = wordCnt
		self.iterTime = iterTime
		self.explosion = explosion

	def _calcSiftFeature(self, img):
		'''
		Method to compute SIFT features.
		Params:
			img: ndarray
		Returns:
			n * 128 ndarray, n equals to num_phi
		'''
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		sift = cv.xfeatures2d_SIFT.create(self.num_phi)
		kp, des = sift.detectAndCompute(gray, None)
		return des

	def _initFeatureSet(self):
		'''
		Method to initialize SIFT features of all images, the features are
		stored in /features/phi.npy
		Params:
			None
		Returns:
			None
		'''
		featureSet = np.float32([]).reshape(0,128)
		print("Extract features from TrainSet :\n")
		for count in range(self.num_img):
			filename = self.dir + "/Image/" + str(count + 1) + '.jpg'
			img = cv.imread(filename)
			des = calcSiftFeature(img)
			featureSet = np.append(featureSet, des, axis=0)
			featCnt = featureSet.shape[0]
		print(str(featCnt) + " features in "
			+ str(self.num_img) + " images\n")
		# save featureSet to file
		filename = self.dir + "/features/" + "phi.npy"
		np.save(filename, featureSet)
		print("Finsh Initializing Phi")

	def _learnVocabulary(self):
		'''
		Method to Compute Kmeans Centers and implement BOW, Centers and Lables
		are stored in /vocabulary/bow.npy
		Params:
			None
		Returns:
			None
		'''
		filename = self.dir + "/features/" + "phi.npy"
		try:
			features = np.load(filename)
		except :
			print("SIFT feature file doesn't exist!!!")
		print("Learn vocabulary ...")
		# use k-means to implement BOW
		criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,
					self.iterTime, self.explosion)
		flags = cv.KMEANS_RANDOM_CENTERS
		# PP_Center??
		compactness, labels, centers = cv.kmeans(features, self.wordCnt, None,
												 criteria, self.iterTime, flags)
		filename = self.dir + "/vocabulary/" + "bow.npy"
		np.save(filename, (labels, centers))
		print("Finish BOW\n")

	def _calcFeatVec(self, feature, centers):
		'''
		Method to compute feature vector for each image/subimage
		Params:
			None
		Return:
			1 * wordCnt vector
		'''
		# feature: sift feature, m * 128 vector, m = # of feature points
		# centers: k-means centers
		featVec = np.zeros((1, self.wordCnt))
		for i in range(0, features.shape[0]):
			fi = features[i]
			diffMat = np.tile(fi, (50, 1)) - centers
			sqSum = (diffMat**2).sum(axis=1)
			dist = sqSum**0.5
			sortedIndices = dist.argsort()
			idx = sortedIndices[0] # index of the nearest center
			featVec[0][idx] += 1
		return featVec

	def generateTrainData(self, num_pos, num_neg):
		trainData = np.float32([]).reshape(0, 50)
		response = np.float32([])
		try:
			labels, centers = np.load(self.dir + "/vocabulary/" + "bow.npy")
		except Exception as e:
			print("No Vocabulary file!!")
		for count in range(num_pos):
			filename = self.dir + "/TrainingData/Positive" + str(count + 1) + '.jpg'
			img = cv.imread(filename)
			features = self.calcSiftFeature(img)
			featVec = self.calcFeatVec(features, centers)
			trainData = np.append(trainData, featVec, axis=0)
		pos_label = np.repeat(np.float32([1]), count)
		response = np.append(response, pos_label)
		for count in range(num_neg):
			filename = self.dir + "/TrainingData/Negative" + str(count + 1) + '.jpg'
			img = cv.imread(filename)
			features = self.calcSiftFeature(img)
			featVec = self.calcFeatVec(features, centers)
			trainData = np.append(trainData, featVec, axis=0)
		neg_label = np.repeat(np.float32([0],count))
		response = np.append(response, neg_label)
		response.reshape(-1, 1)
		return (trainData, response)

	def initialize(self):
		self._initFeatureSet()
		self._learnVocabulary()

	def generatePhi(self, img):
		self._calcSiftFeature(img)
		try:
			labels, centers = np.load(self.dir + "/vocabulary/" + "bow.npy")
		except Exception as e:
			print("No Vocabulary file!!")
		featVec = self.calcFeatVec(features, centers)
		return featVec
