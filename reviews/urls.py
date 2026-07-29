from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewView.as_view(), name='reviews'),
    path('thank-you', views.ThankYouView.as_view(), name='reviews/thank-you.html'),
]