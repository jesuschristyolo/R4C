from rest_framework import serializers
from .models import Robot


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['model', 'version', 'created']

    def validate(self, data):
        if not Robot.objects.filter(model=data['model'], version=data['version']).exists():
            raise serializers.ValidationError("Такой модели с этой версией не существует.")
        return data
