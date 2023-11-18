from rest_framework.routers import DefaultRouter

# import thu vien cho toi
from .views import PoolViewSet

router = DefaultRouter()
router.register('pools', PoolViewSet)


urlpatterns = router.urls