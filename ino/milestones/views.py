from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Milestone
from .serializers import MilestoneSerializer, TeamSerializer, TeamMemberSerializer

# Create your views here.
class TeamAPIView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        #user_id = request.user.id        
        serializer = TeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MilestoneCreateAPIView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        #user_id = request.user.id        
        serializer = MilestoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MilestoneAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MilestoneSerializer
    queryset = Milestone.objects.all()
    permission_classes = (permissions.AllowAny,)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(id=id)

    def qet_queryset(self):
        return self.queryset.filter(id=id)

class MilestoneListAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        milestones = Milestone.objects.order_by('due_date')
        serializer = MilestoneSerializer(milestones, many=True)
        return Response(serializer.data)