from django.contrib import admin
from . models import SignupModel, user,FormModel,LoginModel,ContactModel


admin.site.register(user)

admin.site.register(FormModel)
admin.site.register(LoginModel)
admin.site.register(SignupModel)
admin.site.register(ContactModel)