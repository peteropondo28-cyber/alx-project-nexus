from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, CategoryViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version="v1",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/", include("users.urls")),
    path("swagger/", schema_view.with_ui("swagger")),
]
