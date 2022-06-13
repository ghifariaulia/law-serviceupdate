from django.urls import path

from main.views import UserUpdate

app_name = 'main'

urlpatterns = [
    path('update/', UserUpdate.as_view())
]
