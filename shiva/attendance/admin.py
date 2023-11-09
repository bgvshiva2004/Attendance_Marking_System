from django.contrib import admin
from .models import ClassImage
from .models import Attendance_record,embeddings

# Register your models here.

admin.site.register(ClassImage)
admin.site.register(Attendance_record)
admin.site.register(embeddings)