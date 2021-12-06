from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime
from django.template import Template, Context


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

# Create your views here.
def saludo(request):
    
    temas_curso=['Vistas', 'Formularios', 'Modelos', 'Despliegue']
    p1=Persona('Juan', 'Gonzalez')
    current_time = datetime.datetime.now()  
    ctx = {
            'nombre_persona':p1.nombre, 
            'apellido_persona':p1.apellido,
            'hora_actual': current_time,
            'temas': temas_curso
        }
            
    return render(request, "template1.html", ctx)

def curso_py(request):
    
    fecha_actual=datetime.datetime.now()
    
    return render(request, "curso_py.html", {"dame_fecha":fecha_actual})

def curso_c(request):
    
    fecha_actual=datetime.datetime.now()
    
    return render(request, "curso_c.html", {"dame_fecha":fecha_actual})

def despedida(request):
    
    return HttpResponse("Adios alumnos")

def dame_fecha(request):
    
    fecha_actual=datetime.datetime.now()
    documento = f"La fecha es {fecha_actual}"
    
    return HttpResponse(documento)

def calculate_age(request, actual_age, year):
    
    period = year - datetime.date.today().year
    future_age = actual_age + period  
    documento = f"Tu edad en {year} será {future_age} años"
    
    return HttpResponse(documento)
    