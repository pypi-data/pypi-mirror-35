from django.shortcuts import get_object_or_404, render
# render 的本质是HttpResponse(template.render(context, request))
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    # 当模型对象查询结果为空时会发出Question.DoesNotExist异常,可以设置返回Http404
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    # 或者使用更便捷的 get_object_or_404 ,拿到对象或返回404
    # 在Class.objexts.filter()时则使用  get_list_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# 使用通用视图
class IndexView(generic.ListView):
    # 替换默认的<app name>/<model name>_list.html
    template_name = 'polls/index.html'
    # 对于 ListView， 自动生成的 context 变量是 question_list。为了覆盖这个行为，
    # 我们提供 context_object_name 属性，表示我们想使用 latest_question_list。
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        """Return the last five published questions.
        """
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

