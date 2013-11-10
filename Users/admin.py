from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from Users.models import JadeBusemUser
from Users.forms import JadeBusemUserChangeForm, JadeBusemUserCreationForm

class JadeBusemUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    

    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'message', 'points', 'is_rules_accepted', 'link')}),
        (_('Permissions'), {'fields': ('is_recruter', 'is_tactic','is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')}
        ),
    )
    form = JadeBusemUserChangeForm
    add_form = JadeBusemUserCreationForm
    list_display = ('user_id', 'email', 'name', 'message', 'link', 'points', 'is_active', 'is_recruter', 'is_tactic')
    search_fields = ('email', 'name', 'is_rules_accepted')
    ordering = ('email',)

admin.site.register(JadeBusemUser, JadeBusemUserAdmin)