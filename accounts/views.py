from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.serializer import PersonaSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
#Login imports
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = PersonaSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            account.set_password(request.data.get('password'))
            account.save()
            data['response'] = "Usuario creado exitosamente."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


from rest_framework.exceptions import AuthenticationFailed

@api_view(['POST'])
def login(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if username and password:
        authenticate_user = authenticate(username=username, password=password)
        if authenticate_user is not None:
            token, _ = Token.objects.get_or_create(user=authenticate_user)
            serializer = PersonaSerializer(authenticate_user)
            return Response({'user': serializer.data, 'token': token.key})
        else:
            user_exists = User.objects.filter(username=username).exists()
            if not user_exists:
                raise AuthenticationFailed("El nombre de usuario proporcionado no existe.")
            else:
                raise AuthenticationFailed("La contraseña proporcionada es incorrecta.")
    
    return Response({"detail": "Se requieren tanto nombre de usuario como contraseña."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def TestView(request):
    return Response({"message": "hola mundo"})


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": "Cierre de sesión exitoso"})
