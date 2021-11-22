from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Ojuser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    
