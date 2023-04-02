from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  # admin
                  path('admin/', admin.site.urls),

                  # orders
                  path('', include("orders.urls")),

                  # auth
                  path('account/', include("users.urls")),

                  # debug
                  path('__debug__/', include('debug_toolbar.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.
                                                                                           MEDIA_ROOT)
