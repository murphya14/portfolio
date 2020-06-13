from django.db import models
from hobby_product.models import hobby_product
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Review(models.Model):

        RATING_CHOICES = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        )

        author = models.ForeignKey(User, on_delete=models.CASCADE)
        content = models.TextField()
        published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
        image = models.ImageField(upload_to="img", blank=True, null=True)
        rating = models.IntegerField(choices=RATING_CHOICES, default=5, blank=False)


def __unicode__(self):
        return self.title



def __unicode__(self):
        return self.name

'''Create a str of the model'''
def __str__(self):
            return "Product " + str(self.pk) + " " + self.name
