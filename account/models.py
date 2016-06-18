from django.contrib.auth.models import User
from django.db import models


def content_file_name(instance, filename):
    return '/'.join(['content', str(instance.user.id), filename])


class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    avatar = models.ImageField(upload_to=content_file_name, blank=True)
    location = models.CharField(max_length=16, blank=True)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
