from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Choice, Voter
from django.contrib.auth.models import User

# Create your views here.
@login_required
def vote(request, pk):
    if Voter.objects.filter(user_id=request.user.id).exists():
        return render(request, 'postdetail.html', {
        'poll': p,
        'error_message': "Sorry, but you have already voted."
        })
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'postdetail.html', {
        'poll': p,
        'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        v = Voter(user=request.user, poll=p)
        v.save()
        return HttpResponseRedirect(reverse('posts:results', args=(p.id)))
