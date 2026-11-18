from django.contrib import admin
from django.urls import path
from mylove import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_Churn,name='calculate'),
]
