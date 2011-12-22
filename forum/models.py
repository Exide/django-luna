from django.db.models import Model, DateTimeField, ForeignKey, CharField, TextField
from django.contrib.auth.models import User
from tagging.fields import TagField

class Topic(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    title = CharField(max_length=64)
    tags = TagField(blank=False)

    def __unicode__(self):
        return self.title
    
    def last_updated(self):
        return self.post_set.latest('updated_at')

class Post(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    topic = ForeignKey(Topic)
    author = ForeignKey(User)
    content = TextField()

    def __unicode__(self):
        return self.content