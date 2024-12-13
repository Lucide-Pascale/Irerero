from django.contrib import admin
from irereroapp import models
admin.site.register(models.User)
admin.site.register(models.ParentsDetails)
admin.site.register(models.TeacherDetails)
admin.site.register(models.Teacher)
admin.site.register(models.Class)
admin.site.register(models.Guardian)
admin.site.register(models.child)
admin.site.register(models.HealthMetricType)
admin.site.register(models.HealthMetricRecord)
admin.site.register(models.Attendance)
admin.site.register(models.AttendanceSummary)
admin.site.register(models.School)
