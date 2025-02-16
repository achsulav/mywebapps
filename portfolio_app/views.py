from django.shortcuts import render, redirect
from .models import Project, Service, Education, Experience, AboutMe, MiniProjects  
from django.contrib import messages

def home(request):

    projects = Project.objects.all()
    services = Service.objects.all() 
    education = Education.objects.all()
    experience = Experience.objects.all()
    about_me = AboutMe.objects.first() 
    mini_projects = MiniProjects.objects.all()

 #context for section
    context = {
        'projects': projects,
        'services': services,
        'education': education,
        'experience': experience,
        'about_me': about_me,
        'mini_projects': mini_projects,
    }

    return render(request, 'index.html', context)

def error(request, exception):
    return render(request, 'error.html')
