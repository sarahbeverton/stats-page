from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from django.conf import settings
import os


class LoginView(APIView):
    def post(self, request):
        print("logging in")
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data.get('username'),
            password=serializer.validated_data.get('password')
        )
        print(user)

        if user is not None:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class StatsView(APIView):
    def get(self, request):
        botometer_file_path = os.path.join(settings.BASE_DIR, 'stats_page', 'static', 'data', 'botometer_stats')
        request_counts_dir = os.path.join(settings.BASE_DIR, 'stats_page', 'static', 'data', 'request_counts_logs')
        tweetcount_dir = os.path.join(settings.BASE_DIR, 'stats_page', 'static', 'data', 'tweetcount')

        stats_data = {}

        # Read Botometer stats data
        if os.path.exists(botometer_file_path):
            with open(botometer_file_path, 'r') as file:
                stats_data['botometer_stats'] = file.read()
        else:
            return Response({'status': 'error', 'message': 'Botometer data not found'}, status=status.HTTP_404_NOT_FOUND)

        # Read files from request counts
        if os.path.exists(request_counts_dir):
            stats_data['request_counts'] = {}
            for filename in os.listdir(request_counts_dir):
                file_path = os.path.join(request_counts_dir, filename)
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        stats_data['request_counts'][filename] = file.read()
        else:
            return Response({'status': 'error', 'message': 'Request counts data not found'}, status=status.HTTP_404_NOT_FOUND)


        # Read files from tweetcounts
        if os.path.exists(tweetcount_dir):
            stats_data['tweetcounts'] = {}
            for filename in os.listdir(tweetcount_dir):
                file_path = os.path.join(tweetcount_dir, filename)
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        stats_data['tweetcounts'][filename] = file.read()
        else:
            return Response({'status': 'error', 'message': 'Tweetcount data not found'}, status=status.HTTP_404_NOT_FOUND)

        if not stats_data:
            return Response({'status': 'error', 'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(stats_data)
