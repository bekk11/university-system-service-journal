from django.urls import path

from apps.timetable.api import ListSchedule

urlpatterns = [
    path('list/', ListSchedule.as_view()),
    # path('create/', CreateSubject.as_view()),
    #
    # path('retrieve/<str:pk>/', RetrieveSubject.as_view()),
    # path('update/<str:pk>/', UpdateSubject.as_view()),
    # path('destroy/<str:pk>/', DeleteSubject.as_view()),
]
