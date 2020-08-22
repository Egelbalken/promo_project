from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    """
    docstring for NewUser
    Makes forms fields for user signup
    """
    # We have a model in models.. use it
    class Meta():
        model = User
        fields = "__all__"
