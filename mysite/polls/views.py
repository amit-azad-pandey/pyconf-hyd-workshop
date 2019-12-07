from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import QuestionSerializer
from .models import Question


class QuestionsApiView(APIView):

    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = Question.objects.create(**serializer.validated_data)
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
