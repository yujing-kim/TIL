
from django.db import models
from django.utils import timezone
from django import forms


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

# 게시글의 속성
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) # 글쓴이
    title = models.CharField(max_length=200, validators=[min_length_3_validator]) #제목
    text = models.TextField() # 내용
    created_date = models.DateTimeField(default=timezone.now) # 작성일
    published_date = models.DateTimeField(blank=True, null=True) # 게시일
    # test = models.TextField() # 필드 추가 - 삭제할 예정

    #게시일자에 현재날짜 시간을 대입해주는 함수
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # 승인된 Comments만 반환해주는 함수
    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

# 댓글의 속성
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments' ) # post를 참조
    author = models.CharField(max_length=200) # 저자
    text = models.TextField() # 내용
    created_date = models.DateTimeField(default=timezone.now) # 작성일
    approved_comment = models.BooleanField(default=False) # 댓글 승인 여부

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

