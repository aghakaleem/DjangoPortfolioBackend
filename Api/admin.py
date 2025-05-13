from django.contrib import admin
from .models import Technology, Project, Skill, Experience, Education, Certificate
# Register your models here.



admin.site.register([Technology, Project, Skill, Experience, Education, Certificate])