from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.contrib.auth import logout
from django.forms import ModelForm, CheckboxSelectMultiple
from django.forms.widgets import *
from wstest.app.models import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from simplejson import dumps

def index(request):
    if request.method == "POST":
        pass
    else:
        pass
    template_data = {
    }
    
    return render_to_response('index.html', template_data, context_instance=RequestContext(request))
