from rest_framework import serializers
from .models import Mailbox

class MailboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = ['id', 'email_to', 'email_from']