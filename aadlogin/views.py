from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode

import json


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    else:
        return render(request, 'index.html')


@login_required
def dashboard(request):
    user = request.user
    aadUser = user.social_auth.get(provider='aad')
    userdata = {
        'user_id': aadUser.uid,
        'username': user.first_name
    }

    return render(request, 'dashboard.html', {
        'userdata': json.dumps(userdata, indent=4)
    })

def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://login.microsoftonline.com/' + settings.SOCIAL_AUTH_AAD_DOMAIN + '/oauth2/logout?post_logout_redirect_uri=' + request.build_absolute_uri('/')
    return HttpResponseRedirect(logout_url)
