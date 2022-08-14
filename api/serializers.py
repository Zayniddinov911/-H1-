from rest_framework import serializers
from basic.models import QuizModel


class QuizModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = '__all__'
