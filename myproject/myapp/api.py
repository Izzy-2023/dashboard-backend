# api.py
from django.http import JsonResponse
from rest_framework.views import APIView

class CandlestickData(APIView):
    def get(self, request):
        data = {
            "data": [
                {"x": "2023-01-01", "o": 30, "h": 40, "l": 25, "c": 35},
                {"x": "2023-01-02", "o": 35, "h": 45, "l": 30, "c": 40},
                # more data here
            ]
        }
        return JsonResponse(data)

class LineChartData(APIView):
    def get(self, request):
        data = {
            "labels": ["Jan", "Feb", "Mar", "Apr"],
            "data": [10, 20, 30, 40],
        }
        return JsonResponse(data)

class BarChartData(APIView):
    def get(self, request):
        data = {
            "labels": ["Product A", "Product B", "Product C"],
            "data": [100, 150, 200],
        }
        return JsonResponse(data)

class PieChartData(APIView):
    def get(self, request):
        data = {
            "labels": ["Red", "Blue", "Yellow"],
            "data": [300, 50, 100],
        }
        return JsonResponse(data)
