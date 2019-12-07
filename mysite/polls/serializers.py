import datetime

from .models import Question

from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')

    def validate_pub_date(self, pub_date):
        if pub_date.date() < datetime.datetime.now().date():
            raise ValidationError("pub_date has to be greater than today")
        return pub_date
