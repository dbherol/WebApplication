from django import forms
#from GoodDriverIncentive.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portfolio_site', 'profile_pic')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        def save(self, commit = True):
            user = super(RegistrationForm, self).save(commit = False)
            user.firstName = self.cleaned_data['firstName']
            user.lastName = self.cleaned_data['lastName']
            user.email = self.cleaned_data['email']

            if commit:
                user.save

            return user
