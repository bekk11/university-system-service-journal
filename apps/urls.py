from django.urls import path, include

urlpatterns = [
    path('subject/', include('apps.subject.urls')),
    path('course/', include('apps.course.urls')),

    path('schedule/', include('apps.timetable.urls')),
]
