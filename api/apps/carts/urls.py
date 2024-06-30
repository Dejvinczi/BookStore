from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

carts_router = SimpleRouter(trailing_slash=False)
carts_router.register("cart/items", views.CartItemViewSet, basename="cart-item")

app_name = "carts"

urlpatterns = [
    path("cart", views.CartRetrieveAPIView.as_view(), name="cart-retrieve"),
]

urlpatterns += carts_router.urls
