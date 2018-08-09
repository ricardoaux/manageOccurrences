from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from manageOccurrences.myapp.models import Occurrence
from manageOccurrences.myapp.serializers import OccurrenceSerializer, UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,)

    # API endpoint that allows users to be viewed or edited.
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['category', 'author_id']
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
        Permite atualizar a ocorrencia, caso seja administrador
        - Mudar o estado
    """
    def update(self, request, pk=None):
        if request.user.is_superuser:
            return super(OccurrenceViewSet, self).update(request, pk)

    def partial_update(self, request, pk=None):
        if request.user.is_superuser:
            return super(OccurrenceViewSet, self).partial_update(request, pk)

    """
        Apagar ocorrencia
        - Apenas para administrador ou autor
    """
    def destroy(self, request, pk=None):
        occurrence = Occurrence.objects.get(pk=pk)
        author_id = occurrence.author_id
        if request.user.is_superuser or author_id == request.user.id:
            return super(OccurrenceViewSet, self).destroy(request, pk)
