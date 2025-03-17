from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('landing_page', views.landing_page, name='landing_page'),
    # path('logout/', views.logout_redirect, name='logout'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('books/', views.books_view, name='books'),
    path('software/', views.software_view, name='software'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('account/', views.account, name='account'),
    # path('register/', views.register, name='register'),
    path('auth/', include('django.contrib.auth.urls')),
    path('social/', include('social_django.urls', namespace='social')),

]
# Images to load in the browser
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
