from django.urls import path,include
from .views import CrudView2
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("view",CrudView2)

urlpatterns = [
    path("",include(router.urls))
]
