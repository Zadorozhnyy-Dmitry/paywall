from django.urls import path

from codes.apps import CodesConfig
from codes.views import verify_view

app_name = CodesConfig.name

urlpatterns = [
    path('verify', verify_view, name='verify'),  # маршрутизация к верификации

]
