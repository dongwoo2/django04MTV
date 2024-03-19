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
    
    
def detail1(request): # 얘는 파라미터로 받아서 처리하는 방식
    id = request.GET['id']
    info = Info.objects.get(id=id)
    return render(
        request,
        'infoapp/detail.html',
        {'info':info}
    )
    
def detail2(request, id): # 경로변수를 사용하는 방식 request말고도 경로에 있는 id도 뽑아올 수 있게 id 매개변수 설정
    info = Info.objects.get(id=id)
    return render(
        request,
        'infoapp/detail.html',
        {'info':info}
    )