from django.urls import path

from . import views
#테스트 한것 돌림.

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
