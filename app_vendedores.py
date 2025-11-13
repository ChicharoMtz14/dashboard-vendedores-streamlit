import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Dashboard de Vendedores", layout="wide")

# Título principal de la aplicación
st.title("Dashboard de Vendedores")

# Información del estudiante
st.markdown("**Estudiante:** César Manuel Martínez Soto  |  **Matrícula:** A01280550")
st.markdown("---")

# Cargar los datos desde el archivo Excel
# Leemos el archivo vendedores.xlsx
try:
    df = pd.read_excel('vendedores.xlsx')
    st.success("Datos cargados correctamente")
except FileNotFoundError:
    st.error("No se encontró el archivo vendedores.xlsx")
    st.stop()

# Mostrar información básica del dataset
st.sidebar.header("Información")
st.sidebar.write(f"Total de vendedores: {len(df)}")
st.sidebar.write(f"Total de regiones: {df['REGION'].nunique()}")

# ============================================
# SECCIÓN 1: TABLA FILTRABLE POR REGIÓN
# ============================================
st.header("Tabla de Vendedores")

# Crear un contenedor para el filtro
with st.container():
    # Selector de región para filtrar la tabla
    regiones = ['Todas'] + sorted(df['REGION'].unique().tolist())
    region_seleccionada = st.selectbox(
        "Filtrar por Región:",
        regiones,
        key="filtro_region"
    )
    
    # Aplicar el filtro según la región seleccionada
    if region_seleccionada == 'Todas':
        df_filtrado = df.copy()
    else:
        df_filtrado = df[df['REGION'] == region_seleccionada]
    
    # Mostrar la tabla filtrada
    st.dataframe(df_filtrado, use_container_width=True, height=300)
    
    # Mostrar estadísticas del filtro aplicado
    st.caption(f"Mostrando {len(df_filtrado)} vendedor(es)")

# Separador visual
st.divider()

# ============================================
# SECCIÓN 2: GRÁFICAS
# ============================================
st.header("Gráficas de Ventas")

# Crear tres columnas para las gráficas
col1, col2, col3 = st.columns(3)

# Gráfica 1: Unidades Vendidas
with col1:
    st.subheader("Unidades Vendidas")
    # Agrupamos por región y sumamos las unidades vendidas
    unidades_por_region = df.groupby('REGION')['UNIDADES VENDIDAS'].sum().sort_values(ascending=False)
    st.bar_chart(unidades_por_region)

# Gráfica 2: Ventas Totales
with col2:
    st.subheader("Ventas Totales")
    # Agrupamos por región y sumamos las ventas totales
    ventas_por_region = df.groupby('REGION')['VENTAS TOTALES'].sum().sort_values(ascending=False)
    st.bar_chart(ventas_por_region)

# Gráfica 3: Porcentajes de Ventas
with col3:
    st.subheader("Porcentajes de Ventas")
    # Agrupamos por región y calculamos el promedio de porcentajes
    porcentajes_por_region = df.groupby('REGION')['PORCENTAJE DE VENTAS'].mean().sort_values(ascending=False)
    st.bar_chart(porcentajes_por_region)

# Gráficas adicionales en fila completa
st.subheader("Comparación Detallada")

# Gráfica de líneas para comparar tendencias
col_a, col_b = st.columns(2)

with col_a:
    st.write("**Unidades Vendidas por Vendedor (Top 10)**")
    # Ordenamos por unidades vendidas y tomamos los top 10
    top_unidades = df.nlargest(10, 'UNIDADES VENDIDAS')[['NOMBRE', 'APELLIDO', 'UNIDADES VENDIDAS']]
    top_unidades['Nombre Completo'] = top_unidades['NOMBRE'] + ' ' + top_unidades['APELLIDO']
    st.bar_chart(top_unidades.set_index('Nombre Completo')['UNIDADES VENDIDAS'])

with col_b:
    st.write("**Ventas Totales por Vendedor (Top 10)**")
    # Ordenamos por ventas totales y tomamos los top 10
    top_ventas = df.nlargest(10, 'VENTAS TOTALES')[['NOMBRE', 'APELLIDO', 'VENTAS TOTALES']]
    top_ventas['Nombre Completo'] = top_ventas['NOMBRE'] + ' ' + top_ventas['APELLIDO']
    st.bar_chart(top_ventas.set_index('Nombre Completo')['VENTAS TOTALES'])

# Separador visual
st.divider()

# ============================================
# SECCIÓN 3: DATOS DE VENDEDOR ESPECÍFICO
# ============================================
st.header("Datos de Vendedor Específico")

# Crear un contenedor para la búsqueda de vendedor
with st.container():
    # Crear lista de nombres completos para el selector
    df['Nombre Completo'] = df['NOMBRE'] + ' ' + df['APELLIDO']
    nombres_completos = sorted(df['Nombre Completo'].unique().tolist())
    
    # Selector de vendedor
    vendedor_seleccionado = st.selectbox(
        "Selecciona un vendedor:",
        nombres_completos,
        key="selector_vendedor"
    )
    
    # Filtrar datos del vendedor seleccionado
    vendedor_data = df[df['Nombre Completo'] == vendedor_seleccionado].iloc[0]
    
    # Mostrar los datos del vendedor en columnas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Región", vendedor_data['REGION'])
        st.metric("ID", int(vendedor_data['ID']))
    
    with col2:
        st.metric("Unidades Vendidas", int(vendedor_data['UNIDADES VENDIDAS']))
        st.metric("Ventas Totales", f"${vendedor_data['VENTAS TOTALES']:,.2f}")
    
    with col3:
        st.metric("Porcentaje de Ventas", f"{vendedor_data['PORCENTAJE DE VENTAS']*100:.2f}%")
        st.metric("Salario", f"${vendedor_data['SALARIO']:,.2f}")
    
    with col4:
        st.write("**Información Personal**")
        st.write(f"**Nombre:** {vendedor_data['NOMBRE']}")
        st.write(f"**Apellido:** {vendedor_data['APELLIDO']}")

# Pie de página
st.divider()
st.caption("Dashboard creado con Streamlit - Análisis de datos de vendedores")
st.caption("Concentración de Analítica de Datos e Inteligencia Artificial | Tecnológico de Monterrey | Semestre Agosto-Diciembre 2025")

