from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import DepartamentoSerializer, PropietarioSerializer, UserSerializer,GroupSerializer
# importar las clases de models.py
from administrativo.models import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropietarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        """
        valor = self.request.query_params
        print(valor)
        if 'nombre' in valor.keys():
            return Propietario.objects.filter(nombre=valor['nombre']).all()
        else:
            if 'nacionalidad' in valor.keys():
                return Propietario.objects.filter(correo__contains=valor['nacionalidad']).all()
            else:
                return Propietario.objects.all()


class DepartamentoViewSet(viewsets.ModelViewSet):
# class DepartamentoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    # permission_classes = [permissions.IsAuthenticated]
