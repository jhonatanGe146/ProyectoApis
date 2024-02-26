from django.urls import path
from accounts.views import (

    signup,
    login,
    TestView,
    logout,

)

app_name = "accounts"

urlpatterns = [
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('test-view', TestView, name="test-view"),
    path('logout', logout, name="logout"),
      
]