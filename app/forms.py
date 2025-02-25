
from django import forms
from django.core import validators
from .models import Pacientes

   
class Login(forms.Form):
     
    correo = forms.EmailField(required=False)
    clave = forms.CharField(label='Contraseña',required=False,widget = forms.PasswordInput())
   
    correo.widget.attrs.update({'class': 'form-control'})
    clave.widget.attrs.update({'class': 'form-control'})
    
    
class Examen(forms.Form):
    
    paciente = forms.ModelChoiceField(queryset=Pacientes.objects.all())
    nombre = forms.CharField(label="Nombre Examen")
    valor = forms.CharField(label="valor")
    fecha = forms.DateField(label='Fecha de examen:', widget=forms.SelectDateWidget(years=range(1900,2022)))
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':20}))
    
    paciente.widget.attrs.update({'class': 'form-control'})
    nombre.widget.attrs.update({'class': 'form-control'})
    valor.widget.attrs.update({'class': 'form-control'})
    fecha.widget.attrs.update({'class': 'form-control'})
    observaciones.widget.attrs.update({'class': 'form-control'})


    
    
class FormularioPacientes(forms.Form):
    nombre = forms.CharField(validators=[validators.MinLengthValidator(2,"Su nombre debe poseer mas de 2 caracteres")])
    correo =forms.EmailField()
    clave = forms.CharField(label='Contraseña',required=False,widget = forms.PasswordInput())
    rut = forms.CharField()
    edad = forms.IntegerField()
    fecha = forms.DateField()
    direccion = forms.CharField(label='Dirección')
    ocupacion = forms.CharField(label='Ocupación')
    telefono = forms.CharField(label='Telefono')
    foto = forms.CharField(label='Foto')
    resumen = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    educacion = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    historial = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    
    
    nombre.widget.attrs.update({'class': 'form-control'})
    correo.widget.attrs.update({'class': 'form-control'})
    clave.widget.attrs.update({'class': 'form-control'})
    rut.widget.attrs.update({'class': 'form-control'})
    edad.widget.attrs.update({'class': 'form-control'})
    fecha.widget.attrs.update({'class': 'form-control'})
    foto.widget.attrs.update({'class': 'form-control'})
    resumen.widget.attrs.update({'class': 'form-control'})
    ocupacion.widget.attrs.update({'class': 'form-control'})
    telefono.widget.attrs.update({'class': 'form-control'})
    direccion.widget.attrs.update({'class': 'form-control'})
    educacion.widget.attrs.update({'class': 'form-control'})
    historial.widget.attrs.update({'class': 'form-control'})
    
   
class Selectform(forms.Form):
    Perfiles = forms.ChoiceField(label=False,required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    