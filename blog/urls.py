"""
mysite/urls.py から'http://127.0.0.1:8000/'に来た(adminがない)リクエストは、
include文より、ここを参照するようになっている
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),#ここの引数にpkがないのがすごいキモイ
]
