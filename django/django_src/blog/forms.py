from django import forms
from .models import Post

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator]) # 제목
    text = forms.CharField(widget=forms.Textarea) # 내용


# Model Form을 상속받는
class PostModelForm(forms.ModelForm):
    # ModelForm : Model과 연관된 Form을 만듦
    class Meta: # rule
        model = Post
        fields = ('title', 'text')
    # validate검사를 Modelform에서 할 수 없음
    # 그래서 Model에서 해주어야한다.