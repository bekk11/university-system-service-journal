from django.urls import path

from apps.absent.api.list_absents import ListAbsents

urlpatterns = [
    path('list/', ListAbsents.as_view())
]
