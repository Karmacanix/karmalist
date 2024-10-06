from django.contrib import admin
from tasks.models import Task, TaskList

# Register your models here.
# class TaskAdmin(admin.ModelAdmin):
#     list_display  = ["title", "task_status", "due_date", "assigned", "task_list"]
#     list_filter = ["title", "task_status", "due_date", "assigned"]
class TaskInline(admin.TabularInline):
    model = Task

# class TaskListAdmin(admin.ModelAdmin):
#     fields = ["title", "owner"]
#     list_display  = ["title", "owner"]
class TaskListAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]

admin.site.register(TaskList, TaskListAdmin)
#admin.site.register(Task, TaskInline)
