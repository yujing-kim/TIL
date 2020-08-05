from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/  -> 뒤에 아무것도 안옴
    path('', views.post_list, name='post_list'),
]