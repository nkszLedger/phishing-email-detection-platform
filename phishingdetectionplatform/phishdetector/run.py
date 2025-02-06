import psycopg2
import os
import numpy as np
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# PostgreSQL connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': '127.0.0.1',
    'port': '5432',
}

# Connect to PostgreSQL database
def connect_to_database():
    try:
        connection = psycopg2.connect(**db_params)
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None

# Retrieve saved models
def get_model(filename):
    return tf.saved_model.load(filename)

def update_predictions(cursor, id, column_name, prediction):

    if column_name == 'model_cnn_confidence':
        query = "UPDATE public.phishdetector_mailbox SET model_cnn_confidence="+str(prediction)+" WHERE id="+str(id)+";"
        cursor.execute(query)
    elif column_name == 'model_gru_rnn_confidence':
        query = "UPDATE public.phishdetector_mailbox SET model_gru_rnn_confidence="+str(prediction)+" WHERE id="+str(id)+";"
        cursor.execute(query)
    elif column_name == 'model_lstm_rnn_confidence':
        query = "UPDATE public.phishdetector_mailbox SET model_lstm_rnn_confidence="+str(prediction)+" WHERE id="+str(id)+";"
        cursor.execute(query)
    elif column_name == 'model_hybrid_cnn_gru_rnn_confidence':
        query = "UPDATE public.phishdetector_mailbox SET model_hybrid_cnn_gru_rnn_confidence="+str(prediction)+" WHERE id="+str(id)+";"
        cursor.execute(query)
    elif column_name == 'model_hybrid_cnn_lstm_rnn_confidence':
        query = "UPDATE public.phishdetector_mailbox SET model_hybrid_cnn_lstm_rnn_confidence="+str(prediction)+" WHERE id="+str(id)+";"
        cursor.execute(query)


def run_all_predictions():
    MAX_WORDS = 10000
    MAX_LENGTH = 200
    TOKENIZER = Tokenizer(num_words=MAX_WORDS)
    MODEL_EXP_01 = get_model('experiment-01-cnn')
    MODEL_EXP_02 = get_model('experiment-02-gru-rnn')
    MODEL_EXP_03 = get_model('experiment-02-lstm-rnn')
    MODEL_EXP_04 = get_model('experiment-03-cnn-gru-rnn')
    MODEL_EXP_05 = get_model('experiment-03-cnn-lstm-rnn')

    model_list = {
        'model_cnn_confidence': MODEL_EXP_01, 
        'model_gru_rnn_confidence': MODEL_EXP_02,
        'model_lstm_rnn_confidence': MODEL_EXP_03,
        'model_hybrid_cnn_gru_rnn_confidence': MODEL_EXP_04,
        'model_hybrid_cnn_lstm_rnn_confidence':MODEL_EXP_05
    }

    # Retrieve all messages
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT id, message FROM phishdetector_mailbox WHERE id>=102;"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    # for i in range(len(data)):
    #     # id [0] and messages [1]
    #     print("\n", data[i][1], "\n")
    
    #print("\n", all_messages[0]['message'],"\n")

    connection = connect_to_database()
    cursor = connection.cursor()

    for i in range(len(data)):
        # print("\nProcessing Incident: ", data[i][0],"\n")
        if data[i][1] is not None:
            TOKENIZER.fit_on_texts(data[i][1])
            x = pad_sequences(TOKENIZER.texts_to_sequences(data[i][1]), maxlen=MAX_LENGTH)
        
            # test models
            for key, value in model_list.items():
                prediction = round(np.mean(value.serve(x)), 4)
                #print("Incident ID: ", row['id'], "\n")
                if data[i][0] is not None:
                    update_predictions(cursor, data[i][0], key, prediction)
                    connection.commit()
                
                # if prediction < 0.5:
                #     # print(f"\n--> The text is Benign (Confidence: {(1-prediction)*100:.3f}%)")
                #     confidence = round((1-prediction)*100,4)
                #     # Update tables
                #     update_predictions(cursor, data[i][0], key, confidence)
                #     connection.commit()
                # else:
                #     # print(f"\n--> The text is Phishing (Confidence: {(prediction)*100:.3f}%)")
                #     confidence = round((prediction)*100,4)
                #     # Update tables
                #     update_predictions(cursor, data[i][0], key, confidence)
                #     connection.commit()

    cursor.close()
    connection.close()

    
# Main script
def main():
    print("Predictions Started...")
    run_all_predictions()
    print("Predictions Completed")

if __name__ == "__main__":
    main()