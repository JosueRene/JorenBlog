from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.editpost, name='edit'),
    path('new/', views.newpost, name='new'),
    path('dashboard/', views.dashboard, name="dashboard")
]