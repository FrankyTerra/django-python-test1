from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Film, Comment, Genre, Country

class CommentAdmin(DjangoMpttAdmin):
	pass

admin.site.register(Film)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Genre)
admin.site.register(Country)