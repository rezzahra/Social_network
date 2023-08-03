from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name = 'profile'),
    path('profile/edit/<int:pk>/', views.EditProfileView.as_view(), name='profile_edit'),
    path('follow/<int:pk>/', views.UserFollowView.as_view(), name='follow_user'),
    path('unfollow/<int:pk>/', views.UserUnFollowView.as_view(), name='unfollow_user')

]