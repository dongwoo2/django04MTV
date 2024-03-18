from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Info

def index(request):
    info_list = Info.objects.all()
    return render(
        request,
        'infoapp/index.html',
        {
            'info_list':info_list
        }
    )
    
def add(request):
    if request.method == 'GET':
        return render(request, 'infoapp/add-form.html')
    else:
        name = request.POST['name']
        age = request.POST['age']
        intro = request.POST['intro']
        Info(name=name, age=age, intro=intro).save()
        return HttpResponseRedirect('/info/')