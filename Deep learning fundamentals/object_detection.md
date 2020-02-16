
# Object detection

## 1. Definition
### 1.1 What is the object detection?
Object detection is a common Computer Vision problem which deals with **identifying** and **locating** object of certain classes in the image.


There are four main subjects for computer vision:

**Classification**: solve `what is this` problem, giving a picture or a video to identify includes what kind of object.

**Location**: solve `where is it` problem, localization of the object.

**Detection**: solve `what is it? and where is it? `problem.

**Segmentation**: solve `every pixel belongs to which object or instance`, can be divided into `instance-level` and `scene-level`.

### 1.2 Problem statement for object detection?

Besides object classification, object detection need solve following key problem?

1. object can be found in any location in picture.

2. object size is different.

3. object shape is not the same.

### Object detection algorithm

Based on deep learning, object detection algoriths can be classified into two categories:

#### 1. Two stage algorithm for object detection

find a region proposal for a possible bounding box, then using convolutional neural network to classify the sampling.

Procedure: extract key metrics -> region proposal -> classification / regression.

Algorithms: `R-CNN`, `SPP-Net`, `Fast R-CNN`, `Faster R-CNN`, `R-FCN`.

#### 2. One stage algorithm for object detection

Without region proposal, extract information from network to predict object classification and location.

Procedure: extract key metrics -> classification / regression

Algorithms: `OverFeat`, `YOLOV1`, `YOLOv2`, `YOLOv3`, `SSD`, `RetinaNet`

#### 1.4 Application of object detection.

Object detection can be used in a broad industry, includes face detection, pedestrian detection, car detection, GIS, medical image analysis. In suivellence industry, like helmet detection, safety belt, area detection, object detection.


### R-CNN

1. Using `ConvNet` to calculate the region proposals and feature vectors. 

2. Using `ILSVRC` supervisored training and `PASCAL` small sampling `fine-tuning` to solve the overfitting.

