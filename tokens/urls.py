from django.urls import path

from . import views

urlpatterns = [
    path("create", views.tokens_create, name="create"),
    path("list", views.tokens_list, name="list"),
    path("total_supply", views.tokens_total_supply, name="total_supply"),
]
