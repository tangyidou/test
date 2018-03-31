from django import forms

class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
