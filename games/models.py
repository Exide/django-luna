from django.db.models import Model, CharField
from tagging.fields import TagField


class Game(Model):
    name = CharField(max_length=128)
    tags = TagField(blank=False)

    def __unicode__(self):
        return self.name
