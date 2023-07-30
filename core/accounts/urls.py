from django.urls import path, include
from . views import SignUpView, EditProfileView, ProfileView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name = 'profile_user'),
    path('profile/<int:pk>/edit/', EditProfileView.as_view(), name='profile_edit'),

]