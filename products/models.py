from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=25)
    pub_date = models.DateField()
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    total_votes = models.IntegerField(default=1)
    hunter = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

