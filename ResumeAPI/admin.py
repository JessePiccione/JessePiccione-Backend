from django.contrib import admin
from .models import Award, AwardCategory, Education, Message, Project, HomePageEntry, Technology, SkillCategory, Skill, WorkExperience
# Register your models here.
class AwardCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'issuer')
    search_fields = ('id', 'title', 'year', 'issuer')
    list_filter = ('title', 'year', 'issuer')
admin.site.register(AwardCategory, AwardCategoryAdmin)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'year', 'category')
    search_fields = ('id','title', 'year', 'category')
    list_filter = ('title', 'year', 'category')
admin.site.register(Award, AwardAdmin)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_name', 'location', 'degree_type', 'start_date', 'end_date')
    search_fields = ('id', 'school_name', 'location', 'degree_type', 'start_date', 'end_date')
    list_filter = ('school_name', 'location', 'degree_type', 'start_date', 'end_date')
admin.site.register(Education, EducationAdmin)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'phone', 'subject')
    search_fields = ('id', 'email', 'name', 'phone', 'subject', 'message')
    list_filter = ('email', 'name', 'phone', 'subject', 'message')
admin.site.register(Message, MessageAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sponser', 'start_date', 'end_date')
    search_fields = ('id', 'name', 'sponser', 'start_date', 'end_date', 'contribution')
    list_filter = ('name', 'sponser', 'start_date', 'end_date', 'contribution')
admin.site.register(Project, ProjectAdmin)

class HomePageEntryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'URL')
    search_fields = ('id', 'title', 'description', 'URL')
    list_filter = ('title', 'description', 'URL')
admin.site.register(HomePageEntry, HomePageEntryAdmin)

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'pageEntry')
    search_fields = ('id','title', 'description', 'pageEntry')
    list_filter = ('title', 'description', 'pageEntry')
admin.site.register(Technology, TechnologyAdmin)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('id', 'category_name')
    list_filter = ('category_name',)
admin.site.register(SkillCategory, SkillCategoryAdmin)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('id', 'name', 'category')
    list_filter = ('name', 'category')
admin.site.register(Skill, SkillAdmin)

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'location', 'title_held', 'start_date', 'end_date')
    search_fields = ('id','company_name', 'location', 'title_held', 'start_date', 'end_date', 'description')
    list_filter = ('company_name', 'location', 'title_held', 'start_date', 'end_date', 'description')
admin.site.register(WorkExperience, WorkExperienceAdmin)