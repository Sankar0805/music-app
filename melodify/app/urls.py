from django.contrib import admin
from django.urls import path
from app import views as music_views
from accounts import views as account_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Music app
    path('', music_views.home, name='home'),

    # Accounts app
    path('register/', account_views.register_view, name='register'),
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),

    # Playlist app
    path('add_to_playlist/', views.add_to_playlist, name='add_to_playlist'),
    path('get_playlist/', views.get_playlist, name='get_playlist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
