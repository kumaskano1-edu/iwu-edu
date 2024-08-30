from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.'
def index(request):
    username = request.COOKIES.get('username', None)
    if username:
        return render(request, 'home.html')
    else:
        # Handle the case where the cookie does not exist
        return redirect('/login', message="wrong credentials")
def profile(request):
    username = request.COOKIES.get('username', None)
    if username:
        return render(request, 'profile.html')
    else:
        # Handle the case where the cookie does not exist
        return redirect('/login', message="wrong credentials")
def records(request):
    username = request.COOKIES.get('username', None)
    if username:
        return render(request, 'records.html')
    else:
        # Handle the case where the cookie does not exist
        return redirect('/login', message="wrong credentials")
def financialaid(request):
    username = request.COOKIES.get('username', None)
    if username:
        return render(request, 'financialaid.html')
    else:
        # Handle the case where the cookie does not exist
        return redirect('/login', message="wrong credentials")
def payment(request):
    username = request.COOKIES.get('username', None)
    if username:
        return render(request, 'payment.html')
    else:
        # Handle the case where the cookie does not exist
        return redirect('/login', message="wrong credentials")
def vaccine(request):
    username = request.COOKIES.get('username', None)
    if username:
        return render(request, 'vaccine.html')
    else:
        # Handle the case where the cookie does not exist
        return redirect('/login', message="wrong credentials")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username != "nkalmato@iwu.edu" or password != "Nuraika2104":
            # Redirect with an error message as a query parameter
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')
        else:
            # Set a simple cookie with the username
            response = HttpResponse("You're logged in.")
            response.set_cookie('username', username, httponly=True)
            # Redirect to the home page
            response = redirect('/')
            response.set_cookie('username', username, httponly=True)

            return response
    else: 
        return render(request, 'login.html')
def logout(request): 
    response = HttpResponse("Cookie has been deleted.")
    response.delete_cookie('username')
    response = redirect('/login')
    response.delete_cookie('username')
    return response