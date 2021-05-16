from rest_framework_extensions.routers import ExtendedSimpleRouter

from django_project.order.views import ProductViewSet, OrderViewSet

router = ExtendedSimpleRouter()

(
    router.
    register('products', ProductViewSet, basename='products')
)

(
    router.
    register('orders', OrderViewSet, basename='orders')
)

urlpatterns = router.urls
