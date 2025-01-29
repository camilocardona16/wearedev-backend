from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.settings import knox_settings

class LoginView(KnoxLoginView):
    # Extiende KnoxLoginView para personalizar la respuesta del login
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Validar las credenciales del usuario con AuthTokenSerializer
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)  # Inicia sesión al usuario

        # Obtener el response del KnoxLoginView
        response = super(LoginView, self).post(request, format=None)

        # Modificar el response para incluir datos adicionales del usuario
        response.data.update({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        })

        return response
