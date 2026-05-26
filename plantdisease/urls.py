"""
Root URL configuration — Smart Plant Disease Detection System
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from dashboard import views as home_views

# ── Non-i18n URLs ────────────────────────────────────────────────────────────
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# ── i18n-prefixed URL patterns ───────────────────────────────────────────────
urlpatterns += i18n_patterns(
    path('',          home_views.landing_page, name='landing'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('detector/', include('detector.urls', namespace='detector')),
    path('advisory/', include('advisory.urls', namespace='advisory')),
    path('reports/',  include('reports.urls',  namespace='reports')),
    prefix_default_language=False,
)

# ── Media files (development only) ───────────────────────────────────────────
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
