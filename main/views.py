from django.shortcuts import render
from main.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.serializers import UserSerializer

class UserUpdate(APIView):
    def post(self, request):
        try:
            data = {**request.data}
            user = request.user
            user_data = User.objects.filter(npm=str(data["npm"]))
            user_data = user_data.first()
            serializer = UserSerializer(user_data, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'user tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
