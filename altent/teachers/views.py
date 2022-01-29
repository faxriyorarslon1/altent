from .models import Teacher
from .serializers import TeacherSerializer, RuSerializer, UzSerializer, EngSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.utils.translation import ugettext_lazy as _


class TeacherList(APIView):
    
    """
    List all teachers, or create a new teacher.
    """
    def get(self, request, format=None):
        try:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("Teacher not found.")},
                status=status.HTTP_404_NOT_FOUND
            )


    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetail(APIView):
    """
    Retrieve, update or delete a teacher instance.
    """
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            teacher = self.get_object(pk)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("Teacher not found.")},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk, format=None):
        try:
            teacher = self.get_object(pk)
            serializer = TeacherSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"detail": _("Bad Request.")},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk, format=None):
        try:
            teacher = self.get_object(pk)
            teacher.delete()
            return Response({"Data was deleted."},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {"detail": _("Bad Request.")},
                status=status.HTTP_400_BAD_REQUEST
            )


class TeacherLanguage(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, language):
        try:
            teachers = Teacher.objects.all()
            if language=="uz":
                serializer = UzSerializer(teachers, many=True)
            elif language=="eng":
                serializer = EngSerializer(teachers, many=True)
            else:
                serializer = RuSerializer(teachers, many=True)

            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("Teacher not found.")},
                status=status.HTTP_404_NOT_FOUND
            )