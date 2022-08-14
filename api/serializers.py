from rest_framework import serializers
from basic.models import QuizModel, AnswerModel, QuestionModel, UserModel


class QuizModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = '__all__'


class AnswerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = '__all__'


class QuestionModelSerializer(serializers.ModelSerializer):
    answers = AnswerModelSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionModel
        fields = ['id', 'text', 'image', 'answers']


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
