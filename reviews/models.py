from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from accounts.models import User
from music.models import Album


# Create your models here.
class Review(models.Model):
    class Rating(models.IntegerChoices):
        S = 8, 'S'
        A_plus = 7, 'A+'
        A = 6, 'A'
        B_plus = 5, 'B+'
        B = 4, 'B'
        C = 3, 'C'
        D = 2, 'D'
        F = 1, 'F'

    id = models.CharField(primary_key=True, default=get_random_string, editable=False, max_length=8)
    authors = models.ManyToManyField(User, related_name='reviews')
    rating = models.IntegerField(choices=Rating.choices, default=Rating.F)
    album = models.OneToOneField(Album, related_name='review', on_delete=models.CASCADE)
    standfirst = models.TextField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, blank=True)

    def album_name(self):
        return self.album.name

    def album_artists(self):
        return "\n".join([a.name for a in self.album.artists.all()])

    def review_authors(self):
        return "\n".join([a.name for a in self.authors.all()])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.album_artists() + '-' + self.album_name())
        super(Review, self).save(self, *args, **kwargs)

    def __str__(self):
        return self.album.name
