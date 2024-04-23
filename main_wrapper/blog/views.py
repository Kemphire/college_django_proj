from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm, PostEditForm


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
    if request.method == 'POST':
        form = PostEditForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,f"Post \'{previous_title}\' got changed!")
            return redirect('post-detail',post.pk)
    else:
        form = PostEditForm(instance=post)
    return render(request,"blog/post_edit_form.html",{'form':form})

@login_required(redirect_field_name='login')
def post_delete(request,pk):
    post = Post.objects.filter(pk=pk).first()
    previous_title = Post.objects.get(pk=pk).title
    if request.method == 'POST':
        post.delete()
        messages.success(request,f"Post with title \'{previous_title}\' got deleted!")
        return redirect('blog-home')
    return redirect(request,"blog/post_delete_confirmation.html",{'post':post})


