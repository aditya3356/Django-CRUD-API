from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.views import (
    ActivityCreateView,
    ActivityListView,
    ActivityRetrieveUpdateDestroyView,
    CustomerCreateView,
    CustomerListView,
    CustomerRetrieveUpdateDestroyView,
    ProductCreateView,
    ProductListView,
    ProductRetrieveUpdateDestroyView,
)

app_name = "own_api"

schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version="v1",
        description="Django CRUD API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="aditya.3356@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("customers/", CustomerListView.as_view()),
    path("customers/<int:pk>/", CustomerRetrieveUpdateDestroyView.as_view()),
    path("add_customer/", CustomerCreateView.as_view()),
    path("products/", ProductListView.as_view()),
    path("products/<int:pk>/", ProductRetrieveUpdateDestroyView.as_view()),
    path("add_product/", ProductCreateView.as_view()),
    path("activities/", ActivityListView.as_view()),
    path("activities/<int:pk>/", ActivityRetrieveUpdateDestroyView.as_view()),
    path("add_activity/", ActivityCreateView.as_view()),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
