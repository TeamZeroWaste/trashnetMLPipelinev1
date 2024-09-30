# Image based Waste Classification System

## Overview
This project implements an automated waste classification system using a SVM model and VGG16 architecture. The system captures waste images using OpenCV, processes them through the trained model, and outputs the classification of the waste type. 

## Table of Contents
- [Project Description](#project-description)
- [Datasets](#datasets)
- [Model Architecture](#model-architecture)
- [Performance](#performance)
---

## Project Description
The primary goal of this project is to automate the waste sorting process, aiding in recycling and waste management. The system classifies waste into multiple categories (glass, paper, cardboard, plastic, metal, etc.) based on visual input. The model is trained on the **TrashNet** dataset and achieves an accuracy of 80%.


---

## Datasets
The **TrashNet** dataset was used to train the model. This dataset contains labeled images of waste classified into six categories:
- **Glass**
- **Paper**
- **Cardboard**
- **Plastic**
- **Metal**
- **Trash**

The dataset can be downloaded from [TrashNet](https://github.com/garythung/trashnet).

## Image Preprocessing

### 1. Image Resizing
VGG16 requires images of size **224x224** pixels with 3 color channels (RGB). Since the dataset might contain images of various dimensions, every image is resized to a fixed shape of **224x224x3** before being input into the model.

```python
target_size = (224, 224)
```
### 2. Image Normalization
To standardize the pixel values and ensure that the model performs optimally, images are normalized by scaling the pixel values from their original range of (0, 255) to the range (0,1) .
```python
image = image.astype('float32') / 255.0
```
### 3. Data Augmentation
Data augmentation is used to increase the diversity of the training dataset by creating random variations of the images.
  - Rotation: Randomly rotates the image by up to 20 degrees.
  - Zoom: Applies random zoom-in or zoom-out transformations.
  - Horizontal Flip: Flips the image horizontally.
  - Width and Height Shifts: Randomly shifts the image horizontally or vertically by a fraction of its size.
    
```python
# Applying data augmentation with ImageDataGenerator
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rescale=1.0/255.0,            # Normalize pixel values to [0, 1]
    rotation_range=20,            # Randomly rotate images by 20 degrees
    width_shift_range=0.2,        # Randomly shift images horizontally by 20%
    height_shift_range=0.2,       # Randomly shift images vertically by 20%
    zoom_range=0.15,              # Random zoom by 15%
    horizontal_flip=True,         # Randomly flip images horizontally
    fill_mode='nearest'           # Fill missing pixels after transformations with nearest pixel value
)

```

### 4. Data Generator
The ```ImageDataGenerator``` is used to load images from directories, apply the defined augmentation techniques, and preprocess them in batches. 

---

## Model Architecture
The model is based on the **VGG16** architecture, a popular CNN model designed for image classification tasks. Key features of the model include:

- **Input Shape**: (224, 224, 3)
- **Transfer Learning**: Pre-trained weights from ImageNet were used.
- **Fine-tuning**: The last few layers of the model were trained on the TrashNet dataset.
- **Activation**: Softmax is used for multi-class classification.

### Layers:
1. Input Layer: 224x224x3 images.
2. Convolutional Layers: Several convolutional layers with ReLU activation.
3. Max Pooling: Reducing the spatial dimensions after convolution.
4. Fully Connected Layers: Two dense layers with ReLU and dropout.
5. Output Layer: A softmax layer with 6 neurons corresponding to the 6 waste categories.

## Performance
[image](Performance.png)
