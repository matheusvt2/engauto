from rest_framework import generics
from .serializers import HistorySerializer
from .models import History

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect
from django.contrib import messages

import subprocess
from datetime import datetime

class History(generics.ListAPIView):
    """ 
    Api para listar o histórico de execuções.
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())

            queryset = queryset.order_by('-id')  # change is here  >> sorted with reverse order of 'id'

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


class Insert_run(generics.CreateAPIView):
    """ 
    Api para gravar a execução de uma automação.
    """

    serializer_class = HistorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        server_user = request.data["server_user"]
        server_pass = request.data["server_pass"]
        server = request.data["server"]
        script = request.data["script"]
        terminal_output =  subprocess.run(['python3',f'remediacao/scripts/{script}',server,server_user,server_pass], capture_output=True, text=True)

        try:
            request.data._mutable = True
        except:
            print("API call")
        finally:
            request.data["terminal"] = f"\\n{terminal_output.stdout}"
            request.data["terminal_error"] = f"\\n{terminal_output.stderr}"
            request.data["exectime"] = datetime.now()
            request.data["returncode"] = terminal_output.returncode
            request.data["job"] = "Remediação"

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data saved successfully','STDOUT': terminal_output.stdout,'STDERR': terminal_output.stderr })
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)