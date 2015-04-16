from annotation.models import Entry
from annotation.models import Translation
from django.contrib import admin

class TranslationInline(admin.TabularInline):
    model = Translation
    extra = 3

class AnnotationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['english_word']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [TranslationInline]
    list_display = ('english_word', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
 
#was_published_today.short_description = 'Published today?'

#admin.site.register(Choice)
#admin.site.register(Poll)
admin.site.register(Entry, AnnotationAdmin)
