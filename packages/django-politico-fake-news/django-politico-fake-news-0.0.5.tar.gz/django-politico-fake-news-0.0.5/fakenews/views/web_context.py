from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from fakenews.models import DisinformationType
from fakenews.serializers import DisinformationTypeContextSerializer
from fakenews.authentication import TokenAPIAuthentication


class WebContext(APIView):
    """
    View to handle data from custom Fact Check admin.
    """
    authentication_classes = (TokenAPIAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Returns the context data for the website.
        """
        types = DisinformationTypeContextSerializer(
            DisinformationType.objects.all(),
            many=True
        )
        return Response({"types": types.data})
