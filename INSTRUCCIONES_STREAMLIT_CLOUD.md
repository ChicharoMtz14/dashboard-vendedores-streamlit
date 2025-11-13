# ✅ Instrucciones para desplegar en Streamlit Cloud

## ✅ Paso 1: Repositorio en GitHub (COMPLETADO)

Tu repositorio ya está en GitHub:
- **URL:** https://github.com/ChicharoMtz14/dashboard-vendedores-streamlit
- **Archivos subidos:** ✅ app_vendedores.py, requirements.txt, vendedores.xlsx, README.md

## 🚀 Paso 2: Desplegar en Streamlit Cloud

### Opción A: Desde share.streamlit.io (Recomendado)

1. **Ve a Streamlit Cloud:**
   - Abre tu navegador y ve a: https://share.streamlit.io
   - O directamente: https://share.streamlit.io/deploy

2. **Inicia sesión:**
   - Haz clic en "Sign in"
   - Selecciona "Continue with GitHub"
   - Autoriza la aplicación con tu cuenta de GitHub

3. **Crea una nueva app:**
   - Haz clic en el botón **"New app"** o **"Deploy an app"**
   
4. **Configura la aplicación:**
   - **Repository:** Selecciona `ChicharoMtz14/dashboard-vendedores-streamlit`
   - **Branch:** `main`
   - **Main file path:** `app_vendedores.py` ⚠️ **IMPORTANTE: Escribe esto manualmente**
   - **App URL (opcional):** Déjalo en blanco o elige un nombre personalizado

5. **Despliega:**
   - Haz clic en **"Deploy!"**
   - Espera 1-2 minutos mientras Streamlit Cloud:
     - Clona tu repositorio
     - Instala las dependencias de `requirements.txt`
     - Ejecuta tu aplicación

6. **¡Listo!**
   - Tu aplicación estará disponible en una URL como:
     `https://dashboard-vendedores-streamlit-chicharomtz14.streamlit.app`
   - O la URL personalizada que hayas elegido

### Opción B: Desde GitHub (Alternativa)

1. Ve a tu repositorio: https://github.com/ChicharoMtz14/dashboard-vendedores-streamlit
2. Haz clic en el botón verde **"Code"**
3. Busca la opción **"Deploy to Streamlit Cloud"** (si está disponible)
4. Sigue las instrucciones en pantalla

## 📋 Verificación

Una vez desplegada, verifica que:
- ✅ La aplicación carga correctamente
- ✅ Los datos de `vendedores.xlsx` se muestran
- ✅ Las gráficas se renderizan
- ✅ Los filtros funcionan

## 🔧 Solución de problemas

### Error: "File not found: vendedores.xlsx"
- **Solución:** Verifica que el archivo esté en la raíz del repositorio en GitHub
- Revisa: https://github.com/ChicharoMtz14/dashboard-vendedores-streamlit

### Error: "Module not found"
- **Solución:** Verifica que `requirements.txt` tenga todas las dependencias:
  - streamlit
  - pandas
  - openpyxl
  - matplotlib

### La aplicación no carga
- Revisa los logs en Streamlit Cloud (hay un botón "Manage app" → "Logs")
- Verifica que el "Main file path" sea exactamente `app_vendedores.py`

### Cambios no se reflejan
- Los cambios se actualizan automáticamente cuando haces push a GitHub
- Puede tardar 1-2 minutos en actualizarse
- Si no se actualiza, ve a "Manage app" → "Reboot app"

## 📝 Notas importantes

- **Main file path:** Debe ser exactamente `app_vendedores.py` (no `streamlit_app.py`)
- **Branch:** Usa `main` (no `master`)
- **Archivo Excel:** Asegúrate de que `vendedores.xlsx` esté en la raíz del repositorio

## 🎉 ¡Listo para desplegar!

Tu código ya está en GitHub y listo para Streamlit Cloud. Solo necesitas seguir los pasos del **Paso 2** arriba.
