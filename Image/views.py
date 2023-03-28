import os
import numpy as np
import tensorflow as tf
import wget
import ssl

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage

from django.db import IntegrityError
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, redirect

from keras.models import load_model
from os.path import exists

from .models import Picture


def index(request):
    return render(request, 'landing.html', {})

@login_required
def main(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        image = fs.save(uploaded_file.name, uploaded_file)
        img_path = os.path.join(settings.MEDIA_ROOT, image)

        user = User.objects.get(id=request.user.id)

        predictions = handel_image(img_path)

    # Save the recognized image
        recognized_image = Picture.objects.create(name=uploaded_file, prediction=predictions, owner = user)
    # Delete the uploaded file
    #     os.remove(fs.url(uploaded_file))

        # images = [img_path]
        images = Picture.objects.filter(owner = user)[1:11]
        context = {
            'last': recognized_image,
            'result': predictions,
            'images': images,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html', {})


def load_image(filename):
    image = tf.keras.utils.load_img(filename, target_size=(80, 80))
    image = tf.keras.utils.img_to_array(image)
    image = image.reshape(80, 80, 3)
    return image


def download_file():
    ssl._create_default_https_context = ssl._create_unverified_context

    url = r'https://drive.google.com/u/0/uc?id=1SKNPTuei7EV7EXqjlKD-OfL-SwXhlaU8&export=download&confirm=t&uuid=159dffe1-8919-4bb4-8636-ed770fc12685&at=ANzk5s79gDCl8yiydwX1RXcdCz2O:1679566441866'
    wget.download(url, 'image/static/nn_model/cifar10_new_v6.hdf5')


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

    if not exists('image/static/nn_model/cifar10_new_v6.hdf5'):
        download_file()

    image = load_image(image_path)
    model = load_model('image/static/nn_model/cifar10_new_v6.hdf5')

    result = model.predict(np.expand_dims(image, axis=0))
    prediction = result[0]
    result = np.argmax(prediction)

    if prediction[result] < 0.85:
        return f'Bad photo, please give me another one'
    else:
         return f'Samantha recognize this photo as {classes[result]}'


# @login_required
def delete_picture(request, pk):
    picture = Picture.objects.get(id=pk)
    picture.delete()
    return redirect('index.html')


# @login_required
def find_picture(request):
    query = request.GET.get('q')
    try:
        pk = Picture.objects.filter(Q(name__icontains=query))[0].id
        return redirect('edit-contact', pk)
    except IndexError or ValueError:
        return redirect('index.html')


def image_upload(request):
    uploaded_file = request.FILES['image']
    print(uploaded_file)
    fs = FileSystemStorage()
    picture = fs.save(uploaded_file.name, uploaded_file)
    print(picture)
    owner = request.user.id

    prediction = 'LOADING////'
    Picture.objects.create(owner = owner,
                           name = picture,
                           prediction = prediction
                           )

#
# def recognize_image(request):
#     if request.method == 'POST' and request.FILES['image']:
#         image_file = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(image_file.name, image_file)
#         uploaded_image_url = fs.url(filename)
#         # OpenCV code to recognize the image
#         img = cv2.imread(fs.path(filename))
#         # ... (add your image recognition code here)
#         recognized_image_url = 'https://example.com/recognized_image.jpg'
#         return render(request, 'image_recognition.html', {'image': recognized_image_url})
#     return render(request, 'base.html')


###REGISTER


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('loginuser')
            except IntegrityError as err:
                return render(request, 'registration.html',
                              {'form': UserCreationForm(), 'error': 'Username is already exist'})

        else:
            return render(request, 'registration.html',
                          {'form': UserCreationForm(), 'error': 'Password did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None or False:
            return render(request, 'login.html',
                          {'form': AuthenticationForm, 'error': 'Username or password didn\'t match'})
        else:
            login(request, user)
            return redirect('main')

@login_required
def logoutuser(request):
    logout(request)
    return redirect('index')
