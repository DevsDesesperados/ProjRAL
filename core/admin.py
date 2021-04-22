from django.contrib import admin
from core.models import Engineer, Project, CadastroOperacional,CadastroTecnico
# Register your models here.

admin.site.register(Engineer)
admin.site.register(Project)
admin.site.register(CadastroOperacional)
admin.site.register(CadastroTecnico)