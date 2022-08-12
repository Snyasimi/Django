from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/",views.create_page,name='create_page'),
    path("Random Page/",views.Random_page,name="Random_page"),
]
