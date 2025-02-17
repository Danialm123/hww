from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def redirect_to_threads(request):
    return redirect('thread_list')

def thread_list(request):
    threads = Thread.objects.all()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'threads.html', {'threads': threads, 'form': form})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, pk=id)
    posts = Post.objects.filter(thread=thread)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=id)
    else:
        form = PostForm()
    return render(request, 'thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, pk=id)
    thread.delete()
    return redirect('thread_list')

def thread_edit(request, id):
    thread = get_object_or_404(Thread, pk=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'thread_edit.html', {'form': form})

def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'post': post})
