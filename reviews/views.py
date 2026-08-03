from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from . forms import ReviewForm
from reviews.models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


class ThankYouView(TemplateView):
   template_name = "reviews/thank_you.html"
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['message'] = "Thank you for your review!"
       return context

class ReviewListView(ListView):
  template_name = "reviews/review_list.html"
  model = Review
  context_object_name = 'reviews'


class ReviewDetailView(DetailView):
    template_name = "reviews/review_details.html"
    model = Review
    context_object_name = 'review'


class AddFavoriteView(View):

    def post (self, request):
        review_id = request.POST.get('review_id')
        fav_review =Review.objects.filter(pk=review_id).update(is_favorite=True)
        request.session['favorite_review'] = fav_review
        return HttpResponseRedirect('/reviews/' + review_id)