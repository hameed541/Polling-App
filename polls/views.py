from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Option

def home(request):
    polls = Poll.objects.all()
    return render(request, 'polls/home.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        option_id = request.POST.get('option')
        option = get_object_or_404(Option, id=option_id)
        option.votes += 1
        option.save()
        return redirect('results', poll_id=poll.id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
