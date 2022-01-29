from .models import Pupil
from .serializers import PupilSerializer, RuSerializer, UzSerializer, EngSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.utils.translation import ugettext_lazy as _


class PupilList(APIView):
    
    """
    List all pupils, or create a new pupil.
    """
    def get(self, request, format=None):
        try:
            pupils = Pupil.objects.all()
            serializer = PupilSerializer(pupils, many=True)
            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("Pupil not found.")},
                status=status.HTTP_404_NOT_FOUND
            )


    def post(self, request, format=None):
        serializer = PupilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PupilDetail(APIView):
    """
    Retrieve, update or delete a pupil instance.
    """
    def get_object(self, pk):
        try:
            return Pupil.objects.get(pk=pk)
        except Pupil.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            pupil = self.get_object(pk)
            serializer = PupilSerializer(pupil)
            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("pupil not found.")},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk, format=None):
        try:
            pupil = self.get_object(pk)
            serializer = PupilSerializer(pupil, data=request.data)
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
            pupil = self.get_object(pk)
            pupil.delete()
            return Response({"Data was deleted."},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {"detail": _("Bad Request.")},
                status=status.HTTP_400_BAD_REQUEST
            )


class PupilLanguage(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, language):
        try:
            pupils = Pupil.objects.all()
            if language=="uz":
                serializer = UzSerializer(pupils, many=True)
            elif language=="eng":
                serializer = EngSerializer(pupils, many=True)
            else:
                serializer = RuSerializer(pupils, many=True)

            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("Pupil not found.")},
                status=status.HTTP_404_NOT_FOUND
            )