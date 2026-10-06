from django.urls import path,include

from .views import IndexView
urlpatterns =[
    path("test",IndexView.as_view()),
    path("test/<int:id>",IndexView.as_view()),
]