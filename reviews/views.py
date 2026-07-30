from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import context
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . forms import ReviewForm
from reviews.models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if request.method == 'POST':
            form = ReviewForm(request.POST)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/thank-you')

            return render(request, 'reviews/review.html', {
                'form': form
            })

class ThankYouView(TemplateView):
   template_name = "reviews/thank_you.html"
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['message'] = "Thank you for your review!"
       return context

# class ReviewListView(TemplateView):
#   template_name = "reviews/review_list.html"
#
#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context['reviews'] = Review.objects.all()
#       return context

class ReviewListView(ListView):
  template_name = "reviews/review_list.html"
  model = Review
  context_object_name = 'reviews'


class ReviewDetailView(DetailView):
    template_name = "reviews/review_details.html"
    model = Review
    context_object_name = 'review'



