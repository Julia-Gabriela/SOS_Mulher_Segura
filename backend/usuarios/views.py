
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from .serializers import UserSerializer

User = get_user_model()


@api_view(['POST'])
def login_view(request):
    cpf = request.data.get('cpf')
    senha = request.data.get('senha')

    user = authenticate(username=cpf, password=senha)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })
    else:
        return Response({'error': 'CPF ou senha inválidos'}, status=400)


@api_view(['POST'])
def cadastro_view(request):
    cpf = request.data.get('cpf')
    senha = request.data.get('senha')
    nome = request.data.get('nome')

    if not (cpf and senha and nome):
        return Response({'error': 'Preencha todos os campos.'}, status=400)

    if User.objects.filter(username=cpf).exists():
        return Response({'error': 'Usuário já cadastrado.'}, status=400)

    user = User.objects.create_user(username=cpf, password=senha, first_name=nome)
    user.save()

    return Response({'message': 'Usuário cadastrado com sucesso.'})
