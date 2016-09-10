from django.contrib import admin
from events.models import Event,Team, ParentEvent


admin.site.register(Event)
admin.site.register(ParentEvent)
admin.site.register(Team)
