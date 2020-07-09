from django.contrib import admin

# Register your models here.
from .models import Questions, Choice


admin.site.site_header = "Pollester Admin"
admin.site.site_title = "Pollester Admin Area"
admin.site.index_title = "Welcome to the Pollester Admin Area"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['questions_text']}),
                 ('Date Informations', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


# admin.site.register(Questions)
# admin.site.register(Choice)
admin.site.register(Questions, QuestionAdmin)
