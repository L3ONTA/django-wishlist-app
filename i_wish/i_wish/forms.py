from django import forms
from .models import CustomUser, Wish
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):   

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['title', 'description', 'link', 'image']
        labels = {'title': 'Название желания', 'description': 'Описание', 'link': 'Ссылка', 'image':  'Изображение'}