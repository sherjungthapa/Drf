from django.urls import path,include
from .views import CrudView1
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("view",CrudView1)

urlpatterns = [
    path("",include(router.urls))
]
