from rest_framework.routers import SimpleRouter

from api.viewset import EnderecoViewSet

routerV1 = SimpleRouter()
routerV1.register('endereco', EnderecoViewSet)