from rest_framework_extensions.routers import ExtendedSimpleRouter

from django_project.exhibition.views import ExhibitionViewSet, PictureViewSet

router = ExtendedSimpleRouter()

(
    router.
    register('', ExhibitionViewSet, basename='exhibition').
    register(r'pictures', PictureViewSet, basename='picture', parents_query_lookups=['exhibition'])
)

urlpatterns = router.urls
