from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review, name='reviews'),
    path('thank-you', views.thank_you, name='reviews/thank-you.html'),
]