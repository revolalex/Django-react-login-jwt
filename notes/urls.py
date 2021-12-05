from django.urls import path
# Nous utilisons rest_framework SimpleRouter pour créer automatiquement les routes pour nous.
from rest_framework.routers import SimpleRouter
from .views import NoteViewSet

router = SimpleRouter()
router.register('notes', NoteViewSet, basename="notes")
urlpatterns = router.urls