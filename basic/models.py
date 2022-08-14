from django.db import models

# Create your models here.

from django.db import models


class QuizModel(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class QuestionModel(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    quiz_id = models.ForeignKey(QuizModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class AnswerModel(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='answers')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class UserModel(models.Model):
    external_id = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.external_id


class ScoreModel(models.Model):
    UserId = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,

    )
    QuizId = models.ForeignKey(
        QuizModel,
        on_delete=models.CASCADE,
    )
    Score = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
