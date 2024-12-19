from django.urls import path
from . import views

app_name = 'robots'

urlpatterns = [
    path('report/', views.download_report_page, name='report'),
    path('add_robot/', views.add_robot, name='add_robot'),
    path('download_report/', views.generate_report, name='download_report'),
]
