from django.db import models

class Instructor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    grade = models.IntegerField()

    def __str__(self):
        return self.name

class Semester(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f"{self.from_date} to {self.to_date}"

class Course(models.Model):
    id = models.UUIDField(primary_key=True)
    course_name = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    syllabus = models.TextField()
    course_content = models.TextField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.course_name

class CourseSchedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.IntegerField()  # Assuming day as integer (0=Sunday, 6=Saturday)
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return f"{self.course.course_name} on {self.day}"

class CourseStudent(models.Model):
    id = models.UUIDField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.course_name} - {self.student.name}"
