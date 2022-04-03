from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView ,LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    # path('login/', LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    # path('login/', views.loginPage, name='login'),
    # path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('table_users/', views.tableuser, name='table_users'),
    # path('user_update/<int:id>/update', views.user_update, name='user_update')

]

