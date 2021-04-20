# Create your models here.
import re

from django.contrib.auth.models import User
from django.db import models
from regex_field.fields import RegexField


class Engineer(models.Model): # now the name is fine, updated from "enginner LMAO"
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = RegexField(max_length=11)
    cnpj = RegexField(max_length=14)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    #   cadastro legal
    ANM = RegexField(max_length=12)
    substance = models.CharField(max_length=20)
    use = models.CharField(max_length=20)

    def __str__(self):
        return str(self.ANM)

class CadastroOperacional(models.Model):
    #   cadastro operacional
    ANM_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    operational_situation = models.CharField(max_length=20)
    reason = models.CharField(max_length=50)


class CadastroTecnico(models.Model):

    #   cadastro tecnico
    cpf = Engineer.cpf
    occupation = ''
    occupation_number = ''
    jurisdiction = ''

    elaboration_number = ''
    elaboration_date = ''
    public_authorization = False

