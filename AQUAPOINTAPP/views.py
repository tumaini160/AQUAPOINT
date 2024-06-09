from django.http import JsonResponse
from django.shortcuts import redirect, render 
from .models import Table1, Table2
import random
from django.contrib import messages
from collections import defaultdict
from firebase_admin import db

def index(request):
    return render(request, 'home/index.html')

def graph(request):
    return render(request, 'home/graph.html')

def map(request):
    data_points = Table1.objects.all()
    return render(request, 'home/map.html', {'data_points': data_points})

def table1(request):
    results_data1 = Table1.objects.all()
    return render(request, 'home/table1.html', {'result_data1': results_data1})
def table2(request):
    results_data1 = Table2.objects.all()
    return render(request, 'home/table2.html', {'result_data1': results_data1})

def newPoint(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            number = request.POST['number']
            coordinates = request.POST['coordinates']
            
            pointData = Table1(
                Name = name,
                Number = number,
                Coordinates = coordinates,
            )
            pointData.save()  
            
            messages.success(request, 'Success! Water Point Details Registered')
            return redirect('index')  # Redirect to the home page
            
        except Exception as e:
            print(f"Error: {e}")
            return render(request, 'home/error.html', {'error': str(e)})
   

def fetch_and_store_data():
    try:
        # Reference to the Firebase Realtime Database
        # ref = db.reference('/flowRate')

        # # Fetch the latest posted data
        # latest_data = ref.order_by_key().limit_to_last(1).get()
        water_points = Table1.objects.values_list('Coordinates', flat=True)
        sensorData = 10
        # water_points = ['point1', 'point2', 'point3', 'point4', 'point5']  # Add more points as needed
        for point in water_points:
                unique_flow = sensorData * (1 + random.uniform(-0.05, 0.05))  # Adding a small random variation
                Table2.objects.create(Coordinates=point, SensorValue=unique_flow)
        
        print('data sent')

    except Exception as e:
        print(f"Error: {e}")

def flow_rate_data(request):
    flow_rates = Table2.objects.all().order_by('Date')
    data = defaultdict(list)
    
    for entry in flow_rates:
        data['labels'].append(entry.Date.strftime('%H:%M'))
        data[entry.Coordinates].append(entry.SensorValue)
    
    datasets = []
    colors = [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
    ]
    
    for i, (Coordinates, SensorValue) in enumerate(data.items()):
        if Coordinates != 'labels':
            datasets.append({
                'label': Coordinates,
                'data': SensorValue,
                'borderColor': colors[i % len(colors)],
                'borderWidth': 1,
                'fill': True
            })
    
    return JsonResponse({'labels': data['labels'], 'datasets': datasets})
