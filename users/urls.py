from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserCreateAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, \
    PaymentListAPIView, PaymentDetailAPIView, PaymentDeleteAPIView, UserListAPIView, UserDetailAPIView, \
    UserDeleteAPIView, PaymentCourseCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    # authorization
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # user
    path('user/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('user/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/<int:pk>/detail/', UserDetailAPIView.as_view(), name='user-detail'),
    path('user/<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),

    # payment
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/<int:pk>/detail/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('payment/<int:pk>/update/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/<int:pk>/delete/', PaymentDeleteAPIView.as_view(), name='payment-delete'),
    path('payment/course/<int:pk>/create/', PaymentCourseCreateAPIView.as_view(), name='payment-course'),
]
