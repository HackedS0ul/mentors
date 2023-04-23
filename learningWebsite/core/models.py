from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    picture = models.ImageField(upload_to='users', default='users/user.png')
    birthdate = models.DateField(null=True)
    website = models.CharField(max_length=150, default='https://hackedsoul.com')
    facebook_url = models.CharField(max_length=250)
    mentor_path = models.CharField(max_length=255, default="Python programavimas, IT saugumas")
    github_url = models.CharField(max_length=250)
    ratings = models.FloatField(default=0)
    address = models.CharField(max_length=255, default="Vilnius")
    hour_rate = models.CharField(max_length=10, default="10-30")
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'website']

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    comment = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.user);

class Course(models.Model):
    name = models.CharField(max_length=100)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ratings = models.FloatField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images')
    
    
    def __str__(self):
        return self.name