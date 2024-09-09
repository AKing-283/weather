from django import forms

class CityForm(forms.Form):
    name = forms.CharField(label='City Name', max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter city name'}))
