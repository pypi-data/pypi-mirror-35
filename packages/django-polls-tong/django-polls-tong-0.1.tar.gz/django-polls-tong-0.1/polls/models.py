import datetime

from django.db import models


# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    # 调用print()和admin里方便知道这是个什么对象
    def __str__(self):
        return self.question_text

    # 对象方法,看是不是超过当前时区时间减去一天
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #  was_published_recently方法在后台的排序和列名
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


"""
Django模型操作:
    查询所有(select):
        Question.objects.all()
    增加对象(insert):
        q = Question(question_text="What's new?", pub_date=timezone.now())
    保存对象(commit):
        q.save()
    删除对象(delete):
        c = q.choice_set.filter(choice_text__startswith='Just hacking')
        c.delete()
    修改属性(update):
        q.question_text="What's up"
        q.save()
    查询集合过滤(where): 
        Question.objects.filter(pk=1)  pk表示主键
    还有许多如__startwith由__开头的过滤条件
        Question.objects.filter(question_text__startswith='What')  以What开头的对象
    调用对象自定义方法:
        q.was_published_recently()  
    一对多关系:如问题的所有选项,注意比flask多了all(),在模板里也需要
        question_choices = q.choice_set.all()
        q.choice_set.count()
"""
