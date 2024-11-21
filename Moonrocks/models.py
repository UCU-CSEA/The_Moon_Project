from django.db import models
import datetime


class Cadets(models.Model):
    id = models.AutoField(primary_key=True)
    Names = models.CharField(max_length=50)

    class gender(models.TextChoices):
        Male = 'Male'
        Female = 'Female'

    Gender = models.CharField(max_length=6,choices=gender.choices)
    Organization = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=50)
    Quote = models.CharField(max_length=150)
    DateT = models.DateTimeField(default=datetime.datetime.now())
    Event = models.CharField(max_length=250, default='National ICT Innovation Hub, Nakawa')
    Location = models.CharField(max_length=250, default='8JH7+PQ Kampala')
    #image = models.ImageField(upload_to='{% static /img %}')

    def __str__(self):
        return str(self.id) + '_' + self.Names