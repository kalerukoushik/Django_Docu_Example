from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question, Choice

# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question doesn't exists!")

	question = get_object_or_404(Question, pk=question_id)
	context = {
		'question': question,
	}
	return render(request, 'polls/detail.html', context)


def results(request, question_id):
	return HttpResponse('Result of %s' %question_id)

def vote(request, question_id):
	return HttpResponse('Voting for %s' %question_id)