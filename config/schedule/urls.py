from django.urls import path
from .views import CreateClassTime, UpdateClassTime, ClassTimeList

urlpatterns = [
    path('add-class',CreateClassTime.as_view(), name='CreateClassTime'),
    path('edit-class/<int:pk>', UpdateClassTime.as_view(), name='UpdateClassTime'),
    path('class-list', ClassTimeList.as_view(), name='ClassTimeList')
]
