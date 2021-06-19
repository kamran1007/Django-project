from django.contrib import admin
from loginapp.models import User


# Register your models here.
class Data(admin.ModelAdmin):

	list_display = ('id','username','email','password','repassword','address')

admin.site.register(User,Data)
	
