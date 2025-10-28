from django.shortcuts import render

# Create your views here.
def home(request):
    tasks = [
    {"title": "Aprender los fundamentos de Django", "completed": True},
    {"title": "Configurar el entorno de desarrollo", "completed": True},
    {"title": "Crear el modelo Task", "completed": False},
    {"title": "Hacer las migraciones de la base de datos", "completed": False},
    {"title": "Registrar el modelo en el admin de Django", "completed": False},
    {"title": "Diseñar la plantilla base HTML", "completed": False},
    {"title": "Estilizar la lista de tareas con CSS", "completed": False},
    {"title": "Crear formulario para añadir nuevas tareas", "completed": False},
    {"title": "Implementar funcionalidad para marcar como completada", "completed": False},
    {"title": "Añadir validación a los formularios", "completed": False},
    {"title": "Probar la aplicación en diferentes navegadores", "completed": False},
    {"title": "Hacer commit de los cambios en Git", "completed": True},
    {"title": "Subir el proyecto a GitHub", "completed": True},
    {"title": "Documentar el proceso de desarrollo", "completed": False},
    {"title": "Aprender sobre vistas basadas en clases", "completed": False},
    {"title": "Explorar el uso de Django REST Framework", "completed": False},
    {"title": "Investigar integración con algoritmos de ML", "completed": False},
    {"title": "Diseñar la arquitectura del sistema de recomendación", "completed": False},
    {"title": "Preparar el portafolio para mostrar este proyecto", "completed": False},
    {"title": "Compartir el proyecto en LinkedIn", "completed": False},
]
    return render(request, "tasks/home.html", {'tasks':tasks})