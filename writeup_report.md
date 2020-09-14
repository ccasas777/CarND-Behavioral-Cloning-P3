# **Behavioral Cloning** 

## Writeup 
### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/NVIDIA.jpg "Model Visualization"
[image2]: ./examples/data_dis.jpg "distribution of data(initial)"
[image3]: ./examples/mod_data_dis.jpg "Recovery Image"
[image4]: ./examples/direction.jpg "Recovery Image"
[image5]: ./examples/special.jpg "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"


---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```
#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.


### Project Files
|  Filename   |   Description  | 
|:-------------:|:-------------:|
| data generator.ipynb |  ipython notebook for data preprocessing and argumentation |
| model.py | define and train the neual network |
| model.h5 | saved model by keras |
| drive.py | communicate with simulator and use saved model to predict steering angle  |
| video.ogv | track 1 video record |



### Model Architecture and Training Strategy

### Data Preprocessing & Argumentation

The data Preprocessing and argumentation are in data generator.ipynb

The distribution of data is not good to use to train as the histogram

![alt text][image2]

At the beginning, I throw it into training. The car's behavior don't know how to afford the sharp turn. 
Therefore, I do some modification for the distribution of data.
***
1. add the different camera view including the correction of steering
2. throw out the data of the steering in zero (not including number of close zero )
3. throw out the data of the car speed less than 15
4. blur the steering by multiplying a random number 0-0.1 based on the steering value itself.
***
   
The reason is the data of the steering in zero is very non-useful to learn, and, in playing, the actual steering is not only one solution.
We may choose blue direction to keep or slightly modify the direction or maybe the red direction making the car back to road center.
Both of the solution are the "right" direction in playing. 

![alt text][image4]

The result looks very good:

![alt text][image3]

Before augmentation I play again with inverse race.
Applying some augmentations like:
1. flip the image
2. random the brightness and vertical shift two times. (mean the data would be double)
 
So the data size become the 4 times of the original size.
The final size of X_train_easy data for simple race is up to  1.6G and for complicated race is up to 10 G! 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

My first step was to use a LeNnet convolution neural network that we used before, but it doen't work well enough.
Sometimes, it doen't distinguish the edge well. 
Then I apply the NVIDIA self driving car network model. Initially, it already work very well in the simple race.
And, I try it into complicated race. I found it still doen't distinguish the special stuffs that around the road as:

 ![alt text][image5]

I added two dropout layers, and cropped the image from 160x320 to 76x320 leaving the useful range. The model become very reliable and also in the simple race. 
#### 2. Final Model Architecture

Here is my visualization of the architecture which manly referred NVIDIA self driving car network model

![alt text][image1]

#### 2. Result

I completed the complicated race, though it still not very stable in some corner I think.
The validation accuracy only 0.9. I have tried more epochs, but it didn't give significant improvements.

The result are in the video of run1.mp4 for simple race and run2.mp4 for the complicated race.
(I didn't upload the pictures of run2)

I also upload the video in player perspective to youtube as: 
https://youtu.be/ely6-2Rqak0
