from django.contrib import admin
from .models import Award, AwardCategory, Education
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