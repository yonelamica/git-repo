from django.contrib import admin
from .models import Album, Policy
# registered my models
'''
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
inlines = [ChoiceInline]
'''
admin.site.register(Album)
admin.site.register(Policy)
