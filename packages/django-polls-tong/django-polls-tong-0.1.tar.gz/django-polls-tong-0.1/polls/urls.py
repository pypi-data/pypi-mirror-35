from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index_1'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail_1'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results_1'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote_1'),

    # 通用视图的url:
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# 第二个和第三个匹配准则中，路径字符串中匹配模式的名称已经由 <question_id> 改为 <pk>。
# DetailView 期望从 URL 中捕获名为 "pk" 的主键值，
# 所以我们为通用视图把 question_id 改成 pk 。
"""
为了防止其他app有相同的name,
使得模板引用({% url 'name' args%})时冲突,
最好为每个app指定命名空间:
app_name = 'polls'
"""
