from django.forms import ModelForm
from educportal.models import User
class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password','phone_number']
		
		confirm_password = 	forms.CharField(min_length=6, max_length=32, widget=forms.PasswordInput(label='Повторите пароль'))



