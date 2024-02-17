from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserCreateAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, \
    PaymentListAPIView, PaymentDetailAPIView, PaymentDeleteAPIView, UserListAPIView, UserDetailAPIView, \
    UserDeleteAPIView

app_name = UsersConfig.name

urlpatterns = [
    # authorization
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # user
    path('user/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('user/', UserListAPIView.as_view(), name='user-list'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/detail/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('user/delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),

    # payment
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/detail/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment-delete'),
]
