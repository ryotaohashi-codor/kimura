from django.contrib import admin
from django.urls import path
from .views import ProjectListView, ProjectDetailView, DriverProjectListView


urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('drivers/<int:pk>/projects/', DriverProjectListView.as_view(), name='driver_project_list'),

    ]