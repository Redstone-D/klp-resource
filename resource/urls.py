from django.urls import path 

from . import views 

urlpatterns = [ 
    path("<int:pageId>", views.page, name="page"), 
    path("", views.index, name="index"), 
    path("filter", views.filter, name="filter"), 
    path("search/", views.filter, name="search"), 
    path("search/<int:pt>/<int:st>/<str:name>", views.search, name="search") 
] 
