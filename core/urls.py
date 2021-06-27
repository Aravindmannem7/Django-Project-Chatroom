
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path("",views.home_page,name="home_page"),
    path('accounts/',include('accounts.urls')),
]
