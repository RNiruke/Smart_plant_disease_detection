from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('history/', views.history_list, name='history'),
    path('delete/<int:pk>/', views.delete_detection, name='delete'),
    path('download/', views.download_report, name='download'),
]
