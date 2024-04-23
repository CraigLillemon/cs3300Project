from django.contrib import admin
from .models import Trail, State, ManagerAssessmentRecord
# Register your models here.
admin.site.register(Trail)
admin.site.register(State)

@admin.register(ManagerAssessmentRecord)
class ManagerAssessmentRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "manager", "score"]