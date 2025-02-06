from django.apps import AppConfig
import threading
import time

class PhishdetectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phishdetector'

    # def ready(self):
    #     """ Start the background thread when Django starts """
    #     from phishdetector.tasks import start_prediction_thread
        
    #     prediction_start_time = time.time()
    #     if threading.main_thread().is_alive():  # Prevent multiple threads
    #         start_prediction_thread()
    #     prediction_end_time = time.time()
    #     duration = round(prediction_end_time - prediction_start_time, 4)
    #     print("PhishdetectorConfig.ready(): Background prediction thread complete.")
    #     print(f"PhishdetectorConfig.ready(): Prediction thread took [{duration}] seconds to complete.")