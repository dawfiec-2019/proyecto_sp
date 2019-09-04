from rest_framework import routers

from .viewsets import *

router = routers.SimpleRouter()
router.register('asambleista',AsableistaViewSet)
router.register('usuario',UsuarioViewSet)
router.register('ley',LeyViewSet)
router.register('persona',PersonaViewSet)
router.register('comentario',ComentarioViewSet)
router.register('comentarioley',ComentarioLeyViewSet)
router.register('voto',VotoViewSet)


urlpatterns = router.urls
