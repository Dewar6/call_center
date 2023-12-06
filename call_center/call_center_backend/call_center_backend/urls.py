from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from call_center.views import AgentViewSet, QueueViewSet

router = DefaultRouter()

router.register('agent', AgentViewSet, basename='agents')
router.register('queue', QueueViewSet, basename='queues')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
