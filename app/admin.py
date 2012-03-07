from django.contrib import admin
from wstest.app.models import User, Pitch

class PitchAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'

class UserAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'

admin.site.register(Pitch, PitchAdmin)
admin.site.register(User, UserAdmin)

