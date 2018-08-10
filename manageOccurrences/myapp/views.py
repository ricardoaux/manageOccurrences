from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from manageOccurrences.myapp.models import Occurrence
from manageOccurrences.myapp.serializers import OccurrenceSerializer, UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from django.core.exceptions import PermissionDenied


class UserViewSet(viewsets.ModelViewSet):
    # Apenas o administrador tem permissoes para ver e editar os utilizadores
    permission_classes = (permissions.IsAdminUser,)

    """
        Permite ver e editar todos os utilizadores do sistema
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    # Permite filtras os resultados. Neste caso pela categoria e pelo autor
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['category', 'author']
    read_only_fields = []

    """
        Listar todas as ocorrencias
    """
    def list(self, request):
        return super(OccurrenceViewSet, self).list(request)

    """
        Criar uma ocorrencia
    """
    def create(self, request):
        data = request.data
        # remember old state
        _mutable = data._mutable
        # set to mutable
        data._mutable = True
        # Adicionar o utilizador atual como autor e o estado Por Validar
        data['author'] = request.user.id
        data['state'] = "POR VALIDAR"
        # set mutable flag back
        data._mutable = _mutable
        serializer = OccurrenceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        super(OccurrenceViewSet, self).perform_create(serializer)
        headers = super(OccurrenceViewSet, self).get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    """
        Listar determinada ocorrencia
    """
    def retrieve(self, request, pk=None):
        return super(OccurrenceViewSet, self).retrieve(request, pk)

    """
        Permite atualizar a ocorrencia
        - Mudar o estado
        - Requer permissão de administrador
    """
    def update(self, request, pk=None):
        if request.user.is_superuser:
            return super(OccurrenceViewSet, self).update(request, pk)
        else:
            raise PermissionDenied

    def partial_update(self, request, pk=None):
        if request.user.is_superuser:
            return super(OccurrenceViewSet, self).partial_update(request, pk)
        else:
            raise PermissionDenied

    """
        Apagar ocorrencia
        - Apenas para administrador ou autor
    """
    def destroy(self, request, pk=None):
        occurrence = Occurrence.objects.get(pk=pk)
        author_id = occurrence.author_id
        if request.user.is_superuser or author_id == request.user.id:
            return super(OccurrenceViewSet, self).destroy(request, pk)
        else:
            raise PermissionDenied
