from django.db import models
from login.models import User
# Create your models here.
class PostManager(models.Manager):
    def validation_post(self, postData):
        print (postData)
        errors={}
        a=postData['post']
        b=postData['user_id']
        if len(a)==0:
            errors['post']='You cannot summit an empty message'
        return errors
class CommentManager(models.Manager):
    def validation_comment(self, commentData):
        print('#####################')
        print (commentData)
        errors={}
        a=commentData['comment']
        b=commentData['user_id']
        if len(a)==0:
            errors['comment']='You cannot summit an empty message'
        return errors
class Post(models.Model):
    post= models.TextField()
    author= models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE) 
    created_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)
    objects= PostManager()
    def __repr__(self):
        return self.created_date.strftime('%Y-%m-%d, %H:%M:%S')
class Comment (models.Model):
    comment= models.TextField()
    author= models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post= models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE) 
    created_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)
    objects= CommentManager()
    def __repr__(self):
        return self.created_date.strftime('%Y-%m-%d, %H:%M:%S')