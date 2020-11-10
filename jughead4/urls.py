from django.urls import path
from . import views
#app_name = 'jughead4'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/result/', views.result, name='result'),
]