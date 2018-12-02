# MLCrazi5
## This is just a test on our proj
## PLZ do NOT push to the main stream directly, always pull first, then create a new branch, push to the new branch, solve conflicts, and finally request merge, then confirm merge and always comment on each action.


For FeatureCompute.py, if you want to test it on you own server, be sure that your test environment has already been install Python3, opencv， opencv_contrib and relative package.

FeatureCompute.py provides a method to generate Training Data to train your classifier, and during the test stage, it also offers functions to turn each image or subimage into a feature vector, more details are noted in its docs.



# Object Detection


## Project Abstract
This project addresses the problem of detecting object location in object recognition. More specifically, we implements general classifiers with special feature detection algorithm to make a framework used to detect specific object locations in the image(in demo we use NBA basketball team Lakers logo). Instead of using deep learning frame such as RCNN or CNN, we combine SIFT and BOW, Selective Search and general classifier models into a single framework to improve time cost/performance. A bunch of objects, marked as positive or negative respectively, were later used to train our classifier. In the test stage, we sample some real world objects and try to detect them in photos.

## Project Introduction

<p align="center">
  <img src="flowchart.png" height="714" width="1054"><br/>
  <h6 align="center">Flowchart</h6><br/>
</p><br/>

* Feature Selection with SIFT(OpenCV), including:
  - Movie Name, Genre, Publish Year
  - Poster, Video Preview
  - Director(s), Actor(s)
  - Average Rating, etc.
* Support recommendations of:
  - TOP 10 best unseen movies for every different user and:
  - TOP 10 similar unseen similar movies for every specified movie that the user is checking on
* Support tracing each user's watching and rating history

## Dataset
We fetched the “MovieLens 1M Dataset” which was released in February 2003 from
[This Website](https://grouplens.org/datasets/movielens/)
* It generally contains 1 million ratings from 6,000 users on 4,000 movies, in the format of CSV.
* For the data of user rating, this dataset includes mainly: User, Rating and Movie.
* For the data of user info, this data set includes mainly: User, Gender, Age, Zip-code.
<br/>

We have also crawled
[IMDB](https://www.imdb.com)
to get  detail info about movies in the dataset mentioned above for better user experience.<br/>
A preview of what's the data looks like is shown below<br/>

<p align="center">
  <img src="dataset0.jpg" height="200" width="400"><br/>
  <h6 align="center">User Dataset</h6><br/>
</p><br/>

<p align="center">
  <img src="dataset0.jpg" height="200" width="400"><br/>
  <h6 align="center">User Dataset</h6><br/>
</p><br/>

<p align="center">
  <img src="dataset1.png" height="200" width="400"><br/>
  <h6 align="center">Movie Dataset</h6><br/>
</p><br/>

<p align="center">
  <img src="dataset2.png" height="200" width="400"><br/>
  <h6 align="center">Rating Dataset</h6><br/>
</p><br/>

## Methodology
We have implemented three recommend algorithms in this project:
  - User based collaborate filtering
  - Item based collaborate filtering
  - SVD (Singular Value Decomposition)
  - Word2Vec and CNN sentiment analysis

<br/>
Concepts are shown below as graphs:<br\>

<p align="center">
  <img src="cf0.png" height="200" width="600"><br/>
  <h6 align="center">Collaborative Filtering</h6><br/>
</p><br/>

<p align="center">
  <img src="cf1.png" height="200" width="600"><br/>
  <h6 align="center">Item-Based Collaborative Filtering</h6><br/>
</p><br/>

<p align="center">
  <img src="cf2.png" height="200" width="600"><br/>
  <h6 align="center">User-Based Collaborative Filtering</h6><br/>
</p><br/>

## Evaluation
We used Root Mean Squared Error (RMSE) for evaluation:<br/>

<p align="center">
  <img src="RMSE.png" height="80" width="250"><br/>
  <h6 align="center">RMSE Function</h6><br/>
</p><br/>


And the evaluation result is:




## DEMO Implement
We used Python Django as backend to implement our project.
1. Environment Setup: -- Windows 10, Python 3.6.4, mysql 5.7.21, mysql bench 6.3 CE
2. Python Requirement Packages: -- numpy, pandas, imdbpie, imdbpy, sklearn
3. App start up by: -- Python manage.py runserver 8080, Open in the browser 127.0.0.1:8080

## Project Output
<p align="center">
  <img src="demo0.png" height="350" width="800"><br/>
  <h6 align="center">Login Page</h6><br/>
</p><br/>

<p align="center">
  <img src="demo1.png" height="350" width="800"><br/>
  <h6 align="center">Home Page</h6><br/>
</p><br/>


<p align="center">
  <img src="demo2.png" height="350" width="800"><br/>
  <h6 align="center">Search</h6><br/>
</p><br/>

<p align="center">
  <img src="demo3.png" height="350" width="800"><br/>
  <h6 align="center">Movie Detail</h6><br/>
</p><br/>


<p align="center">
  <img src="demo4.png" height="350" width="800"><br/>
  <h6 align="center">Movie Recommendation</h6><br/>
</p><br/>


<p align="center">
  <img src="demo5.png" height="350" width="800"><br/>
  <h6 align="center">User Profile</h6><br/>
</p><br/>


<p align="center">
  <img src="demo6.png" height="350" width="800"><br/>
  <h6 align="center">Recommend Movie for User</h6><br/>
</p><br/>
