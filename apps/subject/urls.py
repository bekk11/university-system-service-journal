from django.urls import path

from apps.subject.api import RetrieveSubject, ListSubject, CreateSubject, UpdateSubject, DeleteSubject

urlpatterns = [
    path('list/', ListSubject.as_view()),
    path('create/', CreateSubject.as_view()),

    path('retrieve/<str:pk>/', RetrieveSubject.as_view()),
    path('update/<str:pk>/', UpdateSubject.as_view()),
    path('destroy/<str:pk>/', DeleteSubject.as_view()),
]
