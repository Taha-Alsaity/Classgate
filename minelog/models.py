
from django.db import models



# Create your models here.
class Schools(models.Model):
    Rule_CHOICE = (
    ('Pu', 'public'),
    ('Pr', 'private'),
)
    School_Name = models.CharField(max_length=64)
    flex = models.CharField(max_length=2,null=True,choices=Rule_CHOICE)
    def __str__(self):
        return f"{self.id}: {self.School_Name}"


class Students(models.Model):
    Rule_CHOICES = (
    ('S', 'Student'),
    ('T', 'Teacher'),
)
    email = models.CharField(max_length=500,null=True)

    name = models.CharField(max_length=64)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, null=True, related_name='schools')
    password = models.IntegerField()
    rule = models.CharField(max_length=1, choices=Rule_CHOICES,null=True)


    def __str__(self):
        return f"{self.id}: {self.name}  |  School name: {self.school.School_Name}  "
    

class Content(models.Model):
   school = models.ForeignKey(Schools, on_delete=models.CASCADE, null=True, related_name='schoolcontent')
   
   teacher =  models.ForeignKey(Students, on_delete=models.CASCADE, null=True, related_name='contentowner')
   keyword = models.CharField(max_length=40 , null=True)
   title = models.CharField(max_length=200)
  
   vedio = models.CharField(max_length=2000)
   link = models.CharField(max_length=2000)

class ExamMark(models.Model):
    username = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, related_name='markowner')
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, null=True, related_name='schoolmarks')
   
    exam_name = models.CharField(max_length=100)
    mark = models.IntegerField()
    fullmark = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.username.name} - {self.exam_name}: {self.mark}/{self.fullmark}"
    


class Exam(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, null=True, related_name='schoolexams')
   
    teacher =  models.ForeignKey(Students, on_delete=models.CASCADE, null=True, related_name='examowner')
    category = models.CharField(max_length=80, null=True)
    name = models.CharField(max_length=100)
    arname = models.CharField(max_length=200, null=True)
    fullmark = models.FloatField()
    quizsnumber= models.IntegerField(null=True)
    half = models.FloatField()
    def __str__(self):
        return f"{self.category}: {self.name}"

   
class ExamQ(models.Model):
    examid = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, related_name='Examid')
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    qmark = models.FloatField()
    opt1id = models.IntegerField(null=True)
    opt2id = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.examid.category}: {self.examid.name} - {self.id} "