from django.shortcuts import render,redirect
from login.models import User
from .models import Post, Comment
from django.contrib import messages
# Create your views here.
def displaywall(request):
    print('*'*100)
    print('WALL')
    context={
        'posts': Post.objects.all(),
    }
    # user=User.objects.get(id=request.session['user']['id'])
    return render (request,'wall.html',context)
def post_message(request):
    print('*'*100)
    print('A MESSAGE IS POSTED')
    print(request.POST)
    errors= Post.objects.validation_post(request.POST)
    if errors:
        for k,v in errors.items():
            messages.error(request,v, extra_tags='post')
        return redirect('/wall')
    else:
        a=request.POST['post']
        b=request.POST['user_id']
        author=User.objects.get(id=b)
        new_post=Post.objects.create(post=a,author=author)
        return redirect('/wall')
def  comment_a_post(request):
    print('*'*100)
    print('A POST IS COMMENTED')
    print(request.POST)
    errors= Comment.objects.validation_comment(request.POST)
    if errors:
        for k,v in errors.items():
            messages.error(request,v, extra_tags='comment')
        return redirect('/wall')
    else:
        a=request.POST['comment']
        b=request.POST['user_id']
        c=Post.objects.get(id=int(request.POST['post_id']))
        author=User.objects.get(id=b)
        new_comment=Comment.objects.create(comment=a,author=author,post=c)
        return redirect('/wall')