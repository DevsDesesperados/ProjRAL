"""projRAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  #   this line has a bug and i have no idea how to fix it...
                  #   good luck boys
                  path('menu/', views.menu),
                  path('', RedirectView.as_view(url='/menu/')),
                  path('login/', views.login_user),
                  path('login/submit', views.login_submit),
                  path('logout/', views.logout_user),
                  path('accounts/', include('django.contrib.auth.urls')),  # account setting up XD
                  path('menu/cadastrolegal/', views.cadastro_legal),
                  path('menu/cadastrolegal/submit', views.submit_cadastro_legal),
                  path('menu/cadastrotecnico/', views.cadastro_tecnico),
                  path('menu/cadastrotecnico/submit', views.submit_cadastro_tecnico),
                  path('menu/cadastrooperacional/', views.cadastro_operacional),
                  path('menu/cadastrooperacional/submit', views.submit_cadastro_operacional),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
