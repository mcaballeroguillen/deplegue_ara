from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import user
from .forms import SignUpForm


class UserAdmin(UserAdmin):
    model = user
    #form= SignUpForm
    list_display = [
        'id','email', 'is_staff', 'is_active', 'date_joined', 'last_updated'

    ]


    fieldset =(
        (None,{'fields':('email', 'password','username','puesto','unidad')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser', 'groups','user_permissions')}),
        ('Personal info',{'fields':('first_name','last_name','email','puesto','unidad')}),
        ('Important dates',{'fields':('last_login','date_joined')}),
    )

    list_filter = ['email', 'puesto']
    search_fields = ['email']
    ordering = ('email',)
    readonly_fields = ('date_joined',)
    #exclude = ('date_joined',)
admin.site.register(get_user_model(),UserAdmin)
UserAdmin.list_filter+=('puesto','unidad')
#UserAdmin.fieldset+=('puesto','unidad')
UserAdmin.list_display+=('puesto','unidad')
UserAdmin.list_editable+=('puesto','unidad','email')

