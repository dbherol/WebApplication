from GoodDriverIncentive.forms import UserForm, RegistrationForm
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
#def home(request):
#    return HttpResponse("Hello, Django")

#class SignUp(generic.CreateView):
    #form_class = UserCreationForm
    #success_url = reverse_lazy('login') #redirects user to login page upon successful registration
    #template_name = 'signup.html'

def index(request):
    return render(request, 'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'index.html')
        else:
            print(user_form.errors)
    else:
        user_form = RegistrationForm()
    return render(request, 'registration.html',
                            {'user_form': user_form,
                             'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return render(request, 'login.html',
                            {'login_message' : 'Sorry, we couldn\'t find an account with that username and password.'})
    else:
        return render(request, 'login.html', {})
