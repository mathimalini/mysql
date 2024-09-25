from django import forms
from .models import RegisterForm
class MyRegister(forms.ModelForm):
    class Meta:
        model=RegisterForm
        fields=["name","age","address","contact","email"]
 