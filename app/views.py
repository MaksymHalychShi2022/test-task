from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, filters, status
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

from .models import Restaurant, Menu, Vote, CustomUser
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer, CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['day']

    def get_queryset(self):
        queryset = super().get_queryset()
        day = self.request.query_params.get('day', None)
        if day is not None:
            queryset = queryset.filter(day=day)
        return queryset

    @swagger_auto_schema(request_body=VoteSerializer)  # Specify request body schema
    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        menu = self.get_object()
        user = request.user
        vote = request.data.get('vote', None)

        if vote is None or not isinstance(vote, bool):
            return Response({'detail': 'Please provide a boolean value for vote (true/false).'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the user has already liked or disliked the menu
        existing_like = Vote.objects.filter(employee=user, menu=menu).first()

        if existing_like:
            # Update existing like or dislike
            existing_like.vote = vote
            existing_like.save()
            return Response({'detail': 'Menu like/dislike updated successfully.'}, status=status.HTTP_200_OK)
        else:
            # Create a new like or dislike for the menu
            Vote.objects.create(employee=user, menu=menu, vote=vote)
            return Response({'detail': 'Menu like/dislike added successfully.'}, status=status.HTTP_201_CREATED)


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)
