from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from home.models import Staff,Network
from django.db.models import Q
from django.http import HttpResponse, Http404

# Create your views here.



def index(request):
    
    return render(request, 'index.html')


def staff(request):
    return render(request,'staff.html')
    
def desktops(request):
    return render(request,'desktops.html')

def network(request):
    net = get_object_or_404(Network, network_id = neted)
    return render(request,'network.html',{'neted':net})

def servers(request):
    return render(request,'servers.html')

def workstations(request):
    return render(request,'workstations.html')

def storage(request):
    return render(request,'storage.html')

def software(request):
    return render(request,'software.html')

def aboutus(request):
    return render(request,'aboutus.html')
