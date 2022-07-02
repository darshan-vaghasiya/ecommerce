import random

from django.conf import settings
from rest_framework import serializers
from custom_auth.models import User


class SignInSerializer(serializers.ModelSerializer):
    """
    This used for sign up use and send email.
    """

    class Meta:
        model = User
        fields = ['id', 'email']
        extra_kwargs = {
            'email': {'required': True, 'error_messages': {'blank': 'Please enter email'}},
        }

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email'])
        if not user.exists():
            user = User.objects.create(username=validated_data['email'], email=validated_data['email'])
        else:
            user = user.first()
        otp = random.randint(1000, 9999)
        subject = 'welcome to ecommerce world'
        message = f'Please use otp for sign in.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [validated_data["email"]]
        # send_mail(subject, message, email_from, recipient_list)
        user.otp = otp
        user.save()
        return user


class OtpVerification(serializers.ModelSerializer):
    """
    This used for validate otp in registration time etc.
    """

    class Meta:
        model = User
        fields = ['id', 'email', 'otp']
        extra_kwargs = {
            'otp': {'required': True, 'error_messages': {'blank': 'Please Enter Otp'}},
        }

    def verify(self):
        email = self.validated_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            user = user.first()
            if user.otp == self.validated_data['otp']:
                user.otp = '0000'
                user.save()
                return user
            else:
                raise serializers.ValidationError("Invalid otp please try again.")
        else:
            raise serializers.ValidationError("Invalid User.")
