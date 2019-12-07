from .models import Question

from rest_framework.serializers import ModelSerializer


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')
