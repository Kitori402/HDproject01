from django.contrib import admin
from . import models


# Register your models here.

admin.site.register(models.Group)

#since the group member model maybe configured within the group model the groupMember model can be set in line with group model
#this allows the editing of both the groupMember and grp model in db 

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember