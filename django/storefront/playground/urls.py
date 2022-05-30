from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('hello1/', views.say_hello1),
    path('hello2/', views.say_hello2),
    path('hello3/', views.say_hello3),
    path('hello4/', views.say_hello4),
    path('putname/', views.put_name)
]
