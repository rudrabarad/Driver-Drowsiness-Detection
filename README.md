# Driver-Drowsiness-Detection
Drowsiness detection is a safety technology that can prevent accidents that are caused by drivers who fell asleep while driving. This technology will alert the driver when drowsiness is detected. 😴 🚨

<img align="right" alt="GIF" height=200 src="https://github.com/rudrabarad/Driver-Drowsiness-Detection/blob/main/driver.gif" />

## Contents of the Repository
- [CNN Approach](https://github.com/rudrabarad/Driver-Drowsiness-Detection/tree/main/DDDS_CNN)
- [Transfer Learning Approach](https://github.com/rudrabarad/Driver-Drowsiness-Detection/tree/main/Transfer_learning)
- [Readme](https://github.com/rudrabarad/Driver-Drowsiness-Detection#readme)
- [Dataset](https://github.com/rudrabarad/Driver-Drowsiness-Detection#dataset)
- [Required Libraries](https://github.com/rudrabarad/Driver-Drowsiness-Detection#required-libraries)
- [Installation Setup](https://github.com/rudrabarad/Driver-Drowsiness-Detection#installation-setup)
- [Results](https://github.com/rudrabarad/Driver-Drowsiness-Detection#results)
- [Research Article](https://github.com/rudrabarad/Driver-Drowsiness-Detection/blob/main/Research%20Article.docx)
- [Video Demonstration](https://github.com/rudrabarad/Driver-Drowsiness-Detection#video)

## Dataset
Sorry we were not able to upload dataset on GitHub due to size limitation :octocat: <br>
But you can find the links to download the dataset from the following text files
1. For CNN - [Dataset.txt](https://github.com/rudrabarad/Driver-Drowsiness-Detection/blob/main/DDDS_CNN/Dataset.txt)
2. For Transfer Learning - [get_dataset.txt](https://github.com/rudrabarad/Driver-Drowsiness-Detection/blob/main/Transfer_learning/get_dataset.txt)

## Required Libraries
- keras
- cv2
- pygame
- numpy
- matplotlib
- glob
- tqdm

## Installation Setup
#### 1. Clone the repository
You can clone this repository using command: ``git clone https://github.com/rudrabarad/Driver-Drowsiness-Detection.git``
#### 2. Training respective model
- For CNN open and run ``DDDS_CNN/model_training.py``
- For Transfer Learning open and run ``Transfer_learning/Model_Training_TL.ipynb`` 

#### 3. Execute all the cells consecutively to see the accuracy of both models.
#### 4. Execute programs using the models
- For CNN run ``DDDS_CNN/main_capture.py``
- For Transfer Learning run ``Transfer_learning/tl_capture.py``

> **Note:** Currently there is no **Models** folder in both CNN & Transfer folders but it will be created as soon as user executes model training file

## Results
Approach| Training Accuracy | Validation Accuracy
------------ | ------------------|--------------------
CNN | 99.01% | 95.19%
Transfer Learning | 82% |  79%

## Video
For viewing or downloading video click [here](https://github.com/rudrabarad/Driver-Drowsiness-Detection/blob/main/Video_Demonstration.mkv) 🎬

## Facing any issues???

Feel free to [open an issue](https://github.com/rudrabarad/Driver-Drowsiness-Detection/issues/new?assignees=&labels=Query&title=Query). We are glad to help you. ❤️

## License
Project is published under the [MIT license](https://github.com/rudrabarad/Driver-Drowsiness-Detection/blob/master/LICENSE).

<br>

<div align="center">
  
<a href="https://github.com/rudrabarad/Driver-Drowsiness-Detection/stargazers"><img src="https://img.shields.io/github/stars/rudrabarad/Driver-Drowsiness-Detection?style=flat"/></a>
<a href="https://github.com/rudrabarad/Driver-Drowsiness-Detection/network/members"><img src="https://img.shields.io/github/forks/rudrabarad/Driver-Drowsiness-Detection?style=flat"/></a>
<a href="https://github.com/rudrabarad/Driver-Drowsiness-Detection/pulls"><img src="https://img.shields.io/github/issues-pr/rudrabarad/Driver-Drowsiness-Detection?style=flat?color=yellow"/></a>
<a href="https://github.com/rudrabarad/Driver-Drowsiness-Detection/issues"><img src="https://img.shields.io/github/issues/rudrabarad/Driver-Drowsiness-Detection?style=flat"/></a>
<a href="https://github.com/rudrabarad/Driver-Drowsiness-Detection/graphs/contributors"><img src="https://img.shields.io/github/contributors/rudrabarad/Driver-Drowsiness-Detection?color=orange"/></a>
<a href="https://github.com/rudrabarad/Driver-Drowsiness-Detection/blob/master/LICENSE"><img src="https://img.shields.io/github/license/rudrabarad/Driver-Drowsiness-Detection?color=1abc9c"/></a>
<br>
![](https://img.shields.io/badge/Star-If_Liked-%23FF0000.svg?&style=flat&logoColor=white&color=white)
![](https://img.shields.io/badge/Fork-If_you_found_interesting-%23FF0000.svg?&style=flat&logoColor=white&color=white)<br>
</div>  



