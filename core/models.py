# Create your models here.
import re

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from regex_field.fields import RegexField


class Report(models.Model): # this sets the report, each user have one report.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Engineer(models.Model): # now the name is fine, updated from "enginner LMAO"
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = RegexField(max_length=11)
    cnpj = RegexField(max_length=14)
    anm = RegexField(max_length= 12)
