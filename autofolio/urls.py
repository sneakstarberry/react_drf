from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
import api.views 

router = routers.DefaultRouter()
router.register('api', api.views.PostViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]