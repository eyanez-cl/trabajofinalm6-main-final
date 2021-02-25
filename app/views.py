from .models import Examenes, Administradores, Pacientes
from typing import ContextManager
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import Login, Examen, FormularioPacientes,Selectform

# Create your views here.

def buscar(correo,clave,administradores, pacientes):
    for item in administradores:
        print("Estos son los campos obtenidos de administradores", item)
        if item['correo'] == correo and item['clave'] == clave:
            return True
        
    for item in pacientes:
        print("Estos son los campos obtenidos de pacientes", item)
        if item['correo'] == correo and item['clave'] == clave:
            return True
    
def inicio(request):
    if request.method == "GET":
        formulario = Login(request.GET)
        context = {'formulario':formulario}
    return render(request,'app/index.html',context)

def login_user(request):
    if request.method == "POST":
        formulario_lleno = Login(request.POST)
        if formulario_lleno.is_valid() == True:
            
            data = formulario_lleno.cleaned_data
            pacient = Pacientes.objects.values()
            admins = Administradores.objects.values()
            validar = buscar(data['correo'],data['clave'],admins, pacient)
            if validar == True:
                return redirect('app:private')
            else:
                formulario_lleno = Login()
                return redirect('app:inicio')               
        else:
            formulario_lleno = Login()
            return redirect('app:inicio')



def private(request):
    if request.method == "POST":
        id_usuario = request.POST.get('usuarios')
        perfiles = Pacientes.objects.values()
        for perfil in perfiles:
            if int(perfil['id'] == int(id_usuario)):
                usuario = perfil    
        return render(request,'app/Privada.html',{"perfiluser": usuario,'perfiles':perfiles})
        
            
        return redirect('app:private') ### render post de usuario
   
    elif request.method == "GET":
        formulario = Selectform(request.GET)
        perfiles = reversed(Pacientes.objects.values())
        perfilusuario = Pacientes.objects.values()
        context = {'formulario':formulario,'perfiles':perfiles,"perfiluser":perfilusuario[4]}
        return render(request,'app/Privada.html',context)
   
    
                
def graficos(request):
    
    datos = {}
    glucosa = []
    fecha_glucosa = []
    hemograma = []
    fecha_hemograma = []
    orina = []
    fecha_orina = []
    fechas = []
    
    charts = Examenes.objects.values()
    for item in charts:
        if item['nombre'] == 'glucosa':
            glucosa.append(item['valor'])
            fecha_glucosa.append(str(item['fecha']))
        elif item['nombre'] == 'orina':
            orina.append(item['valor'])
            fecha_orina.append(str(item['fecha']))
        elif item['nombre'] == 'hemograma':
            hemograma.append(item['valor'])
            fecha_hemograma.append(str(item['fecha']))
    
    
    datos['glucosa'] = glucosa
    datos['fecha_glucosa'] = fecha_glucosa
    datos['hemograma'] = hemograma
    datos['fecha_hemograma'] = fecha_hemograma     
    datos['orina'] = orina   
    datos['fecha_orina'] = fecha_orina
    return render(request,'app/Graficos.html', {'labels_glucosa':fecha_glucosa, 'labels_orina':fecha_orina, 'labels_hemograma':fecha_hemograma,'data':datos})



def agendar(request):
    return render(request,'app/Agendar.html')

def listar_examenes(request):
        examenes = Examenes.objects.all()
        context = {"lista_examenes": examenes}
        return render(request,'app/examenes/Examenes.html',context)


def crear_examen(request):
    data = dict() # pa meter cosas 
    
    if request.method == 'POST':
        formulario = Examen(request.POST)
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            datos_formulario['fecha'] = datos_formulario['fecha'].strftime("%Y-%m-%d")
            Examenes.objects.create(
                nombre = datos_formulario['nombre'],
                valor = datos_formulario['valor'],
                fecha = datos_formulario['fecha'],
                observaciones = datos_formulario['observaciones'],
                paciente = datos_formulario['paciente']
            )
            data['formulario_is_valid'] = True
            examenes = Examenes.objects.all()
            data['html_examenes_list'] = render_to_string('app/examenes/Examenes_lista_parcial.html',{
                'lista_examenes': examenes
                })      
        else:
            data['formulario_is_valid'] = False 
    else:
        formulario = Examen()
    
    context = {'formulario': formulario}
    data['html_formulario'] = render_to_string('app/examenes/Examen_parcial.html',
                                               context,
                                               request = request,)
    return JsonResponse(data)



