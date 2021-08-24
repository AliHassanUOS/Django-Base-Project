from django.contrib import admin
from django.db import models
from .models import Student,Person,User


# Register your models here.



class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","stu_name","status","stu_email"]
    list_filter = ["id","stu_name","status","stu_email"]
    search_fields = ["id"]
    sortable_by = ["-id"]


admin.site.register(Student,StudentAdmin)
admin.site.register(Person)
admin.site.register(User)