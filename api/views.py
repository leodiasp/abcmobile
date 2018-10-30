from django.shortcuts import render, redirect

from rest_framework.decorators import api_view

from rest_framework import generics, status
from rest_framework.response import Response
from portal.models import User, Responsavel

from .serializers import UserSerializer, ResponsavelSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import mixins

# Create your views here.

def login_form(request):
    return redirect('acesso.html')
    #return render(request,'templates/acesso.html', {})



# class ResponsavelList(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Responsavel.objects.all()
#     serializer_class = ResponsavelSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class ResponsavelList(generics.ListCreateAPIView):
#
#     # snippets = Snippet.objects.all()
#     # serializer = SnippetSerializer(snippets, many=True)
#     # return Response(serializer.data)
#     #
#
#     queryset = Responsavel.objects.all()
#     serializer_class = ResponsavelSerializer(queryset)
#
#     return Response(serializer_class.data)
#
#     #return Response(serializer_class.data)


@api_view(['GET', 'POST'])
def ResponsavelList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        responsavel = Responsavel.objects.all()
        serializer = ResponsavelSerializer(responsavel, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = User.objects.all()
    #queryset = User.objects.filter(pk=pk)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)