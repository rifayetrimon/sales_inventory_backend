
from django.contrib import admin
from django.urls import path, include

api_urlpatterns = [
    path("", include("user.urls")),
    path("", include("categories.urls")),
    path("", include("products.urls")),
    path("", include("customers.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api", include(api_urlpatterns)),
]
