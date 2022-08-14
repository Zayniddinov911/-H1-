from rest_framework.response import Response
from rest_framework.decorators import api_view
from basic.models import QuizModel, AnswerModel, QuestionModel, UserModel
from .serializers import QuizModelSerializer, AnswerModelSerializer, QuestionModelSerializer, UserModelSerializer


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


@api_view(['GET'])
def getTrueAnswers(request):
    t_answers = AnswerModel.objects.all()
    serializer = AnswerModelSerializer(t_answers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getQuestions(request):
    questions = QuestionModel.objects.all()
    serializer = QuestionModelSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request):
    users = UserModel.objects.all()
    serializer = UserModelSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = UserModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
