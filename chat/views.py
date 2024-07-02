from rest_framework import generics

from rest_framework.views import APIView

from rest_framework.response import Response

from chat.models import Chat


# Create your views here.


class ChatApiView(APIView):
    def get(self, request):
        lst = Chat.objects.all()
        return Response({"message": "Hello from get method!", "data": list(lst)})

    def post(self, request):
        return Response({"message": "Hello from post method!", "data": Chat.objects.all()})
