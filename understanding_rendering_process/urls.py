from django.urls import path

from understanding_rendering_process import views

urlpatterns = [
    path('',views.simple_form_view, name='simple_form'),
    path('custom/form/', views.custom_form_view, name='custom_form'),
    path('custom/form/bootstrap/', views.cf_bootstrap_view, name='cf_bootstrap'),

]