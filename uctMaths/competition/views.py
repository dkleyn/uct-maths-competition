# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import loader, Context
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django import forms
from competition.forms import TestContact
from competition.models import SchoolStudent


def allauthtest(request):
	return render_to_response('base.html', {})

def content (request, ):
   #t = loader.get_template('base.html')
   return render_to_response('contents.html',{})
   #return HttpResponse(t.render(base.html))

def main (request, ):
   return render_to_response('main.html',{})

def regStudent (request, ):
   return render_to_response('regStudent.html',{})

#def index(request):
 #   return render_to_response('onlinemaths.html', {})
    
def search_form(request):
    if request.method == 'POST': # If the form has been submitted...
        form = TestContact(request.POST) # A form bound to the POST data
       # print "FORM ", form.as_p ()
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            firstname = form.cleaned_data['firstname']
            surname = form.cleaned_data['surname']
            language = form.cleaned_data['reference']
            reference = form.cleaned_data['reference']
            school = form.cleaned_data['school']
            grade = form.cleaned_data['grade']
            sex = form.cleaned_data['sex']
            venue = form.cleaned_data['venue']

            query = SchoolStudent(firstname = firstname , surname = surname, language = language , reference = reference ,
                school = school, grade = grade , sex = sex, venue = venue)
            query.save()

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = TestContact() # An unbound form
    c = {}
    c.update(csrf(request))
    return render_to_response('search_form.html', c)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 3:
            errors.append('Please enter at most 20 characters.')
            return HttpResponse('You submitted')
        else:
            return HttpResponse('You submitted')
    else:
        return HttpResponse('Please submit a search term.')

def student(request):
    if request.method == 'POST': # If the form has been submitted...
        form = TestContact(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            firstname = form.cleaned_data['firstname']
            surname = form.cleaned_data['surname']
            query = SchoolStudent(firstname = firstname , surname = surname)
            query.save()

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = TestContact() # An unbound form

    return render_to_response('search_form.html', {
        'form': form,
    })
