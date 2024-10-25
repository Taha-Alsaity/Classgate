from django.contrib import admin
from .models import Schools, Students,ExamMark,Content,Exam,ExamQ
# Register your models here.

admin.site.register(Schools)
admin.site.register(Students)
admin.site.register(ExamMark)
admin.site.register(Content)
admin.site.register(Exam)
admin.site.register(ExamQ)

