# from django.conf import settings
# from django.contrib import admin
# from django.contrib.auth import views
# from django.urls import include, path
# from django.urls import re_path 
# from django.views.generic import TemplateView
# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularRedocView,
#     SpectacularSwaggerView,
# )
# from django.views.static import serve
# from django.conf import settings
# import os


# app_name = "crm"

# urlpatterns = [
#     url(
#         r"^healthz/$",
#         TemplateView.as_view(template_name="healthz.html"),
#         name="healthz",
#     ),
#     path("api/", include("common.app_urls", namespace="common_urls")),
#     # Public portal endpoints (no auth required)
#     path("api/public/", include("invoices.public_urls", namespace="public_invoices")),
#     path(
#         "logout/", views.LogoutView.as_view(), {"next_page": "/login/"}, name="logout"
#     ),
#     path("admin/", admin.site.urls),
#     path("schema/", SpectacularAPIView.as_view(), name="schema"),
#     # Optional UI:
#     path(
#         "swagger-ui/",
#         SpectacularSwaggerView.as_view(url_name="schema"),
#         name="swagger-ui",
#     ),
#     path(
#         "api/schema/redoc/",
#         SpectacularRedocView.as_view(url_name="schema"),
#         name="redoc",
#     ),
# ]


# if settings.DEBUG:
#     from django.conf.urls.static import static
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#     urlpatterns += staticfiles_urlpatterns()
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#     # urlpatterns = urlpatterns + static(
#     #     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
#     # )






# # ✅ SPA fallback (LAST)
# urlpatterns += [
#     re_path(
#         r'^(?!api/|admin/|static/|_app/|media/).*$', 
#         TemplateView.as_view(template_name="index.html")
#     ),
# ]


from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

app_name = "crm"

urlpatterns = [
    # Health check
    re_path(
        r"^healthz/$",
        TemplateView.as_view(template_name="healthz.html"),
        name="healthz",
    ),

    # API routes
    path("api/", include("common.app_urls", namespace="common_urls")),

    # Public API
    path("api/public/", include("invoices.public_urls", namespace="public_invoices")),

    # Auth
    path(
        "logout/",
        views.LogoutView.as_view(),
        {"next_page": "/login/"},
        name="logout",
    ),

    # Admin
    path("admin/", admin.site.urls),

    # API Docs
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

# Static + media (ONLY in DEBUG)
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.views.static import serve
import os

urlpatterns += [
    re_path(
        r'^_app/(?P<path>.*)$',
        serve,
        {
            'document_root': os.path.join(settings.BASE_DIR, 'frontend_static/_app')
        }
    ),
]

# ✅ SPA fallback (MUST BE LAST)
urlpatterns += [
    re_path(
        r'^(?!api/|admin/|static/|_app/|media/).*$',
        TemplateView.as_view(template_name="index.html"),
    ),
]
