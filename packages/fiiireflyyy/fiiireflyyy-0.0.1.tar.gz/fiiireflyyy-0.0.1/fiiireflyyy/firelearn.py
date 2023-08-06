import pickle

import numpy as np

import os
from fiiireflyyy import firefiles as ff
from fiiireflyyy import flimage as fi
import matplotlib.pyplot as plt
from keras.models import Sequential, Model
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
import random
from imutils import paths
import datetime
import PIL
from tensorflow import keras
from keras import layers
from keras.models import Sequential
import pathlib
import shutil
import pandas as pd


# todo: modifications have been made to the library. Update needed via gitlab.



def k_fold_cross_validation(k_fold, x, y, clf=None, loading=False, clf_path=''):
    """
    DEPRECATED - Compute a K-fold cross validation method.

    :param k_fold: Number of folds to split the dataset
    :param x: Features dataset
    :param y: target dataset
    :param clf: classifier object, if loading is False.
    :param clf_path: path of a classifier object, if loading is True.
    :param loading: Whether to load a classifier object from path or not.
    :return: k-fold scores, accuracy
    """
    if len(x) != len(y):
        raise ValueError("Features and Targets do not have the same length.")

    data_len = len(y)

    if loading:
        if clf_path == '':
            raise ValueError('No classifier path specified.')
        else:
            clf = pickle.load(open(clf_path, "rb"))
    elif clf is None:
        raise ValueError("no classifier object specified.")

    ori_x_train, ori_x_test, ori_y_train, ori_y_test = train_test_split(x, y, test_size=0.3)
    train_len = len(ori_y_train)
    test_len = len(ori_y_test)
    local_scores = []
    step = int(train_len / k_fold)
    clf.fit(ori_x_train, ori_y_train)
    for k in range(0, train_len - step, step):
        x_train_split = ori_x_train.iloc[k:k + step]
        y_train_split = ori_y_train.iloc[k:k + step]
        y_test_split = pd.concat([ori_y_test.iloc[0:k], ori_y_test.iloc[k + step:data_len]])
        x_test_split = pd.concat([ori_x_test.iloc[0:k], ori_x_test.iloc[k + step:data_len]])
        # clf.fit(x_train_split, y_train_split)
        local_scores.append(clf.score(x_test_split, y_test_split))

    return local_scores


# todo: modifications have been made to the library. Update needed via gitlab.
def generate_classes(data_dir, destination, targets):
    """
    Generate a specific folder structure for Keras models by isolating classes as different folders.

    :param data_dir:
    :type data_dir: str
    :param destination: Where to generate the classes folders
    :type destination: str
    :param targets: the different classes to use
    :type targets: str
    :return:
    """
    ff.verify_dir(destination)
    files = ff.get_all_files(data_dir)

    # Creating directories architecture for keras model
    for target in targets:
        ff.verify_dir(os.path.join(destination, target))

        for file in files:
            if target in file:
                shutil.copy2(file, os.path.join(destination, target))


def basic_keras(model_spec, src, dst, img_size, epochs=10, visualize=False, saving=True):
    """
    Compute a basic Keras model for a images binary classification problem.

    :param model_spec: the name of the model. Identical to the root folder that will contain the model.
    :type model_spec: str
    :param src: Where to find the data.
    :type src: str
    :param dst: Where to save the sorted data
    :type dst: str
    :param img_size: the size of the image.
    :type img_size: tuple[int]
    :param epochs: The number of epochs of the model. Default at 10.
    :param visualize: To visualize the model's results
    :type visualize: bool
    :param saving: To save the model's results
    :type saving: bool
    :return:
    """
    #generate_classes(src, dst, targets=['INF', 'NI'])
    # Getting the dataset

    data_dir = pathlib.Path(dst)
    image_count = len(list(data_dir.glob('*.png')))
    print(image_count)

    # loading data
    batch_size = 8
    img_height = img_size[0]
    img_width = img_size[1]

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset='training',
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset='validation',
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    class_names = train_ds.class_names
    print(class_names)

    # Visualizing data
    if visualize:
        plt.figure(figsize=(10, 10))
        for images, labels in train_ds.take(1):
            for i in range(9):
                ax = plt.subplot(3, 3, i + 1)
                plt.imshow(images[i].numpy().astype("uint8"))
                plt.title(class_names[labels[i]])
                plt.axis("off")
        plt.show()

    for image_batch, labels_batch in train_ds:
        print(image_batch.shape)
        print(labels_batch.shape)
        break

    # Configure the dataset for performance

    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().shuffle(1000) #  .prefetch(buffer_size=AUTOTUNE)  # Once loaded, keep the pictures in memory
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)  # Overlaps data preprocessing/model execution while training

    # Data augmentation
    data_augmentation = keras.Sequential(
        [
            layers.RandomFlip("horizontal_and_vertical",
                              input_shape=(img_height,
                                           img_width,
                                           3)),
            layers.RandomRotation(1.0),
            layers.RandomZoom(0.5),
        ]
    )

    # Basic Keras model
    num_classes = len(class_names)
    model = Sequential([
        data_augmentation,
        layers.Rescaling(1. / 255),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, name="outputs")
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.summary()

    # Train the model

    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    # Visualize training
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')

    save_path = os.path.join(os.path.join(pathlib.Path(dst).parent.parent.absolute(), "RESULTS"), model_spec, "training validation acc loss.png")
    ff.verify_dir(os.path.join(os.path.join(pathlib.Path(dst).parent.parent.absolute(), "RESULTS"), model_spec))
    if saving:
        plt.savefig(save_path)
    if visualize:
        plt.show()
    plt.close()


def keras_tutorial():
    """
    A tutorial use of keras model for image multiclass classification

    :return:
    """
    # downloading the test dataset
    dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
    data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)
    data_dir = pathlib.Path(data_dir)
    image_count = len(list(data_dir.glob('*/*.jpg')))

    # loading data using keras
    batch_size = 32
    img_height = 180
    img_width = 180

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    class_names = train_ds.class_names
    print(class_names)

    # Visualizing data
    plt.figure(figsize=(10, 10))
    for images, labels in train_ds.take(1):
        for i in range(9):
            ax = plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")
    plt.show()

    for image_batch, labels_batch in train_ds:
        print(image_batch.shape)
        print(labels_batch.shape)
        break

    # Configure the dataset for performance

    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)  # Once loaded, keep the pictures in memory
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)  # Overlaps data preprocessing/model execution while training

    # Data augmentation
    data_augmentation = keras.Sequential(
        [
            layers.RandomFlip("horizontal",
                              input_shape=(img_height,
                                           img_width,
                                           3)),
            layers.RandomRotation(0.1),
            layers.RandomZoom(0.1),
        ]
    )

    # Basic Keras model
    num_classes = len(class_names)
    model = Sequential([
        data_augmentation,
        layers.Rescaling(1. / 255),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, name="outputs")
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.summary()

    # Train the model
    epochs = 15
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    # Visualize training
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

    # Predict on new data
    sunflower_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg"
    sunflower_path = tf.keras.utils.get_file('Red_sunflower', origin=sunflower_url)

    img = tf.keras.utils.load_img(
        sunflower_path, target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )


