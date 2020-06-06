from django import forms


class DateForm(forms.Form):
    date = forms.DateField(required=True, widget=forms.DateInput())
