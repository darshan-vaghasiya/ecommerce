from rest_framework import viewsets, status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from custom_auth.serializers import SignInSerializer
from rest_framework.authtoken.models import Token
from custom_auth.serializers import OtpVerification


class UserViewSet(viewsets.GenericViewSet):

    @action(detail=False, methods=['post'], serializer_class=SignInSerializer, url_path='sign-in', url_name='sign_in')
    def sign_in(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_serializer = SignInSerializer(user)
        user_data = user_serializer.data
        user_data['otp'] = user.otp
        return Response(user_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], serializer_class=OtpVerification, url_path='otp-verify',
            url_name='otp_verify')
    def otp_verify(self, request, *args, **kwargs):
        """defined for otp verification"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.verify()
        token = Token.objects.create(user=user)
        user_serializer = SignInSerializer(user)
        user_data = user_serializer.data
        user_data['token'] = token.key
        return Response(user_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'], permission_classes=[permissions.IsAuthenticated],
            authentication_classes=[TokenAuthentication], url_path='logout')
    def logout(self, request):
        auth_token = request._request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
        Token.objects.filter(key=auth_token).delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
