from django.contrib import admin
from django.urls import path,include

#To show media files
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_shop.urls')),
    path('account/',include('app_login.urls')),
    path('shop/',include('app_order.urls')),
    path('payment/',include('app_payment.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)