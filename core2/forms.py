from django.forms import ModelForm
from core2.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        filds = ['titulo','texto']