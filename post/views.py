from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all().values()
    return JsonResponse(list(posts), safe=False, json_dumps_params={'ensure_ascii': False})




def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    data = {
        'title': post.title,
        'description': post.description,
        'author': post.author
    }
    return JsonResponse(data)

@csrf_exempt
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Post created successfully'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = PostForm()
        return render(request, 'post/post_form.html', {'form': form})

@csrf_exempt
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('/todos')
    else:
        return render(request, 'post/confirm_delete.html', {'post': post})
