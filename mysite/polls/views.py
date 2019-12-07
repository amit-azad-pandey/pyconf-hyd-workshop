from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import QuestionSerializer
from .models import Question


class QuestionsApiView(APIView):

    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
