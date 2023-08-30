from rest_framework.routers import DefaultRouter
from .views import TODOViewSet

router = DefaultRouter()
router.register(r'app', TODOViewSet, basename='app')


urlpatterns = router.urls