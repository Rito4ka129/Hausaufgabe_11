from django.urls import path
from rest_framework import routers
from homework_app.views.category_views import CategoryViewSet



router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
urlpatterns = router.urls

