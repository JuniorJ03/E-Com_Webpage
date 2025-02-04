from django.contrib import admin
from userauths.models import User
from import_export.admin import ImportExportModelAdmin



admin.site.register(User)
