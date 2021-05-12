from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Admin_login)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(NewUser)