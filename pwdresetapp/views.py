from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request, 'pwdresetapp/index.html')

def success(request):
    return HttpResponse("Password Reset Successfully")