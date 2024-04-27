from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('register', views.RegisterView)
router.register('inventory', views.InventoryView)


urlpatterns = [
    path('login/', views.CustomAuthToken.as_view()),
    path('', include(router.urls)),
]
