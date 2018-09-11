from django.urls import path

from registroPrincipal.views import indexView

from registroPrincipal.models import RegistroPrincipal

app_name = 'registroPrincipal'
urlpatterns = [
	path('registro/', indexView.as_view(
		model = RegistroPrincipal,
		template_name = 'base.html',
		), 
		name='index-registro'),

]