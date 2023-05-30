from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_spells_by_vocation, name="get_spells_by_vocation"),
]
