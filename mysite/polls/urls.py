from django.urls import path

from . import views

urlpatterns = [
    path('questions/', views.QuestionsApiView.as_view(), name='questions'),
]
