
from django.contrib import admin
from django.urls import path
from . import views  # Correct the import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', views.send_email, name='send_email'),  # Use send_email directly
]

