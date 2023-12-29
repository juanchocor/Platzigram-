from django.urls import reverse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from users.models import Profile

class ProfileCompletionMiddleware:

        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            try:
                if not request.user.is_anonymous:
                    profile = request.user.profile
                    if not profile.picture or not profile.bigoraphy:
                        if request.path not in [ reverse('update_profile'), reverse('logout')]:
                             return redirect('update_profile')
                        
            except ObjectDoesNotExist:
                 profile = Profile(user= request.user)
                 profile.save()

            response = self.get_response(request)
            return response
