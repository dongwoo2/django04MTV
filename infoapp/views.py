from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        return HttpResponseRedirect(reverse('infoapp:index'))
      #  return HttpResponseRedirect('/info/') # 이것도 하드코딩 직접 지정하고 있음
    
    
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
    
def edit(request, id):
    info = Info.objects.get(id=id)
    if request.method == 'GET':
        return render(
            request,
            'infoapp/edit-form.html',
            {'info':info}
        )
    elif request.method == 'POST':
        info.name = request.POST['name']
        info.age = int(request.POST['age'])
        info.intro = request.POST['intro']
        info.save()
        return HttpResponseRedirect(reverse('infoapp:detail2', args=(info.id,)))
    
    
def remove(request, id):
    info = Info.objects.get(id=id)
    if request.method == 'GET':
        return render(
            request,
            'infoapp/remove-form.html',
            {'info':info}
        )
    elif request.method == 'POST':
        info.delete()
        return HttpResponseRedirect(reverse('infoapp:index'))