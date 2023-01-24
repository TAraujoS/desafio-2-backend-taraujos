from django.shortcuts import render
from rest_framework.views import APIView, Response, status, Request
from cnab.serializers import DocumentationSerializer, FileSerializer
from .models import Documentation
from .functions import updload_file


class DocumentationViews(APIView):
    serializer_class = FileSerializer

    def post(self, request):
        file = updload_file(request.FILES["file"])
        serializer = DocumentationSerializer(data=file, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        transctions = Documentation.objects.all()

        serializer = DocumentationSerializer(transctions, many=True)

        return Response(serializer.data)
