from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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


class MilestoneAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, id):
        #user_id = request.user.id
        profile_obj = get_object_or_404(Milestone, id=id)
        serializer = MilestoneSerializer(instance=profile_obj)
        return Response(serializer.data)

    # def put(self, request):
    #     user_id = request.user.id
    #     profile_obj = get_object_or_404(Milestone, team=user_id)
    #     serializer = MilestoneSerializer(instance=profile_obj, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(team=self.request.user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request):
    #     user_id = request.user.id
    #     profile_obj = get_object_or_404(Milestone, team=user_id)
    #     profile_obj.delete()
    #     return Response({'message':'Eliminated'}, status=status.HTTP_204_NO_CONTENT)


class MilestoneListAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        milestones = Milestone.objects.all()
        serializer = MilestoneSerializer(milestones, many=True)
        return Response(serializer.data)