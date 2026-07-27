from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review, name='review'),
]