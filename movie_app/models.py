from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum

# Create your models here.


class Director(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    def movies_count(self):
        return self.film.all().count()


class Movie(models.Model):
    title = models.TextField()
    description = models.TextField()
    duration = models.DurationField(verbose_name=None)
    director = models.ForeignKey(Director,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 related_name='film')
    stars = models.PositiveSmallIntegerField(
        default=1, validators=[MaxValueValidator(5),
                               MinValueValidator(1)])

    def __str__(self):
        return self.title

    def reviews(self):
        review = Review.objects.filter(movie=self)
        return [{'text'} for i in review]

    def rating(self):
        summa = Review.objects.all().aggregate(Sum('stars'))["stars_sum"]
        count = Review.objects.all().count()
        try:
            return summa / count
        except:
            return 0


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)

    def detail_link(self):
        return f'http://127.0.01:8000/api/v1/movies/{self.id}/'