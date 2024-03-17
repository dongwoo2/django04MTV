from django.shortcuts import render

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