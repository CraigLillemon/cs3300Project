from django.contrib import admin
from .models import Trail, State, ManagerAssessmentRecord, TrailFolders, User
# Register your models here.
admin.site.register(Trail)
admin.site.register(State)
admin.site.register(TrailFolders)
admin.site.register(User)
@admin.register(ManagerAssessmentRecord)
class ManagerAssessmentRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "manager", "score"]