from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from .views import fetch_and_store_data

def start():    
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'default')

    # Assuming 'sensor_data_updated' is the trigger event from Firebase
    scheduler.add_job(
        fetch_and_store_data,
        trigger='interval',
        hours = 1,  # Set the interval to your preference
        name='map_sensor_data',
        replace_existing=True
    )
    scheduler.start()
