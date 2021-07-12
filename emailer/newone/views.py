


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import NameForm


def index(request):

    names = Name.objects.all()
    context = {'names':names,

    }
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/view/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'checkbox/emailer.html/', {'form': form}, context)