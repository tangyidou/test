from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    password = models.CharField(null=True, blank=True, max_length=50)
    email = models.CharField(null=True, blank=True, max_length=50)
    url_image = models.URLField(null=True, blank=True)
    author_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.name
