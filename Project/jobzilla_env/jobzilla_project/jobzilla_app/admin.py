from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Jobseeker)
admin.site.register(Jobprovider)
admin.site.register(Jobseeker_details)
admin.site.register(Jobpost)
admin.site.register(Jobapply)