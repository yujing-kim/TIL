# django에서 제공하는 import
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # page handler

# 내가 만든 imports
from .models import Post, Comment
from .forms import PostModelForm, PostForm, CommentModelForm

def post_list(request):
    name = 'Django'

    # return HttpResponse('''<h2>Post List</h2>
    #                         <p>{name}</p>
    #                         <p>{content}</p>'''.format(name=name, content = request.user))

    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #
    # return render(request, 'blog/post_list.html', {'posts' : posts})

    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(post_list, 2) # 한 페이지에 두개씩
    page = request.GET.get('page') # 페이지 번호 : 쿼리 스트링으로 넘기기 위한 변수
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage: # 페이지가 없으면 전체 글을 준다.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts})

# Post 상세조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

# post 등록
@login_required
def post_new(request):
    if request.method == 'POST': # save버튼을 눌렀을때,
        form = PostForm(request.POST)
        if form.is_valid(): # 유효성 검사
            print(form.cleaned_data)
            post = Post.objects.create(author=User.objects.get(username = request.user),
                                       published_date=timezone.now(),
                                       title=form.cleaned_data['title'],
                                       text=form.cleaned_data['text']) # save 필요없다
            # post = form.save(commit=False)
            # post.author = User.objects.get(username = request.user) # ver3에서는 이렇게 해주어야한다.
            # post.published_date = timezone.now()
            # post.save()
            return redirect('post_detail', pk=post.pk) # 저장하자 마자 post_detail로 바로 분기

    else : # http method == 'GET'
        form = PostForm() # 등록 form을 보여준다
    return render(request, 'blog/post_edit.html', {'form': form} )

# Post 수정
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST': # save버튼을 누름
        # 수정을 처리하는 부분
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else : # 연필 버튼을 누름
        # 수정하기 전에 데이터를 읽어오는 부분
        form = PostModelForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# post 삭제
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete() # 삭제하기
    return redirect('post_list') # 지우자 마자 글 list로 이동

# comment 추가하는 함수
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentModelForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

# comment 승인
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


# comment 삭제
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)