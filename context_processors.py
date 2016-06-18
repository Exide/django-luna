def default(request):
    from django.conf import settings
    return {'SITE_NAME': settings.SITE_NAME}
