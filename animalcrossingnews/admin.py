from django.contrib import admin

from .models import Heading
from .models import Story

admin.site.register(Heading)
admin.site.register(Story)