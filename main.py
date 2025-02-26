import os
import requests
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
from datetime import datetime as dt

load_dotenv()

# VARIABLES:
API_ID = os.getenv("API_ID")
API_KEY = os.getenv("API_KEY")
B_TOKEN = os.getenv("BEARER_TOKEN")

# ENPOINTS:
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GET_SHEETY_ENDPOINT = "https://api.sheety.co/3293fc0f387b3b0fa10771de1749f767/gpTrainer/workouts"
POST_SHEETY_ENDPOINT = "https://api.sheety.co/3293fc0f387b3b0fa10771de1749f767/gpTrainer/workouts"

exercise = input("¿Qué ejercicio has hecho?     ")
exercise_text_english = GoogleTranslator(source="auto", target="en").translate(exercise)

# headers para la autenticación con Nutritionix
nutritionix_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# headers para la autenticación con Bearer Token (para Sheety)
sheety_headers = {
    "Authorization": f"Bearer {B_TOKEN}",
    "Content-Type": "application/json"
}

# API params
params = {
    "query": exercise_text_english,
    "gender": "female",
    "weight_kg": 75,
    "height_cm": 185,
    "age": 25
}

response = requests.post(NUTRITIONIX_ENDPOINT, json=params, headers=nutritionix_headers)

if response.status_code == 200:
    data = response.json()
    for exercise in data["exercises"]:

        exercise_name_es = GoogleTranslator(source="en", target="es").translate(exercise['name'])

        # Información que va al Google Sheets:
        workout_data = {
            "workout": {
                "date": dt.now().date().strftime('%d-%m-%Y'),
                "time": dt.now().time().strftime('%H:%M:%S'),
                "exercise": exercise_name_es.title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
            }
        }

        # Hacer GET para obtener las filas actuales
        get_response = requests.get(GET_SHEETY_ENDPOINT, headers=sheety_headers)
        if get_response.status_code == 200:

            # POST para agregar el nuevo ejercicio
            sheety_response = requests.post(POST_SHEETY_ENDPOINT, json=workout_data, headers=sheety_headers)

            # Verificación del estado de la respuesta
            if sheety_response.status_code == 200:
                print(f"✅ {exercise_name_es.title()} guardado correctamente en Google Sheets.")
            else:
                print(f"❌ Error al guardar {exercise_name_es.title()}:", sheety_response.text)
        else:
            print(f"❌ Error al obtener datos de Google Sheets: {get_response.text}")
else:
    print("Error al obtener los datos:", response.text)
