from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from apps.core.views import frontpage, signup, login
from apps.feed.views import feed
from apps.feed.api import api_add_oink

urlpatterns = [

    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),

    #
    #
    path('feed/', feed, name='feed'),

    #
    # API
    path('api/add_oink/', api_add_oink, name='api_add_oink'),
    # Admin
    path('admin/', admin.site.urls),
]
