from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'phishdetector'

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.index, name='index'),
    path('api/affected_accounts/', views.affected_accounts, name='affected_accounts')
]

if not bool(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
