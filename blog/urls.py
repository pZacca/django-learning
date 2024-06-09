from django.urls import path
from . import views

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.blog, name="home"),
    path('zacca/', views.zacca, name="zacca")
]
