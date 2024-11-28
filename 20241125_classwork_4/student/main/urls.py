from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('students/<int:student_id>/', student_grades, name='studentgrades'),
]
