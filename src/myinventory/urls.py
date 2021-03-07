from django.urls import path

from .views import ItemDetailView, ShowHelloWorld


urlpatterns = [
    path(r'', ShowHelloWorld.as_view()),
    path(r'<uuid:pk>/', ItemDetailView.as_view(), name='detail'),
]