from django.urls import path
from . import views
urlpatterns=[
    path ('',views.input),
    path ('register',views.register),
    path ('login',views.login),
    path ('success',views.success),
    path ('log_out',views.log_out),
]