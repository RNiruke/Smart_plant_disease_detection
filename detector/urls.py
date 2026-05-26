from django.urls import path
from . import views

app_name = 'detector'

urlpatterns = [
    path('upload/', views.upload_view, name='upload'),
    path('result/<int:pk>/', views.result_view, name='result'),
    path('history/', views.history_view, name='history'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
    path('download/', views.download_view, name='download'),
]
