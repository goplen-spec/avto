from django.urls import path

from . import views

urlpatterns = [
    path('avito/', views.Login.as_view(), name='login'),
]
