from curses.ascii import HT
from django.template import RequestContext # Try this first

from django.conf import settings # Try this second

from django.http import HttpRequest
from . import util

# # RFER 9 # Revison_v1
# random_entry_v1 = RequestContext(request, {
#     'random_entry':util.random_entry(request)
# })

# RFER 10 # Revison_v2
def get_random_entry(request:HttpRequest):
    return {
        'random_entry':util.random_entry(request)
        }
