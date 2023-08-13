from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('employees/<int:pk>/',views.employee_detail,name="employee_detail"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
