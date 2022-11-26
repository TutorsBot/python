from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
from json import dumps
# Create your views here.

# def index(request):
#     latest_question = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question])
#     output = ''
#     for q in latest_question:
#         output += f'<li>{q.question_text}</li>'
#     return HttpResponse(output)


# def index(request):
#     latest_question = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('appone/index.html')
#     context = {}
#     # return HttpResponse(output)
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('appone/index.html')
    context = {
        'latest_question_list' : latest_question,
    }
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("your are looking for the question is %s" % question_id)

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # return HttpResponse("id %s" % question_id)
    return render(request, 'appone/result.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # print(question.choice_set)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return  render(request, 'appone/form.html', {
            'questions' : question,
            'error_message' : "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result', args=(question_id,)))

    # return HttpResponse("You're Voting on Question %s" %question_id)

def sampleRoute(request):
    jsonData = [{"name" : "Fazlur"}, {"name" : "Rahman"}]
    return JsonResponse(jsonData, safe=False)
