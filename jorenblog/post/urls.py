from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('<int:pk>/', views.detail, name='detail')
]