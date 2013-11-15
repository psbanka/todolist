from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from models import ToDoItem
from forms import ToDoItemForm
from django.forms.models import modelformset_factory


def welcome(request):
    return render_to_response("welcome.html",{})

# Not being used currently
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('ToDoProject/profile')
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
    ToDoItemFormSet = modelformset_factory(ToDoItem)
    response = {"name":request.user, "form": ToDoItemFormSet}
    return render_to_response('profile.html',response)

#def changeProfileView(request):
    #if request.method == 'POST':
    # if the form has been submitted
        #form = ToDoList(request.POST)
        #if form.is_valid():
