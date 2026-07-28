from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(min_length=2, max_length=15)

