from django import forms


class FormUploadFile(forms.Form):
    file = forms.FileField()