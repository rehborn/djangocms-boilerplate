from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.i18n import i18n_patterns
from cms.sitemaps import CMSSitemap

robots_txt = TemplateView.as_view(template_name="robots.txt", content_type="text/plain")

urlpatterns = [
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
    prefix_default_language=False
)
