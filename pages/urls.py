from django.urls import path
from django.urls import path
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='pages'),
    path('about/',views.about,name="pages")
] 