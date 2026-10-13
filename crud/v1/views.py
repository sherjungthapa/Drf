from rest_framework import viewsets
from ..models import Employee
from .serializer import EmployeeSerializer1
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import authentication
from ..custom_permission import CustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..custom_pagination import CustomPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle,ScopedRateThrottle

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from django_filters.rest_framework import DjangoFilterBackend
from ..custom_filter import CustomFilter
from rest_framework.filters import SearchFilter,OrderingFilter

class CrudView1(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer1
    # filter_backends=[DjangoFilterBackend]
    # filter_backends=[SearchFilter]
    filter_backends=[OrderingFilter,DjangoFilterBackend,SearchFilter]
    filterset_fields={
        'name':['icontains','regex'],
        'age':['exact','gte']
    }
    search_fields=['$name','age']
    Ordering_fields=['name','age']
    ordering=['name','age']
    # filterset_class=CustomFilter
    # permission_classes=[permissions.IsAuthenticated]
    # permission_classes=[permissions.IsAdminUser]
    # permission_classes=[permissions.IsAdminUser]
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    # permission_classes=[permissions.DjangoModelPermissions]
    # permission_classes=[CustomPermission]
    permission_classes=[permissions.AllowAny]
    # permission_classes=[permissions.IsAuthenticated]
    # authentication_classes=[JWTAuthentication]

    pagination_class=LimitOffsetPagination
    authentication_classes=[authentication.SessionAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    throtle_scope="ram"
    throttle_classes=[ScopedRateThrottle]



    # authentication_classes=[authentication.BasicAuthentication]
    # authentication_classes=[authentication.TokenAuthentication]
    authentication_classes=[JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid()
        self.perform_create(serializer=serializer)
        return Response(
            {'message':"successfully submitted",
            'data':serializer.data
            }
        )

    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        instance.is_deleted=True
        instance.save()
        return Response(
            {
                'message':"your data is deleted"
            }
        )

    @method_decorator(cache_page(600))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        print("database hit")
        return super().list(request, *args, **kwargs)

    # def get_queryset(self):
    #     import time
    #     time.sleep(3)
    #     return super().get_queryset()


    def get_queryset(self):
        queryset=super().get_queryset()
        age=self.request.query_params.get('age')
        if age:
            queryset=queryset.filter(age=age)
        return queryset