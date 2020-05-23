
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    a = "sadegh"
    test = {
        'latest_question': latest_question_list,
        'name':a
    }
    #return HttpResponse(template.render(test, request))
    return render(request, 'polls/index.html',test)


# Create your views here.
def detail(request, question_id):
    #try:
    question = get_object_or_404(Question, pk=question_id)#.objects.get(pk = question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question.question_text)

def choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/choice.html', {'question': question})

def results(request, question_id):
    question = Question.objects.get(pk= question_id)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice_com'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


def ali(request):
    return HttpResponse("Inja vase ali")


def javadResponse(request):
    return HttpResponse("inja vase javad")

def sajad(rrequest, question_id):
    s = Question.objects.get(pk= question_id)
    response = "Question: " + s.question_text + " publish Date: " + str(s.pub_date)
    return HttpResponse(response)

