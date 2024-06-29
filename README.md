# Classgate
Classgate is a project designed to provide a platform for schools to upload quizzes and educational content online, allowing them to easily manage and monitor student marks. The project offers two options for schools: public and private.

# Public Option
By choosing the public option, schools allow any student or user from around the world to access and utilize their content. This promotes knowledge sharing and enables students to benefit from a wide range of educational resources.

# Private Option
In the private option, only students enrolled in the school are granted access to the content. This ensures that the platform remains exclusive to the school's students and maintains a secure environment.

To maintain security and avoid any potential issues, the project requires schools to provide teacher information so that only authorized individuals can create accounts. This measure ensures that only trusted teachers have access to the system, maintaining a controlled and secure environment.




# Distinctiveness and Complexity
Classgate stands out due to its unique features and the complexity involved in its development. The project addresses the needs of both students and schools, offering significant time-saving benefits. Schools can easily upload exams and educational content, eliminating the need for manual correction and ensuring that all students receive the materials simultaneously.

The project's complexity is evident in the extensive use of models and the substantial work done in the views.py file. These efforts have resulted in an interactive system that provides immediate mark updates after exams are completed. The frontend development, including CSS and JavaScript, further enhances the project's complexity, resulting in a polished and user-friendly interface.

The implementation of the question models is another area of complexity. The project separates exam information and questions into two separate models, establishing a foreign key relationship between each quiz and its corresponding exam. This approach streamlines the management of exams and questions, resulting in efficient data organization and retrieval. If there are alternative approaches or suggestions for improvement, your feedback would be greatly appreciated.




# File Details
The project consists of several files, each serving a specific purpose:

# Taha-21.html, Taha-ar.html, user-ar.html, and user.html:
 These files contain the main page content in both English and Arabic.
# student.html:
 This file displays the list or side bar and the content that appears once a student joins a school.
# Sch1-exams.html:
 This file presents a list of exams uploaded by the school.
# log in.html and register.html:
 These files provide the sign-up and log-in functionality.
# member.html:
 This file guides users on how to become a member, either by joining or providing necessary information for acceptance.
# marks.html:
 This file displays a list of student marks.
# exam.html:
 This file represents the form for exams, which may consist of true or false questions or quizzes with two options.
# add.html:
 This file facilitates the addition of exams or content to the school page.
# edit.html:
 This file provides a form for editing user names.



# Running the Application
To run the application:

Execute the command makemigrations to create necessary database migrations.
Run the command migrate to apply the migrations and set up the database.
Launch the website to start the application.


# Additional Information
There was an issue note when teachers attempt to add exams in uploaded screecast video the issue was that the teachers had to set options numbers manually  For example, if there are two questions and each has two options, the options for the first question should be labeled as 1 and 2, the options for the second question should be labeled as 3 and 4, i fixed this issue in the last update of github code and now it's automaticaly sets the order of options.

We hope this information provides a comprehensive overview of the Classgate project..