from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        app_label = 'app'


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, default='Mon')  # Mon, Tue, Wed, Thu, Fri, Sat, Sun
    # updated_ad = models.DateField()
    items = models.TextField()


class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vote = models.BooleanField(default=True)  # True for like, False for dislike
    date = models.DateField(auto_now_add=True)
