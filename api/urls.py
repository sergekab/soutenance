# from .Views.CategoryView import CategoryViewset
from rest_framework.routers import DefaultRouter

from api.views import EvenementViewSet, ProgrammeViewSet, UtilisateurViewSet

router = DefaultRouter()
router.register('programmes', ProgrammeViewSet, basename="programme")
router.register('utilisateurs', UtilisateurViewSet, basename="utilisateurs")
router.register('evenements', EvenementViewSet, basename="evenements")
urlpatterns = router.urls
