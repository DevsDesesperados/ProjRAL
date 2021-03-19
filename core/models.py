from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from regex_field.fields import RegexField
from django.contrib.auth.models import User

class Relator(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Enginner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = RegexField(max_length= 11)
    cnpj = RegexField(max_length= 14)