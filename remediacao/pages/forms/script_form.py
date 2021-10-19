from django import forms
from datetime import datetime
from api.models import History
import os

class RunForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ("server","script")

#

class RawRunForm(forms.Form):
        server = forms.CharField(label='Server name', max_length=60,  widget=forms.TextInput(attrs={'placeholder': 'Select a server'}))
        server_user= forms.CharField(label='Server username', max_length=60,  widget=forms.TextInput(attrs={'placeholder': 'User to log in a server'}))
        server_pass= forms.CharField(widget=forms.PasswordInput())
        script = forms.ChoiceField(choices=tuple(map(lambda x : (x,x),os.listdir(f"{os.getcwd()}/remediacao/scripts/"))))
        job = forms.CharField(widget=forms.HiddenInput()) 
        terminal_error = forms.CharField(widget=forms.HiddenInput()) 
        exectime = forms.DateTimeField(widget=forms.HiddenInput())
        returncode = forms.IntegerField(widget=forms.HiddenInput()) 
        terminal = forms.CharField(widget=forms.HiddenInput()) 



