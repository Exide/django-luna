from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UserForm, ProfileForm


def profile(request, username):
    user = get_object_or_404(User, username__iexact=username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            return redirect('/account/%s' % user.username)
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)

    return render_to_response('account/profile.html',
                              {
                                  'user_form': user_form,
                                  'profile_form': profile_form,
                                  'userObject': user
                              },
                              context_instance=RequestContext(request))


def index(request):
    return render_to_response('account/index.html',
                              {
                                  'accounts': User.objects.filter(is_active=True)
                              },
                              context_instance=RequestContext(request))
