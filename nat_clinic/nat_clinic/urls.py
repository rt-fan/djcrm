from django.contrib import admin
from django.urls import path, include

from website.views import pageNotFound

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('website.urls'))
]

handler404 = pageNotFound
