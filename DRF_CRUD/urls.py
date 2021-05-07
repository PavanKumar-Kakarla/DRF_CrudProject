"""DRF_CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from crud_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person_list/',views.person_List,name='person_list'),
    path('person_detail/<str:pk>/',views.person_Detail,name='person_detail'),
    path('person_create/',views.person_Create,name='person_create'),
    path('person_update/<str:pk>/',views.person_Update,name='person_update'),
    path('person_delete/<str:pk>/',views.person_Delete,name='person_delete'),
    
]
