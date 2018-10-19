from django.contrib import admin

from .models import Show, Band, Press, Contact

admin.site.register(Show)
admin.site.register(Band)
admin.site.register(Press)
admin.site.register(Contact)