def editar_examen(request,pk):
    data = dict() # pa meter cosas 
    if request.method == 'POST':
        formulario = Examen(request.POST)
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            datos_formulario['fecha'] = datos_formulario['fecha'].strftime("%Y-%m-%d")
            Examenes.objects.filter(id=pk).update(
                nombre = datos_formulario['nombre'],
                valor = datos_formulario['valor'],
                fecha = datos_formulario['fecha'],
                observaciones = datos_formulario['observaciones'],
                paciente = datos_formulario['paciente']
            )
            data['formulario_is_valid'] = True
            examenes = Examenes.objects.all()
            data['html_examenes_list'] = render_to_string('app/examenes/Examenes_lista_parcial.html',{
                'lista_examenes': examenes
                })      
        else:
            data['formulario_is_valid'] = False 
    else:
        examen = Examenes.objects.filter(id=pk).values()[0]
        formulario = Examen(initial=examen)
    context = {'formulario': formulario,"id":pk}
    data['html_formulario'] = render_to_string('app/examenes/Examen_parcial_actualizar.html',
                                               context,
                                               request = request,)
    return JsonResponse(data)


def eliminar_examen(request,pk):
    examen = get_object_or_404(Examenes, pk=pk)
    data = dict()
    if request.method == 'POST':
        examen.delete()
        data['formulario_is_valid'] = True
        examenes = Examenes.objects.all()
        data['html_examenes_list'] = render_to_string('app/examenes/Examenes_lista_parcial.html',{
                'lista_examenes': examenes
                })      
    else:
        context = {'examen': examen}
        data['html_formulario'] = render_to_string('app/examenes/Eliminar_examen_parcial.html',
            context,
            request=request,
        )
    return JsonResponse(data)
            


def context_lista_pacientes():
    
    pacientes = Pacientes.objects.values()
    context= {'lista_pacientes': pacientes}
    print(context)
    return context

            
def agregar_usuario_db(request):
    
    if request.method == 'GET':
        formulario = FormularioPacientes()
        context = {'formulario': formulario}
        pacientes = Pacientes.objects.all()
        context={ 'formulario': formulario,
                 'lista_pacientes': pacientes}
        print(context)
        return render(request,'app/agregar_usuario_db.html',context)

    elif request.method == 'POST':
       
        
        formulario_devuelto = FormularioPacientes(request.POST)
        
        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            datos_formulario['fecha']= datos_formulario['fecha'].strftime("%Y-%m-%d")
            
            Pacientes.objects.create(nombre= datos_formulario['nombre'],
                                    correo= datos_formulario['correo'],
                                    clave= datos_formulario['clave'],
                                    rut= datos_formulario['rut'],
                                    edad = datos_formulario['edad'],
                                    fecha = datos_formulario['fecha'],
                                    direccion= datos_formulario['direccion'],
                                    ocupacion= datos_formulario['ocupacion'],
                                    telefono = datos_formulario['telefono'],
                                    foto = datos_formulario['foto'],
                                    resumen= datos_formulario['resumen'],
                                    educacion = datos_formulario['educacion'],
                                    historial = datos_formulario['historial'],
                                
                                    )
                
            return redirect('app:agregar_usuario_db')
             
        else:
            context= {'formulario': formulario_devuelto}
            context.update(context_lista_pacientes())
            return render(request, 'app/agregar_usuario_db.html', context)
        

    
def eliminar_pacientes_db(request, rut):
    
    if request.method == 'GET':
        context = {'rut': rut}
        return render(request, 'app/eliminar_pacientes_db.html', context)
    
    if request.method == 'POST':
        Pacientes.objects.filter(rut = rut).delete()
        
        return redirect('app:agregar_usuario_db')
    
    
def editar_paciente_db(request, rut):
    
    if request.method == 'GET':
        paciente= Pacientes.objects.filter(rut = rut).values()[0]
        
        formulario = FormularioPacientes(initial=paciente)
        context = {'formulario':formulario, 'rut': rut}
        return render( request, 'app/editar_paciente_db.html', context)
    
    elif request.method == 'POST':
        formulario_devuelto = FormularioPacientes(request.POST)
        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            datos_formulario['fecha']=datos_formulario['fecha'].strftime("%Y-%m-%d")
            paciente = Pacientes.objects.filter(rut=rut).update(
                                    nombre= datos_formulario['nombre'],
                                    correo= datos_formulario['correo'],
                                    clave= datos_formulario['clave'],
                                    rut= datos_formulario['rut'],
                                    edad = datos_formulario['edad'],
                                    fecha = datos_formulario['fecha'],
                                    direccion= datos_formulario['direccion'],
                                    ocupacion= datos_formulario['ocupacion'],
                                    telefono = datos_formulario['telefono'],
                                    foto = datos_formulario['foto'],
                                    resumen= datos_formulario['resumen'],
                                    educacion = datos_formulario['educacion'],
                                    historial = datos_formulario['historial']
                                    )
            return redirect('app:agregar_usuario_db')
        else:
            context = {'formulario': formulario_devuelto}
            return render ( request, 'app/editar_paciente_db.html', context)
        
        
def eliminar_pacientes_db(request, rut):
    
    if request.method == 'GET':
        context = {'rut': rut}
        return render(request, 'app/eliminar_pacientes_db.html', context)
    
    if request.method == 'POST':
        Pacientes.objects.filter(rut = rut).delete()
        
        return redirect('app:agregar_usuario_db')