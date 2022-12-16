from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    spotify_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Review(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    albumArt = models.ImageField(null=True, blank=True, upload_to="images/")
    albumName = models.CharField(max_length=255)
    albumArtist = models.CharField(max_length=255)
    albumGenre = models.CharField(max_length=255)
    albumScore = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
    category = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    review_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='review_posts')


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')