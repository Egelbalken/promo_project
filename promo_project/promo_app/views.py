from django.shortcuts import render
# from promo_app.models import User
# From forms.py
from promo_app.forms import NewUserForm
# Create your views here.
def index(request):
    """
    A views to display the index.html
    Returns the
    """
    return render(request, "promo_app/index.html")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'promo_app/help.html',context=helpdict)

def users(request):
    """
    Make form whit sign up fields
    """
    form = NewUserForm()
    # If somehone hits the submit sends the info to here
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, "promo_app/users.html", {"form" : form})
