from django.shortcuts import render
from . import fake_module
def home(request):
    return render(request,'index.html')

def about(request):
    user_input = request.GET['user_input']
    user_input = fake_module.multiplier(user_input)
    return render(request,'about.html', {'home_input':user_input})