from django.urls import path

from . import views

# 名前空間を設定することで {% url %} で解決するviewのnameの競合を回避することができる
app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    # view の html に直接 URL を記述せず url 構文を使うことで urls のパスを変えてもそれに追従してくれる
    path("specifics/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
