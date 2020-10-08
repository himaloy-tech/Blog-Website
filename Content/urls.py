from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostList, name='home'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('details/<int:post_id>/', views.PostDetail, name='details'),
    path('create/post/', views.PostCreate, name='create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path("profile", views.profile, name="profile-info"),
]