import requests
from datetime import datetime
import os


APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

natural_language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_input = input("Tell me which exercises you did: ")
GENDER = "female"
WEIGHT_KG = 60
HEIGHT_CM = 170
AGE = 22

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

json_data = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=natural_language_endpoint, json=json_data, headers=headers)
result = response.json()

# print(result)

authorization_header = {
    "Authorization": "Bearer ywdhj9d39847ncmw84c7cn"
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_data, headers=authorization_header)
#   print(sheet_response.text)






