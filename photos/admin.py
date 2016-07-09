from django.contrib import admin
from photos.models import Photo
from photos.models import Like

admin.site.register(Photo)
admin.site.register(Like)

#@admin.register(Post) 을 이용하여 admin에 등록가능
