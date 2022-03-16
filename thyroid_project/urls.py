from django.urls import path
from thyroid_project import views

urlpatterns =[
    path('',views.home, name='home'),
    path('predict/',views.predict,name='predict'),
]