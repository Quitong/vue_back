from django.contrib import admin
from blog.models import Post, Comment, Quiz, Question, Answer

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)


class QuestionInline(admin.TabularInline):
    model = Question
class QuizAdmin(admin.ModelAdmin):
    inlines=(QuestionInline,)

admin.site.register(Quiz, QuizAdmin)




admin.site.register(Question)
admin.site.register(Answer)