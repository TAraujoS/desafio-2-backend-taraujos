from django.shortcuts import render
from rest_framework.views import APIView, Response, status, Request
from cnab.serializers import DocumentationSerializer, FileSerializer
from .models import Documentation


class DocumentationViews1(APIView):
    serializer_class = FileSerializer

    def get(self, request):
        transactions = Documentation.objects.all()

        serializer = DocumentationSerializer(transactions, many=True)

        return Response(serializer.data)

    def post(self, request):
        transactions = []

        file = request.FILES.get("file")

        for data in file:
            obj = {
                "type": data[:1].decode("utf-8"),
                "date": f"{data[1:5].decode('utf-8')}-{data[6:7].decode('utf-8')}-{data[8:9].decode('utf-8')}",
                "value": int(data[9:19].decode("utf-8")) / 100,
                "cpf": data[19:30].decode("utf-8"),
                "card": data[30:42].decode("utf-8"),
                "hour": f"{data[42:44].decode('utf-8')}:{data[45:47].decode('utf-8')}:{data[47:48].decode('utf-8')}",
                "store_owner": data[48:62].decode("utf-8"),
                "store_name": data[62:].decode("utf-8"),
            }

            serializer = DocumentationSerializer(data=obj)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            transactions.append(serializer.data)

            return Response(transactions, status.HTTP_201_CREATED)
