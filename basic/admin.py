from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(QuizModel)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created']
    list_display_links = ['name']


@admin.register(QuestionModel)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created']
    list_display_links = ['text']


@admin.register(AnswerModel)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'external_id', 'created']
    list_display_links = ['external_id']


@admin.register(ScoreModel)
class ScoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'UserId', 'QuizId', 'Score', 'created']
    list_display_links = ['UserId', 'QuizId', 'Score']
