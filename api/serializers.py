from rest_framework import serializers
from basic.models import QuizModel, AnswerModel, QuestionModel, UserModel, ScoreModel


class AnswerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = '__all__'


class QuestionModelSerializer(serializers.ModelSerializer):
    answers = AnswerModelSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionModel
        fields = ['id', 'text', 'image', 'answers']


class QuizModelSerializer(serializers.ModelSerializer):
    # questions = QuestionModelSerializer(many=True, read_only=True)

    class Meta:
        model = QuizModel
        fields = ['id', 'name', 'created', 'question']


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class ScoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreModel
        fields = '__all__'
