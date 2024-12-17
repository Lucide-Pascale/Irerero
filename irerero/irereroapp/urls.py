
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('attendance/', views.attendance, name='attendance'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('addclass/', views.add_class,name='add_class'),
    path('homepage/', views.homepage, name='homepage'),
    path('healthmetric/', views.health, name='health'),
    path('', views.landing, name='landing'),
  
    path('register/teacher',views.register_teacher, name='register_teacher'),
    path('register/parent',views.register_parent, name='register_parent'),
    path('register/headteacher/', views.register_headteacher, name='register_headteacher'),
    path('register/schoolinfo/', views.register_schoolinfo, name='register_schoolinfo'),
    # path('register/teacher/', views.register_teacher, name='register_teacher'),
    # path('register/parent/', views.register_parent, name='register_parent'),
    # path('login/', views.login_view, name='login'),
    
    
    
    path('dashboard/', views.AdminDashboard, name='dashboard'),
]
