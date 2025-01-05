from django import forms

class LoginForm(forms.Form):
    input_style = 'w-full border-2 text-gray-700 border-gray-400 text-center rounded-lg p-1 my-2'
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Addresse courriel...',
        'class': input_style
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Mot de passe...',
        'class': input_style
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = ''

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            if email != 'antiquesclub007@gmail.com' or password != '007':
                raise forms.ValidationError('Addresse courriel ou mot de passe erroné.')
            
        return cleaned_data
        
        