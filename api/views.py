from rest_framework.response import Response
from rest_framework.decorators import api_view
from basic.models import QuizModel
from .serializers import QuizModelSerializer


@api_view(['GET'])
def getData(request):
    quizs = QuizModel.objects.all()
    serializer = QuizModelSerializer(quizs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addQuiz(request):
    serializer = QuizModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
