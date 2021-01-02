from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    class Meta:
        db_table = 'Artist'

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    release_date = models.DateField()

    choices = (
        (1, 'Worst'),
        (2, 'Bad'),
        (3, 'Ok'),
        (4, 'Good'),
        (5, 'Best'),
    )

    rating = models.IntegerField(choices=choices)

    class Meta:
        db_table = 'Album'

    def __str__(self):
        return self.name