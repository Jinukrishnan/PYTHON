from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = ["name",'desc','year','img']
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),

        }
        widgets['img'] = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
