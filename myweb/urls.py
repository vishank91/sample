from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('details/<int:num>',views.details),
    path('add_Employee/',views.add_Employee),
    path('registration/',views.registration),
]
