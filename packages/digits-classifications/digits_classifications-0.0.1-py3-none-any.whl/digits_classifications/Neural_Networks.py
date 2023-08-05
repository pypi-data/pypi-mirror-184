import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Input, Dense, Dropout, Flatten, Conv2D, MaxPooling2D, AveragePooling2D, BatchNormalization
from keras.losses import CategoricalCrossentropy, SparseCategoricalCrossentropy
from keras.optimizers import Adam
from keras.utils import normalize, to_categorical
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import os
import cv2
from shutil import rmtree


from digits_classifications.Deep_Learning_Model import Deep_Learning

class NN(Deep_Learning):

    def __init__(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        self.x_train = normalize(self.x_train, axis=1)
        self.x_test = normalize(self.x_test, axis=1)

        self.model = None
        self.batch_images = []

    def prepare_model(self):
        self.model = Sequential([
                Input(shape=(28, 28)),
                Flatten(),
                Dense(32, activation='relu'),
                Dense(32, activation='relu'),
                Dropout(0.25),
                Dense(32, activation='relu'),
                #Dropout(0.2),
                #Dense(16, activation='relu'),
                Dense(10, activation='softmax')
            ])

        self.model.compile(loss=SparseCategoricalCrossentropy(), optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

    def train_model(self):
        self.prepare_model()
        self.model.fit(self.x_train, self.y_train, epochs = 10, validation_split=0.2)
        self.model.evaluate(self.x_test, self.y_test)
        self.model.save('digits_final_nn.model')

    def processing_images(self):
        path = 'images'
        for filename in os.listdir(path):
            f = os.path.join(path, filename)
            if os.path.isfile(f):
                image = cv2.imread(f)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                new_image = normalize(image, axis=1)
                self.batch_images.append(new_image)

    def predict_model(self):
        self.model = load_model('digits_final_nn')
        self.processing_images()
        prediction = self.model.predict(np.array(self.batch_images))
        prediction = np.argmax(prediction, axis=1)
        self.batch_images = []

        rmtree('images') # delete folder with roi images and create for using again
        os.mkdir('images')

        number = ''
        for x in prediction:
            number += str(x)
        return number

class CNN(Deep_Learning):
    def __init__(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        
        self.x_train = self.x_train / 255.0
        self.x_test = self.x_test / 255.0
        
        self.x_train = self.x_train.reshape(-1,28,28,1)
        self.x_test = self.x_test.reshape(-1,28,28,1)
        
        self.y_train = to_categorical(self.y_train, num_classes = 10)
        self.y_test = to_categorical(self.y_test, num_classes = 10)

        self.model = None
        self.batch_images = []
        self.datagen = ImageDataGenerator(
            rotation_range=15,
            zoom_range = 0.15,  
            width_shift_range=0.1, 
            height_shift_range=0.1)
    
    def prepare_model(self):
        
        Conv2D(32, kernel_size = 3, activation='relu', input_shape = (28, 28, 1)),
        BatchNormalization(),
        Conv2D(32, kernel_size = 3, activation='relu'),
        BatchNormalization(),
        Conv2D(32, kernel_size = 5, strides=2, padding='same', activation='relu'),
        BatchNormalization(),
        Dropout(0.4),

        Conv2D(64, kernel_size = 3, activation='relu'),
        BatchNormalization(),
        Conv2D(64, kernel_size = 3, activation='relu'),
        BatchNormalization(),
        Conv2D(64, kernel_size = 5, strides=2, padding='same', activation='relu'),
        BatchNormalization(),
        Dropout(0.4),

        Conv2D(128, kernel_size = 4, activation='relu'),
        BatchNormalization(),
        Flatten(),
        Dropout(0.4),
        Dense(10, activation='softmax')
        
        self.model.compile(loss=CategoricalCrossentropy(), optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

    def train_model(self):
        X_train2, X_val2, Y_train2, Y_val2 = train_test_split(self.x_train, self.y_train, test_size = 0.1)
        self.model.fit(self.datagen.flow(X_train2,Y_train2, batch_size=64),
        epochs = 45, steps_per_epoch = X_train2.shape[0]//64,  
        validation_data = (X_val2,Y_val2))

        self.model.evaluate(self.x_test, self.y_test)
        self.model.save('model_kaggle_original')
    
    def processing_images(self):
        path = 'images'
        for filename in os.listdir(path):
            f = os.path.join(path, filename)
            if os.path.isfile(f):
                image = cv2.imread(f)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                new_image = normalize(image, axis=1)
                new_image = np.array(new_image).reshape(28, 28, 1)
                self.batch_images.append(new_image)
    
    def predict_model(self):
        
        self.model = load_model('digits_final_cnn')


        self.processing_images()
        prediction = self.model.predict(np.array(self.batch_images))
        prediction = np.argmax(prediction, axis=1)
        self.batch_images = []

        rmtree('images') # delete folder with roi images and create for using again
        os.mkdir('images')

        number = ''
        for x in prediction:
            number += str(x)
        return number
