from django.urls import path

from virtual_trial_room.views import home
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home, name= 'home'),
    path('signup/', signupView.as_view(), name= 'signup'),
    path('login/', myloginView.as_view(),name ='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'),name ='logout'),
]
