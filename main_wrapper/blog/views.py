from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm


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
        'title':f'Detail of {pk}',
    }
    return render(request,'blog/post_detail.html',context)

@login_required
def new_post_create(request):
    if request.method =='POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title_of_post = form.cleaned_data.get('title')
            messages.success(request,f"Post with title = {title_of_post} created!")
            return redirect('blog-home')
    else:
        form = PostCreationForm()
    return render(request,"blog/post_creation_form.html",{'form':form})

