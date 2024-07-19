import matplotlib.pyplot as plt
import seaborn as sns

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout 
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

from sklearn.metrics import classification_report,confusion_matrix

import tensorflow as tf

import cv2
import os

import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

img_size = 224
labels = ['cfunc', 'circle', 'ellipse', 'lfunc', 'mfunc', 'sfunc', 'rfunc']
labels_ret = ["cubic function", "circle", "ellipse", "linear function", "reciprocal function", "parabolic function", "square root function"]

def get_data(data_dir):
    '''
    Compiles data from /data
    '''

    data = [] 
    for label in labels: 
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img))[...,::-1] 
                resized_arr = cv2.resize(img_arr, (img_size, img_size)) 
                data.append([resized_arr, class_num])
            except Exception as e:
                print(e)
    return np.array(data, dtype=object)

def get_data_user(path):
    '''
    Formats graph retrieved from user
    '''

    data = [] 
    for img in os.listdir(path):
        try:
            img_arr = cv2.imread(os.path.join(path, img))[...,::-1] 
            resized_arr = cv2.resize(img_arr, (img_size, img_size)) 
            data.append(resized_arr)
        except Exception as e:
            print(e)
    return np.array(data, dtype=object)

def train():
    '''
    Trains model and saves to /model.
    '''

    train = get_data('data/train')
    val = get_data('data/test')

    x_train = []
    y_train = []
    x_val = []
    y_val = []

    for feature, label in train:
        x_train.append(feature)
        y_train.append(label)

    for feature, label in val:
        x_val.append(feature)
        y_val.append(label)

    x_train = np.array(x_train) / 255
    x_val = np.array(x_val) / 255

    x_train.reshape(-1, img_size, img_size, 1)
    y_train = np.array(y_train)

    x_val.reshape(-1, img_size, img_size, 1)
    y_val = np.array(y_val)

    datagen = ImageDataGenerator(
            featurewise_center=False,  
            samplewise_center=False,
            featurewise_std_normalization=False, 
            samplewise_std_normalization=False,
            zca_whitening=False, 
            rotation_range = 30, 
            zoom_range = 0.2, 
            width_shift_range=0.1, 
            height_shift_range=0.1,  
            horizontal_flip = True,  
            vertical_flip=False) 

    datagen.fit(x_train)

    model = Sequential()
    model.add(Conv2D(32,3,padding="same", activation="relu", input_shape=(224,224,3)))
    model.add(MaxPool2D())

    model.add(Conv2D(32, 3, padding="same", activation="relu"))
    model.add(MaxPool2D())

    model.add(Conv2D(64, 3, padding="same", activation="relu"))
    model.add(MaxPool2D())
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dense(128,activation="relu"))
    model.add(Dense(7, activation="softmax"))

    model.summary()

    opt = Adam(lr=0.000001)
    model.compile(optimizer = opt , loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True) , metrics = ['accuracy'])
    history = model.fit(x_train,y_train,epochs = 250 , validation_data = (x_val, y_val))

    model.save('model')

def use_model():
    '''
    Calls on saved model in /model and retrieves best answers.
    '''
    
    model_r = keras.models.load_model("model")

    data = get_data_user('user')
    data = np.array(data) / 255
    data.reshape(-1, img_size, img_size, 1)
    data = np.asarray(data).astype(np.float32)
    data = tf.convert_to_tensor(data)
    predict = model_r.predict(data)
    
    likely = sorted(list(predict[0]))[-3:]
    likely.reverse()
    print()
    for i in likely:
        print("{} - {}".format(labels_ret[list(predict[0]).index(i)], i))

def user_input():
    '''
    Get user input for equation
    '''

    other = input("If circle, ellipse, square root equations, enter [y]es: ")

    fig, axes = plt.subplots()
 
    axes.set_aspect( 1 )

    if other in ['y', 'yes']:
        params1 = input("Enter [y]es if circle or ellipse: ")
        if params1 in ['y', 'yes']:
            eq = input("Enter a equation for the ai to guess as (y = ) in terms of x without the sqrt: ").lower()
            x = np.linspace(-10, 10, 101)
            y = np.linspace(-10, 10, 101)
            with np.errstate(divide='ignore', invalid='ignore'):
                c, d, r = map(int, input("Give coef of first two terms and r separated by spaces: ").strip().split(" "))
                a, b = np.meshgrid( x , y )
                C = (a ** 2)/c + (b ** 2)/d - r
                axes.contour(a, b, C, [0])
        else:
            eq = input("Enter the the equation in (y = ) without the square root: ")
            x = np.linspace(-10, 10, 101)
            with np.errstate(divide='ignore', invalid='ignore'):
                y = np.sqrt(eval(eq))
            plt.plot(x, y)
    else:
        eq = input("Enter a equation for the ai to guess as (y = ) in terms of x: ").lower()
        x = np.linspace(-10, 10, 101)
        with np.errstate(divide='ignore', invalid='ignore'):
            y = eval(eq)
        plt.plot(x, y)

    fig.savefig('user/graph.png')
    print()

def run():
    '''
    Call all functions to run the script
    '''
    
    get_train = input("Train model? WARNING takes at least 6 hours depending on computer. If not, use given saved model. [y]es/[n]o: ").lower()
    print()
    if get_train == "y":
        train()
    
    user_input()
    use_model()

run()