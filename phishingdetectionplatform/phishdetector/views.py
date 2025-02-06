from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .serializer import MailboxSerializer

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def index(request):
    total_emails_count = Mailbox.objects.count()
    total_flagged_emails = Mailbox.objects.filter(label='1').count()
    total_benign_emails = Mailbox.objects.filter(label='0').count()
    total_emails_flagged_by_model = Mailbox.objects.filter(model_cnn_confidence__gte=70).count()

    context = {
        'total_emails_count': total_emails_count,
        'total_flagged_emails': total_flagged_emails,
        'total_benign_emails': total_benign_emails,
        'total_emails_flagged_by_model': total_emails_flagged_by_model,
    }

    return render(request, 'base.html', {'context': context})

@api_view(['GET'])
def affected_accounts(request):
    emails = Mailbox.objects.filter(model_cnn_confidence__gte=50)
    serializer = MailboxSerializer(emails, many=True)

    return Response(serializer.data)