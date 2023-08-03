from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>/<slug:post_slug>/', views.PostDetailView.as_view(), name='detail_post'),
    path('post/delete/<int:pk>/', views.PostDeletView.as_view(), name='delete_post'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='update_post'),
    path('post/create/', views.PostCreateView.as_view(), name='create_post'),

]