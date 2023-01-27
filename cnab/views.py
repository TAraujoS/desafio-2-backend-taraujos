from rest_framework.views import APIView, Response, status
from cnab.serializers import DocumentationSerializer, FileSerializer
from django.db.models import Sum
from .models import Documentation
from .functions import updload_file
import ipdb


class DocumentationViews(APIView):
    serializer_class = FileSerializer

    def post(self, request):
        file = updload_file(request.FILES["file"])
        serializer = DocumentationSerializer(data=file, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        transactions = Documentation.objects.values(
            "store_name", "store_owner"
        ).annotate(total_balance=Sum("value"))

        return Response({"store_balance": transactions})
