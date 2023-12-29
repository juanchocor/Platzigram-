from django.contrib import admin

from users.models import Profile

# Register your models here.

@admin.register(Profile)
class Profileadmin(admin.ModelAdmin):

    list_display=('pk','user','phone_number','website','picture')
    list_display_links=('pk','user')
    list_editable=('phone_number','website','picture')

    search_fields=('user__name','user__email',
                   'user__first_name',
                   'user__last_name',
                   'phone_number'
    )
    
    list_filter=('create','modified',
                 'user__is_active',
                 'user__is_staff'
    )


    fieldsets = (
        ('Profile', {
            'fields':(('user','picture'),),
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('bigoraphy')
            )
        })
    )





