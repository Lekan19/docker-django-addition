from django.urls import path
from .views import AdditionView

urlpatterns = [
    path('api/addition/', AdditionView.as_view(), name='addition'),
]
