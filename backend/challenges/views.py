from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Challenge
from .serializers import ChallengeSerializer

@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # This is for permissions
def get_challenges(request):
    challenges = Challenge.objects.all()
    serializer = ChallengeSerializer(challenges, many=True)
    return Response(serializer.data)
