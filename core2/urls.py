from django.conf.urls import url
from core2.views import home,lista,novo

urlpatterns = [
    url(r'^$',home),
    url(r'^lista-todos/$',lista, name='lista_todos'),
    url(r'^novo/$',novo),
]