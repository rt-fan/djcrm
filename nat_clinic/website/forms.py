from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Имя"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Фамилия"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Логин для входа"
        self.fields["username"].label = ""
        self.fields["username"].help_text = '<span class="form-text text-muted"><small>' \
                      'Обязательно. Не более 150 символов. Только латинские буквы, цифры и знаки @/./+/-/_' \
                      '</small></span>'

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Пароль"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = "<ul class=\"form-text text-muted small\">" \
                      "<li>Ваш пароль не должен быть похож на вашу личную информацию.</li>" \
                      "<li>Ваш пароль должен содержать не менее 8 символов.</li>" \
                      "<li>Ваш пароль не может быть часто используемым паролем.</li>" \
                      "<li>Ваш пароль не может быть полностью цифровым.</li></ul>"

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Подтвердите пароль"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = '<span class="form-text text-muted"><small>' \
                      'Введите тот же пароль, что и раньше, для проверки.</small></span>'


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "region": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "zipcode": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["clients", "phone", "potok", "room", "status", "money"]
        widgets = {
            "clients": forms.SelectMultiple(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "potok": forms.TextInput(attrs={"class": "form-control"}),
            "room": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.TextInput(attrs={"class": "form-control"}),
            "money": forms.TextInput(attrs={"class": "form-control"}),
        }


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ["first_name", "last_name", "phone", "age", "comments"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "comments": forms.TextInput(attrs={"class": "form-control"}),
        }


class AddStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["first_name", "last_name", "phone", "age", "division", "photo_passport"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "division": forms.Select(attrs={"class": "form-control"}),
        }


# class SearchForm(forms.Form):
#     query = forms.CharField(label='Your name', max_length=100)


# class SearchForm(forms.Form):
#     query = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                           'placeholder': 'Search'}))

class SearchForm(forms.Form):
    query = forms.CharField(label="", required=False,
                            widget=forms.TextInput(attrs={"class": "qwer",
                                                          'placeholder': 'Поиск...'}))
