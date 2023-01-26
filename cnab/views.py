from rest_framework.views import APIView, Response, status
from cnab.serializers import DocumentationSerializer, FileSerializer
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
        transactions = Documentation.objects.all()
        serializer = DocumentationSerializer(transactions, many=True)

        total = 0

        for char in transactions:
            if char.type in "239":
                total -= char.value
            else:
                total += char.value

        return Response({"data": serializer.data, "total_balance": total})
