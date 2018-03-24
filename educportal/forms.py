from django import forms
from django.forms import ModelForm
from educportal.models import User
class SignUpForm(ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(label='Подтвердите пароль'),
        strip=False,
        help_text='Введите пароль повторно.'
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'Пользователь с таким именем уже существует!')

        return username.lower()

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            self.add_error('email', 'Пользователь с таким email уже существует!')

        return email.lower()

    def clean (self):
        super().clean()
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError("Пароли должны совпадать!!!")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password','phone_number')





