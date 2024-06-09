from django.urls import path
from . import views

app_name = 'blog'

# blog/
urlpatterns = [
    path('<int:post_id>/', views.post, name="post"),
    path('', views.blog, name="index"),
    path('zacca/', views.zacca, name="zacca")
]
