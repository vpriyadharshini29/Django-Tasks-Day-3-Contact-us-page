from django.urls import path
from . import views

urlpatterns = [
    path("manual/", views.contact_manual, name="contact_manual"),
    path("model/", views.contact_modelform, name="contact_modelform"),
]
