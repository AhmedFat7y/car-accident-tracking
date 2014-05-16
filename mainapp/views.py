from django.http import Http404
from django.shortcuts import render_to_response
from mainapp.models import Vehicle, SensorsData

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll': p})