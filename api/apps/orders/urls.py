from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter(trailing_slash=False)
router.register("orders", views.OrderViewSet, basename="order")

app_name = "orders"

urlpatterns = []
urlpatterns += router.urls
