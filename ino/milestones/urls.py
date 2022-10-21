from django.urls import path
from . import views
  

urlpatterns = [
    path('team/create/', views.TeamAPIView.as_view()),
    path('milestones/create', views.MilestoneCreateAPIView.as_view()),
    path('milestones/<int:id>', views.MilestoneAPIView.as_view()),
    path('milestones/', views.MilestoneListAPIView.as_view()),
]