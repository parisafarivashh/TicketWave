from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import User
from .serializers import DRFTokenSerializer, UserRegisterSerializer, \
    ChangePasswordSerializer


class TokenController(TokenObtainPairView):
    serializer_class = DRFTokenSerializer


class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class ChangePasswordView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()

    def get_object(self):
        return User.objects.get(id=self.request.user.id)

