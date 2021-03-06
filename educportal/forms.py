from django import forms
from django.forms import ModelForm
from educportal.models import User
from educportal.models import AcademicGroup
from django.utils.translation import  ugettext

class SignUpForm(ModelForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    confirm_password = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(),
        strip=False
    )
    academic_group = forms.ModelChoiceField(queryset=AcademicGroup.objects.all(),required=True)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username__iexact=username).exists():
            self.add_error('username', ugettext('Пользователь с таким именем уже существует!'))

        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            self.add_error('email', ugettext('Пользователь с таким email уже существует!'))

        return email.lower()

    def clean (self):
        super().clean()
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                self.add_error(None, ugettext("Пароли должны совпадать!!!"))
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','academic_group', 'password','phone_number')
