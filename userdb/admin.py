from django.contrib import admin
from userdb.models import User,Project

class UsersInline(admin.TabularInline):
    model = User
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [UsersInline]

admin.site.register(User)
admin.site.register(Project,ProjectAdmin)

# Register your models here.
