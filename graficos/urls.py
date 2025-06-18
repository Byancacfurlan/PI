from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('adm/', views.adm, name='adm'),
    path('ads/', views.ads, name='ads'),
    path('ped/', views.ped, name='ped'),
    path('prg/', views.prg, name='prg'),
    path('diversos/', views.diversos, name='diversos'),
    path('login/', views.login_view, name='login'),

] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

