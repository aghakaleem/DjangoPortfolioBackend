from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Project, Technology, Skill, Certificate, Experience, Education
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProjectListSerializer, TechnologySerializer, SkillSerializer, ProjectDetailSerializer, CertificateSerializer, ExperienceSerializer, EducationSerializer
# Create your views here.

@api_view(['GET'])
def projects_featured(request):
    projects = Project.objects.filter(featured=True)
    serializer = ProjectListSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projects_list(request):
    projects = Project.objects.all()
    serializer = ProjectListSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def project_detail(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=404)
    serializer = ProjectDetailSerializer(project)
    return Response(serializer.data)



@api_view(['GET'])
def technologies_list(request):
    technologies = Technology.objects.all()
    serializer = TechnologySerializer(technologies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def skills_list(request):
    skills = Skill.objects.filter(featured=True)
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)

class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.filter(featured=True)
    serializer_class = CertificateSerializer

class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer