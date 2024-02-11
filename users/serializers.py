from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payments_list = PaymentSerializer(source='owner', many=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'payments_list',)
