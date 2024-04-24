from django.urls import path

from . import views

urlpatterns = [
    path("/checkout", views.checkout_book, name="checkout"),
    path("/return", views.return_book, name="return"),
    path("/fulfill", views.fulfill_book, name="fulfill"),
]
