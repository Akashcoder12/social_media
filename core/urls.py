from django.urls import path, re_path
from django.shortcuts import redirect
from . import views


def redirect_to_feed(request):
    return redirect('feed')


urlpatterns = [

    # Redirect root → feed
    path('', redirect_to_feed, name='home'),

    # Auth
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Feed
    path('feed/', views.feed, name='feed'),

    # Posts
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # Comments
    path('post/<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),  # ✅ FIXED

    # Like
    path('post/<int:pk>/like/', views.like, name='like'),

    # User Profile (allows letters, numbers, _, ., @, +, -)
    re_path(r'^profile/(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),  # ✅ FIXED

    # Guest Profile (also allow special chars)
    re_path(r'^guest/profile/(?P<username>[\w.@+-]+)/$', views.guest_profile, name='guest_profile'),  # ✅ FIXED

    # Change Username
    path('profile/change-username/', views.change_username, name='change_username'),

    # Search
    path('search/', views.search_users, name='search_users'),
]
