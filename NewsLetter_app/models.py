from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    mail = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.mail