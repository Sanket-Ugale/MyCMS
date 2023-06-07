from django import forms
class userForm(forms.Form):
    name=forms.CharField(label="Name")
    email =forms.CharField(label="Email")