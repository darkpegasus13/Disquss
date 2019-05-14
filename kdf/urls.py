from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Home/', include('login_page.urls')),
    url(r'^Post/', include('thread.urls'))
]
