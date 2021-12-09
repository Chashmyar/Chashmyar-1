from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    # Login User
    redirect_to = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'dashboard.html', {'username': username})
        else:
            messages.add_message(request, messages.ERROR, 'گذرواژه وارد شده نادرست است!')
            return redirect(redirect_to)
    else:
        return redirect(redirect_to)


def register(request):
    # Registration User
    redirect_to = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if len(password) | len(confirm_password) < 8:
            messages.add_message(request, messages.ERROR, 'گذرواژه وارد شده باید بیشتر از 8 کاراکتر باشد!')
            return redirect(redirect_to)
        else:
            if password != confirm_password:
                messages.add_message(request, messages.ERROR, 'گذرواژه وارد شده درست نیست!')
                return redirect(redirect_to)
            else:
                if User.objects.filter(username=username).exists():
                    messages.add_message(request, messages.ERROR, 'این نام کاربری قبلا انتخاب شده است!')
                    return redirect(redirect_to)
                else:
                    if User.objects.filter(email=email).exists():
                        messages.add_message(request, messages.ERROR, 'این ایمیل قبلا انتخاب شده است!')
                        return redirect(redirect_to)
                    else:
                        user = User.objects.create_user(username=username, password=password, email=email, name=name)
                        user.save()
                        messages.add_message(request, messages.SUCCESS, 'حساب کاربری با موفقیت ساخته شد!')
                        return redirect(redirect_to)
    else:
        return redirect(redirect_to)


def choose_func(request):
    redirect_to = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        if 'name' in request.POST and 'email' in request.POST and 'username' in request.POST \
                and 'password' in request.POST and 'confirm-password' in request.POST:
            return register(request)
        elif 'username' in request.POST and 'password' in request.POST:
            return login(request)
        return redirect(redirect_to)
    return redirect(redirect_to)


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    return choose_func(request)
