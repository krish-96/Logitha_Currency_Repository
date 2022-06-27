from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=64, blank=False, null=False)
    phone_no = models.BigIntegerField(blank=False, null=False)
    Message = models.TextField(max_length=264, blank=False, null=False)

    def __str__(self):
        return self.name + ' - ' +self.email