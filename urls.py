from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('todo_lists')),  # редирект с главной страницы
    path('', include('todos.urls')),  # подключаем маршруты приложения todos
]
