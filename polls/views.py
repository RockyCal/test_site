from django.template import Context, loader, RequestContext
from polls.models import Choice, Question
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404

def vote(request, poll_id):
    q = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['Choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'Question': q,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a 
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results', args=(q.id,)))
