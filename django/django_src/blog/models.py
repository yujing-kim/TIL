
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) # 글쓴이
    title = models.CharField(max_length=200) #제목
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
