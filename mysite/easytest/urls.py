from django.urls import path
from . import views

urlpatterns = [
    path('test_hub/', views.test_hub, name='test_hub'),
    path('result/<str:result_text>', views.result, name='result'),
    path('results/',views.result_render,name="result_render")
]