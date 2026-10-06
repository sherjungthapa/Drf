from rest_framework import viewsets
from .models import Employee
from .serializer import EmployeeSerializer

class CrudView(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer