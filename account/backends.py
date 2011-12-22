from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class CaseInsensitiveBackend(ModelBackend):

	def authenticate(self, username=None, password=None):
		try:
			user = User.objects.get(username__iexact=username)
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None