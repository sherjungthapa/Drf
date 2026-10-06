from django.urls import path,include
from .views import CrudView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("view",CrudView)

urlpatterns = [
    path("",include(router.urls))
]
