# 💪 GPTrainer - Registro Automático de Entrenamientos

GPTrainer es un script en Python que registra automáticamente tus entrenamientos en Google Sheets. Utiliza la API de Nutritionix para analizar los ejercicios, la API de Sheety para guardar los datos en una hoja de cálculo y Google Translator para traducir nombres de ejercicios.

## 🌟 Características
- ✅ Registra ejercicios automáticamente en una hoja de Google Sheets.
- 🌐 Traduce nombres de ejercicios de cualquier idioma a inglés y de vuelta a español.
- 🔐 Usa APIs seguras con autenticación.
- 🔄 Obtiene la duración y calorías quemadas de cada ejercicio.

## ⚙ Requisitos
Antes de empezar, asegúrate de tener instalado:
- Python 3.x
- Una cuenta en [Nutritionix](https://www.nutritionix.com/business/api) para obtener API Key.
- Una cuenta en [Sheety](https://sheety.co/) para vincular Google Sheets.
- Un archivo `.env` con las claves API configuradas.

## 🔧 Instalación y Configuración
1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu-usuario/GPTrainer.git
   cd GPTrainer
   ```
2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` en la carpeta del proyecto y agrega tus credenciales:
   ```env
   API_ID=tu_api_id
   API_KEY=tu_api_key
   BEARER_TOKEN=tu_bearer_token
   ```
4. Ejecuta el script:
   ```sh
   python main.py
   ```

## 🎉 Uso
Cuando ejecutes el script, te pedirá que introduzcas el ejercicio realizado. Automáticamente:
1. Lo traduce al inglés.
2. Envía la consulta a Nutritionix y obtiene la duración y calorías quemadas.
3. Traduce el nombre del ejercicio al español.
4. Guarda los datos en Google Sheets a través de Sheety.
5. Te muestra un mensaje confirmando el registro.

## 📰 Ejemplo de salida
```
¿Qué ejercicio has hecho?     Correr 5km
✅ Correr guardado correctamente en Google Sheets.
```

## 🛠 Mejoras futuras
- [ ] Permitir personalizar peso, altura y género.
- [ ] Agregar opción para visualizar historial de entrenamientos.
- [ ] Crear una interfaz gráfica simple.

## 👋 Contribuir
Si tienes ideas o mejoras, siéntete libre de hacer un fork y enviar un PR.

## ✨ Autor
- **Sergio Sancho** - [LinkedIn](https://linkedin.com/in/tu-perfil](https://www.linkedin.com/in/sergio-sancho-calzada-58b5b2147/)) 
