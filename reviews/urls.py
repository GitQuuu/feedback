from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewView.as_view(), name='reviews'),
    path('thank-you', views.ThankYouView.as_view(), name='reviews/thank-you.html'),
    path('reviews', views.ReviewListView.as_view()),
    path('reviews/favorite', views.AddFavoriteView.as_view(), name='add-favorite'),
    path('reviews/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
]