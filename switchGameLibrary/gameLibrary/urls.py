from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page_view, name='landing_page_view'),
    path('about/', views.about_view, name='about_view'),
]