from django.contrib import admin

from .models import *

admin.site.register(Member)
admin.site.register(ResetPassword)
admin.site.register(JuryGroups)
admin.site.register(Jury)