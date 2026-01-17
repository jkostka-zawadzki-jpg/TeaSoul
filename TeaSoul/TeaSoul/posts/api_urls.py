from rest_framework.routers import DefaultRouter

from .api_views import CategoryViewSet, PostViewSet, TopicViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("topics", TopicViewSet)
router.register("posts", PostViewSet)

urlpatterns = router.urls
