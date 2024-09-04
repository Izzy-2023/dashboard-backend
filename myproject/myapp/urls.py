from django.urls import path
from . import api

urlpatterns = [
    path('api/candlestick-data/', api.CandlestickData.as_view()),
    path('api/line-chart-data/', api.LineChartData.as_view()),
    path('api/bar-chart-data/', api.BarChartData.as_view()),
    path('api/pie-chart-data/', api.PieChartData.as_view()),
]
