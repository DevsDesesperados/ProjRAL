# Create your models here.
import re

from django.contrib.auth.models import User
from django.db import models
from regex_field.fields import RegexField


class Engineer(models.Model): # now the name is fine, updated from "enginner LMAO"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=20, primary_key=True)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #   cadastro legal
    ANM = models.CharField(max_length=12, primary_key=True)
    substance = models.CharField(max_length=20)
    use = models.CharField(max_length=20)

    def __str__(self):
        return str(self.ANM)

class CadastroOperacional(models.Model):
    #   cadastro operacional
    ANM = models.ForeignKey(Project, on_delete=models.CASCADE, db_column='ANM')
    operational_situation = models.CharField(max_length=20)
    reason = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.ANM)

    def get_creation_date(self):
        return self.creation_date.strftime('%d/%m/%Y')
class CadastroTecnico(models.Model):

    #   cadastro tecnico
    cpf = models.OneToOneField(Engineer, max_length=20, on_delete=models.CASCADE, primary_key=True)
    occupation = models.CharField(max_length=30,default='Outros...')
    occupation_number = models.IntegerField(default=0)
    jurisdiction = models.CharField(max_length=8,default='CREA-**')

    elaboration_number = models.IntegerField(default=0)
    elaboration_date = models.DateField()
    ral_jurisdiction= models.CharField(max_length=8,default='CREA-**')
    public_authorization = models.BooleanField(default=False)

    def __str__(self):
        return self.cpf.user


