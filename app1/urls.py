from django.urls import path
from .import views
urlpatterns=[
    path("home1/",views.home1,name="home1"),
    path("home1/examcat/",views.examcat,name="examcat"),
    path("home1/examcat/home1r/",views.home1r,name=""),
    path("home1/examcat/python/",views.pythontest,name="python"),
    path("home1/examcat/python/home1r/",views.home1r,name=""),
    path("home1/examcat/sql/",views.sqltest,name="sql"),
    path("home1/examcat/sql/home1r/",views.home1r,name="sql"),
    path("home1/examcat/ml/",views.mltest,name="ml"),
    path("home1/examcat/ml/home1r/",views.home1r,name="ml"),
    
]