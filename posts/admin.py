from django.contrib import admin
from posts.models import Posts

# Register your models here.

@admin.register(Posts)
class Postsadmin(admin.ModelAdmin):

    list_display=('pk','user','profile','photo','title')
    list_display_links=('pk','user')
    list_editable=('title','photo')

    search_fields=('user__name','user__profile',
                   'user__first_name'
    )
    
    list_filter=('created','modified',
                 'user__is_active',
                 'user__is_staff'
    )


    fieldsets = (
        ('Posts', {
            'fields':('user','photo'),
            'description': 'Primer grupo de campos'
        }),
    
    )
