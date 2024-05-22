from django.urls import path
from . import views
from .views import GetCourseInfo

urlpatterns = [
    path('enrollments', views.OpenEnrollments.as_view(), name='open-enrollments'),
    path('enrollments/<str:courseId>', views.OpenEnrollments.as_view(), name='manage-enrollment'),
    path('courses/search/', GetCourseInfo.as_view(), name='course-search'),
    path('enrollments/signup', views.SignUpEnrollment.as_view(), name='signup-enrollment'),
    path('enrollments/downloads', views.DownloadEnrollmentData.as_view(), name='download-enrollment-data'),
    path('enrollments/payments/generate', views.GeneratePayment.as_view(), name='generate-payment'),
    path('enrollments/on-site/signup', views.OnSiteSignUp.as_view(), name='on-site-signup'),
]
