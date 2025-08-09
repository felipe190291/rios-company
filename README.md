# Proyecto Desierto

## Descripción

Este es un proyecto desarrollado con Django que sirve como plataforma para [breve descripción del propósito del proyecto].

## 🚀 Características

- Gestión de clientes
- [Otras características principales]
- [Otras características principales]

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes)
- SQLite (desarrollo) / PostgreSQL (producción)

## 🛠️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/felipe190291/rios-company.git
   cd desierto
   ```

2. **Crear y activar entorno virtual:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuración del entorno:**
   - Copiar el archivo `.env.example` a `.env`
   - Configurar las variables de entorno según sea necesario

5. **Aplicar migraciones:**
   ```bash
   python manage.py migrate
   ```

6. **Crear superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   El sitio estará disponible en http://127.0.0.1:8000/

## 🌐 Despliegue en Producción

1. Configurar base de datos PostgreSQL
2. Configurar variables de entorno de producción
3. Configurar Gunicorn como servidor WSGI
4. Configurar Nginx como proxy inverso
5. Configurar Whitenoise para archivos estáticos



## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, lee nuestras pautas de contribución antes de enviar pull requests.

