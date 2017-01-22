from django.contrib import admin
from .models import Goal, Role, Explanation, Notation, Code, Membership

admin.site.register(Goal)
admin.site.register(Role)
admin.site.register(Notation)
admin.site.register(Explanation)
admin.site.register(Code)
admin.site.register(Membership)