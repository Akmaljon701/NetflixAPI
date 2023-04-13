from django.contrib import admin
from django.urls import path, include
from film.views import *

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('izohlar', IzohlarViewSet)
router.register('aktyorlar', AktyorlarViewSet)
router.register('kinolar', KinolarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', HelloAPI.as_view()),

    # path('aktyorlar/', AktyorlarAPIView.as_view()),
    # path('aktyor/<int:pk>/', AktyorAPIView.as_view()),

    path('tariflar/', TariflarAPIView.as_view()),
    path('tarif/<int:pk>/', TarifAPIView.as_view()),

    # path('kinolar/', KinolarAPIView.as_view()),
    # path('kino/<int:pk>/', KinoAPIView.as_view()),

    path('', include(router.urls)),
    path('get_token/', obtain_auth_token),
]
