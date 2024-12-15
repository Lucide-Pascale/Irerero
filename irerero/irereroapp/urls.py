
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('landingpage/', views.landing, name='landing'),
    path('register/teacher',views.register_teacher, name='register_teacher'),
    path('register/parent',views.register_parent, name='register_parent'),
    path('register/headteacher/', views.register_headteacher, name='register_headteacher'),
    path('register/schoolinfo/', views.register_schoolinfo, name='register_schoolinfo'),
    # path('register/teacher/', views.register_teacher, name='register_teacher'),
    # path('register/parent/', views.register_parent, name='register_parent'),
    # path('login/', views.login_view, name='login'),
]
