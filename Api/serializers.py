from rest_framework import serializers
from .models import Technology, Project, Skill, Experience, Education, Certificate
from django.contrib.auth import get_user_model


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model: Technology
        fields = ['id' ,'name', 'slug', 'image', 'description']


class ProjectListSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    class Meta:
        model: Project
        fields = ['id', 'title', 'image', 'slug', 'technologies']

class ProjectDetailSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    class Meta:
        model: Project
        fields = ['id', 'title', 'description', 'image', 'slug', 'technologies', 'github_link', 'live_link']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model: Skill
        fields = ['id', 'name', 'slug', 'description']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model: Experience
        fields = ['id', 'title', 'description', 'company_name', 'work_location' 'start_date', 'end_date']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model: Education
        fields = ['id', 'title', 'institution_name', 'start_date', 'end_date', 'cgpa', 'grade']

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model: Certificate
        fields = ['id', 'title', 'description', 'slug', 'image', 'issued_link', 'issued_by', "issued_month_year"]

