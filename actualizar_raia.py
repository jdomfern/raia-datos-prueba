import requests
import json
from datetime import datetime
import os

# --- Configuración ---
URL = "https://api.raia.es/api/censoPublico?codigoPostal=41089&especie=gato"
FILE_PATH = "censoPublico.json"

print("🔄 Descargando datos desde RAIA...")

try:
    r = requests.get(URL, timeout=20)
    if r.status_code == 200:
        data = r.json()

        # Guardar los datos formateados
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Datos actualizados correctamente ({len(data)} registros).")
    else:
        print(f"⚠️ Error al conectar con RAIA. Código: {r.status_code}")
except Exception as e:
    print(f"❌ Error: {e}")
