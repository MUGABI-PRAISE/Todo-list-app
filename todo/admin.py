from django.contrib import admin
from.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'completed', 'created_at', 'updated_at', 'user')
    #list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('description',)
    ordering = ('-created_at',)

admin.site.register(Task, TaskAdmin)
# Register your models here.
