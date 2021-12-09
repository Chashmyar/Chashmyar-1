import os

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from captcha.image import ImageCaptcha
from random import randint

# Create your views here.
from Cheshmyar import settings
from Cheshmyar.settings import STATIC_ROOT, STATICFILES_DIRS


def intern(request):
    print(request.path)
    cap = ImageCaptcha(280, 80)
    text = str(randint(10000, 99999))
    with open("Cheshmyar/static/captcha.txt", 'w') as file:
        file.write(text)
        file.close()
    data = cap.generate(text)
    cap.write(text, "Cheshmyar/static/images/Captcha.png")
    return render(request, 'intern/intern.html')


def submit(request):
    if request.method == 'POST':
        with open("Cheshmyar/static/captcha.txt", 'r') as file:
            text = file.readline()
            file.close()
        if 'captcha' in request.POST and text == request.POST['captcha']:
            if request.FILES['cv']:
                file = request.FILES['cv']
                fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'CVs/'))
                filename = fs.save(file.name, file)
                return render(request, 'intern/submit.html')
            else:
                return redirect('intern')
        else:
            messages.add_message(request, messages.ERROR, 'کد امنیتی وارد شده اشتباه است!')
            return redirect('intern')
    return redirect('intern')
