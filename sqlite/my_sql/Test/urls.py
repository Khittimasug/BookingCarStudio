from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('data', views.data),
    path('login', views.login),
    path('form', views.form),
    path('form_view', views.form_view),
    path('success', views.success, name="success"),
    path('upload', views.upload_file, name='upload_file'),
    path('uploadList', views.uploadList, name='upload_list'),
    
] 