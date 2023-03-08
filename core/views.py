from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'Homepage'})

def cv(request):
    return render(request, 'cv.html')

def hireme(request):
    return render(request,'hire-me.html')

def projects(request):
    return render(request, 'projects.html')