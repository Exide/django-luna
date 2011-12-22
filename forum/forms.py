from django.forms import ModelForm
from models import Topic, Post

class TopicForm(ModelForm):
    class Meta:
        model = Topic

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['topic', 'author']
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''