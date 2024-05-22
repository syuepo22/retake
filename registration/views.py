from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import MySQLdb  
from django.conf import settings
from django.db.models import Q



def login(request):
    return render(request, 'login.html')
@login_required
def home(request):
    return render(request, 'home.html')

class OpenEnrollments(APIView):
    def post(self, request, *args, **kwargs):
        course_name = request.data.get('course_name')
        instructor_id = request.data.get('instructor_id')
        syllabus = request.data.get('syllabus')
        course_content = request.data.get('course_content')
        semester_id = request.data.get('semester_id')

        if not all([course_name, instructor_id, syllabus, course_content, semester_id]):
            return Response({"error": "All fields are required"}, status=400)

        try:
            db = MySQLdb.connect(
                host=settings.DATABASES['default']['HOST'],
                user=settings.DATABASES['default']['USER'],
                passwd=settings.DATABASES['default']['PASSWORD'],
                db='web',
                charset='utf8'
            )
            cursor = db.cursor()
            sql = """
            INSERT INTO course (course_name, instructor_id, syllabus, course_content, semester_id) 
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (course_name, instructor_id, syllabus, course_content, semester_id))
            db.commit()
        except MySQLdb.DatabaseError as e:
            db.rollback()
            return Response({"error": str(e)}, status=500)
        finally:
            db.close()

        return Response({"status": "Course created", "course_name": course_name})

    def delete(self, request, courseId, *args, **kwargs):
        try:
            db = MySQLdb.connect(
                host=settings.DATABASES['default']['HOST'],
                user=settings.DATABASES['default']['USER'],
                passwd=settings.DATABASES['default']['PASSWORD'],
                db='web',
                charset='utf8'
            )
            cursor = db.cursor()
            sql = "DELETE FROM course WHERE instructor_id = %s"
            cursor.execute(sql, (courseId,))
            db.commit()
        except MySQLdb.DatabaseError as e:
            db.rollback()
            return Response({"error": str(e)}, status=500)
        finally:
            db.close()

        return Response({"status": "Course deleted"})

    def patch(self, request, courseId, *args, **kwargs):
        updates = []
        values = []

        for field in ['course_name', 'instructor_id', 'syllabus', 'course_content', 'semester_id']:
            if field in request.data:
                updates.append(f"{field} = %s")
                values.append(request.data[field])

        if not updates:
            return Response({"error": "No fields provided for update"}, status=400)

        values.append(courseId)  # Append courseId at the end for the WHERE condition
        sql = f"UPDATE course SET {', '.join(updates)} WHERE instructor_id = %s"

        try:
            db = MySQLdb.connect(
                host=settings.DATABASES['default']['HOST'],
                user=settings.DATABASES['default']['USER'],
                passwd=settings.DATABASES['default']['PASSWORD'],
                db='web',
                charset='utf8'
            )
            cursor = db.cursor()
            cursor.execute(sql, values)
            db.commit()
        except MySQLdb.DatabaseError as e:
            db.rollback()
            return Response({"error": str(e)}, status=500)
        finally:
            db.close()

        return Response({"status": "Course updated"})
class GetCourseInfo(APIView):
    def get(self, request, *args, **kwargs):
        course_name = request.query_params.get('course_name')
        instructor_id = request.query_params.get('instructor_id')
        semester_id = request.query_params.get('semester_id')

        query_conditions = []
        query_params = []

        if course_name:
            query_conditions.append("course_name = %s")
            query_params.append(course_name)
        if instructor_id:
            query_conditions.append("instructor_id = %s")
            query_params.append(instructor_id)
        if semester_id:
            query_conditions.append("semester_id = %s")
            query_params.append(semester_id)

        if not query_conditions:
            return Response({"error": "At least one query parameter is required"}, status=400)

        try:
            db = MySQLdb.connect(
                host=settings.DATABASES['default']['HOST'],
                user=settings.DATABASES['default']['USER'],
                passwd=settings.DATABASES['default']['PASSWORD'],
                db='web',
                charset='utf8'
            )
            cursor = db.cursor(MySQLdb.cursors.DictCursor)
            sql = f"SELECT * FROM course WHERE {' AND '.join(query_conditions)}"
            cursor.execute(sql, query_params)
            courses = cursor.fetchall()
        except MySQLdb.DatabaseError as e:
            return Response({"error": str(e)}, status=500)
        finally:
            db.close()

        return Response({"courses": courses})

class SignUpEnrollment(APIView):
    def post(self, request, *args, **kwargs):
        # 實現報名的邏輯
        return Response({"status": "signup successful"})

class DownloadEnrollmentData(APIView):
    def get(self, request, *args, **kwargs):
        # 實現下載報名資料的邏輯
        return Response({"status": "download link"})

class GeneratePayment(APIView):
    def post(self, request, *args, **kwargs):
        # 實現生成支付資訊的邏輯
        return Response({"status": "payment generated"})

class OnSiteSignUp(APIView):
    def post(self, request, *args, **kwargs):
        # 實現現場報名的邏輯
        return Response({"status": "signed up on-site"})
