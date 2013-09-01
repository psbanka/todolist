from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from models import ToDoItem


def welcome(request):
    return render_to_response("welcome.html",{})

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('ToDoProject/welcome.html')
            # Redirect to a success page.
        else:
            print ("Your account has been disabled.")
            # Return a 'disabled account' error message
    else:
        print ("The username and password were incorrect.")
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def profile(request):
    todos=ToDoItem.objects.filter(user=request.user)
    response = {"name":request.user.first_name, "todos":todos}
    return render_to_response('profile.html',response)