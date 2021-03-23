# Create your models here.
import re

from django.contrib.auth.models import User
from django.db import models
from regex_field.fields import RegexField


class Engineer(models.Model): # now the name is fine, updated from "enginner LMAO"
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = RegexField(max_length=11)
    cnpj = RegexField(max_length=14)

class Project(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    #   cadastro legal
    ANM = RegexField(max_length=12)
    substance = ''
    use = ''

    #   cadastro operacional
    operational_situation = ''
    reason = ''

    #   cadastro tecnico
    cpf = Engineer.cpf
    occupation = ''
    occupation_number = ''
    jurisdiction = ''

    elaboration_number = ''
    elaboration_date = ''
    public_authorization = False