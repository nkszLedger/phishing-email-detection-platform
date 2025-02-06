from django.db import models

# Dataset 1: process_data
class FirstDataset(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    email_to = models.TextField(null=True, blank=True)
    email_from = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

# Dataset 2: messages
class SecondDataset(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    label = models.CharField(null=True, blank=True)

# Dataset 3: Merged Dataset 1 and Dataset 2
class Mailbox(models.Model):
    id = models.BigAutoField(primary_key=True)
    email_to = models.TextField(null=True, blank=True)
    email_from = models.TextField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    label = models.CharField(null=True, blank=True)
    model_cnn_confidence = models.FloatField(null=True, blank=True)
    model_lstm_rnn_confidence = models.FloatField(null=True, blank=True)
    model_gru_rnn_confidence = models.FloatField(null=True, blank=True)
    model_hybrid_cnn_lstm_rnn_confidence = models.FloatField(null=True, blank=True)
    model_hybrid_cnn_gru_rnn_confidence = models.FloatField(null=True, blank=True)