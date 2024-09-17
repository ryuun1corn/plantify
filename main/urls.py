from django.urls import path
from main.views import redirect_home, show_main

app_name = 'main'

urlpatterns = [
    path('home/', show_main, name='show_main'),
    path('', redirect_home, name='redirect_home')
]
