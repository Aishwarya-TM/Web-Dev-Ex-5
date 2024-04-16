from django import forms

class CylinderForm(forms.Form):
    radius = forms.FloatField(label='Radius')
    height = forms.FloatField(label='Height')
