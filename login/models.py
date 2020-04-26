from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[a-zA-Z]+$')
class UserManager(models.Manager):
    def cleandata_reg(self, data):
        print(data)
        errors={}
        a=data['f_name']
        b=data['l_name']
        c=data['email']
        d=data['pw']
        e=data['r_pw']
        for k in data:
            if len(data[k])==0:
                errors[k]='This cannot be empty'
        if not errors:
            if len(a)<2 or not NAME_REGEX.match(a):
                errors['f_name']='This need to be more than 2 character; letter only'
            if len(b)<2 or not NAME_REGEX.match(b):
                errors['l_name']='This need to be more than 2 character; letter only'
            if not EMAIL_REGEX.match(c):# test whether a field matches the pattern
                errors['email'] = "Invalid email address!"
            elif User.objects.filter(email=c):
                print (User.objects.filter(email=c))
                errors['email'] = "This account was already registered. Please login!" # special
            if len(d)<8:
                errors['pw']='This need to be more than 8 character'
            elif d != e :
                errors['r_pw']='PW does not match. Please try again!'
        
        return errors

    def cleandata_log(self, data):
        print(data)
        errors={}
        a=data['l_email']
        b=data['l_pw']
        for k in data:
            if len(data[k])==0:
                errors[k]='This cannot be empty'
        if not errors:
            if EMAIL_REGEX.match(a):    # test whether a field matches the pattern            
                if User.objects.filter(email=a):
                    c=User.objects.get(email=a).pw
                    if len(b)<8:
                        errors['l_pw']='This need to be more than 8 character'
                    elif not bcrypt.checkpw(b.encode(),c.encode()):
                        errors['l_pw']= 'password is not correct'
                else:
                    errors['l_email']= 'This email is not registered. Please register!'     
            else:
                errors['l_email'] = "Invalid email address!"
        
        return errors




class User(models.Model):
    f_name= models.CharField(max_length=255)
    l_name= models.CharField(max_length=255)
    email= models.CharField (max_length=255)
    pw= models.CharField (max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= UserManager()
    def __repr__(self):
        return self.f_name
# Create your models here.
