from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("CVPDF", views.CD_PDF, name="CVPDF"),
    path("register", views.register_user, name="register"),
]