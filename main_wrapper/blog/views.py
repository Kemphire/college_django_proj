from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostCreationForm, PostEditForm
from django.urls import reverse


def welcome(request):
    context = {
        'posts':Post.objects.filter().order_by("-date_posted"),
        'title':'Home'
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'Contact us'})

def post_detail(request,pk):
    context = {
        'post':Post.objects.filter(pk=pk).first(),
        'title':f'Detail of {pk}\' post',
    }
    return render(request,'blog/post_detail.html',context)

@login_required(redirect_field_name='login')
def new_post_create(request):
    if request.method =='POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title_of_post = form.cleaned_data.get('title')
            messages.success(request,f"Post with title '{title_of_post}' created sucessfully!")
            return redirect('post-detail',post.pk)
    else:
        form = PostCreationForm()
    return render(request,"blog/post_creation_form.html",{'form':form})

@login_required(redirect_field_name='login')
def post_edit(request,pk):
    post = Post.objects.filter(pk=pk).first()
    previous_title = Post.objects.get(pk=pk).title
    if post.author == request.user:
        if request.method == 'POST':
            form = PostEditForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,f"Post \'{previous_title}\' got changed!")
                return redirect('post-detail',post.pk)
            else:
                messages.warning(request,f"Error in editing the form!")
                return redirect('post-detail',post.pk)
        else:
            form = PostEditForm(instance=post)
        return render(request,"blog/post_edit_form.html",{'form':form})
    else:
        messages.warning(request,f"No permission to change this post")
        return redirect('post-detail',pk=post.pk)

@login_required(redirect_field_name='login')
def post_delete(request,pk):
    post = Post.objects.filter(pk=pk).first()
    title = Post.objects.get(pk=pk).title
    if post.author == request.user:
        post.delete()
        messages.success(request,f"Post with title \'{title}\' got deleted!")
        return redirect('blog-home')
    else:
        messages.warning(request,"you are not the owner of the post! kindly refrain from doing this!")
        return redirect('post-detail',pk=post.pk)
    
@login_required(redirect_field_name='login')
def profile_view(request,username):
    user = User.objects.get(username=username)
    return render(request,"blog/profile_view.html",{'user':user})
    




