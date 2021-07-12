
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import ImagerForm


def get_name(request):

    names = Imager.objects.all()
    form = ImagerForm()


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ImagerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/view/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ImagerForm()

    context = {'names': names,
               'form': form,
               }
    return render(request, 'checkbox/emailer.html', context)