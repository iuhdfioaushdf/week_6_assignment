from django.contrib import admin
from polling.models import Poll, Group, Membership, Person

# store your ModelAdmin classes in here


@admin.action(description='Mark selected polls as published')
def check_completed(modeladmin, request, queryset):
    queryset.update(status='p')


class PollAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "score", "status", "text"]
    ordering = ['title']
    actions = [check_completed]


class MembershipInline(admin.TabularInline):
    model = Group.members.through
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ["invite_reason"]

# Register your models here.

admin.site.register(Poll, PollAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)


