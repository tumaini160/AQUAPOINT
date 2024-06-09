from django.urls import path
from AQUAPOINTAPP import views

urlpatterns = [
    path("", views.index, name="index"),
    path('map/', views.map, name='map'),
    path('newPoint/', views.newPoint, name='newPoint'),
    path('analytics/table-1', views.table1, name='table1'),
    path('analytics/table-2', views.table2, name='table2'),
    path('graphData', views.flow_rate_data, name='graphData'),
    # path('result_data/2/', views.fetch_result_data2, name='fetch_result_data2'),
    path('analytics/chart/', views.graph, name='graph')
]