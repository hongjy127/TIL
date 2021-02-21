from django.contrib import admin

# Register your models here.

from bookmark.models import Bookmark

# Bookmark를 통째로 등록 (모든 행을 관리)
# admin.site.register(Bookmark)

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')