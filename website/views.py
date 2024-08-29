from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
def records(request):
    return render(request, 'records.html')
def financialaid(request):
    return render(request, 'financialaid.html')