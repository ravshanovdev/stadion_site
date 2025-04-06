from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import StadionSerializer, StadionListSerializer, OrderStadionSerializer
from .models import Stadion, OrderStadion


# POST

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_stadion(request):
    serializer = StadionSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_stadions(request):

    stadions = Stadion.objects.filter(is_approve=True)

    if not stadions:
        return Response({"error": "Stadion Not Found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StadionListSerializer(stadions, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_stadion(request, pk):
    try:

        stadion = Stadion.objects.get(pk=pk)

        if not stadion.is_approve:
            return Response({"message": "bu stadion hali tasdiqlanmagan"})

        serializer = StadionListSerializer(stadion)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Stadion.DoesNotExist:
        return Response({"error": "Stadion Not Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_stadion(request, pk):
    stadion = Stadion.objects.get(pk=pk, owner=request.user)

    if request.data.get('is_approve') and not request.user.is_superuser:
        return Response({"error": "only admin can change this field"})

    serializer = StadionSerializer(stadion, data=request.data, partial=True)

    if serializer.is_valid(raise_exception=True):
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_stadion(request, pk):
    stadion = Stadion.objects.get(pk=pk, owner=request.user)

    if not stadion:
        return Response({"error": "Stadion Not Found"}, status=status.HTTP_404_NOT_FOUND)

    stadion.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


# ORDER_STADION

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_order(request):
    order = OrderStadion.objects.all()

    serializer = OrderStadionSerializer(order, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
