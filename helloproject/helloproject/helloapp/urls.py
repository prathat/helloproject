from helloapp import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("page1",views.page1,name="page1"),
    path("timepage/<name>/<colorval>",views.timepage,name="timepage"),
]