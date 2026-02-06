
from django.contrib import admin
from django.urls import path,include
from Route import routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('',include(routes)),
    path("health/", lambda request: HttpResponse("ok")),
]
