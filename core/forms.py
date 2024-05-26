from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'class':"form_input col-md-2", "placeholder":"Email"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':"form_input col-md-2", "placeholder":"Пароль"}))

class LoginFormMod(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':"form_input col-md-2", "placeholder":"Имя пользователя", 'name':'username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':"form_input col-md-2", "placeholder":"Пароль"}))

class RegForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':"form_input col-md-2", "placeholder":"ФИО"}))
    company = forms.CharField(label="", widget=forms.TextInput(attrs={'class':"form_input col-md-2", "placeholder":"Название компании"}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'class':"form_input col-md-2", "placeholder":"Email"}))
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':"form_input col-md-2", "placeholder":"Телефон"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':"form_input col-md-2", "placeholder":"Пароль"}))

class ResetForm(forms.Form):
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'class':"form_input col-md-2", "placeholder":"Email"}))

class NewPassword(forms.Form):
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':"form_input col-md-2", "placeholder":"Новый пароль"}))