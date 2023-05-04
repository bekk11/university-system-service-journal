from django.contrib import admin

from apps.journal.models import Journal


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_id', ]
