from django.shortcuts import render
from django.http import HttpResponseRedicrect

# Create your views here.
def review(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
    return HttpResponseRedicrect('/thank-you')

def thank_you(request):
    return render(request, 'reviews/thank_you.html')