from django.contrib import admin
from .models import Award, AwardCategory
# Register your models here.

class AwardAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'year', 'category')
    search_fields = ('id','title', 'year', 'category')
    list_filter = ('title', 'year', 'category')
admin.site.register(Award, AwardAdmin)