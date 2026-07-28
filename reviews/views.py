from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method == 'POST':
        username = request.POST['username']
        if username == "":
            return render(request, 'reviews/review.html', {
                'has_error': True,
                'error_message': 'Username is required'
            })
        print(username)
        return HttpResponseRedirect('/thank-you')
    return render(request, 'reviews/review.html')

def thank_you(request):
    return render(request, 'reviews/thank_you.html', {
        'has_error': False ,
    })