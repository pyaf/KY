from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin


from KYusers.models import KYProfile, CAProfile,College

class KYprofileInline(admin.StackedInline):
    model = KYProfile
    can_delete = False

class UserAdmin(UserAdmin):

    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)


    def college(obj):
        return obj.kyprofile.college


    def mobile_number(obj):
        return obj.kyprofile.mobile_number


    name.short_description = 'Name'
    college.short_description = 'College'
    mobile_number.short_description = 'Mobile No.'


    list_display = ('email',name, college, mobile_number)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User,UserAdmin)
admin.site.register(CAProfile)
admin.site.register(KYProfile)
admin.site.register(College)
