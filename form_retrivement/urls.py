from django.urls import path
from . import views

urlpatterns = [
    path('done', views.done),
    path('', views.index)
]
