from django.shortcuts import render


# Create your views here.
def webservice(request):
    return render(request, 'service.html')
