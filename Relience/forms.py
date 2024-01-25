from django import forms

class csvuploadform(forms.Form):
    csv_file = forms.FileField()


