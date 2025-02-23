from django import forms


#login form
class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'enter username'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder':'enter password', }), required=True)
    


#sing up form
class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=100, required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label='email', required=True)

    class Meta:
        # set widgets for each field outside the form
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'enter username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'enter password'}),
            'email': forms.EmailInput(attrs={'placeholder': 'enter email'}),
        }