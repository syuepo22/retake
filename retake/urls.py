from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('registration.urls')), 
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("", views.home, name='home'),
]