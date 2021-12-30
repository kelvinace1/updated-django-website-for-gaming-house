from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Debt(models.Model):
    CHOICES = {
        ('ps2', 'ps2'),
        ('ps3', 'ps3'),
        ('ps4', 'ps4')
    }
    name = models.CharField(max_length=50, null=True)
    game = models.CharField(null=True,max_length=200, choices=CHOICES)
    amount = models.IntegerField(null=True)
    paid = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)
    keeper = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('debt_detail', kwargs={'pk':self.pk})
    
class Booking(models.Model):
    GAME_CHOICE = (
        ('1', 'ps1'),
        ('2', 'ps2'),
        ('3', 'ps3'),
        ('4', 'ps4')
    )
    name = models.CharField(max_length=30)
    number =models.IntegerField()
    console = models.CharField(max_length=30, choices=GAME_CHOICE)
    description = models.TextField()
    booker = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('book_list')