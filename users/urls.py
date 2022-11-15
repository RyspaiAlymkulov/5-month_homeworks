from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.LoginAPIview.as_view()),
    path('register/', views.RegisterAPIview.as_view())
]