from django.urls import path
from . import views

app_name = 'Api'

urlpatterns = [
    path('projects_featured', views.projects_featured, name='projects_featured'),
    path('projects_list', views.projects_list, name='projects_list'),
    path('project_detail/<slug:slug>', views.project_detail, name='project_detail'),
    path('technologies_list', views.technologies_list, name='technologies_list'),
    path('skills_list', views.skills_list, name='skills_list'),
    path('certificates', views.CertificateListView.as_view(), name='certificates'),
    path('experiences', views.ExperienceListView.as_view(), name='experiences'),
    path('educations', views.EducationListView.as_view(), name='educations'),
]
 