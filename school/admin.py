from django.contrib import admin

from .models import Student, Teacher, StudentTeachers


class StudentTeachersInline(admin.TabularInline):
    model = StudentTeachers
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "group"]
    list_filter = ["group"]
    inlines = [StudentTeachersInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "subject"]
