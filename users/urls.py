from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('userData/<int:id>',views.userData,name='userdata'),
    path('signup',views.SignupUser.as_view(),name='signup'),
]
