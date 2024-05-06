from django.contrib import admin

from .models import Drawing, Rectangle, Tag

admin.site.register(Drawing)
admin.site.register(Rectangle)
admin.site.register(Tag)