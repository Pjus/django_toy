from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class RecoveryIdForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput,)
	email = forms.EmailField(widget=forms.EmailInput,)

	class Meta:
		fields = ['name', 'email']

	def __init__(self, *args, **kwargs):
		super(RecoveryIdForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "이름"
		self.fields['name'].widget.attrs.update({
			'class' : 'form-control',
			'id' : 'form-name'
		})

		self.fields['email'].label = "이메일"
		self.fields['email'].widget.attrs.update({
			'class' : 'form-control',
			'id' : 'form-control'
		})