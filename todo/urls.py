from django.urls import path
from todo import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:id>',views.deletetodo,name='deletetodo')
] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)