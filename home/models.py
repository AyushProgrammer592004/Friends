from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Friend(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name