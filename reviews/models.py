from django.db import models

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length = 500,unique = True, error_messages= {
        'unique' : "A user with that username already exists.",
        'required' : "This field is required.",
        'blank' : "This field may not be blank.",
        'null' : "This field may not be null.",
    })
    review_text = models.TextField()
    rating = models.IntegerField()
    review_date = models.DateField(auto_now_add=True)