from django.contrib import admin
from .models import Blog
from .models import School
from .models import Team

admin.site.register(Blog)
admin.site.register(School)
admin.site.register(Team)
