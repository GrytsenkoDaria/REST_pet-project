from django.contrib import admin
from user.models import User
from project.models import ProjectUser
from tasks.models import Task


class ProjectInline(admin.TabularInline):
    model = ProjectUser
    extra = 1


class InitiatorTaskInline(admin.TabularInline):
    model = Task
    extra = 1
    fk_name = 'assignee'


class UserAdmin(admin.ModelAdmin):
    inlines = (
        ProjectInline,
        InitiatorTaskInline,
    )


admin.site.register(User, UserAdmin)
