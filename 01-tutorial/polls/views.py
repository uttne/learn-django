from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # get_object_or_404 は便利関数
    # 内部でオブジェクトが存在しないとき(raise Question.DoesNotExist) Http404 を発生させる
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except:
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        # F() は競合回避のために直接フィールドとして値を参照しないようにするために用いる
        # 結局使うとどうなるかというと SQL の中で計算するように変換がされる
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        # reverse() を使用すると URL をハードコードせずにすむ
        # html に記述するのと同じように urls の名前と位置引数を与える
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
