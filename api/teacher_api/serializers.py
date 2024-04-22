from teacher_api.models import Teacher
from rest_framework import serializers
class Teacherserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"