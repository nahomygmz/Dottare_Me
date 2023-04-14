from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from .forms import ContactoForm
from .forms import DonacionForm
from django.conf import settings
from django.http import FileResponse, Http404
from django.templatetags.static import static
from django.urls import reverse

import paypalrestsdk
import os


def home (request):
    return render(request, 'home.html')
def adoptar(request):
   
    return render(request, 'adoptar.html')

def buscar_resultados(request):
    query = request.GET.get('busqueda')
    tipo = request.GET.get('tipo')

    # Filtro los animales según los parámetros de búsqueda
    if query:
        resultados = Animal.objects.filter(Nombre__icontains=query, Tipo=tipo)
    else:
        resultados = Animal.objects.filter(Tipo=tipo)

    # Renderizo la plantilla con los resultados
    return render(request, 'busqueda_resultados.html', {'resultados': resultados})

def error (request):
    return render(request, 'error.html')

#Info de animal específico
def perfil_animal(request):
    return render(request, 'perfil_animal.html')

#* * * * * * C O M O   A D O P T A R * * * * * *
def como_adoptar(request):
    pdf_url = static('PDF/Requisitos-esenciales-para-adoptar-un-animal.pdf')
    pdf_url2 = static('PDF/Siete-factores-importantes-a-considerar-antes-de-adoptar-un-animal.pdf')
    context = {
        'pdf_url': pdf_url,
        'pdf_url2': pdf_url2
    }
    return render(request, 'como_adoptar.html', context)

#Función para descargar los archivos pdf
def download_file(request, file_name):
    # obtén la ruta completa del archivo
    file_path = os.path.join(settings.STATIC_ROOT, 'PDF', file_name)
    # abre el archivo en modo lectura binaria
    with open(file_path, 'rb') as f:
        # crea una respuesta de archivo para descargar el archivo
        response = FileResponse(f, as_attachment=True, filename=file_name)
        return response

def about (request):
    return render(request, 'about.html')

#* * * * * * D O N A C I Ó N * * * * * *
#Importar las credenciales del API de PAYPAL desde settings.py
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

def donacion(request):
    if request.method == 'POST':
        form = DonacionForm(request.POST)
        if form.is_valid():
            # Procesar la información del formulario y crear una transacción de PayPal
            monto = form.cleaned_data['Monto']
            pago = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "redirect_urls": {
                    "return_url": "http://localhost:8000/donacion/",
                    "cancel_url": "http://localhost:8000/donacion/"
                },
                "transactions": [{
                    "amount": {
                        "total": str(monto),
                        "currency": "USD"
                    },
                    "description": "Donación"
                }]
            })

            # Crear el pago en PayPal y redirigir al usuario a la página de confirmación de PayPal
            if pago.create():
                form.save() # Guardar el formulario en la base de datos
                for link in pago.links:
                    if link.method == "REDIRECT":
                        return redirect(link.href)
            else:
                return render(request, 'error.html', {'error': 'No se pudo procesar el pago'})

    else:
        form = DonacionForm()

    return render(request, 'donacion.html', {'form': form})

# * * * * * * C O N T A C T O * * * * * *

def contacto(request):
    form = ContactoForm()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')

    return render(request, 'contacto.html', {'form': form})