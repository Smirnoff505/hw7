from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserCreateAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, \
    PaymentListAPIView, PaymentDetailAPIView, PaymentDeleteAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/', UserListAPIView.as_view(), name='user-list'),
    path('user/update/<int:pk>', UserUpdateAPIView.as_view(), name='user-update'),

    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/detail/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment-delete'),
]
