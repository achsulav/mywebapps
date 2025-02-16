from django.contrib import admin
from .models import Project, Service, Education, Experience, AboutMe, MiniProjects
#regestering models that i can add in admin django interface
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'Source_link', 'Live_Link', 'image')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(Service)  
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')  
    search_fields = ('name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Starting_Date', 'Ending_Date')
    search_fields = ('Name',)
    list_filter = ('Starting_Date', 'Ending_Date')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('post', 'company_name', 'from_date', 'to_date')
    search_fields = ('post', 'company_name')
    list_filter = ('from_date', 'to_date')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(MiniProjects)
class MiniProjectsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


