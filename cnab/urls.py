from django.urls import path
from . import views

urlpatterns = [path("cnab/", views.DocumentationViews.as_view())]
