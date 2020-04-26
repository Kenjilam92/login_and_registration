from django.urls import path
from . import views

urlpatterns= [
    path ('',views.displaywall),
    path ('/post',views.post_message),
    path ('/comment',views.comment_a_post),
]