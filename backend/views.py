
from .serializers import HistoricoSerializer
from .models import Historico
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework import generics, status
import subprocess
import datetime
from datetime import datetime, date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
import re



class ListaHistorico(generics.ListAPIView):

    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        # queryset = queryset.order_by('-id') 
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
        queryset = self.get_queryset()
        serializer = HistoricoSerializer(queryset, many=True)
        lista = serializer.data
        for i in lista:
            
            data = i['data'].replace('T', ' ')
            data = re.sub(r"[a-zA-Z]", "", data)
            data = datetime.fromisoformat(data)
            i['data'] = data.strftime('%d/%m/%Y %H:%M:%S')

        p = Paginator(lista, 5)  # creating a paginator object
        # getting the desired page number from url
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)
        # return Response(serializer.data)
        return render(request, 'frontend/historico.html', {'page_obj':page_obj})
        # return Response(serializer.data, template_name='rontend/historico.html')
        


class Insert(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    
    def post(self,request):
        servidor = request.data["servidor"]
        usuario = request.data["usuario"]
        senha = request.data["senha"]
        script = f'backend/scripts/{request.data["script"]}'

        output =  subprocess.run(['python3',script,servidor,usuario,senha], capture_output=True, text=True)

        try:
            request.data._mutable = True
        except:
            print("Except")

            
        finally:
            request.data["terminal"] = f"\\n{output.stdout}"
            request.data["error"] = f"\\n{output.stderr}"
            request.data["data"] = datetime.now()



        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response({'Status': 'Salvo com sucesso','Mensagem': output.stdout,'Erro': output.stderr })
            return render(request, 'frontend/return.html', {'status': 'Salvo com sucesso','mensagem': output.stdout,'erro': output.stderr})
        # return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        return render(request, 'frontend/return.html', {'status': status.HTTP_400_BAD_REQUEST ,'mensagem': '','erro': serializer.errors})

    
        