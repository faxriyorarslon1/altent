from .models import Yordam
from .serializers import YordamSerializer, RuSerializer, UzSerializer, EngSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.utils.translation import ugettext_lazy as _


class YordamList(APIView):
    
    """
    List all yordams, or create a new yordam.
    """
    def get(self, request, format=None):
        try:
            yordams = Yordam.objects.all()
            serializer = YordamSerializer(yordams, many=True)
            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("Help not found.")},
                status=status.HTTP_404_NOT_FOUND
            )


    def post(self, request, format=None):
        serializer = YordamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class YordamDetail(APIView):
    """
    Retrieve, update or delete a yordam instance.
    """
    def get_object(self, pk):
        try:
            return Yordam.objects.get(pk=pk)
        except Yordam.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            yordam = self.get_object(pk)
            serializer = YordamSerializer(yordam)
            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("Help not found.")},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk, format=None):
        try:
            yordam = self.get_object(pk)
            serializer = YordamSerializer(yordam, data=request.data)
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
            yordam = self.get_object(pk)
            yordam.delete()
            return Response({"Data was deleted."},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {"detail": _("Bad Request.")},
                status=status.HTTP_400_BAD_REQUEST
            )


class YordamLanguage(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, language):
        try:
            yordams = Yordam.objects.all()
            if language=="uz":
                serializer = UzSerializer(yordams, many=True)
            elif language=="eng":
                serializer = EngSerializer(yordams, many=True)
            else:
                serializer = RuSerializer(yordams, many=True)

            return Response(serializer.data)
        except:
            return Response(
                {"detail": _("Help not found.")},
                status=status.HTTP_404_NOT_FOUND
            )