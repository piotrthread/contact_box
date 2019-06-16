"""contact_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from my_contacts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_contacts),
    path('delete/<to_delete>', del_contact),
    path('new/', add_contact),
    path('show/<id>', show_by_id),
    path('modify/<id>', modify_contact),
    path('<id>/addAdress', add_adress),
    path('<id>/addEmail', add_email),
    path('<id>/addPhone', add_phone),
    path('<id>/deleteAdress/<to_delete>', del_adress),
    path('<id>/deleteEmail/<to_delete>', del_email),
    path('<id>/deletePhone/<to_delete>', del_phone),
    path('groups/', all_groups),
    path('groups/delete/<to_delete>', del_group),
    path('newGroup/', add_group),
    path('groups/show/<id>', group_by_id),
    path('groups/<group_id>/delete/<person_id>', delete_from_group),
    path('groups/<group_id>/addMembers', add_members),
    path('add/<person_id>/group/<group_id>', add_member_to_group),
]
