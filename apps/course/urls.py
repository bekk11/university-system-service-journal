from django.urls import path

from apps.course.api import ListCourse, CreateCourse, RetrieveCourse, UpdateCourse, DeleteCourse

urlpatterns = [
    path('list/', ListCourse.as_view()),
    path('create/', CreateCourse.as_view()),

    path('retrieve/<str:pk>/', RetrieveCourse.as_view()),
    path('update/<str:pk>/', UpdateCourse.as_view()),
    path('destroy/<str:pk>/', DeleteCourse.as_view()),
]
