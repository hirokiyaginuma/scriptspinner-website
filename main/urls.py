from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('download/', views.download, name='download'),
    path('test1/', views.test1, name='test1'),
]