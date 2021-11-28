from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html',{'text':'Hello World', 'number':100})

def other(request):
    return render(request, 'basicapp/other.html')

def relative(request):
    return render(request, 'basicapp/relative_url.html')
