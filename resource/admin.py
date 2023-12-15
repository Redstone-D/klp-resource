from django.contrib import admin 
from .models import * 

class PostAdmin(admin.ModelAdmin): 

    filter_horizontal = ("ver",) 
    list_display = ("tid", "postType", "title") 
    

# Register your models here.

admin.site.register(Quality) 
admin.site.register(Board) 
admin.site.register(PT) 
admin.site.register(Version) 
admin.site.register(Originality) 
admin.site.register(Tag) 
admin.site.register(Post, PostAdmin) 
