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
    review_text = forms.CharField(
        max_length=500,
        widget=forms.Textarea,
        label="Your review",
        error_messages={
            'required': 'Please enter a review.',
            'max_length': 'Please enter a review.',
        }
    )
    rating = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        ),
        error_messages={
            'required': 'Please enter a review.',
        }
    )

