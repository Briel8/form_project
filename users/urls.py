from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_user, name='new_user'),
    path('create/', views.create_user, name='create_user'),
    path('edit/<int:user_id>/', views.edit, name='edit'),
]