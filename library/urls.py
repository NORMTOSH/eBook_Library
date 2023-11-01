from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('admin:index')

urlpatterns = [
    path('admin-redirect/', redirect_to_admin, name='admin_redirect'),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('search/', include('search.urls')),
    path('',include("store.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
