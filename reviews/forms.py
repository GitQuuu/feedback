from django import forms

from reviews.models import Review


# class ReviewForm(forms.Form):
#     username = forms.CharField(
#         min_length=2,
#         max_length=15,
#         label="Your username",
#         error_messages={
#             'required': 'Please enter a username.',
#             'min_length': 'Please enter a username greater than 2.',
#         },
#     )
#     review_text = forms.CharField(
#         max_length=500,
#         widget=forms.Textarea,
#         label="Your review",
#         error_messages={
#             'required': 'Please enter a review.',
#             'max_length': 'Please enter a review.',
#         }
#     )
#     rating = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         ),
#         error_messages={
#             'required': 'Please enter a review.',
#         }
#     )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'username': 'Your name',
            'review_text': 'Your feedback',
            'rating': 'Your rating',
        },
        error_messages = {
            'username': {
                'required': 'Please enter a valid username.',
                'invalid': 'Please enter a valid username.',
            },
            'review_text': {
                'required': 'Please enter a valid review text.',
            },
            'rating': {
                'required': 'Please enter a valid rating.',
            }
        }

