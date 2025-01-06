from django.urls import path
from .import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.blog_page,name='blog_page'),
    path('view/', views.blog_view,name='blog_view'),
    path('view/<slug:id>/', views.blog_view,name='blog_view'),
    path('category/<slug:id>/', views.category,name='category'),

    path('contact', views.contact,name='contact'),
    path('search/', views.blog_search,name='my_search'),
    # path('updates/', views.updates,name='updates'),
]