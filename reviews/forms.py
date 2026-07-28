from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(
        min_length=2,
        max_length=15,
        label="Your username",
        error_messages={
            'required': 'Please enter a username.',
            'min_length': 'Please enter a username greater than 2.',
        },
    )

