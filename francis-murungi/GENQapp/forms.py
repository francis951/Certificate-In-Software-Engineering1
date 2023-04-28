from django import forms
from .models import GENQModels

class GENQModelsForm(forms.ModelForm):
    class Meta:
        model = GENQModels
        fields = ('f_name','l_name', 'date', 'gender', 'country', 'state','town', 'zip','phone1','phone2', 'email')

        labels = {
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'email': 'Email',
        }
        #placeholders
        widgets = {
            'f_name' : forms.TextInput(attrs={'placeholder':'Your First Name'}),
            'l_name' : forms.TextInput(attrs={'placeholder':'Your Last Name'}),
            'date' : forms.TextInput(attrs={'placeholder':'Your Date Of Birth'}),
            # 'gender' : forms.TextInput(attrs={'placeholder':'Your Gender'}),
            'country' : forms.TextInput(attrs={'placeholder':'Your Country'}),
            'state' : forms.TextInput(attrs={'placeholder':'Your State'}),
            'town' : forms.TextInput(attrs={'placeholder':'Your Town'}),
            # 'zip' : forms.TextInput(attrs={'placeholder':'Your zipcode'}),
            'phone1' : forms.TextInput(attrs={'placeholder':'Your phone 1'}),
            'phone2' : forms.TextInput(attrs={'placeholder':'Your phone 2'}),
            'email' : forms.TextInput(attrs={'placeholder':'Your email'}),
        }
        
    
    def __init__(self, *args, **kwargs):
        super(GENQModelsForm, self).__init__(*args, **kwargs)
        self.fields['gender'].choices = [('', 'select a gender'),] + list(self.fields['gender'].choices)[1:]
        self.fields['email'].required = True