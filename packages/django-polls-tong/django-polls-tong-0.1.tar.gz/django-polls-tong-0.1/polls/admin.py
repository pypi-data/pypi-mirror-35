# coding=utf-8
from django.contrib import admin
from .models import Question, Choice


# Register your models here.
# 注册模型到管理系统

# admin.site.register(Question)
# admin.site.register(Choice)

# 需要注册一个超级用户: python manage.py createsuperuser

#
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
# admin.site.register(Question, QuestionAdmin)

# 你需要遵循以下流程——创建一个模型后台类，接着将其作为第二个参数传给
# admin.site.register() ——在你需要修改模型的后台管理选项时这么做。
# 以上修改使得 "Publication date" 字段显示在 "Question" 字段之前

# class ChoiceInline(admin.StackedInline):
# TabularInline单行显示关联对象更紧凑
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # 默认情况下，Django显示每个对象的str()返回的值。
    # 但有时如果我们能够显示单个字段，它会更有帮助。
    # 为此，使用list_display后台选项，它是一个包含要显示的字段名的元组
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加了一个“过滤器”侧边栏，允许人们以pub_date字段来过滤列表：
    list_filter = ['pub_date']
    # 在列表的顶部增加一个搜索框。当输入待搜项时，Django将搜索question_text字段。
    # 你可以使用任意多的字段——由于后台使用LIKE来查询数据，
    # 将待搜索的字段数限制为一个不会出问题大小，会便于数据库进行查询操作。
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# fieldsets 元组中的第一个元素是字段集的标题
