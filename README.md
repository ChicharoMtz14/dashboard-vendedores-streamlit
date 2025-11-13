# Dashboard de Vendedores - Streamlit

Aplicación web desarrollada con Streamlit para visualizar y analizar datos de vendedores.

## Descripción

Este proyecto es un dashboard interactivo que permite:
- Visualizar una tabla de vendedores filtrable por región
- Mostrar gráficas de unidades vendidas, ventas totales y porcentajes de ventas
- Consultar información detallada de vendedores específicos

## Autor

**Estudiante:** César Manuel Martínez Soto  
**Matrícula:** A01280550  
**Concentración:** Analítica de Datos e Inteligencia Artificial  
**Institución:** Tecnológico de Monterrey  
**Semestre:** Agosto-Diciembre 2025

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/ChicharoMtz14/dashboard-vendedores-streamlit.git
cd dashboard-vendedores-streamlit
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar la aplicación:
```bash
streamlit run app_vendedores.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## Archivos del Proyecto

- `app_vendedores.py` - Código principal de la aplicación Streamlit
- `vendedores.xlsx` - Archivo de datos con información de vendedores
- `requirements.txt` - Dependencias de Python necesarias

## Dependencias

- streamlit >= 1.28.0
- pandas >= 2.0.0
- openpyxl >= 3.1.0
- matplotlib >= 3.7.0

## Características

- Tabla filtrable por región
- Gráficas de unidades vendidas
- Gráficas de ventas totales
- Gráficas de porcentajes de ventas
- Búsqueda de vendedor específico
- Interfaz intuitiva y responsiva

## Despliegue en Streamlit Cloud

Esta aplicación está desplegada en Streamlit Cloud. Puedes acceder a ella en:
https://share.streamlit.io/user/chicharomtz14
