import numpy as np
import tensorflow as tf
import wget

from keras.models import load_model
from os.path import exists
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def load_image(filename):
    image = tf.keras.utils.load_img(filename, target_size=(80, 80))
    image = tf.keras.utils.img_to_array(image)
    image = image.reshape(80, 80, 3)
    return image


def download_file():
    url = r'https://drive.google.com/u/0/uc?id=1SKNPTuei7EV7EXqjlKD-OfL-SwXhlaU8&export=download&confirm=t&uuid' \
          r'=159dffe1-8919-4bb4-8636-ed770fc12685&at=ANzk5s79gDCl8yiydwX1RXcdCz2O:1679566441866 '
    wget.download(url)


def handel_image(image_path):
    classes = [
        'Airplane',
        'Automobile',
        'Bird',
        'Cat',
        'Deer',
        'Dog',
        'Frog',
        'Horse',
        'Ship',
        'Truck']

    if not exists('cifar10_new_v6.hdf5'):
        download_file()

    image = load_image(image_path)
    model = load_model('cifar10_new_v6.hdf5')

    result = model.predict(np.expand_dims(image, axis=0))
    prediction = result[0]
    result = np.argmax(prediction)

    if prediction[result] < 0.85:
        return 'Bad photo, please give me another one'
    else:
        return classes[result]
