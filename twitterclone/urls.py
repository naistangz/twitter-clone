from apps.conversation.api import api_add_message
from apps.oinkerprofile.views import oinkerprofile, follow_oinker, unfollow_oinker, followers, follows, edit_profile
from apps.feed.api import api_add_oink, api_add_like
from apps.feed.views import feed, search
from apps.core.views import frontpage, signup, login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from apps.conversation.views import conversations, conversation


urlpatterns = [
    #
    #

    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),

    #
    #
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('conversations/', conversations, name='conversations'),
    path('conversation/<int:user_id>', conversation, name='conversation'),
    path('u/<str:username>/', oinkerprofile, name='oinkerprofile'),
    path('u/<str:username>/follow/', follow_oinker, name='follow_oinker'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('u/<str:username>/follows/', follows, name='follows'),
    path('u/<str:username>/unfollow/', unfollow_oinker, name='unfollow_oinker'),
    #
    # API
    path('api/add_oink/', api_add_oink, name='api_add_oink'),
    path('api/add_like/', api_add_like, name='api_add_like'),
    path('api/add_message/', api_add_message, name='api_add_message'),

    # Admin
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
In production, serve media using Apache, nginx or any other web server
"""
