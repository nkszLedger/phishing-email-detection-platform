import threading
import time
import os
from django.conf import settings
import numpy as np
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from phishdetector.models import Mailbox
from pathlib import Path

# Signal event for stopping thread
stop_event = threading.Event()

# Load models dynamically
APP_DIR = Path(__file__).resolve().parent

# Retrieve saved models
def get_model(filename):
    return tf.saved_model.load(filename)

def run_model_predictions():
    MAX_WORDS = 10000
    MAX_LENGTH = 200
    TOKENIZER = Tokenizer(num_words=MAX_WORDS)
    
    # Load models once per task execution
    models = {
        "cnn": get_model(os.path.join(APP_DIR, "models","experiment-01-cnn")),
        "gru": get_model(os.path.join(APP_DIR, "models","experiment-02-gru-rnn")),
        "lstm": get_model(os.path.join(APP_DIR, "models","experiment-02-lstm-rnn")),
        "cnn_gru": get_model(os.path.join(APP_DIR, "models","experiment-03-cnn-gru-rnn")),
        "cnn_lstm": get_model(os.path.join(APP_DIR, "models","experiment-03-cnn-lstm-rnn"))
    }
    print("phishdetector.tasks.run_model_predictions(): Models loaded. Starting background processing...")

    while not stop_event.is_set():
        emails = Mailbox.objects.filter(id__lt=200)
        for item in emails:
            message = item.message
            if message:
                TOKENIZER.fit_on_texts([message])
                message_padded_sequences = pad_sequences(TOKENIZER.texts_to_sequences([message]), maxlen=MAX_LENGTH)
                
                # Run model predictions
                predictions = {}
                for name, model in models.items():
                    prediction = np.mean(model.serve(message_padded_sequences))
                    confidence = 0.0000
                    if prediction < 0.5:
                        confidence = round((1 - prediction) * 100, 4)
                    else:
                        confidence = round(prediction * 100, 4)
                    predictions[name] = confidence

                # Save predictions to database
                item.model_cnn_confidence = predictions["cnn"]
                item.model_gru_rnn_confidence = predictions["gru"]
                item.model_lstm_rnn_confidence = predictions["lstm"]
                item.model_hybrid_cnn_gru_rnn_confidence = predictions["cnn_gru"]
                item.model_hybrid_cnn_lstm_rnn_confidence = predictions["cnn_lstm"]
                item.save()
        
            time.sleep(5)  # Run every 5 seconds
        stop_prediction_thread()

# Start the background thread
def start_prediction_thread():
    thread = threading.Thread(target=run_model_predictions(), daemon=False)
    thread.start()
    print("phishdetector.tasks.start_prediction_thread(): Background prediction thread started.")

# Stop the background thread gracefully
def stop_prediction_thread():
    stop_event.set()
    print("phishdetector.tasks.stop_prediction_thread(): Stop signal sent. Waiting for thread to exit...")
