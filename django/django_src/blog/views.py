from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

def post_list(request):
    name = 'Django'
    # return HttpResponse('''<h2>Post List</h2>
    #                         <p>{name}</p>
    #                         <p>{content}</p>'''.format(name=name, content = request.user))
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts' : posts})