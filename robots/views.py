from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RobotSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render
from .reports.reports_generator import generate_week_report
from .services import RobotService


def download_report_page(request):
    return render(request, 'download_report.html')


def generate_report(request):
    return generate_week_report()


@swagger_auto_schema(
    method='post',
    request_body=RobotSerializer,
    operation_description="Создание записи о роботе",
    responses={201: RobotSerializer, 400: 'Bad Request'}
)
@api_view(['POST'])
def add_robot(request):
    if request.method == 'POST':
        serializer = RobotSerializer(data=request.data)
        if serializer.is_valid():
            model = serializer.validated_data['model']
            version = serializer.validated_data['version']
            created = serializer.validated_data['created']

            try:
                robot = RobotService.create_robot(model, version, created)
                robot_data = RobotSerializer(robot).data
                return Response(robot_data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
