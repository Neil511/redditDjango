from django import forms

class PostForm(forms.Form):
    name = forms.CharField(max_length = 200)
    created_by = forms.CharField(max_length = 100)
    content = forms.CharField(max_length = 255)
