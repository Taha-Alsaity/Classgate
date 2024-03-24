# Classgate
 This project idea is to be used by any school upload their quizzes and content online and see their students marks,  they just have to send their name and choose if eathir they want the school to be public or private.

# public:
Means that any student or user in the world can join and use their content.
# private:
no new user can enroll only the student that school sens their users to us is allowed.

school also have to send teachers info to create there accounts, theres no new user can be teacher for security and make sure there's no mess.

# Distinctiveness and Complexity:
the need of this kind of project is not improtant for students only, schools save alot of time correcting exams or trying to find old exams,content and data, and its easier to upload it online for all students at once.

the main reason is the use of modles and alot of work on the veiws.py file makes it not simple at all  that makes the project interactive like marks immediately added when finish exams, also the frontend with css and javascript.

# qustions models:
 what i did is to put exam info in model and the quistions in other one then did a foreign key relation between every quiz to its exam this idea seems to work and saves alot of time, if there any other ways let me know.

 
# What’s contained in each file you created:

   # Taha-21.html, Taha-ar.html, user-ar.html and user.html:
    Have the main page content in both eng and arabic.
   # student.html:
    Have the list or side bar and the content appears after student joins a schools.
   # Sch1-exams.html:
    Have list of exams uploaded in the shcool.
   # log in.html and reqister.html:
    for sign up and log in.
   # member.html:
    is how to be member either to join or send info until you be accepted
   # marks.html:
    list of student marks
   # exam.html:
    the form of exams and its only true or false or 2 options quiz.
   # add.html:
    for adding exams or content to school page.
   # edit.html:
    form of editing username:


# How to run your application.
just makemigrations and migrate then run the website.


# Any other additional information the staff should know about your project.

when teacher try to add exam they must list the options in order of the exam not the quistion like if they have 2 quistions each one has 2 options the first quistion options should be 1 and then the 2nd quistion options should be 3 and 4 not 1 and 2.