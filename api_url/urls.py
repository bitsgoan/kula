from django.urls import include, path

from . import views

urlpatterns = [
    path('add/', views.convert), #POST
    path('list/<str:pk>/', views.list), #GET
    path('delete/<str:pk>/', views.delete), #DELETE

#optional
    path('', views.home),
    path('listall/', views.listall), #GET

#User realated
    ##path('register/', views.registerPage, name="register"),
    #path('login/', views.loginPage, name="login"),  
    #path('logout/', views.logoutUser, name="logout"),
]
