"""
Login Proxy Authentication

Uses the login information from the HTTP_X_USERNAME etc. HTTP headers
"""

from django.core.mail import send_mail
from django.conf import settings

import logging

import os

# some parameters to indicate that status updating is possible
STATUS_UPDATES = False


def get_auth_url(request, redirect_url = None):
  return '/ICSLogin/auth-up?url=/auth/after'

def get_user_info_after_auth(request):
  username = request.META['HTTP_X_USERNAME']
  name = request.META['HTTP_X_FIRSTNAME'] + ' ' + request.META['HTTP_X_LASTNAME']
  info = {'email': request.META['HTTP_X_EMAIL']}

  if username:
    return {'type': 'opensuse', 'user_id' : username, 'name': username, 'info': info, 'token': None}
  else:
    return None

def update_status(token, message):
  pass

def send_message(user_id, user_name, user_info, subject, body):
  email = user_info['email']
  name = user_name
  send_mail(subject, body, settings.SERVER_EMAIL, ["\"%s\" <%s>" % (name, email)], fail_silently=False)

def check_constraint(constraint, user_info):
  """
  for eligibility
  """
  # XXX doesn't seem to work :-( (actually I'm not sure if this function gets called at all) -> upload list of valid voters!
  pass

#
# Election Creation
#

def can_create_election(user_id, user_info):
  if user_id in settings.ELECTION_CREATORS:
    return True

  return False
