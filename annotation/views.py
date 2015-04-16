# Create your views here.
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from annotation.models import Entry
import datetime
import re

def index(request):
    latest_entry_list = Entry.objects.all().order_by('english_word')[:10]
   # t = loader.get_template('annotation/index.html')
   # c = Context({
   #     'latest_entry_list': latest_entry_list,
   # })
   # return HttpResponse(t.render(c))
    return render_to_response('annotation/index.html', {'latest_entry_list': latest_entry_list},
        context_instance=RequestContext(request))

def detail(request, entry_id):
    e = get_object_or_404(Entry, pk=entry_id)
    return render_to_response('annotation/detail.html', {'entry': e},
                               context_instance=RequestContext(request))

def search_helper(request):
    string = request.POST['search']
    return HttpResponseRedirect(reverse('annotation.views.search', args=(string, )))
    #render_to_response('search.html', {'string': string},
    #               context_instance=RequestContext(request))


def search(request, string):
    regex = re.compile(string)
    search_entry_list = Entry.objects.all().order_by('-pub_date')
    search_entry_list = [entry for entry in search_entry_list if regex.match(entry.english_word.lower())]
    t = loader.get_template('annotation/search.html')
    c = Context({
        'string': string,
        'search_entry_list': search_entry_list,
    })
    return HttpResponse(t.render(c))


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def add(request, entry_id):
    e = get_object_or_404(Entry, pk=entry_id)
    
    new_translation = request.POST['translation']
    e.translation_set.create(foreign_word=new_translation)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('annotation.views.detail', args=(e.id,)))

def add_new(request):
    new_word = request.POST['add_new']
    Entry.objects.create(english_word=new_word, pub_date=datetime.datetime.utcnow())
    return HttpResponseRedirect(reverse('annotation.views.index'))
