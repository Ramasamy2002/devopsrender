from django.contrib import admin

# Register your models here.
from app1.models import python
from app1.models import Sql
from app1.models import Ml
admin.site.register(python)
admin.site.register(Sql)
admin.site.register(Ml)