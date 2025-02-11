from django.urls import path
from . import views

urlpatterns = [
    path('create-pr/', views.create_pr_document, name='create_pr_document'),
]