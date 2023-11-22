from allauth.account.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def social_login(request, user, **kwargs):

    user.is_social = True
    user.save()