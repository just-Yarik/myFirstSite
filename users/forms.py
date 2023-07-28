from django import forms
from django.contrib.auth.models import User

class UserRegForm(forms.Form):
    username = forms.CharField(label='Введи нікнейм',required=True, widget=forms.TextInput)
    email = forms.EmailField(label='Введи свою пошту',required=True, widget=forms.TextInput ,help_text='Вводь ретельно!')
    password1 = forms.CharField(label='Введи пароль',required=True, help_text='Введи так щоб ніхто не вгадав!', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

