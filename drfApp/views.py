from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from .golobal_msg import Message

'''
'''

class IndexView(APIView):
    def get(self,request):
        abc=Student.objects.all()
        serializer=StudentSerializer(abc,many=True)
        return Response({"message":serializer.data}, status=status.HTTP_200_OK)

    def post(self,request):
        try:
            serailizer=StudentSerializer(data=request.data)
            if serailizer.is_valid():
                serailizer.save()
                return Response({Message:"submitted data...."},
                status=status.HTTP_200_OK)
            else:
                return Response({Message:serailizer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({Message:f"error:{e} "},status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request,id):
        instance=Student.objects.get(id=id)

        serializer=StudentSerializer(instance=instance,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({Message:"Successfully updated!!!"})
        else:
            return Response({Message:serializer.errors},status= status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        instance=Student.objects.get(id=id)

        serializer=StudentSerializer(instance=instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({Message:"Update Successfully!!!"})
        else:
            return Response({Message:serializer.errors},status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            student = Student.objects.get(
                id=id,
                is_deleted=False)
            student.is_deleted = True
            student.save()
            return Response(
                {"Message": "Student deleted successfully"},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"Message": "Student not found"},status=status.HTTP_404_NOT_FOUND)