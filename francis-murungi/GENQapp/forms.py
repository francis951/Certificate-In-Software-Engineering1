from django import forms
from .models import GENQModels

class GENQModelsForm(forms.ModelForm):
    class Meta:
        model = GENQModels
        fields = ('f_name','l_name', 'date', 'gender', 'country', 'state','town', 'zip','phone1','phone2', 'email')

        labels ={
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'email':'Email',
        }
        #placeholders
        widget = {
            'f_name' : forms.TimeInput(attrs={'placeholder':'Your name'}),
            'phone1' : forms.TimeInput(attrs={'placeholder':'Your phone'}),
            'email' : forms.TimeInput(attrs={'placeholder':'Your email'}),
        }
        
    
    def __init__(self, *args, **kwargs):
        super(GENQModelsForm, self).__init__(*args, **kwargs)
        self.fields['gender'].choices = [('', 'select a gender'),] + list(self.fields['gender'].choices)[1:]
        self.fields['email'].required = True